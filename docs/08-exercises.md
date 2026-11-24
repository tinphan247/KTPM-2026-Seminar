# Đề Xuất Bài Tập Thực Hành: Desktop Automation Testing
## Chuyên đề: Automation Testing cho Desktop Applications

- **Hình thức:** Thực hành trực tiếp tại lớp (In-Class Hands-on Lab).
- **Thời lượng:** Đúng **30 phút**.
- **Công cụ chính:** Katalon Studio (bản Free) · Ứng dụng mẫu: `MiniSum.exe` (WinForms C# .NET 8).
- **Mục tiêu:** Giúp sinh viên tiếp cận nhanh, tự tay xây dựng được kịch bản kiểm thử tự động hoàn chỉnh từ thao tác giao diện đến thiết lập Checkpoint xác minh kết quả chỉ trong một buổi học.

---

## 1. Mục Tiêu và Định Hướng Tinh Gọn (Cho 30 Phút Tại Lớp)

Bài tập được thiết kế lại nhằm **giảm thiểu tối đa rào cản kỹ thuật** và loại bỏ các bước chuẩn bị rườm rà (không bắt buộc cấu hình Data Binding với file Excel phức tạp):
1. **Thời lượng vừa vặn 30 phút:** Sinh viên có thể hoàn thành trọn vẹn 2 bài tập nhỏ ngay tại phòng máy.
2. **Sử dụng Starter Project có sẵn:** Cung cấp sẵn kho đối tượng (*Object Repository*) của `MiniSum` trong thư mục `demo-scripts/katalon/` để sinh viên không mất thời gian dò tìm locator (`AutomationId`) bằng Object Spy.
3. **Trọng tâm vào tư duy kiểm thử (Test Oracle):** Tập trung rèn luyện 2 kỹ năng cốt lõi:
   - Thao tác tự động với điều khiển Desktop (`Set Text`, `Click`).
   - Thiết lập điểm kiểm tra kết quả kỳ vọng bằng **Checkpoint** (`Verify Element Text`).

---

## 2. Chuẩn Bị Nhanh (5 Phút Đầu Giờ)

1. Nháy đúp mở file `case-study-app/MiniSum.exe` để chắc chắn máy đã có **.NET 8 Desktop Runtime** (thấy cửa sổ *MiniSum - Dang nhap* hiện lên là đạt).
2. Mở Katalon Studio, mở project hoặc nạp thư mục `demo-scripts/katalon/`.
3. Kiểm tra các đối tượng giao diện đã có sẵn trong *Object Repository*:
   - Màn hình Login: `txtUser`, `txtPass`, `btnLogin`, `lblMessage`.
   - Màn hình Calculator: `txtA`, `txtB`, `btnSum`, `lblResult`, `lblError`.

---

## 3. Nội Dung Chi Tiết Bài Tập Thực Hành 30 Phút

### BÀI TẬP 1 (15 Phút): Tự Động Hóa Đăng Nhập & Xác Minh Thông Báo (4.0 Điểm)

* **Mục tiêu:** Tạo kịch bản kiểm thử luồng đăng nhập và xác minh kết quả phản hồi bằng Checkpoint.
* **Các bước thực hiện:**
  1. Tạo Test Case mới đặt tên: `TC_Login_<MSSV>`.
  2. Thêm bước mở ứng dụng `MiniSum.exe` (sử dụng từ khóa `Start Application` trỏ tới file `.exe`).
  3. **Ca 1 (Đăng nhập hợp lệ):**
     - Nhập `txtUser` = `"admin"`.
     - Nhập `txtPass` = `"1234"`.
     - Nhấp chuột vào nút `btnLogin`.
     - **Thêm Checkpoint:** Dùng từ khóa `Verify Element Text` trên đối tượng `lblMessage` với nội dung kỳ vọng là: `Dang nhap thanh cong`.
  4. **Ca 2 (Đăng nhập sai):**
     - Nhập mật khẩu sai: `txtPass` = `"wrongpass"`.
     - Nhấp nút `btnLogin`.
     - **Thêm Checkpoint:** Xác minh `lblMessage` hiển thị: `Sai tai khoan hoac mat khau`.
  5. Chạy thử nghiệm và đảm bảo kết quả kiểm thử báo **PASSED (màu xanh)**.

---

### BÀI TẬP 2 (12 Phút): Tự Động Hóa Tính Tổng & Kiểm Thử Giá Trị Biên (6.0 Điểm)

* **Mục tiêu:** Tương tác với màn hình tính toán và kiểm thử chức năng tính tổng với các giá trị biên của bài toán $A, B \in [-99, 99]$.
* **Các bước thực hiện:**
  1. Tạo Test Case mới đặt tên: `TC_Calculate_<MSSV>` (hoặc viết tiếp vào sau bước đăng nhập thành công của Bài 1).
  2. **Thao tác tính tổng cơ bản (3.0 điểm):**
     - Xóa ô và nhập `txtA` = `"10"`.
     - Xóa ô và nhập `txtB` = `"20"`.
     - Nhấp chuột vào nút tính tổng `btnSum`.
     - **Thêm Checkpoint:** Dùng `Verify Element Text` kiểm tra nhãn kết quả `lblResult` có đúng chuỗi: `Ket qua: 10 + 20 = 30`.
  3. **Kiểm thử giá trị biên đơn giản (3.0 điểm):**
     Thực hiện liên tiếp 2 ca kiểm thử biên trực tiếp trên giao diện:
     - **Ca biên trên:** Nhập $A = 99$, $B = 0 \to$ Nhấp `btnSum` $\to$ Checkpoint xác minh `lblResult` = `Ket qua: 99 + 0 = 99`.
     - **Ca biên dưới:** Nhập $A = -99$, $B = 0 \to$ Nhấp `btnSum` $\to$ Checkpoint xác minh `lblResult` = `Ket qua: -99 + 0 = -99`.
  4. Chạy kiểm thử toàn bộ và quan sát kết quả thực thi tự động.

---

### PHẦN MỞ RỘNG / ĐIỂM THƯỞNG (Tùy Chọn – Bonus +1.0 Điểm)
* Nếu hoàn thành sớm, sinh viên mở ứng dụng `case-study-app/MiniSum_v3.exe` (bản có kiểm tra ràng buộc biên và nhãn lỗi `lblError`).
* Nhập giá trị vượt biên: $A = 100$, $B = 0 \to$ Nhấp `btnSum`.
* **Thêm Checkpoint:** Xác minh nhãn lỗi `lblError` hiển thị đúng thông điệp: `A ngoai mien [-99, 99]`.

---

## 4. Hướng Dẫn Nộp Bài (3 Phút Cuối Giờ)

Sinh viên nộp sản phẩm trực tiếp cho giảng viên/trợ giảng theo một trong hai hình thức:
1. **Xuất báo cáo HTML:** Vào mục *Reports* của Katalon Studio $\to$ Mở file HTML Report thể hiện các bước thực thi đều **PASSED** $\to$ Chụp ảnh màn hình toàn bộ kèm thông tin MSSV.
2. **Nén thư mục Test Case:** Nén các file kịch bản trong thư mục `Test Cases/` thành file `<MSSV>_Lab30m.zip` để nộp.

---

## 5. Barem Chấm Điểm Chi Tiết (Thang Điểm 10)

| Hạng mục | Tiêu chí đánh giá chi tiết | Điểm |
|---|---|:---:|
| **Bài tập 1: Đăng nhập** | - Mở được ứng dụng `MiniSum.exe` thành công.<br>- Thực hiện đúng thao tác đăng nhập hợp lệ và Checkpoint `lblMessage` PASS.<br>- Bổ sung ca đăng nhập sai và xác minh thông báo lỗi PASS. | **4.0 điểm**<br>(1.0 đ)<br>(2.0 đ)<br>(1.0 đ) |
| **Bài tập 2: Tính tổng & Biên** | - Nhập dữ liệu A, B, bấm nút `btnSum` và Checkpoint `lblResult` PASS.<br>- Thực hiện đúng ca kiểm thử biên trên ($A = 99$).<br>- Thực hiện đúng ca kiểm thử biên dưới ($A = -99$). | **6.0 điểm**<br>(2.0 đ)<br>(2.0 đ)<br>(2.0 đ) |
| **Điểm thưởng (Bonus)** | - Bắt được nhãn lỗi `lblError` khi nhập giá trị vượt biên trên `MiniSum_v3.exe`. | **+1.0 điểm**<br>*(tối đa 10.0)* |
| **TỔNG CỘNG** | **Đánh giá trọn vẹn kỹ năng Desktop Automation cơ bản trong 30 phút** | **10.0 điểm** |
