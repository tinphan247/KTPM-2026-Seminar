# Case Study App — MiniSum

## 1. Giới thiệu
`MiniSum.exe` là ứng dụng desktop WPF (.NET 6) được xây dựng làm **case study chung** cho đề tài Seminar "Automation Testing cho Desktop Applications (Katalon Studio & WinAppDriver)".

Ứng dụng gồm 2 màn hình chính:
1. **Login**: Xác thực người dùng (User: `abc` / Pass: `123`) với các nhãn trạng thái và thông báo lỗi.
2. **Calculator**: Tính tổng $A + B$ trong phạm vi số nguyên $[-99, 99]$ với nhãn kết quả `lblResult` và nhãn lỗi `lblError` phục vụ kiểm thử giá trị biên (BVA).

---

## 2. Cấu trúc thư mục
```text
case-study-app/
├── MiniSum/              # Mã nguồn dự án WPF C# (.NET 6)
│   ├── App.xaml / App.xaml.cs
│   ├── LoginWindow.xaml / LoginWindow.xaml.cs
│   ├── MainWindow.xaml / MainWindow.xaml.cs
│   ├── MiniSum.csproj
│   └── README.md
├── MiniSum.exe           # Bản build thực thi v1 (Login + Calculator)
└── README.md             # Hướng dẫn này
```

---

## 3. Yêu cầu môi trường & Cách chạy

### Yêu cầu môi trường
- Hệ điều hành: Windows 10 / Windows 11
- .NET Desktop Runtime 6.0 trở lên: [Tải tại Microsoft](https://dotnet.microsoft.com/download/dotnet/6.0)
- Bật **Developer Mode** trên Windows nếu kết hợp kiểm thử với WinAppDriver.

### Chạy trực tiếp file thực thi
Nhấp đúp chuột vào file `MiniSum.exe` tại thư mục này hoặc chạy từ dòng lệnh:
```bash
./MiniSum.exe
```

### Build lại từ mã nguồn
Nếu muốn chỉnh sửa hoặc build lại mã nguồn:
```bash
cd MiniSum/
dotnet build -c Release
# Hoặc publish bản single-file:
dotnet publish -c Release -r win-x64 --self-contained false -p:PublishSingleFile=true -o ../
```

---

## 4. Bảng danh danh định danh (AutomationId)
Bảng định danh được chuẩn hóa để phục vụ Object Spy trên Katalon Studio và FindElement trên WinAppDriver:

| Màn hình | Điều khiển (Control) | Loại | AutomationId |
|---|---|---|---|
| **Login** | Cửa sổ Đăng nhập | Window | `winLogin` |
| **Login** | Ô nhập tài khoản | TextBox | `txtUser` |
| **Login** | Ô nhập mật khẩu | PasswordBox | `txtPass` |
| **Login** | Nút đăng nhập | Button | `btnSubmit` |
| **Login** | Nhãn thông báo | TextBlock | `lblMessage` |
| **Calculator** | Cửa sổ Tính toán | Window | `winMain` |
| **Calculator** | Ô nhập số A | TextBox | `txtA` |
| **Calculator** | Ô nhập số B | TextBox | `txtB` |
| **Calculator** | Nút tính tổng | Button | `btnSum` |
| **Calculator** | Nhãn kết quả | TextBlock | `lblResult` |
| **Calculator** | Nhãn thông báo lỗi | TextBlock | `lblError` |
| **Calculator** | Nút đăng xuất | Button | `btnLogout` |
