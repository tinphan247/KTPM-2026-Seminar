# Báo Cáo Đánh Giá Chất Lượng Test Case BVA Do AI Sinh (AI Evaluation Report)
## Chuyên đề: Automation Testing cho Desktop Applications

- **Người thực hiện:** Trần Vũ Quang (MSSV: 23120346) - Nhóm 02
- **Mục tiêu:** Đánh giá khoa học về chất lượng bộ test case BVA do các mô hình AI sinh ra dựa trên các độ đo chất lượng kiểm thử: Độ bao phủ biên (Boundary Coverage), Tính đúng đắn số học, Lỗi logic & Nguy cơ ảo giác (Hallucination Risk).

---

## 1. Phương Pháp Luận Đánh Giá

Bộ ca kiểm thử được kiểm định dựa trên chuẩn lý thuyết kiểm thử hộp đen (Black-box Boundary Value Analysis):
* **Miền giá trị đầu vào:** $A, B \in [-99, 99]$
* **Các lớp biên lý thuyết cần kiểm tra:**
  1. *Biên hợp lệ dưới (Valid Min):* $A = -99$
  2. *Biên hợp lệ trên (Valid Max):* $A = 99$
  3. *Biên ngoài dưới (Invalid Min / Robustness):* $A = -100$
  4. *Biên ngoài trên (Invalid Max / Robustness):* $A = 100$
  5. *Tương tự cho biến B:* $B = -99, 99, -100, 100$
  6. *Điểm danh định trung tâm (Nominal):* $(0, 0)$ hoặc các giá trị thông thường
  7. *Ca kiểm thử cực biên kép (Worst-case Extreme Testing):* $(-99, -99)$ và $(99, 99)$
  8. *Ca kiểm tra ngoại lệ kiểu dữ liệu (Invalid Data Type):* Nhập chuỗi ký tự không phải số.

---

## 2. Bảng Phân Tích Độ Phủ Biên (Boundary Coverage Matrix)

| Phân Loại Ca Kiểm Thử | Mục Tiêu Kỹ Thuật | Human Tester (Thủ công) | AI Zero-Shot (Chưa tối ưu) | AI Prompt-Engineered (Few-Shot) |
|---|---|:---:|:---:|:---:|
| **Biên hợp lệ đơn biến A** | $A \in \{-99, 99\}, B = 9$ | ✅ Đạt | ✅ Đạt (với $B=0$) | ✅ Đạt 100% |
| **Biên ngoại lệ đơn biến A** | $A \in \{-100, 100\}, B = 9$ | ✅ Đạt | ✅ Đạt (với $B=0$) | ✅ Đạt 100% |
| **Biên hợp lệ đơn biến B** | $B \in \{-99, 99\}, A = 10$ | ✅ Đạt | ✅ Đạt (với $A=0$) | ✅ Đạt 100% |
| **Biên ngoại lệ đơn biến B** | $B \in \{-100, 100\}, A = 10$ | ✅ Đạt | ✅ Đạt (với $A=0$) | ✅ Đạt 100% |
| **Điểm danh định (Nominal)** | $A = 0, B = 0$ | ✅ Đạt | ✅ Đạt | ✅ Đạt 100% |
| **Lỗi sai kiểu dữ liệu** | $A = \text{"xyz"}, B = 10$ | ✅ Đạt | ⚠️ Thiếu định dạng chuẩn | ✅ Đạt 100% |
| **Cực biên kép cực tiểu** | $A = -99, B = -99 \rightarrow -198$ | ⚠️ Dễ bị bỏ quên | ❌ **BỊ BỎ SÓT** | ✅ Đạt 100% |
| **Cực biên kép cực đại** | $A = 99, B = 99 \rightarrow 198$ | ⚠️ Dễ bị bỏ quên | ❌ **BỊ BỎ SÓT** | ✅ Đạt 100% |
| **TỶ LỆ ĐỘ PHỦ BIÊN TỔNG THỂ** | **Đầy đủ 8 nhóm biên** | **87.5%** | **62.5%** | **100%** |

---

## 3. Nhận Diện & Phân Tích Hiện Tượng Ảo Giác (Hallucination) Của AI Trong Kiểm Thử

Trong quá trình thực nghiệm đa vòng, nhóm đã cô lập và phân loại được 3 dạng ảo giác tiềm ẩn mà kỹ sư QA cần đặc biệt cảnh giác:

### 3.1 Ảo giác diễn dịch kết quả ngoại lệ (Boundary Overflow Hallucination)
* **Hiện tượng:** Ở một số prompt lỏng lẻo, khi người dùng nhập $A = 100, B = 9$, thay vì xuất Expected = `"LOI"` theo đặc tả, AI tự động tính toán $100 + 9 = 109$ và ghi vào cột Expected.
* **Nguyên nhân gốc rễ:** Mô hình ngôn ngữ bản chất được huấn luyện để giải toán tự nhiên, do đó thiên hướng mặc định của nó là "cộng hai số" thay vì tuân thủ luật nghiệp vụ phần mềm giới hạn $[-99, 99]$.
* **Biện pháp ngăn chặn:** Phải áp dụng ràng buộc phủ định rõ ràng trong System Prompt: *"Nếu bất kỳ giá trị nào vượt ngoài $[-99, 99]$, Expected BẮT BUỘC phải là chuỗi 'LOI', không được phép thực hiện phép cộng số học"*.

### 3.2 Ảo giác dấu toán học với số âm (Negative Arithmetic Flaw)
* **Hiện tượng:** Khi cộng $A = -99$ và $B = 9$, nếu không có Few-shot, có lần mô hình nhầm thành $-108$ hoặc $+90$ do nhầm lẫn quy tắc dấu.
* **Biện pháp ngăn chặn:** Cung cấp ít nhất 1 ví dụ Few-shot mẫu chứa phép cộng số âm có kết quả mẫu chuẩn xác: `TC01 | -99 | 9 | -90`.

### 3.3 Ảo giác cấu trúc dữ liệu nạp vào tool (Format Incompatibility)
* **Hiện tượng:** AI tự động thêm các cột không cần thiết như `Priority`, `Pre-condition`, `Actual Result`, `Status (Pass/Fail)`.
* **Hậu quả:** Khi export sang Excel để nạp vào Katalon Studio hoặc WinAppDriver (NPOI), code Data-Driven Testing sẽ bị lệch cột (`IndexOutOfRangeException`).
* **Biện pháp ngăn chặn:** Khóa cứng danh sách 5 cột: `TC_ID, A, B, Expected, Description`.

---

## 4. So Sánh Hiệu Quả Giữa Human Tester Và AI-Assisted Testing

| Chỉ số đo đạc | Human Tester (Thủ công) | AI Zero-Shot | AI Few-Shot Engineered |
|---|:---:|:---:|:---:|
| **Thời gian thiết kế bộ 12 test case** | 20 – 30 phút | 15 giây | **2.5 phút** (bao gồm prompt) |
| **Độ chính xác phép tính số học** | 98% (có thể nhầm nhẩm) | 90% | **100%** |
| **Độ phủ ca kiểm thử cực biên** | 75% – 85% | 62.5% | **100%** |
| **Công sức chuyển đổi sang Excel** | Gõ tay 12 dòng | Copy/paste | **Copy bảng Markdown nạp trực tiếp** |
| **Mức độ tiêu hao năng lực nhận thức** | Cao (mệt mỏi khi số lượng lớn) | Cực thấp | **Rất thấp** |

---

## 5. Kết Luận & Khuyến Nghị Thực Tiễn Cho Đội Ngũ QA

1. **AI là trợ thủ khuếch đại năng suất cực mạnh:** Giảm thời gian thiết kế test data từ 25 phút xuống dưới 3 phút (tiết kiệm **~90% thời gian**).
2. **Con người giữ vai trò phê duyệt (Human-in-the-loop):** Không bao giờ nạp trực tiếp output của AI vào pipeline kiểm thử tự động mà không qua bước kiểm tra chéo (Verification step).
3. **Prompt Engineering là kỹ năng bắt buộc:** Bộ test case do AI sinh ra chỉ đáng tin cậy khi kỹ sư kiểm thử biết cách đặt đề bài kèm ràng buộc toán học và kỹ thuật Few-shot.
