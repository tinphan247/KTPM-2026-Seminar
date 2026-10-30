# Kỹ Thuật Prompt Engineering: Sinh Ca Kiểm Thử Phân Tích Giá Trị Biên (BVA)
## Chuyên đề: Automation Testing cho Desktop Applications

- **Người thiết kế:** Trần Vũ Quang (MSSV: 23120346) - Nhóm 02
- **Mục tiêu:** Thiết kế bộ Prompt chuẩn mực áp dụng các kỹ thuật Prompt Engineering hiện đại (Role Prompting, Zero-shot, Few-shot, Chain-of-Thought, và Structured Output Enforcement) để các mô hình LLM (ChatGPT-4, Claude 3.5, Gemini 1.5 Pro) sinh ra danh sách ca kiểm thử BVA chất lượng cao, không bị sót biên, không bị ảo giác kết quả.

---

## 1. Cấu Trúc Kỹ Thuật Của Bộ Prompt

Bộ Prompt được tổ chức theo cấu trúc chuẩn 5 phần dành cho kỹ sư QA/SDET:
```
┌────────────────────────────────────────────────────────┐
│ 1. SYSTEM ROLE: Định hình tư duy chuyên gia QA Lead    │
├────────────────────────────────────────────────────────┤
│ 2. CONTEXT: Cung cấp đặc tả hệ thống và miền giá trị   │
├────────────────────────────────────────────────────────┤
│ 3. INSTRUCTION: Chỉ định rõ phương pháp BVA 2 biến     │
├────────────────────────────────────────────────────────┤
│ 4. FEW-SHOT EXAMPLES: Cung cấp dữ liệu mẫu định dạng   │
├────────────────────────────────────────────────────────┤
│ 5. CONSTRAINTS & OUTPUT FORMAT: Bảng Markdown chuẩn hóa│
└────────────────────────────────────────────────────────┘
```

---

## 2. Prompt 1: Thử Nghiệm Zero-Shot (Không Cung Cấp Mẫu)

Dùng để đánh giá khả năng suy luận tự nhiên của LLM khi chỉ nhận đặc tả và yêu cầu:

```markdown
[ROLE]
Bạn là chuyên gia kiểm thử phần mềm (Senior QA Engineer) với hơn 10 năm kinh nghiệm trong kiểm thử hộp đen (Black-box Testing) và tự động hóa Desktop Applications.

[CONTEXT]
Ứng dụng desktop MiniSum có chức năng tính tổng hai số nguyên A và B:
- Miền giá trị hợp lệ của A: số nguyên trong khoảng [-99, 99].
- Miền giá trị hợp lệ của B: số nguyên trong khoảng [-99, 99].
- Nếu A hoặc B nằm ngoài miền [-99, 99] hoặc không phải số nguyên, hệ thống báo "LOI".
- Nếu hợp lệ, hệ thống trả về kết quả số học: Expected = A + B.

[TASK]
Hãy áp dụng kỹ thuật Phân tích giá trị biên (Boundary Value Analysis - BVA) kết hợp Phân hoạch tương đương (Equivalence Partitioning) để sinh ra danh sách ca kiểm thử bao phủ toàn diện các biên hợp lệ, biên không hợp lệ và lỗi định dạng.

[OUTPUT FORMAT]
Bảng Markdown gồm các cột: TC_ID, A, B, Expected, Description.
```

---

## 3. Prompt 2: Kỹ Thuật Few-Shot & Chain-of-Thought (Khuyến Nghị Sử Dụng)

Đây là mẫu Prompt tối ưu hóa có kèm định nghĩa biên toán học và 2 ví dụ Few-shot mẫu để ép mô hình tuân thủ tuyệt đối cấu trúc dữ liệu xuất ra:

```markdown
[ROLE & PERSONA]
Bạn là Lead QA Automation Engineer tại một tập đoàn công nghệ lớn. Nhiệm vụ của bạn là thiết kế bộ ca kiểm thử chuẩn xác 100% để nạp trực tiếp vào hệ thống Data-Driven Automation Testing (Katalon Studio và WinAppDriver).

[SPECIFICATION & CONTEXT]
Hệ thống: Desktop MiniSum Calculator
- Đầu vào A: Số nguyên $[-99, 99]$
- Đầu vào B: Số nguyên $[-99, 99]$
- Điểm mốc biên chuẩn cho mỗi biến:
  * Biên dưới ngoài (Invalid Min-): min - 1 = -100 (Expected: LOI)
  * Biên dưới trong (Valid Min): min = -99
  * Cận biên dưới (Valid Min+): min + 1 = -98
  * Giá trị danh định (Nominal): 0, 9, 10
  * Cận biên trên (Valid Max-): max - 1 = 98
  * Biên trên trong (Valid Max): max = 99
  * Biên trên ngoài (Invalid Max+): max + 1 = 100 (Expected: LOI)
  * Sai kiểu dữ liệu (Invalid Type): chuỗi ký tự (Expected: LOI)

[FEW-SHOT EXAMPLES]
Dưới đây là 2 ca kiểm thử mẫu minh họa định dạng và quy tắc tính Expected:
| TC_ID | A | B | Expected | Description |
|---|---|---|---|---|
| TC01 | -99 | 9 | -90 | Biên dưới A hợp lệ (A = min = -99, B = nominal = 9) |
| TC03 | -100 | 9 | LOI | Biên dưới A ngoại lệ (A = min - 1 = -100) -> Báo lỗi ngoài miền |

[CONSTRAINTS & RULES]
1. Tính toán số học phải chính xác tuyệt đối: Với các ca hợp lệ, Expected phải bằng đúng A + B (chú ý số âm: ví dụ -99 + 9 = -90; -99 + (-99) = -198).
2. Khi có giá trị vượt biên (như -100, 100) hoặc ký tự không hợp lệ, Expected PHẢI là "LOI".
3. Thiết kế đúng 12 ca kiểm thử trọng tâm bao gồm:
   - 4 ca kiểm tra biên của biến A (khi B cố định ở nominal = 9)
   - 1 ca kiểm tra lỗi kiểu dữ liệu của A (A = "xyz", B = 10)
   - 4 ca kiểm tra biên của biến B (khi A cố định ở nominal = 10)
   - 1 ca danh định trung tâm (A = 0, B = 0)
   - 2 ca cực biên đồng thời cả 2 biến (A = min & B = min; A = max & B = max)
4. Tên cột bắt buộc: `TC_ID | A | B | Expected | Description`.
5. Không xuất thêm lời giải thích rườm rà ngoài bảng Markdown.
```

---

## 4. Bảng Tiêu Chí Đánh Giá Phản Hồi Của AI (Rubric Đánh Giá)

| Tiêu chí đánh giá | Trọng số | Mô tả kiểm định |
|---|:---:|---|
| **Độ phủ biên (Boundary Coverage)** | 35% | Phủ đủ các mốc: $-100, -99, 99, 100$, danh định $0$, cực biên kép $\pm 198$. |
| **Tính đúng đắn số học (Arithmetic Correctness)** | 30% | Không có phép cộng nào bị tính sai (đặc biệt các số âm và phép cộng lớn). |
| **Không ảo giác (Zero Hallucination)** | 15% | Không tự bịa thêm các trường dữ liệu ngoài đặc tả, Expected tuân thủ đúng quy ước `"LOI"`. |
| **Tính tuân thủ cấu trúc (Format Adherence)** | 10% | Đúng 5 cột yêu cầu, sẵn sàng chuyển đổi 1-1 sang file Excel `.xlsx`. |
| **Ngữ nghĩa mô tả (Clarity of Description)** | 10% | Mô tả giải thích rõ ràng lý do kiểm thử và vị trí biên đang kiểm tra. |
