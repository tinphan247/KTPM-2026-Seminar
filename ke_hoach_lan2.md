# KẾ HOẠCH SEMINAR LẦN 2 – Group 02 (ZipTool)
# Chủ đề: Automation Testing for Desktop Applications
# Deadline nộp: 29–30/10/2026 (trước 31/10)

---

## 📋 TỔNG QUAN TÌNH HÌNH

| Hạng mục | Trạng thái Lần 1 | Cần làm thêm Lần 2 |
|---|---|---|
| Lý thuyết cơ bản (Theory) | ✅ Hoàn thành | 🔧 Bổ sung khái niệm theo GV feedback |
| Khảo sát Tool Survey | ✅ Hoàn thành | 🔧 Bổ sung nguyên lý hoạt động tool demo |
| So sánh Tool (Comparison) | ✅ Hoàn thành | ✅ Dùng lại |
| App mẫu MiniSum.exe | ❌ Chưa có | 🔴 Phải build mới |
| Kịch bản demo Katalon | ❌ Chưa có | 🔴 Phải làm mới |
| Kịch bản demo WinAppDriver | ❌ Chưa có | 🔴 Phải làm mới |
| AI demo thực tế | ❌ Chưa có | 🔴 Phải làm mới |
| Video demo (YouTube) | ❌ Chưa có | 🔴 Phải làm mới |
| Slide PowerPoint | ❌ Chưa có | 🔴 Phải làm mới |
| Git repo chung | ❌ Chưa có | 🔴 Phải setup ngay |
| Git commit log (Markdown) | ❌ Chưa có | 🔴 Phải làm mới |
| AI usage declaration | ❌ Chưa có | 🔴 Phải làm mới |
| Bài tập thực hành (08-exercises.md) | ✅ Hoàn thành | ✅ Dùng lại |
| Báo cáo toàn văn (report.md) | ✅ Bản thảo đầy đủ | 🔧 Cập nhật + export PDF |

---

## 👥 PHÂN CÔNG THÀNH VIÊN – LẦN 2

| Thành viên | Vai trò Lần 2 | Trách nhiệm chính | Ước tính giờ |
|---|---|---|---|
| **Tín (Leader)** | M1 + Project Setup + MiniSum Dev | Setup Git repo, build MiniSum.exe & v2.exe, bổ sung lý thuyết GV yêu cầu, tích hợp báo cáo cuối | ~20h |
| **Kan** | M2 – Katalon Studio Demo | Cài Katalon, thực nghiệm 3 nhóm demo, quay video, viết nguyên lý hoạt động | ~16h |
| **Tùng** | M3 – WinAppDriver Demo | Cài WinAppDriver + Accessibility Insights, viết script C#/Python, thực nghiệm 3 nhóm demo, quay video | ~16h |
| **Quang** | M4 – AI Demo + Comparison | Thực hiện AI demo thực tế (GenAI sinh test script + Self-healing), cập nhật comparison với số liệu thực | ~14h |
| **Phát (Mới)** | M5 – Slide + Git | Thiết kế Slide PowerPoint toàn bộ dựa trên các file .md, quản lý Git commit log, AI usage declaration | ~12h |

---

## 📅 TIMELINE 4 NGÀY (27–30/10)

### 🗓️ NGÀY 1 – THỨ 3 (27/10): SETUP NỀN TẢNG

> **Mục tiêu:** Tất cả có thể làm việc song song từ ngày 2.

| Người | Task | Output |
|---|---|---|
| **Tín** | [STEP 1] Tạo GitHub repo (xem hướng dẫn bên dưới) | Repo `Group02-ZipTool-Seminar` đã có |
| **Tín** | [STEP 2] Commit toàn bộ nội dung Lần 1 lên repo | Mọi .md file đã lên GitHub |
| **Tín** | [STEP 3] Bắt đầu build MiniSum.exe (WinForms C#) | Nháp đầu tiên chạy được |
| **Phát** | Clone repo, tìm hiểu template Slide, tạo file .pptx khung | File Slide khung có đầy đủ mục |
| **Kan** | Cài đặt Katalon Studio + WinAppDriver service | Chụp ảnh màn hình confirm cài xong |
| **Tùng** | Cài đặt WinAppDriver, Accessibility Insights, VS + NUnit | Chụp ảnh màn hình confirm cài xong |
| **Quang** | Đọc lại `07-ai-desktop-automation.md`, chuẩn bị prompt template | File `ai/prompts/testcase-gen.md` nháp |

---

### 🗓️ NGÀY 2 – THỨ 4 (28/10): DEMO CHÍNH + LÝ THUYẾT BỔ SUNG

> **Mục tiêu:** Có app mẫu + ít nhất 1 tool demo hoàn chỉnh.

| Người | Task | Output |
|---|---|---|
| **Tín** | Hoàn thiện MiniSum.exe v1 + v2 (đổi btnSum → btnCalculate) | 2 file .exe commit lên repo |
| **Tín** | Bổ sung lý thuyết theo GV feedback (xem mục chi tiết bên dưới) | `02-theory-v2.md` hoặc cập nhật trực tiếp |
| **Kan** | Demo 1: Cài đặt Katalon + mở MiniSum | Ảnh chụp màn hình từng bước |
| **Kan** | Demo 2: Record & Playback login + Checkpoint | Script Katalon + ảnh PASS |
| **Tùng** | Demo 1: Cài WinAppDriver + mở MiniSum bằng code | Script C# cơ bản chạy được |
| **Tùng** | Demo 2: Tìm phần tử bằng Accessibility Insights + viết test login | Script C# + ảnh PASS |
| **Quang** | AI Demo 1: Dùng ChatGPT/Gemini sinh test case BVA từ đặc tả | File Excel BVA_TestData.xlsx (AI sinh) |
| **Phát** | Điền nội dung Phần 1-3 vào Slide (dựa trên các .md file) | Slide Part 1: Introduction + Theory + Tool Survey |

---

### 🗓️ NGÀY 3 – THỨ 5 (29/10): HOÀN THIỆN + QUAY VIDEO

> **Mục tiêu:** Tất cả demo xong, bắt đầu quay video.

| Người | Task | Output |
|---|---|---|
| **Tín** | Bổ sung nguyên lý hoạt động tool demo vào `04-katalon-studio.md` và `05-winappdriver.md` | Phần mới: kiến trúc thực thi chi tiết hơn |
| **Tín** | Tổng hợp báo cáo toàn văn cập nhật (report.md v2) | `report_v2.md` commit |
| **Kan** | Demo 3: Data-driven với file Excel BVA | Script DDT + Report HTML |
| **Kan** | Quay video demo Katalon (3 demo) | `demo-katalon.mp4` |
| **Tùng** | Demo 3: Data-driven với NUnit [TestCaseSource] từ Excel | Script C# DDT + kết quả |
| **Tùng** | Quay video demo WinAppDriver (3 demo) | `demo-winappdriver.mp4` |
| **Quang** | AI Demo 2: Dùng AI sinh script Katalon/C# từ test case | File script AI-generated + đánh giá |
| **Quang** | Cập nhật comparison với số liệu thực (giờ chạy, dòng code) | `06-comparison-v2.md` |
| **Phát** | Điền nội dung Phần 4-8 vào Slide (Tool A, Tool B, AI, Comparison, Exercise) | Slide gần hoàn chỉnh |

---

### 🗓️ NGÀY 4 – THỨ 6 SÁNG (30/10): ĐÓNG GÓI + NỘP BÀI

> **Mục tiêu:** Nộp bài trước 18:00.

| Người | Task | Output |
|---|---|---|
| **Tín** | Upload 3 video lên YouTube (unlisted) | 3 link YouTube |
| **Tín** | Tạo `video-links.md` + `git-commit-log.md` | 2 file commit lên repo |
| **Tín** | Tạo `ai-usage-declaration.md` | File khai báo AI |
| **Tín** | Export báo cáo ra PDF | `report_v2.pdf` |
| **Phát** | Hoàn thiện Slide + export PDF | `seminar-final.pptx` + `.pdf` |
| **Quang** | Viết `video-links.md` + cập nhật contribution sheet | Google Sheets điền xong |
| **Tín** | Đóng gói ZIP (tên file có "ZipTool") + nộp | `Group02_ZipTool_Lan2.zip` |

---

## 🎯 CHI TIẾT CÔNG VIỆC BỔ SUNG THEO GV FEEDBACK

### A. Bổ sung "Nguyên lý hoạt động của tool demo"

Lần 1 đã có sơ đồ kiến trúc, nhưng GV muốn **chi tiết hơn về quá trình thực thi**. Cần bổ sung vào `04-katalon-studio.md` và `05-winappdriver.md`:

**Cho Katalon Studio:**
- Giải thích chi tiết hơn giao thức HTTP/JSON Wire giữa Katalon → WinAppDriver
- Vòng đời 1 test step: từ lúc Katalon gửi lệnh → WinAppDriver nhận → UIA xử lý → phản hồi
- Cách Katalon chụp ảnh màn hình khi test fail
- Cách WinAppDriver Server khởi động (port 4723, log)

**Cho WinAppDriver:**
- Giải thích chi tiết DesiredCapabilities: `app`, `platformName`, `deviceName`
- Cách WindowsDriver session được tạo và hủy
- Cách tìm phần tử bằng `FindElement(By.AccessibilityId("btnSum"))` trên thực tế

### B. Bổ sung "Lý thuyết – Khái niệm còn thiếu"

Xem lại `02-theory.md` và bổ sung thêm:
- **Page Object Model (POM)** – mô hình thiết kế kịch bản bền vững (hiện chỉ đề cập nhắc qua)
- **Flaky Test** – định nghĩa đầy đủ + nguyên nhân + cách phòng tránh
- **Explicit Wait vs Implicit Wait vs Thread.Sleep** – bảng so sánh cụ thể
- **Test Oracle** – khái niệm chi tiết hơn (hiện chỉ đề cập trong Checkpoint section)
- **Locator Strategy hierarchy** – bảng ưu tiên AutomationId > Name > ClassName > XPath (có số liệu về performance)

---

## 🛠️ HƯỚNG DẪN SETUP GIT REPO TỪNG BƯỚC

### Bước 1: Tạo Repository trên GitHub

```bash
# Trên trình duyệt: github.com → New Repository
# Tên: Group02-ZipTool-Seminar
# Visibility: Private (thêm thành viên sau) hoặc Public
# Tick vào: Add a README file
# License: MIT
```

### Bước 2: Clone về máy Tín (Leader)

```bash
# Mở Git Bash hoặc PowerShell
git clone https://github.com/[username]/Group02-ZipTool-Seminar.git
cd Group02-ZipTool-Seminar
```

### Bước 3: Copy toàn bộ nội dung Lần 1 vào repo

```bash
# Copy tất cả file từ C:\HCMUS\hk7\Testing\seminar\Group02_ZipTool\Group02_ZipTool\
# vào thư mục repo vừa clone

# Tạo cấu trúc thư mục chuẩn
mkdir docs
mkdir demo-scripts
mkdir demo-scripts\katalon
mkdir demo-scripts\winappdriver
mkdir demo-scripts\ai
mkdir case-study-app
mkdir slides
mkdir ai
mkdir exercises
mkdir reviews
mkdir videos
```

### Bước 4: Cấu trúc thư mục repo đề xuất

```
Group02-ZipTool-Seminar/
├── README.md
├── docs/                          ← Tài liệu .md chính
│   ├── 01-introduction.md
│   ├── 02-theory.md
│   ├── 03-toolsurvey.md
│   ├── 04-katalon-studio.md
│   ├── 05-winappdriver.md
│   ├── 06-comparison.md
│   ├── 07-ai-desktop-automation.md
│   ├── 08-exercises.md
│   └── report.md
├── case-study-app/               ← MiniSum source code + .exe
│   ├── MiniSum/                  ← Visual Studio project
│   ├── MiniSum.exe
│   └── MiniSum_v2.exe
├── demo-scripts/
│   ├── katalon/                  ← Katalon project
│   └── winappdriver/             ← C# NUnit project
├── ai/
│   ├── prompts/
│   └── output/
├── slides/
│   └── seminar-final.pptx
├── git-commit-log.md
├── video-links.md
└── ai-usage-declaration.md
```

### Bước 5: Commit toàn bộ nội dung Lần 1

```bash
# Sau khi copy file xong
git add .
git commit -m "feat: add Round 1 content - theory, tool survey, comparison, exercises"
git push origin main
```

### Bước 6: Thêm thành viên vào repo

```
GitHub → Settings → Collaborators → Add people
Thêm: Kan, Tùng, Quang, Phát (bằng email hoặc username GitHub)
```

### Bước 7: Mỗi thành viên clone về máy mình

```bash
git clone https://github.com/[username]/Group02-ZipTool-Seminar.git
```

### Bước 8: Quy trình làm việc hàng ngày

```bash
# Trước khi làm việc: luôn pull mới nhất
git pull origin main

# Sau khi làm xong 1 task: commit ngay
git add [file bạn sửa]
git commit -m "feat(katalon): add demo 1 installation script + screenshots"
# Prefix commit: feat (tính năng mới), fix (sửa lỗi), docs (tài liệu)

# Push lên
git push origin main
```

---

## 📦 DANH SÁCH 50 TASK CHO SPREADSHEET (Google Sheets)

> Copy danh sách này vào Sheet 2 của file Google Sheets.

| No | Student | Task Description | Hours |
|---|---|---|---|
| 1 | Tín | Setup GitHub repo + cấu trúc thư mục + thêm thành viên | 1 |
| 2 | Tín | Commit toàn bộ nội dung Lần 1 lên repo | 1 |
| 3 | Tín | Build MiniSum v1 (WinForms C#): Login screen + Calculation screen | 3 |
| 4 | Tín | Build MiniSum v2 (đổi btnSum → btnCalculate để demo maintenance) | 1 |
| 5 | Tín | Bổ sung nguyên lý hoạt động Katalon vào 04-katalon-studio.md | 2 |
| 6 | Tín | Bổ sung nguyên lý hoạt động WinAppDriver vào 05-winappdriver.md | 2 |
| 7 | Tín | Bổ sung khái niệm POM vào 02-theory.md | 1 |
| 8 | Tín | Bổ sung khái niệm Flaky Test + Explicit Wait vào 02-theory.md | 1 |
| 9 | Tín | Cập nhật report.md v2 tích hợp toàn bộ nội dung mới | 2 |
| 10 | Tín | Export báo cáo ra PDF | 0.5 |
| 11 | Tín | Upload 3 video lên YouTube (unlisted) | 1 |
| 12 | Tín | Viết video-links.md | 0.5 |
| 13 | Tín | Viết ai-usage-declaration.md | 1 |
| 14 | Tín | Tạo git-commit-log.md (export log từ git log) | 0.5 |
| 15 | Tín | Đóng gói ZIP + kiểm tra file size + nộp bài | 1 |
| 16 | Kan | Cài đặt Katalon Studio Free + WinAppDriver Service | 1 |
| 17 | Kan | Demo 1 Katalon: Cài đặt môi trường + cấu hình WinAppDriver port | 2 |
| 18 | Kan | Demo 2 Katalon: Record & Playback kịch bản đăng nhập hợp lệ | 2 |
| 19 | Kan | Demo 2 Katalon: Thêm Checkpoint xác minh lblMessage | 1 |
| 20 | Kan | Demo 2 Katalon: Thêm ca đăng nhập sai + Checkpoint | 1 |
| 21 | Kan | Demo 3 Katalon: Data-driven Testing từ file Excel BVA | 3 |
| 22 | Kan | Viết mô tả nguyên lý Object Repository và Object Spy chi tiết | 1 |
| 23 | Kan | Chụp ảnh màn hình + ghi lại kết quả PASS/FAIL tất cả demo | 1 |
| 24 | Kan | Quay video Demo Katalon (3 demo), đúng yêu cầu: nền trắng, chữ đen, thuyết minh | 2 |
| 25 | Kan | Review toàn bộ script Katalon, chuẩn hóa comment | 1 |
| 26 | Tùng | Cài đặt WinAppDriver + Accessibility Insights for Windows | 1 |
| 27 | Tùng | Cài đặt Visual Studio + NUnit Test Project | 1 |
| 28 | Tùng | Demo 1 WinAppDriver: Mở MiniSum.exe, kiểm tra session khởi tạo | 2 |
| 29 | Tùng | Demo 2 WinAppDriver: Viết test login hợp lệ + Assert.AreEqual | 2 |
| 30 | Tùng | Demo 2 WinAppDriver: Thêm ca login sai + Assert | 1 |
| 31 | Tùng | Demo 3 WinAppDriver: Data-driven với [TestCaseSource] từ Excel | 3 |
| 32 | Tùng | Viết Page Object Model cho MiniSum (LoginPage + CalculatorPage) | 2 |
| 33 | Tùng | Chụp ảnh màn hình PASS/FAIL tất cả test WinAppDriver | 1 |
| 34 | Tùng | Quay video Demo WinAppDriver (3 demo), đúng yêu cầu | 2 |
| 35 | Tùng | Review code C# NUnit, chuẩn hóa comment | 1 |
| 36 | Quang | AI Demo 1: Prompt ChatGPT/Gemini sinh 12 test case BVA từ đặc tả | 2 |
| 37 | Quang | AI Demo 1: Xuất kết quả vào BVA_TestData.xlsx + đánh giá độ chính xác | 1 |
| 38 | Quang | AI Demo 1: Prompt sinh script Katalon (Groovy) từ test case | 2 |
| 39 | Quang | AI Demo 1: Review và chạy thử script do AI sinh ra | 1 |
| 40 | Quang | AI Demo 2: Demo Self-healing - chạy kịch bản cũ trên MiniSum_v2 (FAIL) | 1 |
| 41 | Quang | AI Demo 2: Dùng AI đề xuất locator mới (btnCalculate) + chạy lại (PASS) | 2 |
| 42 | Quang | Cập nhật 06-comparison.md với số liệu thực (thời gian chạy, dòng code) | 2 |
| 43 | Quang | Quay video AI demo (2 demo) | 2 |
| 44 | Quang | Điền contribution percentage vào Google Sheets | 0.5 |
| 45 | Phát | Tạo file Slide khung .pptx đầy đủ mục theo cấu trúc báo cáo | 1 |
| 46 | Phát | Điền nội dung Phần 1-3 vào Slide (Introduction + Theory + Tool Survey) | 3 |
| 47 | Phát | Điền nội dung Phần 4-5 vào Slide (Katalon + WinAppDriver) | 3 |
| 48 | Phát | Điền nội dung Phần 6-8 vào Slide (Comparison + AI + Exercise) | 2 |
| 49 | Phát | Thiết kế đẹp slide: font lớn, nền trắng, chữ đen (theo yêu cầu GV) | 2 |
| 50 | Phát | Export Slide ra PDF + final review | 1 |

---

## ✅ CHECKLIST NỘP BÀI LẦN 2

Trước khi nộp, Tín kiểm tra lần lượt:

- [ ] **Báo cáo:** `report_v2.md` + `report_v2.pdf` (có đủ 9 phần, cập nhật nguyên lý tool)
- [ ] **Slide:** `seminar-final.pptx` + `seminar-final.pdf` (font to, nền trắng, chữ đen)
- [ ] **Video links:** `video-links.md` có đủ 3 link YouTube (Katalon / WinAppDriver / AI)
- [ ] **Source code:** thư mục `demo-scripts/` có cả Katalon project và WinAppDriver C# project
- [ ] **App mẫu:** `MiniSum.exe` + `MiniSum_v2.exe` kèm README hướng dẫn chạy
- [ ] **Git commit log:** `git-commit-log.md` (chạy lệnh: `git log --oneline > git-commit-log.md`)
- [ ] **AI usage:** `ai-usage-declaration.md` + export PDF
- [ ] **Contribution:** Đã điền vào Google Sheets (Spreadsheet link)
- [ ] **File size:** Mỗi file ≤ 20MB. Nếu không → dùng 7-Zip chia nhỏ
- [ ] **Tên file ZIP:** Có chứa chữ "ZipTool" (ví dụ: `Group02_ZipTool_Lan2.zip`)
- [ ] **Số file:** ≤ 20 files tổng cộng

---

## 💬 PHÂN PHỐI % CONTRIBUTION (GỢI Ý)

Dựa trên 50 task × giờ làm việc:

| Thành viên | Tasks | Task Hours | Ghi chú |
|---|---|---|---|
| Tín | 15 tasks | ~17.5h | Leader + Dev + Tích hợp |
| Kan | 10 tasks | ~15h | Katalon demo + video |
| Tùng | 10 tasks | ~16h | WinAppDriver demo + video |
| Quang | 10 tasks | ~13.5h | AI demo + comparison |
| Phát | 5 tasks | ~12h | Slide + Git |

> **Lưu ý:** Đảm bảo mỗi người ≥ 5 tasks, số commit Git thể hiện công việc thực tế.
