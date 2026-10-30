# Kịch Bản Thuyết Minh Video Thực Nghiệm AI Trong Desktop Automation (AI Demo Video Script)
## Chuyên đề: Automation Testing cho Desktop Applications

- **Thành viên thực hiện:** Trần Vũ Quang (MSSV: 23120346) - Nhóm 02
- **Thời lượng dự kiến:** 5 - 7 phút
- **Chất lượng:** Full HD (1080p), 60fps, thu âm rõ ràng, không lẫn tạp âm.
- **Mục tiêu:** Thể hiện trọn vẹn luồng công việc hiện đại: `Tài liệu đặc tả` $\rightarrow$ `Prompt Engineering` $\rightarrow$ `AI sinh Test Case BVA` $\rightarrow$ `AI sinh Script C# NUnit POM` $\rightarrow$ `Debug & Thực thi PASS 100% trên WinAppDriver`.

---

## 1. Bảng Phân Cảnh & Timeline Chi Tiết (Storyboard)

| Thời gian | Cảnh quay (Screen Action) | Lời thoại thuyết minh tiếng Việt |
|:---:|---|---|
| **00:00 - 00:45** | - Mở slide tiêu đề hoặc màn hình Desktop chứa thư mục dự án `KTPM-2026-Seminar`.<br>- Mở tài liệu [`minisum-spec.md`](../ai/prompts/minisum-spec.md). | *"Xin chào thầy và các bạn. Em là Trần Vũ Quang, đại diện nhóm 2 báo cáo phần thực nghiệm Ứng dụng AI trong Automation Testing cho Desktop Applications. Hôm nay em sẽ minh họa cách GenAI giúp chúng ta rút ngắn 75% thời gian từ khâu thiết kế test case đến khi chạy kịch bản hoàn chỉnh trên ứng dụng mẫu MiniSum."* |
| **00:45 - 02:00** | **DEMO 1: Sinh Test Case BVA**<br>- Mở file [`testcase-bva-prompt.md`](../ai/prompts/testcase-bva-prompt.md).<br>- Copy prompt gửi vào giao diện ChatGPT-4 / Claude / Gemini.<br>- Quay màn hình AI sinh bảng Markdown 12 test cases.<br>- Mở file [`bva-testcases.xlsx`](../ai/output/bva-testcases.xlsx) đối chiếu. | *"Đầu tiên là bài toán thiết kế dữ liệu kiểm thử biên BVA cho hàm tính tổng với miền giá trị từ -99 đến 99. Thay vì tính nhẩm thủ công dễ sai sót số âm, chúng em áp dụng kỹ thuật Few-shot Prompting với các ví dụ mẫu. Như mọi người thấy, AI đã sinh ra đúng 12 ca kiểm thử trọng tâm bao gồm cả các ca cực biên kép như -99 cộng -99 bằng -198 và bắt lỗi LOI khi nhập 100 hoặc chữ cái."* |
| **02:00 - 03:30** | **DEMO 2A: Sinh Mã Nguồn C# POM**<br>- Mở file [`script-gen-prompt.md`](../ai/prompts/script-gen-prompt.md).<br>- Trình chiếu prompt yêu cầu cấu trúc Page Object Model.<br>- Trình chiếu mã nguồn do AI sinh ra tại [`chatgpt-script-output.cs`](../ai/output/chatgpt-script-output.cs). | *"Tiếp theo, em yêu cầu AI sinh mã nguồn kiểm thử tự động bằng C# NUnit và WinAppDriver. Để mã nguồn dễ bảo trì, prompt bắt buộc AI phải áp dụng mô hình Page Object Model (POM), tách riêng class LoginPage và CalculatorPage thay vì viết script nguyên khối. Toàn bộ mã nguồn 215 dòng được sinh ra chỉ trong chưa đầy 10 giây."* |
| **03:30 - 04:45** | **DEMO 2B: Debug & Chạy Thật Trên Môi Trường**<br>- Mở cửa sổ Command Prompt chạy `WinAppDriver.exe 4723`.<br>- Mở Visual Studio / VS Code chạy lệnh `dotnet test` hoặc NUnit Test Explorer.<br>- Quay màn hình app MiniSum tự động mở lên, login, nhập 12 cặp số và trả về PASS xanh lá! | *"Bây giờ, em tiến hành chạy thực tế trên môi trường thật với WinAppDriver. Trong quá trình verify, nhóm phát hiện AI gặp một số lỗi kinh điển của lập trình desktop như mất window handle khi chuyển form và cách xóa TextBox trong WinForms. Sau khi nhóm refactor 15% mã nguồn, toàn bộ 14 ca kiểm thử đã PASS 100% chỉ trong 18 giây!"* |
| **04:45 - 05:30** | **TỔNG KẾT & SỐ LIỆU SO SÁNH**<br>- Mở bảng so sánh thời gian và biểu đồ trong [`docs/06-comparison.md`](../docs/06-comparison.md).<br>- Tóm tắt kết luận. | *"Qua thực nghiệm, nhóm đo đạc được thời gian hoàn thành một bộ test suite giảm từ 120 phút xuống chỉ còn 29 phút. Tỷ lệ tái sử dụng mã đạt tới 84.6%. AI thực sự là một trợ lý đắc lực giải phóng kỹ sư kiểm thử khỏi các tác vụ lặp đi lặp lại. Cảm ơn thầy và các bạn đã chú ý lắng nghe."* |

---

## 2. Hướng Dẫn Kỹ Thuật Khi Quay Video
1. **Chuẩn bị môi trường trước khi quay:**
   - Bật sẵn tiến trình `WinAppDriver.exe` dưới quyền Administrator.
   - Biên dịch sẵn file `case-study-app/MiniSum.exe`.
   - Mở sẵn các tab: Prompt Markdown, Web ChatGPT/Gemini, và IDE Visual Studio.
2. **Cấu hình OBS Studio / Windows Game Bar:**
   - Độ phân giải: 1920x1080.
   - Tốc độ khung hình: 60 FPS.
   - Microphone: Chọn mic lọc tiếng ồn (Noise suppression).
3. **Lưu trữ video:**
   - Xuất file định dạng `.mp4` (H.264, AAC).
   - Đặt tên file: `videos/quang-ai-demo.mp4` hoặc upload lên YouTube (Unlisted) và dán link vào `video-links.md`.
