# Đặc Tả Kỹ Thuật Ứng Dụng MiniSum (Cho Prompt Engineering)

## 1. Thông Tin Chung
- **Tên ứng dụng:** MiniSum (WinForms .NET 8)
- **Kiến trúc:** Windows Forms Desktop Application (tương thích UI Automation)
- **Mục tiêu:** Kiểm thử tự động tính năng Đăng nhập và Tính tổng hai số nguyên A + B.

## 2. Quy Tắc Nghiệp Vụ & Ràng Buộc Miền Giá Trị
- **Miền giá trị hợp lệ của A và B:** $[-99, 99]$ với , B \in \mathbb{Z}$.
- **Tài khoản hợp lệ:** dmin / 1234.
- **Thông điệp ASCII:** 
  - Thành công: Dang nhap thanh cong
  - Sai tài khoản/mật khẩu: Sai tai khoan hoac mat khau
  - Để trống: Vui long nhap day du gia tri A va B
  - Kết quả: Ket qua: {A} + {B} = {A+B}
  - Lỗi ngoài miền: A ngoai mien [-99, 99] hoặc B ngoai mien [-99, 99]

## 3. AutomationId Mapping
- winLogin, 	xtUser, 	xtPass, tnLogin, lblMessage
- winMain, 	xtA, 	xtB, tnSum, lblResult, lblError, tnLogout
