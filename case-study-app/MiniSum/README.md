# MiniSum - Demo App for Katalon Studio Seminar

## Mô tả
`MiniSum.exe` là ứng dụng desktop WPF/C# dùng làm **case study chung** cho seminar
"Automation Testing cho Desktop Applications". Ứng dụng có 2 màn hình:

1. **Login** — xác thực tài khoản (abc/123) với 3 nhãn trạng thái:
   - `"Dang nhap thanh cong"` (khi hợp lệ)
   - `"Sai tai khoan hoac mat khau"` (khi sai)
   - `"Ten dang nhap khong duoc de trong"` / `"Mat khau khong duoc de trong"` (khi rỗng)

2. **Calculator** — tính tổng 2 số nguyên A, B ∈ [-99, 99] với:
   - `lblResult` hiển thị kết quả khi hợp lệ (vd: `"Ket qua: 99 + 9 = 108"`)
   - `lblError` hiển thị thông báo lỗi khi ngoài biên hoặc sai kiểu dữ liệu

## AutomationId (dùng cho Katalon Object Spy / WinAppDriver)
| Màn hình | Control | AutomationId |
|---|---|---|
| Login | Window | `winLogin` |
| Login | Tài khoản | `txtUser` |
| Login | Mật khẩu | `txtPass` |
| Login | Nút đăng nhập | `btnSubmit` |
| Login | Nhãn thông báo | `lblMessage` |
| Calculator | Window | `winMain` |
| Calculator | Số A | `txtA` |
| Calculator | Số B | `txtB` |
| Calculator | Nút tính tổng | `btnSum` |
| Calculator | Kết quả | `lblResult` |
| Calculator | Lỗi | `lblError` |
| Calculator | Nút đăng xuất | `btnLogout` |

## Build & Run

### Yêu cầu môi trường
- .NET 6 SDK (Windows): https://dotnet.microsoft.com/download/dotnet/6.0
- Hoặc Visual Studio 2022 trở lên có workload ".NET desktop development"

### Build bằng dòng lệnh
```bash
cd MiniSum/
dotnet build -c Release
# File exe tại: bin\Release\net6.0-windows\MiniSum.exe
```

### Chạy thử
```bash
dotnet run --project MiniSum.csproj
# hoặc nhấp đúp MiniSum.exe sau khi build
```

### Tài khoản demo
- User: `abc`
- Pass: `123`

## Lưu ý cho Demo Seminar
- Đảm bảo **Developer Mode** đã bật trên Windows (Settings → Privacy & Security → For developers)
- `WinAppDriver.exe` phải chạy quyền Administrator ở cổng 4723 trước khi Katalon khởi tạo Session
- Ứng dụng được đóng gói với assembly name `MiniSum` → Katalon dùng app path:
  `C:\\...\\MiniSum\\bin\\Release\\net6.0-windows\\MiniSum.exe`

## BVA Test Suite (12 ca kiểm thử)
File dữ liệu mẫu: `../KatalonStudio/Test Data/BVA_TestData.xlsx`

| TC | A | B | Expected | Loại |
|---|---|---|---|---|
| TC01 | -99 | 9 | -90 | Biên dưới A hợp lệ |
| TC02 | 99 | 9 | 108 | Biên trên A hợp lệ |
| TC03 | -100 | 9 | LOI | Biên dưới A ngoại lệ |
| TC04 | 100 | 9 | LOI | Biên trên A ngoại lệ |
| TC05 | xyz | 10 | LOI | Sai kiểu dữ liệu |
| TC06 | 10 | -99 | -89 | Biên dưới B hợp lệ |
| TC07 | 10 | 99 | 109 | Biên trên B hợp lệ |
| TC08 | 10 | -100 | LOI | Biên dưới B ngoại lệ |
| TC09 | 10 | 100 | LOI | Biên trên B ngoại lệ |
| TC10 | 0 | 0 | 0 | Giá trị trung bình |
| TC11 | -99 | -99 | -198 | Cả 2 biên dưới |
| TC12 | 99 | 99 | 198 | Cả 2 biên trên |

> Khi `Expected = LOI`, kỳ vọng `lblError` hiển thị nội dung lỗi
> Khi `Expected` là số, kỳ vọng `lblResult` hiển thị `"Ket qua: A + B = Expected"`
