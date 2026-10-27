# Seminar: Automation Testing for Desktop Applications

> **Khoa Công nghệ Thông tin – Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM**  
> **Môn học:** Software Testing (Kiểm thử phần mềm)  
> **Nhóm thực hiện:** Nhóm 02 (ZipTool)  
> **Chủ đề:** Tự động hóa kiểm thử cho ứng dụng Desktop (Windows)

---

## 👥 Danh sách thành viên nhóm

| STT | Họ và Tên | MSSV | Vai trò chính | Branch Git |
|:---:|---|:---:|---|---|
| M1 | **Phan Trung Tín** *(Leader)* | 23120372 | Trưởng nhóm, Build `MiniSum.exe`, Lý thuyết, Tích hợp báo cáo, Đóng gói | `feature/tin-setup-report` |
| M2 | **Nguyễn Lê Quang Kan** | 23120279 | Nghiên cứu & Demo thực hành **Katalon Studio** | `feature/kan-katalon` |
| M3 | **Bùi Quang Tùng** | 20120397 | Nghiên cứu & Demo thực hành **WinAppDriver** + C# NUnit | `feature/tung-winappdriver` |
| M4 | **Trần Vũ Quang** | 23120346 | Nghiên cứu **AI in Test Automation** + So sánh số liệu thực | `feature/quang-ai-comparison` |
| M5 | **Phạm Tấn Phát** | 20120636 | Thiết kế Slide PowerPoint toàn bộ (8 phần) | `feature/phat-slide` |

---

## 📁 Cấu trúc thư mục dự án

```text
KTPM-2026-Seminar/
├── README.md                           # Giới thiệu tổng quan & hướng dẫn
├── .gitignore                          # Quy tắc bỏ qua file rác (.NET, Katalon, OS, Temp)
├── docs/                               # Toàn bộ tài liệu báo cáo Markdown
│   ├── 01-introduction.md              # 1. Giới thiệu tổng quan kiểm thử Desktop
│   ├── 02-theory.md                    # 2. Cơ sở lý thuyết kiểm thử tự động Desktop
│   ├── 03-toolsurvey.md                # 3. Khảo sát bức tranh công cụ (Tool Landscape)
│   ├── 04-katalon-studio.md            # 4. Chi tiết công cụ Katalon Studio
│   ├── 05-winappdriver.md              # 5. Chi tiết công cụ WinAppDriver
│   ├── 06-comparison.md                # 6. So sánh đối chiếu toàn diện (Katalon vs WinAppDriver)
│   ├── 07-ai-desktop-automation.md     # 7. Ứng dụng AI trong Automation Testing
│   ├── 08-exercises.md                 # 8. Hệ thống câu hỏi & bài tập thực hành
│   └── report.md                       # Báo cáo toàn văn tổng hợp
├── case-study-app/                     # Ứng dụng mẫu phục vụ kiểm thử (MiniSum)
│   ├── MiniSum/                        # Mã nguồn ứng dụng WinForms C# (.NET)
│   ├── MiniSum.exe                     # Bản build v1 – Login + Calculator
│   ├── MiniSum_v2.exe                  # Bản build v2 – đổi btnSum → btnCalculate
│   └── MiniSum_v3.exe                  # Bản build v3 – thêm Validation + Dashboard
├── demo-scripts/                       # Kịch bản kiểm thử tự động
│   ├── katalon/                        # Dự án Katalon Studio (Kan – M2)
│   └── winappdriver/                   # Dự án C# NUnit + WinAppDriver (Tùng – M3)
├── ai/                                 # Tài nguyên thực nghiệm AI (Quang – M4)
│   ├── prompts/                        # Các mẫu Prompt sinh Test case & Script
│   └── output/                         # Kết quả sinh tự động từ AI & đối chiếu
├── slides/                             # Slide báo cáo thuyết trình (Phát – M5)
├── video-links.md                      # Danh sách 3 link video demo YouTube
├── git-commit-log.md                   # Nhật ký commit lịch sử đóng góp
└── ai-usage-declaration.md             # Kê khai chi tiết việc sử dụng AI
```

---

## 🛠️ Công nghệ & Công cụ sử dụng

| Vai trò | Công cụ |
|---|---|
| Application Under Test (AUT) | `MiniSum.exe` – WinForms C# (.NET) |
| Object Inspection | Accessibility Insights for Windows, Inspect.exe |
| Low-code Automation Tool | Katalon Studio (Windows Desktop Testing Engine) |
| Code-based Automation Tool | Windows Application Driver (WinAppDriver) + C# NUnit |
| AI Test Generation | ChatGPT-4 / Gemini Advanced – Prompt Engineering |

---

## 🚀 Hướng dẫn bắt đầu (Quick Start)

### 1. Clone repository
```bash
git clone https://github.com/tinphan247/KTPM-2026-Seminar.git
cd KTPM-2026-Seminar
```

### 2. Tạo branch và làm việc
```bash
# Mỗi thành viên tạo branch theo phân công
git checkout -b feature/[branch-của-bạn]

# Commit thường xuyên
git add .
git commit -m "feat(kan): add Katalon demo script record-playback"
git push origin feature/[branch-của-bạn]
```

### 3. Yêu cầu môi trường
- Hệ điều hành: **Windows 10 / 11** (Bật **Developer Mode** trong Windows Settings)
- .NET Desktop Runtime (.NET 6.0+ hoặc .NET Framework 4.8)
- [WinAppDriver v1.2.1+](https://github.com/microsoft/WinAppDriver/releases)
- [Accessibility Insights for Windows](https://accessibilityinsights.io/en/downloads/)
- [Katalon Studio](https://katalon.com/) (cho demo M2 – Kan)
- Visual Studio 2022 + C# (cho demo M3 – Tùng)

---

## 📌 Quy ước Commit (Conventional Commits)

```
feat(kan):     Thêm script/tài liệu Katalon mới
feat(tung):    Thêm script/tài liệu WinAppDriver mới
feat(quang):   Thêm prompt/output AI thực nghiệm mới
slide(phat):   Cập nhật slide thuyết trình
docs(tin):     Cập nhật tài liệu markdown
fix(tung):     Sửa lỗi script C# NUnit
chore(tin):    Task admin – merge, packaging, setup
```

> Luôn chạy `git pull origin main` trước khi bắt đầu làm việc để tránh conflict.
