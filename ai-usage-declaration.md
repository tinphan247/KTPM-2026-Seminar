# KÊ KHAI VIỆC SỬ DỤNG AI (AI USAGE DECLARATION)

- **Người kê khai:** **Phan Trung Tín**
- **MSSV:** **23120372**
- **Nhóm:** **Nhóm 02 (ZipTool)**
- **Học kỳ:** **KTPM – 2026**
- **Ngày:** **30/10/2026**

---

## 1. Tổng quan

Theo **Nội quy & Quy tắc làm việc nhóm** mục 6 (Nguyên tắc sử dụng trí tuệ nhân tạo – AI), thành viên **được phép** sử dụng các cộng đồng AI
(ChatGPT, Gemini, Claude, GitHub Copilot…) để **hỗ trợ** công việc. Tuy nhiên, **toàn bộ việc sử dụng AI phải được kê khai trung thực** trong
tài liệu này.

Trong giai đoạn seminar **Automation Testing for Desktop Applications – Lần 2**, AI được sử dụng như một trợ lý hỗ trợ cho các task của nhóm,
đặc biệt trong lĩnh vực lý thuyết, thiết kế test, sinh mã kiểm thử và tổng hợp tài liệu.

---

## 2. Các công cụ AI đã sử dụng

| Công cụ AI | Phiên bản / Gói | Phân loại |
|---|---|---|
| ChatGPT | GPT-4 | Generative AI – hỗ trợ sinh test case, script, tài liệu |
| Gemini | Gemini Advanced | Generative AI – hỗ trợ phân tích & sinh nội dung |
| Claude | Claude 3.x | Generative AI – hỗ trợ viết code/tài liệu |
| GitHub Copilot | – | AI pair-programming – hỗ trợ viết mã C# |

---

## 3. Bảng mô tả từng lần / phạm vi sử dụng AI trong giai đoạn làm việc

| Task / Nội dung | AI hỗ trợ nội dung | Công cụ | Kết quả sau khi kiểm chứng | Đánh giá |
|---|---|---|---|---|
| **T08–T12** (docs/02-theory.md – POM, Flaky Test, Wait Strategy, Test Oracle, Recovery Testing) | Gợi ý cấu trúc section, khái niệm, mẫu code tham khảo | ChatGPT-4 / Claude | Nội dung đã được đọc, viết và rà soát lại thủ công; chỉ giữ phần kiến thức đã hiểu và kiểm chứng | ✅ Được phép – có kiểm tra lại |
| **T03–T06** (Build MiniSum v1/v2/v3, source code WinForms) | Gợi ý hướng đi, debug cú pháp, cấu hình project | GitHub Copilot / ChatGPT-4 | Code đã được viết, build và smoke test bằng `build.ps1` / `Verify-MiniSum.ps1` thực tế | ✅ Được phép – phải chạy thử |
| **T16** (video-links.md) | Soạn thảo nội dung tài liệu | ChatGPT-4 | Nội dung do lập trình viên tự viết, chỉ tham khảo format | ✅ Được phép |
| **T17** (git-commit-log.md) | – | – | Tự động sinh từ git log | ✅ Không dùng AI |

> **Lưu ý:** Mọi kết quả do AI sinh ra (test case, script, tài liệu, config…) phải được **chạy / kiểm tra / rà soát bởi người lập trình
> thực sự** trước khi đưa vào sản phẩm. AI chỉ là trợ lý hỗ trợ.

---

## 4. Các trường hợp AI có thể gây sai / cần xác minh

- **AI có thể bịa thông tin** (hallucination) về API, locator, cú pháp — đặc biệt khi hỗ trợ code C# WinForms / Katalon / WinAppDriver.
- **AI có thể sinh ra code không compile** hoặc sai logic.
- **AI có thể đề xuất locator không chính xác** với ứng dụng desktop.
- **Quy trình xử lý:** Khi AI đưa ra sai, phải ghi nhận lại, **sửa thủ công** và ghi chú trong báo cáo so sánh / tài liệu tương ứng.

---

## 5. Cam kết & xác nhận

Theo quy định nhóm, tôi **xin cam kết** rằng:

1. Toàn bộ nội dung, code, tài liệu được đưa vào sản phẩm đều **do cá nhân / nhóm kiểm tra lại** và chịu trách nhiệm cuối cùng.
2. Việc sử dụng AI được thực hiện **trong phạm vi được phép** và **minh bạch** qua file này.
3. Các kết quả do AI sinh ra chỉ được sử dụng khi **đã được xác minh** (build thành công, script chạy đúng, dữ liệu kiểm chứng).

---

**Đã kê khai đầy đủ.** Người kê khai: **Phan Trung Tín** – MSSV **23120372**.
