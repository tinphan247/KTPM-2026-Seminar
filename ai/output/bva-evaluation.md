# Đánh Giá Chất Lượng Bộ Test Case Do AI Sinh Ra

## 1. Tiêu Chí Đánh Giá
- **Độ phủ giá trị biên (Boundary Coverage):** 100% các điểm biên {-100, -99, -98, 0, 98, 99, 100} đều được khảo sát.
- **Tính chính xác của kết quả mong đợi (Oracle Accuracy):** Đúng 100% theo đặc tả nghiệp vụ MiniSum.
- **Hiện tượng ảo giác (Hallucination):** 
  - Ở lượt prompt ban đầu (zero-shot), AI có xu hướng dùng chuỗi tiếng Việt có dấu (Kết quả là:) trong khi AUT yêu cầu ASCII (Ket qua:).
  - Sau khi cung cấp few-shot prompt với chuỗi ASCII chuẩn, cả ChatGPT và Gemini đều đạt độ chính xác 100%.

## 2. Đối Chiếu Hai Mô Hình
| Tiêu chí | ChatGPT-4 | Gemini Advanced |
|---|---|---|
| Thời gian phản hồi | 4.2 giây | 2.8 giây |
| Độ phủ biên | 100% | 100% |
| Khả năng định dạng bảng | Chuẩn Markdown + ASCII | Chuẩn Markdown + ASCII |
| Rủi ro cú pháp / quy ước | Thấp (tuân thủ prompt) | Rất thấp |
