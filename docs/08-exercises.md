# Đề Xuất Bài Tập Thực Hành: Desktop Automation Testing
## Chuyên đề: Automation Testing cho Desktop Applications

- **Người thực hiện:** Quang
- **Mục tiêu:** Thiết kế hệ thống bài tập thực hành theo phân tầng mức độ nhận thức (Cơ bản - Vừa sức - Nâng cao), giúp sinh viên củng cố lý thuyết kiểm thử hộp đen và thực hành kỹ năng tự động hóa trên ứng dụng desktop thực tế.

---

## 1. Mục Tiêu và Nguyên Tắc Xây Dựng Bài Tập

Hệ thống bài tập được thiết kế tuân thủ 3 nguyên tắc sư phạm và kỹ thuật:
1. **Bám sát chương trình lý thuyết:** Gắn kết trực tiếp với các bài học trong chương trình: Kỹ thuật phân tích giá trị biên (BVA - Bài 4), Chuyển trạng thái (State Transition - Bài 6), Cấu trúc Test Case (Bài 7) và Tái hiện lỗi trong Bug Report (Bài 8).
2. **Khả thi về công cụ và bản quyền:** Toàn bộ bài tập thực hiện trên **Katalon Studio (bản Free)** — không mất phí giấy phép, không cần lập trình, phù hợp với quỹ thời gian 15–45 phút mỗi bài. Sinh viên đã có nền C#/.NET có thể nộp **track B bằng Microsoft WinAppDriver** với cùng đề bài và cùng thang điểm (xem mục 2).
3. **Sử dụng ứng dụng mẫu chung (MiniSum):** Cung cấp sẵn file thực thi `.exe` chuẩn hóa về mặt định danh (`AutomationId`), giúp sinh viên tập trung rèn luyện tư duy kiểm thử thay vì mất thời gian sửa lỗi môi trường.

---

## 2. Công Cụ Và Môi Trường Thực Hành

> **Hướng dẫn từng bước cho sinh viên** (từ clone repo đến khi nộp bài): [`09-huong-dan-bai-tap.md`](09-huong-dan-bai-tap.md). Mục dưới đây chỉ tóm tắt yêu cầu kỹ thuật.

### 2.1. Công cụ chính: Katalon Studio (bản Free)

| Tiêu chí | Yêu cầu |
|---|---|
| Công cụ | Katalon Studio 11.x (bản Free) |
| Hệ điều hành | Windows 10/11 64-bit |
| Runtime | **.NET 8 Desktop Runtime (x64)** — bắt buộc để chạy `MiniSum*.exe` |
| Cấu hình | RAM ≥ 8 GB, còn trống ≥ 5 GB đĩa |
| Tài khoản | Có tài khoản Katalon (miễn phí), kích hoạt online ở lần mở đầu tiên |
| Quyền | Không cần quyền admin, **không cần bật Developer Mode** |
| Kiến thức | Không cần biết lập trình (Groovy là tùy chọn ở bài nâng cao) |

**Vì sao chọn Katalon cho lớp:**

1. **Vừa thời lượng.** Record & Playback + checkpoint hoàn thành bài 1 trong 15–20 phút; nếu dùng công cụ code-first, riêng việc dựng môi trường đã lâu hơn cả bài.
2. **Đúng trọng tâm bài học.** Bài tập dạy BVA, checkpoint, data-driven và bảo trì locator — Katalon che bớt phần hạ tầng để sinh viên tập trung vào tư duy kiểm thử.
3. **Bài 3 thể hiện rõ nguyên lý.** Khi `btnSum` đổi thành `btnCalculate`, sinh viên chỉ sửa **một thuộc tính trong Object Repository**, không đụng vào test case — đúng thông điệp "quản lý locator tập trung".
4. **Chấm bài nhanh.** Mỗi bài nộp kèm HTML report sẵn có; giảng viên mở project và chạy lại để kiểm chứng.
5. **Đồng nhất với phần demo trên lớp.** Sinh viên thao tác lại đúng những gì đã thấy ở slide Demo 1–3.

### 2.2. Track B (tùy chọn): WinAppDriver + C#

Chỉ áp dụng cho sinh viên đáp ứng **cả ba** điều kiện:

- Đã học C#/.NET, đọc được code trong `demo-scripts/winappdriver/`.
- Máy có .NET 8 SDK và quyền admin (cài WinAppDriver MSI, bật Developer Mode).
- Tự lo được môi trường **trước** buổi học.

Track B dùng **cùng đề bài, cùng dữ liệu, cùng thang điểm**; phần trình bày thêm Page Object Model và chạy `dotnet test` được cộng tối đa **0,5 điểm**, tổng điểm không vượt 10.

### 2.3. Chuẩn bị trước buổi học (bắt buộc)

Sinh viên hoàn tất ở nhà, **không làm trong giờ bài tập**:

1. Cài **.NET 8 Desktop Runtime (x64)**, mở thử `MiniSum_v3.exe` để chắc chắn ứng dụng chạy được.
2. Cài Katalon Studio 11.x và đăng nhập tài khoản Katalon một lần.
3. Clone repo (hoặc tải ZIP) và kiểm tra đủ 3 file `.exe` trong `case-study-app/`.
4. Tạo **project Katalon rỗng** rồi copy 7 thư mục nội dung từ `demo-scripts/katalon/` vào (repo không chứa `.project` — xem hướng dẫn mục 3).
5. Sửa `appPath` trong `TC01`–`TC03` thành đường dẫn trên máy mình.
6. Chạy thử `TC01_Login_Success` một lần để chắc chắn môi trường hoạt động.
7. Dùng laptop Windows; không dùng macOS/Linux (WinAppDriver và Windows Desktop Testing Engine chỉ chạy trên Windows).

> Nếu máy lab không cho cài phần mềm hoặc không có mạng để kích hoạt Katalon, sinh viên làm bài trên máy cá nhân và chỉ nộp kết quả; buổi lab dùng để chữa bài.

### 2.4. Starter project: phần có sẵn và phần sinh viên tự làm

| Có sẵn trong `demo-scripts/katalon/` | Sinh viên tự làm |
|---|---|
| Object Repository đầy đủ của MiniSum (`txtUser`, `txtPass`, `btnSubmit`, `lblMessage`, `txtA`, `txtB`, `btnSum`, `lblResult`, `lblError`, `winLogin`, `winMain`, `btnLogout`) | Thêm checkpoint và ca kiểm thử còn thiếu |
| `TC01_Login_Success` mẫu (record + verify) | Tự tạo `TC01_Login_<MSSV>` và `TC02_LoginFail_<MSSV>` (bản mẫu chỉ để đối chiếu) |
| Test Suite + Data Binding mẫu | File Excel ≥ 6 ca BVA của mình và cấu hình binding |
| Custom Keyword `LoginKeyword.groovy` | Sửa locator khi chuyển sang `MiniSum_v2` (bài 3) |

Lý do phát sẵn: nếu bắt sinh viên Object Spy và record lại từ đầu, bài 1 sẽ kéo dài gấp đôi và phần lớn thời gian mất vào thao tác công cụ, không phải vào thiết kế ca kiểm thử. Bộ `TC01`–`TC03` là **bản demo của nhóm**, không phải bài nộp.

### 2.5. Quy định nộp và chấm

- **Bài nộp:** thư mục project Katalon (nén `.zip`) + HTML report của lần chạy cuối + file `BVA_TestData.xlsx` (bài 2).
- **Chấm:** mở project, chạy lại test suite, đối chiếu với report đã nộp; sai lệch giữa report và lần chạy lại tính là không đạt.
- **Track B:** repo C# + kết quả `dotnet test` + ảnh chụp màn hình khi fail.

---

## 3. Thông Tin Ứng Dụng Mẫu (MiniSum)

Sinh viên tải các file thực thi trong thư mục `case-study-app/` của kho lưu trữ nhóm. Các thuộc tính định danh chính được cung cấp sẵn:
* **Màn hình Đăng nhập (Login Window):**
  * Ô nhập tài khoản: `txtUser` (Tài khoản hợp lệ: `admin`)
  * Ô nhập mật khẩu: `txtPass` (Mật khẩu hợp lệ: `1234`)
  * Nút đăng nhập: `btnLogin`
  * Nhãn thông báo trạng thái: `lblMessage`
* **Màn hình Tính toán (Main Window):**
  * Ô nhập số A: `txtA` (Giới hạn số nguyên $A \in [-99, 99]$)
  * Ô nhập số B: `txtB` (Giới hạn số nguyên $B \in [-99, 99]$)
  * Nút tính tổng: `btnSum` (bản v1, v3) hoặc `btnCalculate` (bản v2)
  * Nhãn kết quả hợp lệ: `lblResult`
  * Nhãn thông báo lỗi: `lblError` (chỉ có ở bản v3)
  * Nút đăng xuất: `btnLogout`

> **Chọn đúng file theo bài tập:** Bài 1 dùng `MiniSum.exe` (v1); Bài 2 dùng `MiniSum_v3.exe` vì chỉ bản này có `lblError`; Bài 3 dùng `MiniSum_v2.exe`. Mọi thông điệp của ứng dụng đều là **ASCII không dấu** (ví dụ `Dang nhap thanh cong`), nên checkpoint phải so sánh đúng từng ký tự.

---

## 4. Nội Dung Chi Tiết Bộ 3 Bài Tập

> Toàn bộ bài tập dưới đây mặc định làm trên **Katalon Studio** (bản Free). Sinh viên nộp **track B (WinAppDriver)** làm đúng các yêu cầu tương ứng, thay "Test Case" bằng lớp Page Object.

### BÀI TẬP 1 (Mức độ Cơ bản): Xây Dựng Kịch Bản Đăng Nhập & Checkpoint
* **Thời lượng ước tính:** 15 – 20 phút.
* **Mục tiêu:** Làm quen với Object Repository và cơ chế nhận diện phần tử (`AutomationId`), thêm bước kiểm thử trong Manual view của Katalon, và thiết lập điểm kiểm tra kết quả kỳ vọng (Test Oracle).
* **Nội dung yêu cầu:**
  1. Mở **starter project** trong `demo-scripts/katalon/`, chạy thử `TC01_Login_Success` (bản mẫu) để xác nhận môi trường hoạt động.
  2. Khởi động ứng dụng `MiniSum.exe` từ Test Case (dùng lại bước `startApplicationWithTitle` có sẵn).
  3. Thực hiện kịch bản kiểm thử ca hợp lệ: Nhập `txtUser = "admin"`, `txtPass = "1234"`, nhấp chuột vào nút `btnLogin`.
  4. Thêm một **Checkpoint (Verify Element Text)** để xác minh nhãn `lblMessage` hiển thị đúng nội dung: `Dang nhap thanh cong`.
  5. Tạo tiếp `TC02` cho trường hợp đăng nhập thất bại (nhập sai mật khẩu) và xác minh nhãn hiển thị `Sai tai khoan hoac mat khau`.
  6. Lưu ý: sau khi đăng nhập thành công, ứng dụng giữ màn hình Login thêm **1 giây** rồi mới chuyển sang màn hình Tính toán — cần dùng explicit wait thay vì `sleep` cứng khi chuyển màn hình.
  7. Test case nộp bài phải do sinh viên tự tạo và có MSSV trong tên (`TC01_Login_<MSSV>`, `TC02_LoginFail_<MSSV>`); `TC01`–`TC03` trong starter chỉ là bản mẫu để đối chiếu.
* **Yêu cầu nộp:**
  * Project Katalon (nén `.zip`) chứa `TC01` đã bổ sung checkpoint và `TC02` cho ca đăng nhập thất bại.
  * HTML report của lần chạy cuối, thể hiện **cả hai ca đều PASS**.

---

### BÀI TẬP 2 (Mức độ Vừa sức): Kiểm Thử Điều Khiển Bằng Dữ Liệu (Data-Driven BVA)
* **Thời lượng ước tính:** 30 – 45 phút.
* **Mục tiêu:** Vận dụng lý thuyết phân tích giá trị biên (BVA) để xây dựng bộ dữ liệu kiểm thử và áp dụng kỹ thuật Data-Driven Testing để kiểm thử tự động hàng loạt.
* **Nội dung yêu cầu:**
  1. **Thiết kế dữ liệu:** Trên `MiniSum_v3.exe` (bản duy nhất có `lblError`), tạo một file Excel (`BVA_TestData.xlsx`) chứa ít nhất **6 ca kiểm thử** cho chức năng tính tổng hai số nguyên $A, B \in [-99, 99]$:
     * 2 ca giá trị biên hợp lệ (ví dụ: $A = -99, B = 9 \rightarrow \text{Tổng} = -90$; $A = 99, B = 9 \rightarrow \text{Tổng} = 108$).
     * 2 ca giá trị ngoài biên dưới và trên (ví dụ: $A = -100, B = 9$; $A = 100, B = 9 \rightarrow$ Kỳ vọng `lblError` = `A ngoai mien [-99, 99]`).
     * 1 ca giá trị không hợp lệ về kiểu dữ liệu (ví dụ: $A = \text{"xyz"}, B = 10 \rightarrow$ Kỳ vọng `lblError` = `Gia tri khong hop le: phai la so nguyen`).
     * 1 ca biên của toán tử thứ hai ($B = -99$).
  2. **Xây dựng kịch bản Data-Driven:**
     * Tham số hóa kịch bản tính tổng để nhận giá trị `${A}`, `${B}`, `${Expected}` từ file Excel (dùng **Data Binding** của Test Suite, không hard-code đường dẫn tuyệt đối).
     * Cấu hình logic kiểm tra: Nếu `${Expected}` là giá trị số thì kiểm tra nhãn `lblResult`; nếu `${Expected}` là `"LOI"` thì kiểm tra nhãn `lblError` và so sánh đúng nội dung thông điệp lỗi.
  3. Thực thi toàn bộ bộ dữ liệu trong một phiên chạy tự động.
* **Yêu cầu nộp:**
  * File dữ liệu `BVA_TestData.xlsx`.
  * Test Case + Test Suite Katalon đã cấu hình Data Binding tới file Excel.
  * HTML report thể hiện kết quả Pass/Fail cho **từng dòng dữ liệu**.

---

### BÀI TẬP 3 (Mức độ Nâng cao): Xử Lý Biến Động Giao Diện & Bảo Trì Kịch Bản
* **Thời lượng ước tính:** Bài tập về nhà / Nghiên cứu chuyên sâu.
* **Mục tiêu:** Rèn luyện tư duy thiết kế kịch bản bền vững và kỹ năng bảo trì — giải quyết bài toán "kịch bản dễ gãy" (fragile tests) khi phần mềm nâng cấp giao diện.
* **Tình huống giả định:** 
  * Nhà phát triển phát hành phiên bản cập nhật `MiniSum_v2.exe`. Trong phiên bản này, để chuẩn hóa mã nguồn, định danh (`AutomationId`) của nút bấm tính tổng được đổi từ `btnSum` thành `btnCalculate` (nhãn hiển thị trên nút vẫn là `TINH TONG`), đồng thời bổ sung màn hình Lịch sử.
  * Hậu quả: Toàn bộ kịch bản kiểm thử xây dựng ở Bài tập 2 khi chạy trên bản v2 đều bị FAIL hàng loạt do lỗi không tìm thấy phần tử (*ElementNotFoundException*).
  * Lưu ý: v2 **không có** `lblError`, nên bài 3 chỉ chạy bộ dữ liệu **toàn ca hợp lệ** (ví dụ 4 ca: `-99+9`, `99+9`, `0+0`, `10+-99`). Các ca `Expected = LOI` thuộc về v3 — đây cũng là bài học: dữ liệu kiểm thử phải khớp với phiên bản AUT.
* **Nội dung yêu cầu:**
  1. Chạy kịch bản cũ trên bản v2, chụp lại log lỗi thực thi và phân tích nguyên nhân gốc của lỗi (Root Cause).
  2. Thực hiện **bảo trì và tái cấu trúc (Refactoring)** bộ định vị theo nguyên tắc tập trung:
     * *Mặc định (Katalon):* Cập nhật lại thuộc tính của đối tượng trong *Object Repository* từ `btnSum` sang `btnCalculate` mà **không sửa đổi bất kỳ dòng kịch bản nào** trong Test Case.
     * *Track B (WinAppDriver):* Cập nhật lại biến locator trong lớp *Page Object* tương ứng.
  3. Thực thi lại toàn bộ kịch bản và chứng minh toàn bộ các ca kiểm thử PASS trở lại.
  4. Trả lời câu hỏi phân tích ngắn (khoảng 5-7 dòng): *Tại sao việc quản lý locator tập trung (Object Repository / Page Object Model) lại giúp giảm chi phí bảo trì so với việc gán cứng locator trực tiếp trong kịch bản? Liên hệ với nguyên lý kiểm thử "Nghịch lý thuốc trừ sâu".*
* **Yêu cầu nộp:**
  * Báo cáo phân tích lỗi ban đầu (log `ElementNotFoundException`) và HTML report sau khi khắc phục thành công.
  * Đoạn trả lời câu hỏi phân tích lý thuyết bảo trì.

---

## 5. Barem đánh giá chi tiết

| Hạng mục | Tiêu chí đánh giá chi tiết | Điểm tối đa |
|---|---|:---:|
| **Bài tập 1** | - Mở được ứng dụng, thực thi đúng thao tác đăng nhập.<br>- Thiết lập Checkpoint đúng nhãn và chạy PASS.<br>- Có ca kiểm thử phụ cho trường hợp đăng nhập sai. | **3.0 điểm**<br>(1.0 đ)<br>(1.0 đ)<br>(1.0 đ) |
| **Bài tập 2** | - Thiết kế file dữ liệu Excel chuẩn lý thuyết BVA (đủ ca hợp lệ và biên lỗi).<br>- Tham số hóa và binding dữ liệu vào kịch bản thành công.<br>- Xử lý đúng điều kiện kiểm tra kết quả số và thông báo lỗi. | **4.0 điểm**<br>(1.5 đ)<br>(1.5 đ)<br>(1.0 đ) |
| **Bài tập 3** | - Phân tích đúng nguyên nhân lỗi khi đổi ID phần tử.<br>- Thực hiện cập nhật locator tập trung (Object Repository / Page Object).<br>- Câu trả lời phân tích lý thuyết bảo trì mạch lạc, đúng bản chất. | **3.0 điểm**<br>(1.0 đ)<br>(1.0 đ)<br>(1.0 đ) |
| **Track B (tùy chọn)** | - Cùng đề bài, làm bằng WinAppDriver/C#.<br>- Trình bày Page Object Model rõ ràng, chạy được `dotnet test`. | **+0.5 điểm**<br>(không vượt quá 10.0) |
| **TỔNG CỘNG** | **Đánh giá toàn diện kỹ năng thực hành và tư duy lý thuyết** | **10.0 điểm** |
