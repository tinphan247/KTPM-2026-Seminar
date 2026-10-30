# Thực Nghiệm AI Demo 1b: Đối Chiếu Cùng Prompt Với Gemini Advanced & Claude
## Khảo Sát Tính Nhất Quán & Năng Lực Suy Luận Của Các LLM Hàng Đầu

- **Người thực nghiệm:** Trần Vũ Quang (MSSV: 23120346) - Nhóm 02
- **Các mô hình đối chiếu:**
  1. Google Gemini Advanced (Gemini 1.5 Pro)
  2. Anthropic Claude 3.5 Sonnet
  3. Đối sánh với OpenAI ChatGPT-4 (từ Demo 1a)
- **Prompt sử dụng:** Mẫu Few-shot & Chain-of-Thought chuẩn hóa (từ file `ai/prompts/testcase-bva-prompt.md`).

---

## 1. Kết Quả Sinh Ca Kiểm Thử Từ Google Gemini Advanced (Gemini 1.5 Pro)

### 1.1 Kết quả dạng bảng Markdown từ Gemini 1.5 Pro

| TC_ID | A | B | Expected | Description |
|---|---|---|---|---|
| TC01 | -99 | 9 | -90 | Biên dưới của A (hợp lệ: A = min = -99, B = 9) |
| TC02 | 99 | 9 | 108 | Biên trên của A (hợp lệ: A = max = 99, B = 9) |
| TC03 | -100 | 9 | LOI | Biên ngoài dưới của A (ngoại lệ: A = -100 < -99) |
| TC04 | 100 | 9 | LOI | Biên ngoài trên của A (ngoại lệ: A = 100 > 99) |
| TC05 | xyz | 10 | LOI | A không phải số nguyên (lỗi kiểu chuỗi chữ) |
| TC06 | 10 | -99 | -89 | Biên dưới của B (hợp lệ: A = 10, B = min = -99) |
| TC07 | 10 | 99 | 109 | Biên trên của B (hợp lệ: A = 10, B = max = 99) |
| TC08 | 10 | -100 | LOI | Biên ngoài dưới của B (ngoại lệ: B = -100 < -99) |
| TC09 | 10 | 100 | LOI | Biên ngoài trên của B (ngoại lệ: B = 100 > 99) |
| TC10 | 0 | 0 | 0 | Điểm danh định gốc tọa độ (A = 0, B = 0) |
| TC11 | -99 | -99 | -198 | Cực biên dưới đồng thời (Worst-case: A = -99, B = -99) |
| TC12 | 99 | 99 | 198 | Cực biên trên đồng thời (Worst-case: A = 99, B = 99) |

### 1.2 Đặc điểm phản hồi của Gemini 1.5 Pro
* **Tốc độ sinh (Generation Latency):** Cực kỳ nhanh (khoảng 3.2 giây để sinh xong toàn bộ bảng).
* **Độ chính xác số học:** Đạt 100% (cả phép cộng số âm $-99 + (-99) = -198$ và $10 + (-99) = -89$ đều chuẩn xác).
* **Cột Description:** Gemini diễn giải rõ ràng cả mệnh đề điều kiện toán học (ví dụ: `A = -100 < -99`).
* **Tính tuân thủ:** Tuân thủ xuất sắc 5 cột không bị thừa cột, không kèm theo lời chào mở đầu rườm rà khi được yêu cầu.

---

## 2. Kết Quả Sinh Ca Kiểm Thử Từ Anthropic Claude 3.5 Sonnet

### 2.1 Kết quả dạng bảng Markdown từ Claude 3.5 Sonnet

| TC_ID | A | B | Expected | Description |
|---|---|---|---|---|
| TC01 | -99 | 9 | -90 | Valid lower bound A: A = min (-99), B = nominal (9) |
| TC02 | 99 | 9 | 108 | Valid upper bound A: A = max (99), B = nominal (9) |
| TC03 | -100 | 9 | LOI | Robustness test: A below min (-100), B = nominal (9) |
| TC04 | 100 | 9 | LOI | Robustness test: A above max (100), B = nominal (9) |
| TC05 | xyz | 10 | LOI | Invalid type check: non-numeric string for input A |
| TC06 | 10 | -99 | -89 | Valid lower bound B: A = nominal (10), B = min (-99) |
| TC07 | 10 | 99 | 109 | Valid upper bound B: A = nominal (10), B = max (99) |
| TC08 | 10 | -100 | LOI | Robustness test: B below min (-100), A = nominal (10) |
| TC09 | 10 | 100 | LOI | Robustness test: B above max (100), A = nominal (10) |
| TC10 | 0 | 0 | 0 | Nominal center case: both inputs at origin (0, 0) |
| TC11 | -99 | -99 | -198 | Extreme lower corner: both A and B at minimum |
| TC12 | 99 | 99 | 198 | Extreme upper corner: both A and B at maximum |

### 2.2 Đặc điểm phản hồi của Claude 3.5 Sonnet
* **Thuật ngữ kiểm thử phần mềm:** Rất chuyên nghiệp theo chuẩn ISTQB (sử dụng các thuật ngữ như *Robustness test*, *Extreme lower corner*, *Invalid type check*).
* **Độ chính xác logic:** Hoàn hảo 100%, không xuất hiện bất kỳ ảo giác nào.
* **Thời gian phản hồi:** Khoảng 4.8 giây.

---

## 3. Bảng Ma Trận So Sánh Năng Lực 3 Mô Hình LLM Hàng Đầu

| Tiêu chí đánh giá | OpenAI ChatGPT-4 | Google Gemini 1.5 Pro | Anthropic Claude 3.5 Sonnet |
|---|:---:|:---:|:---:|
| **Thời gian phản hồi (Latency)** | 5.5 giây | **3.2 giây (Nhanh nhất)** | 4.8 giây |
| **Độ chính xác tính toán (Math)** | 100% | 100% | 100% |
| **Độ phủ biên (BVA Coverage)** | Hoàn thiện (sau Turn 2) | **Hoàn thiện ngay Turn 1** | **Hoàn thiện ngay Turn 1** |
| **Độ bám sát cấu trúc Output** | Rất tốt | Rất tốt | Rất tốt |
| **Tính học thuật / Thuật ngữ QA** | Tốt | Tốt (Toán học) | **Xuất sắc (Chuẩn ISTQB)** |
| **Hiện tượng ảo giác (Hallucination)** | Thấp | Rất thấp | Cực thấp |

---

## 4. Kết Luận Khảo Sát

1. Khi được cung cấp tài liệu đặc tả chặt chẽ (`minisum-spec.md`) và Prompt được cấu trúc theo phương pháp Few-shot (`testcase-bva-prompt.md`), **cả 3 mô hình hàng đầu thế giới đều cho ra kết quả đồng thuận 100%** đối với 12 ca kiểm thử trọng tâm.
2. Điều này chứng minh rằng: **Chìa khóa của việc ứng dụng AI thành công trong kiểm thử phần mềm không nằm ở việc chọn model nào, mà nằm ở kỹ năng kỹ nghệ câu lệnh (Prompt Engineering) và độ rõ ràng của tài liệu đặc tả ban đầu.**
