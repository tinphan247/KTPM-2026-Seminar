# Case Study App — MiniSum

Ứng dụng desktop **WinForms (C# / .NET 8)** dùng làm **Application Under Test (AUT)** chung cho toàn bộ demo của Seminar "Automation Testing for Desktop Applications".

MiniSum gồm 2 màn hình: **Đăng nhập** và **Tính tổng A + B**, được build thành 3 phiên bản phục vụ 3 kịch bản demo khác nhau (xem bảng bên dưới).

---

## 1. Ba phiên bản và mục đích sử dụng

| Phiên bản | File chạy | Khác biệt so với bản trước | Dùng cho demo |
|---|---|---|---|
| **v1** | `MiniSum.exe` | Bản gốc: Login + Calculator, **chưa có validation** | Record & Playback, Checkpoint, kiểm thử cơ bản |
| **v2** | `MiniSum_v2.exe` | Đổi `btnSum` → **`btnCalculate`**, thêm màn hình **Lịch sử** (`btnHistory`) | Maintenance & Self-healing (locator bị đổi tên) |
| **v3** | `MiniSum_v3.exe` | Thêm **validation** + nhãn lỗi `lblError`: bỏ trống, không phải số, ngoài miền `[-99, 99]` | Negative test, BVA / Data-Driven Testing |

> **Lưu ý về nguồn gốc:** v2 và v3 đều phát triển từ v1 theo hai hướng độc lập. Vì vậy **v3 vẫn dùng `btnSum`** (không có `btnCalculate`) và **v2 không có `lblError`**. Hãy chọn đúng file theo kịch bản demo.

---

## 2. Yêu cầu môi trường

- Windows 10 / 11 (bật **Developer Mode** nếu chạy cùng WinAppDriver).
- **.NET Desktop Runtime 8.0** trở lên — tải tại <https://dotnet.microsoft.com/download/dotnet/8.0>.
- File `.exe` là bản **framework-dependent single-file**: chỉ cần runtime, **không cần** cài .NET SDK và không cần các file `.dll` đi kèm.

## 3. Cách chạy

Nhấp đúp vào file `.exe` tương ứng, hoặc:

```powershell
.\MiniSum.exe        # v1
.\MiniSum_v2.exe     # v2
.\MiniSum_v3.exe     # v3
```

**Tài khoản hợp lệ:** `admin` / `1234`

---

## 4. Quy tắc nghiệp vụ

### Màn hình Đăng nhập
| Trường hợp | Kết quả |
|---|---|
| Đúng `admin` / `1234` | `lblMessage` = `Dang nhap thanh cong`, sau 1 giây chuyển sang màn hình Tính tổng |
| Sai tài khoản hoặc mật khẩu | `lblMessage` = `Sai tai khoan hoac mat khau`, ô mật khẩu được xoá trắng |
| Bỏ trống cả hai | `lblMessage` = `Vui long nhap tai khoan va mat khau` |
| Bỏ trống tài khoản | `lblMessage` = `Ten dang nhap khong duoc de trong` |
| Bỏ trống mật khẩu | `lblMessage` = `Mat khau khong duoc de trong` |

### Màn hình Tính tổng (v1, v2)
- Nhập A, B là số nguyên → `lblResult` = `Ket qua: {A} + {B} = {A+B}`
- Nhập dữ liệu không phải số → `lblResult` = `Nhap sai dinh dang` (chưa có validation riêng)

### Màn hình Tính tổng (v3)
- Hợp lệ (`A`, `B` ∈ `[-99, 99]`) → `lblResult` = `Ket qua: {A} + {B} = {A+B}`, `lblError` rỗng
- Thiếu dữ liệu → `lblError` = `Vui long nhap day du gia tri A va B`
- Không phải số nguyên → `lblError` = `Gia tri khong hop le: phai la so nguyen`
- A ngoài miền → `lblError` = `A ngoai mien [-99, 99]`
- B ngoài miền → `lblError` = `B ngoai mien [-99, 99]`

> Toàn bộ thông điệp dùng **ASCII không dấu** để so sánh chuỗi trong test script ổn định.

---

## 5. Bảng AutomationId (dùng cho Object Spy / WinAppDriver)

| Màn hình | Control | Loại | AutomationId | Ghi chú |
|---|---|---|---|---|
| Login | Cửa sổ đăng nhập | Window | `winLogin` | Title: `MiniSum - Dang nhap` |
| Login | Ô tài khoản | TextBox | `txtUser` | |
| Login | Ô mật khẩu | TextBox | `txtPass` | Có `UseSystemPasswordChar` |
| Login | Nút đăng nhập | Button | `btnLogin` | |
| Login | Nhãn thông báo | Label | `lblMessage` | |
| Calculator | Cửa sổ tính toán | Window | `winMain` | Title: `MiniSum - Tinh tong` |
| Calculator | Ô nhập A | TextBox | `txtA` | |
| Calculator | Ô nhập B | TextBox | `txtB` | |
| Calculator | Nút tính tổng | Button | `btnSum` (v1, v3) / `btnCalculate` (v2) | **Khác nhau theo phiên bản** |
| Calculator | Nhãn kết quả | Label | `lblResult` | |
| Calculator | Nhãn lỗi | Label | `lblError` | Chỉ có ở **v3** |
| Calculator | Nút lịch sử | Button | `btnHistory` | Chỉ có ở **v2** |
| Calculator | Nút đăng xuất | Button | `btnLogout` | Quay về màn hình Login |
| History | Cửa sổ lịch sử | Window | `winHistory` | Chỉ có ở **v2**, title `MiniSum - Lich su tinh toan` |
| History | Danh sách lịch sử | List | `lstHistory` | |
| History | Nút đóng | Button | `btnClose` | |

Màn hình Lịch sử (v2) mở dạng **modeless** để thao tác mở cửa sổ không chặn luồng automation.

---

## 6. Cấu trúc thư mục

```text
case-study-app/
├── MiniSum.exe                 # Bản build v1
├── MiniSum_v2.exe              # Bản build v2
├── MiniSum_v3.exe              # Bản build v3
├── README.md                   # Tài liệu này
└── MiniSum/                    # Mã nguồn
    ├── MiniSum.sln             # Solution gồm 3 project
    ├── build.ps1               # Build & publish cả 3 phiên bản
    ├── src/                    # Mã nguồn dùng chung
    │   ├── Program.cs
    │   ├── LoginForm.cs
    │   ├── CalculatorForm.cs   # Có #if V2 / #if V3 cho phần khác biệt
    │   ├── HistoryForm.cs      # Chỉ v2
    │   └── CalculationHistory.cs  # Chỉ v2
    ├── v1/MiniSum.csproj
    ├── v2/MiniSum_v2.csproj
    ├── v3/MiniSum_v3.csproj
    └── tools/Verify-MiniSum.ps1   # Smoke test UI Automation cho cả 3 bản
```

## 7. Build lại từ mã nguồn

Yêu cầu **.NET SDK 8.0+**:

```powershell
cd case-study-app\MiniSum
powershell -ExecutionPolicy Bypass -File .\build.ps1
```

Script sẽ publish 3 phiên bản (single-file, framework-dependent) và tự copy `.exe` ra `case-study-app/`.

Build từng phiên bản:

```powershell
dotnet build v1\MiniSum.csproj -c Release
dotnet publish v2\MiniSum_v2.csproj -c Release -r win-x64 --self-contained false -p:PublishSingleFile=true -o out\v2
```

## 8. Kiểm tra nhanh trước khi bàn giao

```powershell
cd case-study-app\MiniSum\tools
powershell -ExecutionPolicy Bypass -File .\Verify-MiniSum.ps1 -Exe ..\..\MiniSum.exe    -Version v1
powershell -ExecutionPolicy Bypass -File .\Verify-MiniSum.ps1 -Exe ..\..\MiniSum_v2.exe -Version v2
powershell -ExecutionPolicy Bypass -File .\Verify-MiniSum.ps1 -Exe ..\..\MiniSum_v3.exe -Version v3
```

Script tự mở app, đăng nhập, tính toán, kiểm tra validation/lịch sử và in kết quả `PASS`/`FAIL` cho từng bước.

## 9. Ghi chú cho phần automation

- Ưu tiên locator theo **AutomationId**; title cửa sổ dùng để chuyển window (`MiniSum - Dang nhap`, `MiniSum - Tinh tong`, `MiniSum - Lich su tinh toan`).
- Sau khi đăng nhập thành công, ứng dụng **giữ màn hình Login thêm 1 giây** để test runner kịp đọc checkpoint `lblMessage` trước khi chuyển màn hình.
- Kịch bản BVA (12 ca, miền `[-99, 99]`) phải chạy trên **`MiniSum_v3.exe`** vì chỉ bản này có `lblError`.
- Đường dẫn tới `.exe` nên đặt thành biến ở đầu script, không hard-code đường dẫn tuyệt đối của máy cá nhân.
