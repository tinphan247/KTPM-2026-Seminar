# Tài Liệu Đặc Tả Kỹ Thuật Ứng Dụng Mẫu MiniSum (Specification Document)
## Phục Vụ Kiểm Thử Tự Động & Thiết Kế Prompt Engineering Cho AI

- **Hệ thống mục tiêu:** Ứng dụng Desktop MiniSum (`case-study-app/MiniSum.exe`)
- **Tác giả đặc tả:** Trần Vũ Quang (MSSV: 23120346) - Nhóm 02
- **Mục đích:** Cung cấp context chuẩn xác, chi tiết cho các mô hình AI (ChatGPT-4, Claude, Gemini) để sinh test case BVA và mã kịch bản automation testing không bị ảo giác (hallucination).

---

## 1. Tổng Quan Kiến Trúc Ứng Dụng

MiniSum là ứng dụng Windows Forms (.NET Core / .NET Framework) mô phỏng hệ thống tính toán tài chính - kế toán thu nhỏ, được thiết kế theo chuẩn **Windows UI Automation (UIA)** với các thuộc tính định danh (`AutomationId`, `Name`, `ControlType`) rõ ràng.

Ứng dụng gồm hai màn hình tuần tự:
1. **Màn hình Đăng nhập (`LoginForm` / `winLogin`)**: Xác thực quyền truy cập của người dùng.
2. **Màn hình Tính tổng (`CalculatorForm` / `winMain`)**: Nhập hai số nguyên $A, B$ trong miền giới hạn $[-99, 99]$ và tính tổng $A + B$.

---

## 2. Đặc Tả Chi Tiết Màn Hình 1: Đăng Nhập (`LoginForm`)

### 2.1 Thông tin kỹ thuật & UI Controls
| Tên phần tử | ControlType | AutomationId / Name | Mô tả & Ràng buộc |
|---|---|---|---|
| Cửa sổ chính | Window | `winLogin` | Title: `"MiniSum - Dang nhap"`, kích thước 460x518 |
| Ô nhập tài khoản | Edit (TextBox) | `txtUser` | Placeholder / Label: `"TÀI KHOẢN"`, hỗ trợ nhập text |
| Ô nhập mật khẩu | Edit (TextBox) | `txtPass` | Ký tự ẩn `*` (PasswordChar), hỗ trợ nhập text |
| Nút Đăng nhập | Button | `btnLogin` | Văn bản hiển thị: `"ĐĂNG NHẬP"`, kích hoạt sự kiện kiểm tra |
| Nhãn thông báo | Text (Label) | `lblMessage` | Hiển thị kết quả đăng nhập (trống ban đầu) |

### 2.2 Quy tắc nghiệp vụ (Business Rules)
* **Tài khoản mặc định hợp lệ:**
  * `Username`: `admin`
  * `Password`: `1234`
* **Xử lý đăng nhập thành công:**
  * Điều kiện: Nhập đúng `admin` và `1234`.
  * Trạng thái UI: `lblMessage.Text = "Đăng nhập thành công!"` (màu xanh lá `#107C41`).
  * Hành động hệ thống: Sau độ trễ chuyển cảnh 1000ms, form `winLogin` ẩn đi và form `winMain` xuất hiện.
* **Xử lý đăng nhập thất bại:**
  * Điều kiện: Sai username, sai password, hoặc để trống một/cả hai trường.
  * Trạng thái UI: `lblMessage.Text = "Sai tài khoản hoặc mật khẩu!"` (màu đỏ `#D83B01`).
  * Hành động hệ thống: Giữ nguyên form, không chuyển màn hình, xóa trường mật khẩu và focus lại.

---

## 3. Đặc Tả Chi Tiết Màn Hình 2: Tính Tổng (`CalculatorForm`)

### 3.1 Thông tin kỹ thuật & UI Controls
| Tên phần tử | ControlType | AutomationId | Biến thể theo Version |
|---|---|---|---|
| Cửa sổ tính toán | Window | `winMain` | Title: `"MiniSum - Tinh tong"` |
| Ô nhập số A | Edit (TextBox) | `txtA` | Chỉ chấp nhận số nguyên $[-99, 99]$ |
| Ô nhập số B | Edit (TextBox) | `txtB` | Chỉ chấp nhận số nguyên $[-99, 99]$ |
| Nút Tính tổng | Button | `btnSum` *(v1, v3)*<br>`btnCalculate` *(v2)* | Nút kích hoạt tính toán |
| Nhãn kết quả | Text (Label) | `lblResult` | Hiển thị kết quả tổng hoặc để trống |
| Nhãn báo lỗi | Text (Label) | `lblError` *(chỉ có ở v3)* | Hiển thị thông điệp lỗi chi tiết |
| Nút Đăng xuất | Button | `btnLogout` | Đăng xuất, quay lại màn hình Login |
| Nút Lịch sử | Button | `btnHistory` *(chỉ có ở v2)* | Mở cửa sổ xem bảng DataGrid lịch sử |

### 3.2 Miền Giá Trị và Quy Tắc Tính Toán (Calculation Rules)
* **Tập xác định dữ liệu vào:**
  * $A \in \mathbb{Z}$ với $-99 \le A \le 99$
  * $B \in \mathbb{Z}$ với $-99 \le B \le 99$
* **Quy tắc tính toán:**
  * Nếu $A$ và $B$ hợp lệ: $\text{Result} = A + B$.
  * Giá trị tổng nhỏ nhất có thể đạt được: $-99 + (-99) = -198$.
  * Giá trị tổng lớn nhất có thể đạt được: $99 + 99 = 198$.
  * Kết quả hiển thị: `lblResult.Text = "<giá trị tổng>"` (ví dụ: `"0"`, `"108"`, `"-90"`).

### 3.3 Phân Tích Giá Trị Biên (Boundary Value Analysis - BVA)
Áp dụng kỹ thuật kiểm thử BVA 2 biến $A$ và $B$ trên miền $[-99, 99]$:
* **Các điểm mốc của mỗi biến:**
  * Giá trị cực tiểu biên ngoài (Invalid Min / Min-): $-100$
  * Giá trị cực tiểu biên trong (Valid Min): $-99$
  * Giá trị cận tiểu (Valid Min+): $-98$
  * Giá trị danh định (Nominal): $0$, $9$, hoặc $10$
  * Giá trị cận đại (Valid Max-): $98$
  * Giá trị cực đại biên trong (Valid Max): $99$
  * Giá trị cực đại biên ngoài (Invalid Max / Max+): $100$
* **Phân lớp tương đương không hợp lệ (Negative Classes):**
  * Giá trị rỗng (Empty / Whitespace): `""`
  * Chuỗi ký tự chữ cái (Alphabetic): `"xyz"`, `"abc"`
  * Ký tự đặc biệt hoặc số thực (Special / Float): `"@#$"`, `"12.5"`

### 3.4 Quy Tắc Báo Lỗi (Error Handling Specification - Phiên bản v3)
Khi dữ liệu nhập không hợp lệ, hệ thống sẽ gán chuỗi cảnh báo vào `lblError.Text` và đặt `lblResult.Text = ""` (hoặc mã nhận diện `"LOI"` trong kịch bản automation):
1. **Để trống:** `"Vui long nhap day du gia tri A va B"`
2. **Sai định dạng kiểu dữ liệu:** `"Gia tri khong hop le: phai la so nguyen"`
3. **A ngoài miền:** `"A ngoai mien [-99, 99]"`
4. **B ngoài miền:** `"B ngoai mien [-99, 99]"`

---

## 4. Bảng Ma Trận Khác Biệt Giữa 3 Phiên Bản Ứng Dụng (Mục Tiêu Đánh Giá AI)

| Tiêu chí | Phiên bản v1 | Phiên bản v2 | Phiên bản v3 |
|---|---|---|---|
| **File thực thi** | `case-study-app/MiniSum.exe` | `case-study-app/MiniSum_v2.exe` | `case-study-app/MiniSum_v3.exe` |
| **AutomationId Nút tính** | `btnSum` | `btnCalculate` *(Test Self-Healing)* | `btnSum` |
| **Validation đầu vào** | Cơ bản, không có nhãn lỗi | Cơ bản, không có nhãn lỗi | Nghiêm ngặt với banner lỗi |
| **Nhãn báo lỗi** | Không có | Không có | `lblError` |
| **Tính năng bổ sung** | Form tính cơ bản | Thêm Form Lịch Sử (`HistoryForm`) | Lưu lịch sử & Error State |
| **Ý nghĩa trong Seminar** | Baseline cho Manual & Script | Minh họa kịch bản bảo trì / gãy script | Minh họa ca kiểm thử Negative BVA |
