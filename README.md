# Seminar: Automation Testing for Desktop Applications

> **Khoa Công nghệ Thông tin – Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM**  
> **Môn học:** Software Testing (Kiểm thử phần mềm)  
> **Nhóm thực hiện:** Nhóm 02 (ZipTool)  
> **Chủ đề:** Tự động hóa kiểm thử cho ứng dụng Desktop (Windows)

---

## 👥 Danh sách thành viên nhóm

| STT | Họ và Tên | MSSV | Vai trò chính | GitHub |
|:---:|---|:---:|---|---|
| 1 | **Phan Thanh Tín** (Leader) | 23120372 | Trưởng nhóm, Architecture, App Dev (`MiniSum.exe`), Tích hợp báo cáo | [@tinphan247](https://github.com/tinphan247) |
| 2 | **Nguyễn Tuấn Kan** | 23120281 | Nghiên cứu & Demo thực hành **Katalon Studio** | [@KanNguyen1702](https://github.com/KanNguyen1702) |
| 3 | **Nguyễn Thanh Tùng** | 23120387 | Nghiên cứu & Demo thực hành **WinAppDriver** + C# NUnit | [@ThanhTung1208](https://github.com/ThanhTung1208) |
| 4 | **Trần Đăng Quang** | 23120340 | Nghiên cứu **AI in Test Automation** + So sánh thực nghiệm | [@DangQuang104](https://github.com/DangQuang104) |
| 5 | **Phạm Tấn Phát** | 23120330 | Thiết kế Slide thuyết trình, Báo cáo & Quản lý Git logs | [@tanphat1510](https://github.com/tanphat1510) |

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
│   ├── MiniSum.exe                     # Bản build v1 phục vụ kịch bản kiểm thử
│   └── MiniSum_v2.exe                  # Bản build v2 (thay đổi UI để demo bảo trì/self-healing)
├── demo-scripts/                       # Kịch bản kiểm thử tự động
│   ├── katalon/                        # Dự án kiểm thử Katalon Studio
│   └── winappdriver/                   # Dự án C# NUnit + WinAppDriver
├── ai/                                 # Tài nguyên thực nghiệm AI
│   ├── prompts/                        # Các mẫu Prompt sinh Test case & Script
│   └── output/                         # Kết quả sinh tự động từ AI & đối chiếu
├── slides/                             # Slide báo cáo thuyết trình (.pptx / .pdf)
├── video-links.md                      # Danh sách liên kết video demo trên YouTube
├── git-commit-log.md                   # Nhật ký đóng góp và lịch sử commit
└── ai-usage-declaration.md             # Bản kê khai chi tiết việc sử dụng AI (AI Declaration)
```

---

## 🛠️ Công nghệ & Công cụ sử dụng

- **Application Under Test (AUT):** `MiniSum.exe` (.NET WinForms / C#)
- **Object Inspection:** Accessibility Insights for Windows, UI Spy / Inspect.exe
- **Commercial / Low-code Tool:** Katalon Studio (Windows Desktop Testing Engine)
- **Open-source / Code-based Tool:** Windows Application Driver (WinAppDriver), Appium, C# NUnit
- **AI Automation:** Prompt Engineering (Sinh test cases BVA, test script tự động)

---

## 🚀 Hướng dẫn bắt đầu (Quick Start)

### 1. Clone repository
```bash
git clone https://github.com/tinphan247/KTPM-2026-Seminar.git
cd KTPM-2026-Seminar
```

### 2. Yêu cầu môi trường
- Hệ điều hành: **Windows 10 / 11** (Bật tính năng **Developer Mode** trong Windows Settings)
- .NET Desktop Runtime (.NET 6.0 / .NET 8.0 hoặc .NET Framework 4.8)
- [WinAppDriver v1.2.1+](https://github.com/microsoft/WinAppDriver/releases)
- [Accessibility Insights for Windows](https://accessibilityinsights.io/en/downloads/)
- [Katalon Studio](https://katalon.com/) (cho demo Katalon)
- Visual Studio 2022 / VS Code với C# Dev Kit (cho demo WinAppDriver)

---

## 📌 Quy ước Git & Làm việc nhóm

1. **Commit Message tuân thủ Conventional Commits:**
   - `feat:` Thêm tính năng, demo script hoặc tài liệu mới.
   - `fix:` Sửa lỗi script hoặc đính chính tài liệu.
   - `docs:` Cập nhật tài liệu markdown, slide, báo cáo.
   - `refactor:` Tối ưu mã nguồn kiểm thử.
2. **Quy trình làm việc:**
   - Mỗi thành viên phụ trách các thư mục được phân công.
   - Luôn chạy `git pull origin main` trước khi làm việc để tránh xung đột (conflict).
