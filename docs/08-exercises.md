# Đề Bài Tập Thực Hành Cá Nhân: Desktop Automation Testing
## Môn học: Kiểm Thử Phần Mềm · Chuyên đề: Automation Testing cho Desktop Applications

- **Đối tượng:** Sinh viên thực hành cá nhân trực tiếp tại lớp (In-Class Hands-on Lab).
- **Thời lượng:** Đúng **30 phút** (5' Chuẩn bị + 12' Bài 1 + 10' Bài 2 + 3' Nộp bài).
- **Công cụ thực hành:** **Katalon Studio** (phiên bản Free 11.x) trên hệ điều hành Windows.
- **Ứng dụng mẫu (AUT):** `MiniSum.exe` (WinForms C# .NET 8).
- **Kho tài nguyên chính thức:** [https://github.com/tinphan247/KTPM-2026-Seminar.git](https://github.com/tinphan247/KTPM-2026-Seminar.git)

---

## 1. Mục Tiêu Bài Thực Hành Cá Nhân

1. **Tiếp cận nhanh và độc lập:** Mỗi sinh viên tự thao tác trên máy tính của mình, làm quen với quy trình xây dựng kịch bản kiểm thử tự động cho ứng dụng Windows desktop.
2. **Sử dụng tài nguyên chuẩn từ GitHub:** Toàn bộ ứng dụng kiểm thử và kho đối tượng (*Object Repository*) được clone trực tiếp từ GitHub, không phụ thuộc vào đường dẫn máy cá nhân của nhóm thuyết trình.
3. **Nắm vững bản chất Test Oracle & Checkpoint:** Tự tay thiết lập các điểm kiểm tra kết quả kỳ vọng (`Verify Element Text`) để đánh giá Pass/Fail một cách tự động, chính xác.

---

## 2. Chuẩn Bị Tài Nguyên (5 Phút Đầu Giờ)

### Bước 1: Lấy mã nguồn & Ứng dụng từ GitHub
Sinh viên mở **PowerShell** hoặc **Terminal** trên máy của mình và clone repository:
```powershell
# Clone mã nguồn về thư mục làm việc (ví dụ C:\KTPM hoặc D:\Testing)
git clone https://github.com/tinphan247/KTPM-2026-Seminar.git
cd KTPM-2026-Seminar
```
*(Nếu không cài sẵn Git, sinh viên bấm vào link GitHub → chọn **Code** → **Download ZIP** và giải nén ra máy).*

### Bước 2: Kiểm tra ứng dụng MiniSum
- Vào thư mục `case-study-app/`, nháy đúp chạy thử `MiniSum.exe` (hoặc `MiniSum_v3.exe`).
- Cửa sổ đăng nhập **"MiniSum - Dang nhap"** xuất hiện là máy đã có sẵn **.NET 8 Desktop Runtime**.
- Tài khoản demo mặc định: `admin` / Mật khẩu: `1234`.

### Bước 3: Nạp Starter Kit vào Katalon Studio
- Mở **Katalon Studio** $\to$ Mở project mới hoặc nạp sẵn các thư mục tài nguyên từ `demo-scripts/katalon/` (đã có sẵn *Object Repository* chứa đầy đủ locator của `txtUser`, `txtPass`, `btnLogin`, `lblMessage`, `txtA`, `txtB`, `btnSum`, `lblResult`, `lblError`).

---

## 3. Nội Dung Chi Tiết Bài Tập Thực Hành (30 Phút)

### BÀI TẬP 1 (12 Phút): Tự Động Hóa Đăng Nhập & Checkpoint Thông Báo (4.0 Điểm)

* **Tên Test Case:** `TC_Login_<MSSV>` (Ví dụ: `TC_Login_23120001`).
* **Các bước kịch bản:**
  1. **Khởi động ứng dụng:** Dùng từ khóa `Start Application`, trỏ đường dẫn tới file `MiniSum.exe` trong thư mục `case-study-app/` vừa clone về máy bạn.
  2. **Ca 1 (Đăng nhập thành công):**
     - Nhập `txtUser` = `"admin"`.
     - Nhập `txtPass` = `"1234"`.
     - Nhấp chuột nút `btnLogin`.
     - **Checkpoint 1 (Xác minh thông báo):** Thêm từ khóa `Verify Element Text` trên nhãn `lblMessage` với nội dung kỳ vọng: `Dang nhap thanh cong`.
  3. **Ca 2 (Đăng nhập thất bại):**
     - Nhập mật khẩu sai: `txtPass` = `"wrongpass"`.
     - Nhấp chuột nút `btnLogin`.
     - **Checkpoint 2 (Xác minh báo lỗi):** Kiểm tra `lblMessage` hiển thị đúng thông báo: `Sai tai khoan hoac mat khau`.
  4. Chạy kiểm thử và kiểm tra tab **Log Viewer** báo trạng thái **PASSED (màu xanh)**.

---

### BÀI TẬP 2 (10 Phút): Tự Động Hóa Tính Tổng & Kiểm Thử Giá Trị Biên (6.0 Điểm)

* **Tên Test Case:** `TC_Calculate_<MSSV>`.
* **Mục tiêu:** Kiểm tra chức năng tính tổng $A + B$ và xác minh các mốc giá trị biên của miền hợp lệ $A, B \in [-99, 99]$.
* **Các bước kịch bản:**
  1. Sau khi đăng nhập thành công vào màn hình tính toán:
  2. **Thao tác tính tổng thông thường (2.0 điểm):**
     - Nhập `txtA` = `"15"`, nhập `txtB` = `"25"`.
     - Nhấp nút `btnSum`.
     - **Checkpoint:** Kiểm tra nhãn `lblResult` có đúng chuỗi: `Ket qua: 15 + 25 = 40`.
  3. **Kiểm thử Giá Trị Biên (BVA) (4.0 điểm):**
     - **Ca biên trên (2.0 điểm):** Nhập $A = 99$, $B = 0 \to$ Bấm `btnSum` $\to$ Checkpoint xác minh `lblResult` = `Ket qua: 99 + 0 = 99`.
     - **Ca biên dưới (2.0 điểm):** Nhập $A = -99$, $B = 0 \to$ Bấm `btnSum` $\to$ Checkpoint xác minh `lblResult` = `Ket qua: -99 + 0 = -99`.
  4. Thực thi kịch bản và quan sát màn hình tự động điền dữ liệu, tính toán và xác minh.

---

### PHẦN MỞ RỘNG (Bonus +1.0 Điểm Tùy Chọn)
* Dành cho sinh viên hoàn thành sớm trong 30 phút:
* Trỏ đường dẫn ứng dụng sang `case-study-app/MiniSum_v3.exe` (phiên bản có bắt lỗi ngoài biên).
* Nhập giá trị ngoài biên: $A = 100$, $B = 0 \to$ Bấm `btnSum`.
* **Thêm Checkpoint:** Dùng `Verify Element Text` xác minh nhãn lỗi `lblError` hiển thị thông báo: `A ngoai mien [-99, 99]`.

---

## 4. Hướng Dẫn Nộp Bài (3 Phút Cuối Giờ)

Sinh viên nộp kết quả cho Giảng viên / Trợ giảng lớp học bằng một trong hai cách:
1. **Cách 1 (Ảnh chụp màn hình Report):** Chụp toàn màn hình Katalon Studio thể hiện cây Test Case mang tên `<MSSV>`, tab Log Viewer thể hiện các bước thực thi đều **PASSED**, và cửa sổ ứng dụng đang mở.
2. **Cách 2 (File Báo cáo HTML):** Mở thư mục `Reports/` trong project Katalon $\to$ Lấy file `report.html` (hoặc nén thư mục test case thành `<MSSV>_LabKatalon.zip`) để gửi qua Google Form / Zalo nộp bài của lớp.

---

## 5. Barem Chấm Điểm Thực Hành (Thang Điểm 10)

| STT | Nội dung đánh giá | Tiêu chí chi tiết | Điểm |
|:---:|---|---|:---:|
| **1** | **Môi trường & Khởi động** | Clone repo thành công, cấu hình đúng đường dẫn `MiniSum.exe` trên máy cá nhân và khởi động được app. | **1.0 đ** |
| **2** | **Bài 1: Đăng nhập & Checkpoint** | - Thực hiện ca đăng nhập đúng `admin/1234` + Checkpoint `lblMessage` PASS.<br>- Thực hiện ca đăng nhập sai + Checkpoint báo lỗi PASS. | **3.0 đ**<br>(1.5 đ)<br>(1.5 đ) |
| **3** | **Bài 2: Tính tổng cơ bản** | Nhập giá trị hợp lệ, bấm tính và Checkpoint `lblResult` hiển thị đúng kết quả. | **2.0 đ** |
| **4** | **Bài 2: Kiểm thử Biên (BVA)** | - Thực hiện đúng ca biên trên ($A = 99, B = 0$) + Checkpoint PASS.<br>- Thực hiện đúng ca biên dưới ($A = -99, B = 0$) + Checkpoint PASS. | **4.0 đ**<br>(2.0 đ)<br>(2.0 đ) |
| **5** | **Điểm thưởng (Bonus)** | Bắt được nhãn lỗi `lblError` khi nhập ngoài biên trên `MiniSum_v3.exe`. | **+1.0 đ**<br>*(tối đa 10đ)* |
| | **TỔNG CỘNG** | **Hoàn thành trọn vẹn kịch bản kiểm thử tự động Desktop trong 30 phút** | **10.0 đ** |

<p class="table-caption"><b>Bảng 8.1:</b> <i>Barem chấm điểm chi tiết bài tập thực hành cá nhân 30 phút tại lớp (Thang điểm 10)</i></p>

