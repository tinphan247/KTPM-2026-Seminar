# Thực Nghiệm AI Demo 1a: Sinh Test Case BVA Bằng ChatGPT-4
## Phân Tích Phản Hồi & Tinh Chỉnh Đa Vòng (Multi-Turn Prompt Refinement)

- **Người thực nghiệm:** Trần Vũ Quang (MSSV: 23120346) - Nhóm 02
- **Mô hình sử dụng:** OpenAI ChatGPT-4 (GPT-4o / GPT-4 Turbo)
- **Mục tiêu:** Kiểm chứng năng lực sinh ca kiểm thử hộp đen BVA, phát hiện các điểm nghẽn/ảo giác và áp dụng kỹ thuật tinh chỉnh đa vòng (Refinement) để đạt 100% độ chính xác cho kịch bản Data-Driven Testing.

---

## 1. Vòng 1 (Turn 1): Thực Nghiệm Với Zero-Shot Prompt

### 1.1 Nội dung Prompt gửi vào ChatGPT-4
```text
Bạn là một chuyên gia kiểm thử phần mềm. Hãy sinh bộ test case theo phương pháp Phân tích giá trị biên (BVA) cho hàm tính tổng 2 số nguyên A và B với điều kiện A, B thuộc [-99, 99]. Nếu sai miền hoặc sai kiểu dữ liệu báo LOI. Xuất bảng Markdown: TC_ID, A, B, Expected, Description.
```

### 1.2 Phản hồi thô nhận được từ ChatGPT-4 (Turn 1 Output)
| TC_ID | A | B | Expected | Description |
|---|---|---|---|---|
| TC01 | -99 | 0 | -99 | Biên dưới A |
| TC02 | 99 | 0 | 99 | Biên trên A |
| TC03 | -100 | 0 | LOI | A nhỏ hơn biên dưới |
| TC04 | 100 | 0 | LOI | A lớn hơn biên trên |
| TC05 | 0 | -99 | -99 | Biên dưới B |
| TC06 | 0 | 99 | 99 | Biên trên B |
| TC07 | 0 | -100 | LOI | B nhỏ hơn biên dưới |
| TC08 | 0 | 100 | LOI | B lớn hơn biên trên |
| TC09 | 0 | 0 | 0 | Giá trị trung bình |
| TC10 | abc | 10 | LOI | A không phải số nguyên |

### 1.3 Nhận xét & Đánh giá Vòng 1
* **Ưu điểm:**
  * Hiểu đúng miền giá trị $[-99, 99]$ và xác định được các điểm biên cơ bản $\pm 99$ và ngoài biên $\pm 100$.
  * Cú pháp Markdown chuẩn, nhận diện được trường hợp lỗi ký tự `abc`.
* **Điểm yếu & Thiếu sót:**
  * **Thiếu các ca cực biên đồng thời (Worst-case / Extreme Dual Boundaries):** Mô hình chỉ test đơn biến khi biến còn lại bằng $0$, hoàn toàn bỏ sót trường hợp cả hai biến cùng đạt giá trị cực tiểu $(A = -99, B = -99)$ hoặc cực đại $(A = 99, B = 99)$. Đây là nơi dễ gây lỗi tràn số hoặc lỗi tính toán giao diện nhất!
  * **Cố định biến phụ ở giá trị 0:** Trong thực tế kiểm thử BVA đa biến, việc cố định biến còn lại ở giá trị danh định (ví dụ $9$ hoặc $10$) sẽ phát hiện tốt hơn lỗi tính toán số học so với phép cộng với $0$.

---

## 2. Vòng 2 (Turn 2): Tinh Chỉnh Prompt Với Few-Shot & Ràng Buộc Cực Biên

### 2.1 Nội dung Prompt tinh chỉnh (Turn 2 Refinement Prompt)
```text
Cảm ơn bạn. Bộ test case trên đã có các biên cơ bản nhưng chưa đầy đủ. Hãy tinh chỉnh lại bộ test case để đảm bảo đạt chuẩn Data-Driven Testing cho dự án:
1. Cố định biến còn lại ở giá trị danh định thực tế (B = 9 khi test biên của A; A = 10 khi test biên của B).
2. Bổ sung bắt buộc 2 ca cực biên đồng thời cả 2 biến:
   - Ca cực tiểu: A = -99, B = -99 -> Expected: -198
   - Ca cực đại: A = 99, B = 99 -> Expected: 198
3. Thêm 1 ca kiểm tra sai kiểu dữ liệu chữ cái: A = "xyz", B = 10 -> Expected: LOI.
4. Tổng cộng chuẩn hóa đúng 12 ca kiểm thử trọng tâm (TC01 đến TC12). Hãy tính toán số học chính xác, không được sai dấu âm.
```

### 2.2 Phản hồi hoàn thiện từ ChatGPT-4 (Turn 2 Refined Output)

| TC_ID | A | B | Expected | Description |
|---|---|---|---|---|
| **TC01** | -99 | 9 | -90 | Biên dưới A hợp lệ (A = min = -99, B = nominal = 9) |
| **TC02** | 99 | 9 | 108 | Biên trên A hợp lệ (A = max = 99, B = nominal = 9) |
| **TC03** | -100 | 9 | LOI | Biên dưới A ngoại lệ (A = min - 1 = -100) -> Báo lỗi ngoài miền |
| **TC04** | 100 | 9 | LOI | Biên trên A ngoại lệ (A = max + 1 = 100) -> Báo lỗi ngoài miền |
| **TC05** | xyz | 10 | LOI | A không phải số nguyên (sai kiểu dữ liệu) -> Báo lỗi định dạng |
| **TC06** | 10 | -99 | -89 | Biên dưới B hợp lệ (A = nominal = 10, B = min = -99) |
| **TC07** | 10 | 99 | 109 | Biên trên B hợp lệ (A = nominal = 10, B = max = 99) |
| **TC08** | 10 | -100 | LOI | Biên dưới B ngoại lệ (B = min - 1 = -100) -> Báo lỗi ngoài miền |
| **TC09** | 10 | 100 | LOI | Biên trên B ngoại lệ (B = max + 1 = 100) -> Báo lỗi ngoài miền |
| **TC10** | 0 | 0 | 0 | Giá trị trung bình danh định (nominal case: A = 0, B = 0) |
| **TC11** | -99 | -99 | -198 | Cực biên dưới đồng thời (A = min = -99, B = min = -99) |
| **TC12** | 99 | 99 | 198 | Cực biên trên đồng thời (A = max = 99, B = max = 99) |

---

## 3. Phân Tích Kỹ Thuật Chi Tiết 12 Ca Kiểm Thử Sau Khi Tinh Chỉnh

1. **Nhóm kiểm tra biến A (TC01 - TC04):**
   - Giữ cố định biến $B = 9$ (giá trị danh định dương nhỏ).
   - Kiểm tra chính xác 2 giá trị biên trong hợp lệ ($-99$ cho kết quả $-90$; $+99$ cho kết quả $108$).
   - Kiểm tra chính xác 2 giá trị biên ngoài ngoại lệ ($-100$ và $+100$ đều được gắn cờ `"LOI"`).
2. **Nhóm kiểm tra lỗi kiểu dữ liệu (TC05):**
   - Đưa chuỗi không phải số `"xyz"` vào $A$, $B = 10$, hệ thống gắn cờ `"LOI"`.
3. **Nhóm kiểm tra biến B (TC06 - TC09):**
   - Giữ cố định biến $A = 10$ (giá trị danh định khác $0$).
   - Kiểm tra chính xác biên dưới trong $B = -99 \rightarrow 10 + (-99) = -89$.
   - Kiểm tra chính xác biên trên trong $B = 99 \rightarrow 10 + 99 = 109$.
   - Kiểm tra chính xác 2 giá trị biên ngoài $B = -100$ và $B = 100 \rightarrow \text{Expected: LOI}$.
4. **Nhóm danh định trung tâm (TC10):**
   - $A = 0, B = 0 \rightarrow 0$. Trường hợp cơ sở kiểm tra tính nguyên vẹn hệ thống.
5. **Nhóm cực biên kép đồng thời (TC11 - TC12):**
   - $A = -99, B = -99 \rightarrow -198$: Giá trị tổng âm lớn nhất về độ lớn.
   - $A = 99, B = 99 \rightarrow 198$: Giá trị tổng dương lớn nhất.

---

## 4. Kết Luận Thực Nghiệm Với ChatGPT-4

* **Khả năng tiếp thu:** ChatGPT-4 phản hồi rất nhạy bén với các chỉ dẫn có tính cấu trúc toán học.
* **Thời gian thực hiện:** Từ lúc soạn prompt đến khi có kết quả hoàn chỉnh 12 test case chỉ mất **khoảng 2.5 phút** (so với viết thủ công khoảng 20-25 phút).
* **Kết quả:** Bộ 12 ca kiểm thử này đã được kiểm định chéo và dùng làm file chuẩn `bva-testcases.xlsx` cho cả hai nhánh automation test của Kan (Katalon) và Tùng (WinAppDriver).
