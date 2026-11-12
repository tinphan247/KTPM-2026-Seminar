# CHECKLIST NỘP BÀI – SEMINAR AUTOMATION TESTING FOR DESKTOP APPLICATIONS (ROUND 2)

- **Nhóm thực hiện:** Nhóm 02 (ZipTool)
- **Môn học:** Kiểm thử Phần mềm (Software Testing)
- **Học kỳ:** HK1 – Năm học 2026-2027
- **Ngày hoàn tất:** 30/10/2026
- **Hạn chót giảng viên:** 31/10/2026

---

## 1. BÁO CÁO KỸ THUẬT TOÀN VĂN
- [x] **Báo cáo chi tiết PDF:** [`seminar-final.pdf`](seminar-final.pdf) (1.68 MB) – Xuất bản toàn văn 9 phần, chuẩn A4, typography học thuật, có ảnh chụp thực nghiệm và bảng số liệu định lượng.
- [x] **Bản thảo Markdown đầy đủ:** [`docs/report_v2.md`](docs/report_v2.md) và [`docs/report.md`](docs/report.md) (tích hợp toàn bộ 8 chương + chương 9 kết luận & minh chứng).
- [x] **Bản sao lưu PDF trong thư mục docs:** [`docs/report_v2.pdf`](docs/report_v2.pdf) (1.68 MB).

## 2. SLIDE THUYẾT TRÌNH POWERPOINT
- [x] **File trình chiếu gốc:** [`slides/seminar-group02.pptx`](slides/seminar-group02.pptx) – 15 slide chuẩn 16:9, nền trắng, chữ đậm rõ ràng (font ≥18pt), có biểu đồ và ảnh chụp thực tế.
- [x] **File slide PDF:** [`slides/seminar-slides.pdf`](slides/seminar-slides.pdf) (591 KB) – Xuất từ PowerPoint phục vụ trình chiếu.

## 3. VIDEO DEMO THỰC NGHIỆM (YOUTUBE)
- [x] **Danh sách video:** [`video-links.md`](video-links.md)
  - [x] **Video 1 – Katalon Studio (Kan):** [https://www.youtube.com/watch?v=w7c_X5f5SFo](https://www.youtube.com/watch?v=w7c_X5f5SFo) (Full HD 1080p, thuyết minh tiếng Việt, 3 demo).
  - [ ] **Video 2 – WinAppDriver (Tùng):** ⚠️ Thành viên không nộp video đúng hạn.
  - [ ] **Video 3 – AI (Quang):** ⚠️ Thành viên không nộp video đúng hạn.

## 4. MÃ NGUỒN KIỂM THỬ (TEST SCRIPTS)
- [x] **Katalon Studio:** Thư mục [`demo-scripts/katalon/`](demo-scripts/katalon/) (Object Repository, Test Cases TC01, TC02, TC03 DDT, BVA_TestSuite, Custom Keyword `LoginKeyword.groovy`).
- [x] **WinAppDriver C# NUnit:** Thư mục [`demo-scripts/winappdriver/`](demo-scripts/winappdriver/) (`MiniSumTests.csproj`, `LoginPage.cs`, `CalculatorPage.cs`, `Demo1`, `Demo2`, `Demo3`).
- [x] **AI-generated test (Quang):** Thư mục [`demo-scripts/ai-winappdriver/`](demo-scripts/ai-winappdriver/) (`MiniSumAiTests.csproj`, `PageObjects/`, `Tests/AiGeneratedBvaTests.cs`).

## 5. TÀI NGUYÊN THỰC NGHIỆM AI
- [x] **Thư mục Prompt:** [`ai/prompts/`](ai/prompts/) (`minisum-spec.md`, `testcase-bva-prompt.md`, `script-gen-prompt.md`).
- [x] **Thư mục Kết quả (Output):** [`ai/output/`](ai/output/) (`bva-testcases.xlsx`, `chatgpt-bva-output.md`, `gemini-bva-output.md`, `bva-evaluation.md`, `chatgpt-script-output.cs`, `verified-script-output.cs`, `ai-script-debug-and-verification.md`).

## 6. ỨNG DỤNG MẪU (APPLICATION UNDER TEST)
- [x] **App mẫu:** [`case-study-app/MiniSum.exe`](case-study-app/MiniSum.exe) (v1), [`MiniSum_v2.exe`](case-study-app/MiniSum_v2.exe) (v2), [`MiniSum_v3.exe`](case-study-app/MiniSum_v3.exe) (v3).
- [x] **Tài liệu hướng dẫn:** [`case-study-app/README.md`](case-study-app/README.md) (bảng AutomationId mapping, kiến trúc Fluent Light).

## 7. TÀI LIỆU QUẢN LÝ & MINH CHỨNG
- [x] **Nhật ký Git Commit:** [`git-commit-log.md`](git-commit-log.md) (toàn bộ lịch sử commit trên GitHub).
- [x] **Kê khai sử dụng AI:** [`ai-usage-declaration.md`](ai-usage-declaration.md) (kê khai đầy đủ theo quy định môn học).

## 8. ĐÁNH GIÁ ĐÓNG GÓP (% CONTRIBUTION)
- [x] **Bảng đánh giá chính thức theo mẫu khoa:** [`2026-2027-HK1-Group02-Project Contribution.xlsx`](2026-2027-HK1-Group02-Project Contribution.xlsx)
  - **Phan Trung Tín:** **35.0%** (Lead, MiniSum, Theory, Slide, AI, Report, Packaging)
  - **Nguyễn Lê Quang Kan:** **35.0%** (Katalon Studio trọn gói, Keyword, DDT, Video YouTube)
  - **Bùi Quang Tùng:** **30.0%** (WinAppDriver + C# NUnit, Page Object Model, DDT)
  - **Trần Vũ Quang:** **0.0%** (Không đạt tiến độ)
  - **Phạm Tấn Phát:** **0.0%** (Không đạt tiến độ)
- [x] **Bảng theo dõi nội bộ:** [`Group02_Task_List.xlsx`](Group02_Task_List.xlsx) (đồng bộ 35/35/30).

## 9. ĐÓNG GÓI SẢN PHẨM (ZIP PACKAGE)
- [x] **Tên file nén:** `Group02_ZipTool_Lan2.zip` (chứa đúng tiền tố ZipTool theo quy định).
- [x] **Dung lượng file:** ≤ 20MB (đạt tiêu chuẩn nộp qua cổng đào tạo).
- [x] **Tổng số file:** ≥ 20 files (thực tế > 100 files bao gồm source, report, ảnh, build).

---

**Trưởng nhóm xác nhận:** Phan Trung Tín (MSSV: 23120372)  
**Ngày hoàn tất:** 30/10/2026
