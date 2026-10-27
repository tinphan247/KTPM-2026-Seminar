# KẾ HOẠCH CHI TIẾT SEMINAR LẦN 2 – NHÓM 02 (ZipTool)
## Chủ đề: Automation Testing for Desktop Applications
## Deadline nộp: Trước 31/10/2026 (mục tiêu nội bộ: 30/10 sáng)

---

## 👥 THÔNG TIN THÀNH VIÊN & PHÂN CHIA ĐÓNG GÓP

> **Chính sách phân chia:** Chia đều khối lượng công việc, mỗi thành viên đảm nhận đúng **24.0 giờ làm việc ước tính** và gợi ý mức đóng góp **20.0%** (tổng 100%).

| STT | Họ và Tên | MSSV | Vai trò chính Lần 2 | Branch Git | Tasks | Giờ ước tính | % Gợi ý |
|:---:|---|:---:|---|---|:---:|:---:|:---:|
| M1 | **Phan Trung Tín** *(Leader)* | 23120372 | Project Lead, Build MiniSum.exe, Bổ sung Theory, Tích hợp & Đóng gói | `feature/tin-setup-report` | 22 | **24.0h** | **20%** |
| M2 | **Nguyễn Lê Quang Kan** | 23120279 | Demo thực nghiệm Katalon Studio & Tài liệu kỹ thuật | `feature/kan-katalon` | 18 | **24.0h** | **20%** |
| M3 | **Bùi Quang Tùng** | 20120397 | Demo thực nghiệm WinAppDriver + C# NUnit & POM | `feature/tung-winappdriver` | 21 | **24.0h** | **20%** |
| M4 | **Trần Vũ Quang** | 23120346 | Thực nghiệm AI Automation & Đo đạc Comparison | `feature/quang-ai-comparison` | 17 | **24.0h** | **20%** |
| M5 | **Phạm Tấn Phát** | 20120636 | Thiết kế Slide PowerPoint toàn bộ (8 phần) | `feature/phat-slide` | 16 | **24.0h** | **20%** |
| **Tổng** | | | | | **94 tasks** | **120.0h** | **100%** |

---

## 📋 TỔNG QUAN TÌNH HÌNH (TRƯỚC LẦN 2)

| Hạng mục | Trạng thái Lần 1 | Cần làm thêm Lần 2 |
|---|---|---|
| Lý thuyết cơ bản (Theory) | ✅ Hoàn thành | 🔧 Bổ sung POM, Flaky Test, Explicit Wait (GV feedback) |
| Khảo sát Tool Survey | ✅ Hoàn thành | 🔧 Bổ sung nguyên lý hoạt động chi tiết của tool demo |
| So sánh Tool (Comparison) | ✅ Hoàn thành | 🔧 Cập nhật số liệu thực từ thực nghiệm |
| App mẫu MiniSum.exe | ❌ Chưa có | 🔴 Build mới WinForms C# (v1 + v2 + v3) |
| Demo Katalon Studio | ❌ Chưa có | 🔴 3 kịch bản: Record & Playback, Checkpoint, Data-driven |
| Demo WinAppDriver | ❌ Chưa có | 🔴 3 kịch bản: Basic, Assert + Screenshot, Data-driven POM |
| AI Demo thực tế | ❌ Chưa có | 🔴 2 kịch bản: Sinh test case BVA, Sinh test script |
| Video demo (YouTube) | ❌ Chưa có | 🔴 3 video riêng (Katalon / WinAppDriver / AI) |
| Slide PowerPoint | ❌ Chưa có | 🔴 Toàn bộ 8 phần, font to, nền trắng, biểu đồ |
| Git repo + commit log | ✅ Đã setup (27/10) | 🔧 Mỗi thành viên push lên branch riêng |
| AI usage declaration | ❌ Chưa có | 🔴 Kê khai đầy đủ theo quy định môn học |
| Báo cáo (report.md) | ✅ Bản thảo | 🔧 Cập nhật + tích hợp nội dung mới + export PDF |

---

## 📅 TIMELINE 4 NGÀY (27–30/10)

### 🗓️ NGÀY 1 – THỨ 3 (27/10): SETUP NỀN TẢNG *(Hôm nay)*

> **Mục tiêu:** Git repo sẵn sàng, mỗi người tạo branch, Tín bắt tay build MiniSum.

| Người | Task | Priority | Output |
|---|---|:---:|---|
| **Tín** | ✅ Init Git repo + push nội dung Lần 1 | 🔴 HIGH | Repo trên GitHub đã có |
| **Tín** | Tạo branch cho từng thành viên | 🔴 HIGH | 5 branches sẵn sàng |
| **Tín** | Bắt đầu code MiniSum v1 WinForms (Login + Calculator) | 🔴 HIGH | Project .sln khởi tạo |
| **Kan** | Clone repo, tạo branch `feature/kan-katalon`, cài Katalon Studio | 🟡 MED | Katalon Studio chạy được |
| **Tùng** | Clone repo, tạo branch `feature/tung-winappdriver`, cài WinAppDriver + Accessibility Insights | 🟡 MED | WinAppDriver.exe chạy được |
| **Quang** | Clone repo, tạo branch `feature/quang-ai-comparison`, đọc kỹ `07-ai-desktop-automation.md` + chuẩn bị prompt template | 🟡 MED | File `ai/prompts/minisum-spec.md` |
| **Phát** | Clone repo, tạo branch `feature/phat-slide`, tạo file `.pptx` với đầy đủ mục theo cấu trúc 8 phần | 🟡 MED | File `.pptx` khung có đủ mục |

---

### 🗓️ NGÀY 2 – THỨ 4 (28/10): DEMO CHÍNH + LÝ THUYẾT BỔ SUNG

> **Mục tiêu:** MiniSum.exe sẵn sàng, triển khai các kịch bản demo chính.

| Người | Task | Priority | Output |
|---|---|:---:|---|
| **Tín** | Hoàn thiện MiniSum v1 (Login + Calculator + Validation) | 🔴 HIGH | `MiniSum.exe` chạy được, commit lên branch |
| **Tín** | Build MiniSum v2 (đổi `btnSum` → `btnCalculate`, thêm Dashboard/History) | 🔴 HIGH | `MiniSum_v2.exe` commit lên branch |
| **Tín** | Bổ sung vào `docs/02-theory.md`: POM đầy đủ + Flaky Test + Explicit vs Implicit Wait | 🔴 HIGH | Section mới trong `02-theory.md` |
| **Tín** | Bổ sung vào `docs/02-theory.md`: Test Oracle + Recovery Testing | 🟡 MED | Section mới trong `02-theory.md` |
| **Kan** | Demo Katalon 1: Cài đặt + cấu hình WinAppDriver + mở MiniSum bằng Katalon | 🔴 HIGH | Screenshot từng bước |
| **Kan** | Demo Katalon 2: Record & Playback kịch bản đăng nhập hợp lệ + Checkpoint `lblMessage` | 🔴 HIGH | Script Katalon + ảnh PASS |
| **Kan** | Bắt đầu viết bổ sung nguyên lý Katalon: Object Repository, Object Spy, Session init vào `docs/04-katalon-studio.md` | 🟡 MED | Draft section kỹ thuật |
| **Tùng** | Demo WinAppDriver 1: Mở MiniSum.exe bằng `AppiumDriver`, kiểm tra session khởi tạo | 🔴 HIGH | Script C# cơ bản chạy được |
| **Tùng** | Demo WinAppDriver 2: Viết test login hợp lệ + `Assert.AreEqual` + test login sai | 🔴 HIGH | Script C# + ảnh PASS/FAIL |
| **Tùng** | Bắt đầu viết bổ sung nguyên lý WinAppDriver: UIAutomation, WinAPI, cách tìm element vào `docs/05-winappdriver.md` | 🟡 MED | Draft section kỹ thuật |
| **Quang** | AI Demo 1: Dùng ChatGPT/Gemini sinh 12 test case BVA từ đặc tả MiniSum | 🔴 HIGH | File `ai/output/bva-testcases.xlsx` |
| **Quang** | Lưu lại toàn bộ prompt đã dùng vào `ai/prompts/testcase-bva-prompt.md` | 🟡 MED | File prompt hoàn chỉnh |
| **Phát** | Điền nội dung Phần 1–3 vào Slide (Introduction + Theory + Tool Survey) | 🟡 MED | Slide 1-3 hoàn chỉnh |

---

### 🗓️ NGÀY 3 – THỨ 5 (29/10): HOÀN THIỆN + QUAY VIDEO

> **Mục tiêu:** Tất cả demo xong, quay video, Tín bắt đầu tích hợp báo cáo.

| Người | Task | Priority | Output |
|---|---|:---:|---|
| **Tín** | Bổ sung nguyên lý hoạt động Katalon (tham khảo từ Kan) vào `04-katalon-studio.md` | 🟡 MED | Section kỹ thuật hoàn chỉnh |
| **Tín** | Bổ sung nguyên lý hoạt động WinAppDriver (tham khảo từ Tùng) vào `05-winappdriver.md` | 🟡 MED | Section kỹ thuật hoàn chỉnh |
| **Tín** | Cập nhật `06-comparison.md` với số liệu thực (lấy từ Quang) | 🟡 MED | `06-comparison.md` cập nhật |
| **Tín** | Tổng hợp `report_v2.md` tích hợp toàn bộ nội dung mới | 🔴 HIGH | `report_v2.md` commit |
| **Kan** | Demo Katalon 2 (tiếp): Thêm ca đăng nhập sai + Checkpoint (`lblMessage` → "Sai!") | 🔴 HIGH | Script + ảnh FAIL có checkpoint |
| **Kan** | Demo Katalon 3: Data-driven Testing từ file Excel BVA (đọc file từ Quang) | 🔴 HIGH | Script DDT + Report HTML |
| **Kan** | Hoàn thiện phần nguyên lý Katalon trong `docs/04-katalon-studio.md` + chụp ảnh mô tả kiến trúc | 🟡 MED | Section kỹ thuật hoàn chỉnh |
| **Kan** | Quay video Demo Katalon (3 demo nối tiếp), thuyết minh tiếng Việt, nền trắng, chữ dễ đọc | 🔴 HIGH | Video Demo Katalon |
| **Tùng** | Demo WinAppDriver 3: Data-driven với `[TestCaseSource]` đọc từ file Excel BVA | 🔴 HIGH | Script C# DDT + kết quả |
| **Tùng** | Viết Page Object Model cho MiniSum: `LoginPage.cs` + `CalculatorPage.cs` | 🟡 MED | 2 file .cs trong repo |
| **Tùng** | Hoàn thiện phần nguyên lý WinAppDriver trong `docs/05-winappdriver.md` + ảnh kiến trúc | 🟡 MED | Section kỹ thuật hoàn chỉnh |
| **Tùng** | Quay video Demo WinAppDriver (3 demo nối tiếp), thuyết minh tiếng Việt | 🔴 HIGH | Video Demo WinAppDriver |
| **Quang** | AI Demo 2: Dùng ChatGPT/Gemini sinh test script C# / Katalon từ các test case đã có | 🔴 HIGH | Script AI-generated + đánh giá chất lượng |
| **Quang** | Đo thời gian: so sánh "viết test thủ công" vs "AI sinh" (đo thực tế 3 lượt) | 🔴 HIGH | Bảng số liệu thực nghiệm |
| **Quang** | Cập nhật `docs/06-comparison.md`: thêm cột "AI hỗ trợ", số liệu thực (thời gian, LOC, tỷ lệ phát hiện lỗi) | 🔴 HIGH | `06-comparison.md` v2 |
| **Quang** | Quay video AI Demo (prompt → sinh test case → sinh script → chạy kiểm tra kết quả) | 🔴 HIGH | Video Demo AI |
| **Phát** | Điền nội dung Phần 4–5 vào Slide (Katalon + WinAppDriver), chèn ảnh từ Kan và Tùng gửi | 🔴 HIGH | Slide 4-5 hoàn chỉnh |
| **Phát** | Điền nội dung Phần 6–8 vào Slide (Comparison + AI + Exercise) | 🟡 MED | Slide 6-8 hoàn chỉnh |

---

### 🗓️ NGÀY 4 – THỨ 6 SÁNG (30/10): ĐÓNG GÓI + NỘP BÀI

> **Mục tiêu:** Nộp bài trước 18:00.

| Người | Task | Priority | Output |
|---|---|:---:|---|
| **Kan** | Merge branch `feature/kan-katalon` → `main`, review xung đột | 🔴 HIGH | Code trên main |
| **Tùng** | Merge branch `feature/tung-winappdriver` → `main`, review xung đột | 🔴 HIGH | Code trên main |
| **Quang** | Merge branch `feature/quang-ai-comparison` → `main` | 🔴 HIGH | Code trên main |
| **Phát** | Merge branch `feature/phat-slide` → `main`, upload file `.pptx` + export PDF | 🔴 HIGH | Slide trên main |
| **Tín** | Upload 3 video lên YouTube (unlisted) | 🔴 HIGH | 3 link YouTube |
| **Tín** | Tạo `video-links.md` với đầy đủ 3 link + mô tả | 🔴 HIGH | File commit trên main |
| **Tín** | Chạy `git log --oneline --all > git-commit-log.md` | 🟡 MED | File `git-commit-log.md` |
| **Tín** | Viết `ai-usage-declaration.md` (kê khai AI đã dùng của cả nhóm) | 🔴 HIGH | File AI declaration |
| **Tín** | Export `report_v2.md` → `report_v2.pdf` | 🔴 HIGH | File PDF |
| **Tín** | Đóng gói ZIP: kiểm tra size ≤20MB/file, đặt tên đúng `Group02_ZipTool_Lan2.zip` | 🔴 HIGH | File ZIP nộp bài |
| **Tín** | Nộp bài lên hệ thống | 🔴 HIGH | ✅ Done |
| **Phát** | Thiết kế đẹp: kiểm tra font to, nền trắng, chữ đen, thêm biểu đồ so sánh | 🟡 MED | Slide final |
| **Phát** | Export Slide → PDF, đặt tên `seminar-final.pdf` | 🔴 HIGH | File PDF |

---

## 📋 DANH SÁCH CHI TIẾT 94 TASKS (CHIA ĐỀU 24.0h/NGƯỜI)

### 🧑‍💻 M1 – PHAN TRUNG TÍN (23120372) – Leader + Dev + Báo cáo
**Tổng: 22 tasks – 24.0h – 20% đóng góp**

| # | Task | Giờ | Output |
|---|---|:---:|---|
| T01 | ✅ Init Git repo, remote origin, push nội dung Lần 1 | 1.0 | Repo GitHub sẵn sàng |
| T02 | Tạo 5 branches riêng cho từng thành viên | 0.5 | 5 branches tạo sẵn |
| T03 | Build MiniSum v1: Login screen (user=admin/pass=1234) + Calculate screen (a+b=?) | 3.0 | `MiniSum.exe` chạy, có `btnLogin`, `txtUser`, `txtPass`, `btnSum`, `lblResult` |
| T04 | Build MiniSum v2: Đổi `btnSum` → `btnCalculate`, thêm Dashboard/History screen | 2.0 | `MiniSum_v2.exe` – demo maintenance & self-healing |
| T05 | Build MiniSum v3: Thêm validation (cảnh báo khi đầu vào không phải số) | 1.0 | `MiniSum_v3.exe` – demo negative test |
| T06 | Commit MiniSum source + 3 file .exe lên `case-study-app/` | 0.5 | Thư mục `case-study-app/MiniSum/` hoàn chỉnh |
| T07 | Viết `case-study-app/README.md`: hướng dẫn chạy app, yêu cầu .NET Runtime | 0.5 | README cho case study |
| T08 | Bổ sung `docs/02-theory.md`: Page Object Model (POM) – định nghĩa, ví dụ code, ưu điểm | 1.5 | Section POM trong theory |
| T09 | Bổ sung `docs/02-theory.md`: Flaky Test – định nghĩa, nguyên nhân, cách xử lý | 1.0 | Section Flaky Test trong theory |
| T10 | Bổ sung `docs/02-theory.md`: Explicit Wait vs Implicit Wait – so sánh chi tiết | 1.0 | Section Wait Strategy trong theory |
| T11 | Bổ sung `docs/02-theory.md`: Test Oracle – định nghĩa, phân loại | 0.5 | Section Test Oracle |
| T12 | Bổ sung `docs/02-theory.md`: Recovery Testing – định nghĩa + ví dụ | 0.5 | Section Recovery Testing |
| T13 | Tổng hợp `report_v2.md`: tích hợp toàn bộ nội dung mới từ Kan/Tùng/Quang/Phát | 3.5 | `report_v2.md` hoàn chỉnh |
| T14 | Export `report_v2.md` → `report_v2.pdf` (dùng Markdown to PDF / Pandoc) | 0.5 | File PDF |
| T15 | Cập nhật `docs/06-comparison.md` với số liệu thực từ Quang | 1.0 | Comparison v2 |
| T16 | Viết `video-links.md` với 3 link YouTube + mô tả nội dung từng video | 0.5 | File `video-links.md` |
| T17 | Chạy `git log --oneline --all > git-commit-log.md` và định dạng đẹp | 0.5 | File `git-commit-log.md` |
| T18 | Viết `ai-usage-declaration.md`: kê khai AI tools đã dùng (ChatGPT/Gemini/GitHub Copilot), mục đích, output | 1.0 | File AI declaration |
| T19 | Điền % contribution vào Google Sheets | 0.5 | Spreadsheet hoàn tất |
| T20 | Merge tất cả branches → main, giải quyết conflict | 1.5 | `main` branch sạch |
| T21 | Đóng gói ZIP cuối cùng, kiểm tra ≤20MB/file, đặt tên đúng quy định | 1.5 | `Group02_ZipTool_Lan2.zip` |
| T22 | Kiểm tra checklist nộp bài và nộp sản phẩm | 0.5 | ✅ Done |

---

### 🧑‍💻 M2 – NGUYỄN LÊ QUANG KAN (23120279) – Katalon Studio
**Tổng: 18 tasks – 24.0h – 20% đóng góp**

| # | Task | Giờ | Output |
|---|---|:---:|---|
| K01 | Clone repo, tạo branch `feature/kan-katalon`, cài Katalon Studio Free | 1.0 | Katalon Studio chạy được |
| K02 | Cài WinAppDriver service (dùng chung với Tùng), kiểm tra port 4723 | 0.5 | WinAppDriver service OK |
| K03 | Cấu hình Katalon kết nối WinAppDriver: `winappdriver://` URL, `platformName=Windows` | 1.0 | Profile cấu hình trong Katalon |
| K04 | Tìm hiểu + viết `docs/04-katalon-studio.md`: Kiến trúc thực thi (Session → Katalon Engine → WinAppDriver → AUT) | 2.0 | Section kiến trúc kỹ thuật |
| K05 | Tìm hiểu + viết: Object Repository – cách lưu, cách tìm element (XPath, Name, AutomationId) | 1.5 | Section Object Repository trong docs |
| K06 | Tìm hiểu + viết: Object Spy – cách sử dụng, chụp ảnh element | 1.0 | Section Object Spy trong docs |
| K07 | Tìm hiểu + viết: Test Suite, Test Case, Test Listener trong Katalon | 1.0 | Section cấu trúc project Katalon |
| K08 | **Demo 1:** Cài đặt từ đầu – mở MiniSum.exe bằng Katalon (chụp từng bước, không bỏ sót) | 2.0 | Screenshot step-by-step |
| K09 | **Demo 2a:** Record & Playback kịch bản đăng nhập hợp lệ (admin/1234) | 1.5 | Script Katalon + ảnh PASS |
| K10 | **Demo 2b:** Thêm Checkpoint xác minh `lblMessage` = "Đăng nhập thành công!" | 1.0 | Script + ảnh Checkpoint PASS |
| K11 | **Demo 2c:** Thêm ca đăng nhập sai (admin/wrong) + Checkpoint `lblMessage` = "Sai!" | 1.0 | Script + ảnh Checkpoint FAIL |
| K12 | **Demo 3a:** Tạo file Excel BVA với 12 test case (nhận từ Quang hoặc tự tạo) | 1.0 | File `bva-testcases.xlsx` |
| K13 | **Demo 3b:** Data-driven Testing: đọc Excel, chạy 12 test case tự động | 3.0 | Script DDT + Report HTML |
| K14 | **Demo 3c (Bonus):** Keyword-driven / Custom keyword: tạo `LoginKeyword.groovy` tái sử dụng | 2.0 | Script keyword tái sử dụng |
| K15 | Chụp ảnh toàn bộ kết quả PASS/FAIL, lưu vào `docs/screenshots/katalon/` | 1.0 | Thư mục ảnh |
| K16 | Quay video Demo Katalon (3 demo nối tiếp): thuyết minh tiếng Việt, nền trắng, font dễ đọc | 2.0 | Video file gửi Tín upload |
| K17 | Review toàn bộ script Katalon, chuẩn hóa comment (tiếng Việt), commit | 1.0 | Code sạch trên branch |
| K18 | Tạo Pull Request và merge branch `feature/kan-katalon` → `main` | 0.5 | ✅ Merge |

---

### 🧑‍💻 M3 – BÙI QUANG TÙNG (20120397) – WinAppDriver + C# NUnit
**Tổng: 21 tasks – 24.0h – 20% đóng góp**

| # | Task | Giờ | Output |
|---|---|:---:|---|
| W01 | Clone repo, tạo branch `feature/tung-winappdriver`, cài WinAppDriver v1.2.1+ | 0.5 | WinAppDriver.exe chạy được |
| W02 | Cài Accessibility Insights for Windows, tìm `AutomationId` các element của MiniSum | 0.5 | Danh sách AutomationId |
| W03 | Tạo project C# NUnit trong Visual Studio: `MiniSumTests.csproj` | 1.0 | Project VS khởi tạo trong `demo-scripts/winappdriver/` |
| W04 | Thêm package: `Appium.WebDriver`, `NUnit`, `NUnit3TestAdapter`, `NPOI` | 0.5 | `MiniSumTests.csproj` có dependencies |
| W05 | Tìm hiểu + viết `docs/05-winappdriver.md`: Kiến trúc (WinAppDriver → UI Automation API → Win32 → AUT) | 1.5 | Section kiến trúc kỹ thuật |
| W06 | Tìm hiểu + viết: Cách tìm element bằng `FindElementByAccessibilityId`, `FindElementByName`, `FindElementByXPath` | 1.0 | Section tìm element trong docs |
| W07 | Tìm hiểu + viết: Session – cách khởi tạo `AppiumOptions`, `AppiumDriver`, session lifecycle | 1.0 | Section Session trong docs |
| W08 | Tìm hiểu + viết: Screenshot on Fail – `GetScreenshot()`, lưu ảnh khi test fail | 1.0 | Section Screenshot trong docs |
| W09 | **Demo 1:** Khởi tạo session, mở MiniSum.exe bằng code, đóng app | 1.5 | Script `Demo1_OpenApp.cs` + ảnh |
| W10 | **Demo 2a:** Viết test method đăng nhập hợp lệ (admin/1234) + `Assert.AreEqual("Đăng nhập thành công!", lblText)` | 1.5 | `Demo2_LoginTest.cs` + ảnh PASS |
| W11 | **Demo 2b:** Thêm test method đăng nhập sai (admin/wrong) + `Assert.AreEqual("Sai!", lblText)` | 1.0 | `Demo2_LoginTest.cs` bổ sung + ảnh FAIL |
| W12 | **Demo 2c:** Tự động chụp ảnh màn hình khi test FAIL (implement `TearDown`) | 1.0 | Logic `TearDown` + ảnh auto-captured |
| W13 | **Demo 3a:** Tạo file Excel BVA (dùng chung với Kan), hàm đọc Excel bằng NPOI | 1.5 | `ExcelHelper.cs` |
| W14 | **Demo 3b:** Data-driven với `[TestCaseSource]`: chạy 12 BVA case từ Excel | 2.5 | `Demo3_DDT.cs` + Report |
| W15 | Viết `LoginPage.cs` (Page Object Model): gom toàn bộ thao tác Login vào 1 class | 1.5 | `LoginPage.cs` trong `demo-scripts/winappdriver/PageObjects/` |
| W16 | Viết `CalculatorPage.cs` (Page Object Model): gom thao tác Calculator | 1.5 | `CalculatorPage.cs` |
| W17 | Refactor `Demo2_LoginTest.cs` để dùng `LoginPage` (thể hiện lợi ích POM) | 1.0 | Code refactored |
| W18 | Chụp ảnh toàn bộ PASS/FAIL, lưu vào `docs/screenshots/winappdriver/` | 1.0 | Thư mục ảnh |
| W19 | Quay video Demo WinAppDriver (3 demo nối tiếp): thuyết minh tiếng Việt | 2.0 | Video file gửi Tín upload |
| W20 | Review toàn bộ code C#, chuẩn hóa comment + xmldoc, commit | 1.0 | Code sạch trên branch |
| W21 | Tạo Pull Request và merge branch `feature/tung-winappdriver` → `main` | 0.5 | ✅ Merge |

---

### 🧑‍💻 M4 – TRẦN VŨ QUANG (23120346) – AI Demo + Comparison
**Tổng: 17 tasks – 24.0h – 20% đóng góp**

| # | Task | Giờ | Output |
|---|---|:---:|---|
| Q01 | Clone repo, tạo branch `feature/quang-ai-comparison`, phân tích yêu cầu Prompt Engineering | 1.0 | Hiểu sâu kỹ thuật prompt cho desktop app |
| Q02 | Viết đặc tả chức năng MiniSum (domain, boundaries, error cases) vào `ai/prompts/minisum-spec.md` | 1.5 | File đặc tả hoàn chỉnh |
| Q03 | Thiết kế prompt "Sinh test case BVA": Zero-shot & Few-shot prompt engineering | 1.5 | Prompt tại `ai/prompts/testcase-bva-prompt.md` |
| Q04 | **AI Demo 1a:** Chạy prompt với ChatGPT-4 → multi-turn refinement | 1.5 | File `ai/output/chatgpt-bva-output.md` |
| Q05 | **AI Demo 1b:** Chạy cùng prompt với Claude / Gemini để so sánh độ chính xác | 1.5 | File `ai/output/gemini-bva-output.md` |
| Q06 | Đánh giá chất lượng test case AI sinh: độ phủ biên, lỗi logic, hallucination | 1.5 | Bảng đánh giá trong `ai/output/bva-evaluation.md` |
| Q07 | Xuất file Excel từ test case AI sinh (12 test case chuẩn hóa cho Kan và Tùng) | 1.0 | `ai/output/bva-testcases.xlsx` |
| Q08 | Thiết kế prompt "Sinh test script C# / Katalon" kèm ràng buộc POM | 1.5 | Prompt tại `ai/prompts/script-gen-prompt.md` |
| Q09 | **AI Demo 2a:** Chạy prompt với ChatGPT → ghi lại script C# sinh ra | 1.5 | `ai/output/chatgpt-script-output.cs` |
| Q10 | **AI Demo 2b:** Chạy script C# do AI sinh, debug sửa lỗi cú pháp & locator | 2.0 | Script đã verified + ghi chú chỉnh sửa |
| Q11 | **Đo thực nghiệm:** Ghi chép thời gian viết thủ công vs AI sinh (đo 3 lượt) | 1.5 | Bảng số liệu định lượng |
| Q12 | **Đo thực nghiệm:** Đếm số dòng code (LOC), độ phức tạp và tỷ lệ code sửa lại | 1.0 | Số liệu LOC & phân tích |
| Q13 | Cập nhật `docs/06-comparison.md`: thêm cột "AI hỗ trợ", biểu đồ thời gian & LOC | 2.5 | Comparison v2 có số liệu thực |
| Q14 | Cập nhật `docs/07-ai-desktop-automation.md`: tổng hợp bài học thực tế khi dùng AI | 1.5 | Section "Kết quả thực nghiệm nhóm" |
| Q15 | Quay video AI Demo (nối tiếp 2 demo): prompt → output → verify → số liệu so sánh | 2.0 | Video file gửi Tín upload |
| Q16 | Quản lý lưu trữ prompt + output vào các file `ai/prompts/` và `ai/output/` | 1.0 | Thư mục AI đầy đủ |
| Q17 | Tạo Pull Request và merge branch `feature/quang-ai-comparison` → `main` | 0.5 | ✅ Merge |

---

### 🧑‍💻 M5 – PHẠM TẤN PHÁT (20120636) – Slide PowerPoint
**Tổng: 16 tasks – 24.0h – 20% đóng góp**

| # | Task | Giờ | Output |
|---|---|:---:|---|
| P01 | Clone repo, tạo branch `feature/phat-slide`, đọc toàn bộ 9 file `.md` trong `docs/` | 1.5 | Hiểu đầy đủ nội dung báo cáo |
| P02 | Tạo file `slides/seminar-group02.pptx` với layout chuẩn: nền trắng, font ≥18pt, chữ đen | 1.0 | File PPTX khung |
| P03 | **Slide Phần 1 (5-7 slide):** Introduction – Giới thiệu đề tài, mục tiêu, phạm vi seminar | 1.5 | Slide 1 hoàn chỉnh |
| P04 | **Slide Phần 2 (8-10 slide):** Theory – UI Automation, AUT, UIA API, POM, Flaky Test, Wait | 2.5 | Slide 2 hoàn chỉnh |
| P05 | **Slide Phần 3 (5-6 slide):** Tool Survey – Bức tranh công cụ tổng quan, bảng so sánh sơ bộ | 1.5 | Slide 3 hoàn chỉnh |
| P06 | **Slide Phần 4 (8-10 slide):** Katalon Studio – Kiến trúc, Object Spy, 3 Demo (ảnh từ Kan) | 2.5 | Slide 4 hoàn chỉnh |
| P07 | **Slide Phần 5 (8-10 slide):** WinAppDriver – Kiến trúc, UIAutomation, 3 Demo (ảnh từ Tùng) | 2.5 | Slide 5 hoàn chỉnh |
| P08 | **Slide Phần 6 (5-6 slide):** Comparison – Bảng so sánh đầy đủ, phân tích định tính & định lượng | 2.0 | Slide 6 hoàn chỉnh |
| P09 | **Slide Phần 7 (5-6 slide):** AI Demo – Prompt engineering, output, so sánh AI vs thủ công | 2.0 | Slide 7 hoàn chỉnh |
| P10 | **Slide Phần 8 (3-4 slide):** Exercises – Hệ thống câu hỏi, bài tập thực hành | 1.0 | Slide 8 hoàn chỉnh |
| P11 | Thiết kế slide kết/tổng kết (Q&A, kết luận, tài liệu tham khảo, cảm ơn) | 1.0 | Slide kết hoàn chỉnh |
| P12 | Chèn ảnh screenshot từ Kan (Katalon) + Tùng (WinAppDriver) + Quang (AI) vào đúng phần | 2.0 | Ảnh minh họa đúng chỗ |
| P13 | Thêm biểu đồ so sánh tại Phần 6 (Bar chart: thời gian, LOC, tỷ lệ phát hiện lỗi) | 1.0 | Biểu đồ trực quan |
| P14 | Review toàn bộ slide: font to, nền trắng, chữ đen, không rối, không quá chữ/slide | 2.0 | Slide final review |
| P15 | Export `seminar-group02.pptx` → `seminar-final.pdf` | 0.5 | File PDF |
| P16 | Tạo Pull Request và merge branch `feature/phat-slide` → `main` | 0.5 | ✅ Merge |

---

## 🌿 QUY TRÌNH LÀM VIỆC NHÓM VỚI GIT

### Tạo branch và làm việc

```bash
# Mỗi thành viên tự tạo branch của mình từ main
git checkout main
git pull origin main
git checkout -b feature/[tên-branch]

# Làm việc, commit thường xuyên với message rõ ràng
git add .
git commit -m "feat(kan): add Katalon Object Repository technical section"
git push origin feature/kan-katalon
```

### Quy ước commit message (Conventional Commits)
```
feat(kan):    Thêm tính năng / script / tài liệu mới (Kan)
fix(tung):    Sửa lỗi script (Tùng)
docs(tin):    Cập nhật tài liệu markdown (Tín)
demo(quang):  Thêm file demo AI (Quang)
slide(phat):  Cập nhật slide (Phát)
chore(tin):   Task admin (setup, packaging, merge)
```

### Merge vào main (Ngày 4 – 30/10)
```bash
# Tín merge tất cả khi mọi người đã push xong
git checkout main
git pull origin main
git merge feature/kan-katalon
git merge feature/tung-winappdriver
git merge feature/quang-ai-comparison
git merge feature/phat-slide
git push origin main
```

---

## ✅ CHECKLIST NỘP BÀI LẦN 2

Trước khi nộp, Tín kiểm tra lần lượt:

- [ ] **Báo cáo:** `report_v2.md` + `report_v2.pdf` (có đủ 9 phần, cập nhật nguyên lý tool)
- [ ] **Slide:** `seminar-group02.pptx` + `seminar-final.pdf` (font to, nền trắng, chữ đen, biểu đồ)
- [ ] **Video links:** `video-links.md` có đủ 3 link YouTube (Katalon / WinAppDriver / AI)
- [ ] **Source code Katalon:** `demo-scripts/katalon/` có đủ script 3 demo
- [ ] **Source code WinAppDriver:** `demo-scripts/winappdriver/` có `MiniSumTests.csproj` + PageObjects
- [ ] **AI output:** `ai/prompts/` + `ai/output/` có đủ file prompt + kết quả + Excel BVA
- [ ] **App mẫu:** `case-study-app/MiniSum.exe` + `MiniSum_v2.exe` + `MiniSum_v3.exe` + README
- [ ] **Git commit log:** `git-commit-log.md` (chạy `git log --oneline --all`)
- [ ] **AI usage:** `ai-usage-declaration.md` (kê khai đầy đủ)
- [ ] **Contribution:** Đã điền vào Google Sheets (20% đều cho cả 5 người)
- [ ] **File size:** Mỗi file ≤20MB. Nếu không → dùng 7-Zip chia nhỏ
- [ ] **Tên file ZIP:** Chứa chữ "ZipTool": `Group02_ZipTool_Lan2.zip`
- [ ] **Số file:** ≥20 files tổng cộng

---

## 📊 BẢNG TỔNG HỢP PHÂN PHỐI % CONTRIBUTION (CHIA ĐỀU)

| Thành viên | MSSV | Vai trò chính | Tasks | Giờ ước tính | % Gợi ý |
|---|:---:|---|:---:|:---:|:---:|
| **Phan Trung Tín** | 23120372 | Leader, Build App, Bổ sung Theory, Tích hợp & Nộp | 22 | **24.0h** | **20.0%** |
| **Nguyễn Lê Quang Kan** | 23120279 | Demo thực nghiệm Katalon Studio & Tài liệu kỹ thuật | 18 | **24.0h** | **20.0%** |
| **Bùi Quang Tùng** | 20120397 | Demo thực nghiệm WinAppDriver + C# NUnit & POM | 21 | **24.0h** | **20.0%** |
| **Trần Vũ Quang** | 23120346 | Demo thực nghiệm AI Test Automation & Comparison | 17 | **24.0h** | **20.0%** |
| **Phạm Tấn Phát** | 20120636 | Thiết kế Slide thuyết trình PowerPoint toàn bộ (8 phần) | 16 | **24.0h** | **20.0%** |
| **Tổng cộng** | | | **94 tasks** | **120.0h** | **100.0%** |

> 💡 **Kết luận:** Kế hoạch đã được cân bằng chính xác **24.0 giờ** và **20.0%** cho mỗi thành viên trong nhóm, đảm bảo công bằng, rõ ràng trách nhiệm và minh bạch trên Git commit history.
