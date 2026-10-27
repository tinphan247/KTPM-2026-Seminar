# Đề Xuất Bài Tập Thực Hành: Desktop Automation Testing
## Chuyên đề: Automation Testing cho Desktop Applications

- **Người thực hiện:** Quang
- **Mục tiêu:** Thiết kế hệ thống bài tập thực hành theo phân tầng mức độ nhận thức (Cơ bản - Vừa sức - Nâng cao), giúp sinh viên củng cố lý thuyết kiểm thử hộp đen và thực hành kỹ năng tự động hóa trên ứng dụng desktop thực tế.

---

## 1. Mục Tiêu và Nguyên Tắc Xây Dựng Bài Tập

Hệ thống bài tập được thiết kế tuân thủ 3 nguyên tắc sư phạm và kỹ thuật:
1. **Bám sát chương trình lý thuyết:** Gắn kết trực tiếp với các bài học trong chương trình: Kỹ thuật phân tích giá trị biên (BVA - Bài 4), Chuyển trạng thái (State Transition - Bài 6), Cấu trúc Test Case (Bài 7) và Tái hiện lỗi trong Bug Report (Bài 8).
2. **Khả thi về công cụ và bản quyền:** Sinh viên có thể tự do lựa chọn thực hiện bằng **Katalon Studio (Bản Free)** hoặc **Microsoft WinAppDriver (C# / Python)** mà không chịu ràng buộc về chi phí giấy phép.
3. **Sử dụng ứng dụng mẫu chung (MiniSum):** Cung cấp sẵn file thực thi `.exe` chuẩn hóa về mặt định danh (`AutomationId`), giúp sinh viên tập trung rèn luyện tư duy kiểm thử thay vì mất thời gian sửa lỗi môi trường.

---

## 2. Thông Tin Ứng Dụng Mẫu (MiniSum)

Sinh viên tải file thực thi `MiniSum.exe` từ kho lưu trữ của nhóm. Các thuộc tính định danh chính được cung cấp sẵn:
* **Màn hình Đăng nhập (Login Window):**
  * Ô nhập tài khoản: `txtUser` (Tài khoản hợp lệ: `abc`)
  * Ô nhập mật khẩu: `txtPass` (Mật khẩu hợp lệ: `123`)
  * Nút đăng nhập: `btnSubmit`
  * Nhãn thông báo trạng thái: `lblMessage`
* **Màn hình Tính toán (Main Window):**
  * Ô nhập số A: `txtA` (Giới hạn số nguyên $A \in [-99, 99]$)
  * Ô nhập số B: `txtB` (Giới hạn số nguyên $B \in [-99, 99]$)
  * Nút tính tổng: `btnSum`
  * Nhãn kết quả hợp lệ: `lblResult`
  * Nhãn thông báo lỗi: `lblError`
  * Nút đăng xuất: `btnLogout`

---

## 3. Nội Dung Chi Tiết Bộ 3 Bài Tập

### BÀI TẬP 1 (Mức độ Cơ bản): Xây Dựng Kịch Bản Đăng Nhập & Checkpoint
* **Thời lượng ước tính:** 15 – 20 phút.
* **Mục tiêu:** Làm quen với cơ chế nhận diện phần tử (`AutomationId`), ghi thao tác (Record) hoặc viết mã kịch bản cơ bản, và thiết lập điểm kiểm tra kết quả kỳ vọng (Test Oracle).
* **Nội dung yêu cầu:**
  1. Khởi động ứng dụng `MiniSum.exe`.
  2. Thực hiện kịch bản kiểm thử ca hợp lệ: Nhập `txtUser = "abc"`, `txtPass = "123"`, nhấp chuột vào nút `btnSubmit`.
  3. Thêm một **Checkpoint (Assertion)** để xác minh nhãn `lblMessage` hiển thị đúng nội dung: `"Đăng nhập thành công"`.
  4. Tạo tiếp một ca kiểm thử phụ cho trường hợp đăng nhập thất bại (nhập sai mật khẩu) và xác minh nhãn hiển thị `"Sai tài khoản hoặc mật khẩu"`.
* **Yêu cầu nộp:**
  * File kịch bản kiểm thử (Test Case của Katalon hoặc file mã nguồn C#/Python).
  * Ảnh chụp màn hình kết quả chạy thực thi (Execution Report) thể hiện trạng thái PASS.

---

### BÀI TẬP 2 (Mức độ Vừa sức): Kiểm Thử Điều Khiển Bằng Dữ Liệu (Data-Driven BVA)
* **Thời lượng ước tính:** 30 – 45 phút.
* **Mục tiêu:** Vận dụng lý thuyết phân tích giá trị biên (BVA) để xây dựng bộ dữ liệu kiểm thử và áp dụng kỹ thuật Data-Driven Testing để kiểm thử tự động hàng loạt.
* **Nội dung yêu cầu:**
  1. **Thiết kế dữ liệu:** Tạo một file Excel (`BVA_TestData.xlsx`) chứa ít nhất **6 ca kiểm thử** cho chức năng tính tổng hai số nguyên $A, B \in [-99, 99]$:
     * 2 ca giá trị biên hợp lệ (ví dụ: $A = -99, B = 9 \rightarrow \text{Tổng} = -90$; $A = 99, B = 9 \rightarrow \text{Tổng} = 108$).
     * 2 ca giá trị ngoài biên dưới và trên (ví dụ: $A = -100, B = 9$; $A = 100, B = 9 \rightarrow$ Kỳ vọng xuất hiện `"Thông báo lỗi"`).
     * 1 ca giá trị không hợp lệ về kiểu dữ liệu (ví dụ: $A = \text{"xyz"}, B = 10 \rightarrow$ Kỳ vọng xuất hiện `"Thông báo lỗi"`).
     * 1 ca biên của toán tử thứ hai ($B = -99$).
  2. **Xây dựng kịch bản Data-Driven:**
     * Tham số hóa kịch bản tính tổng để nhận giá trị `${A}`, `${B}`, `${Expected}` từ file Excel.
     * Cấu hình logic kiểm tra: Nếu `${Expected}` là giá trị số thì kiểm tra nhãn `lblResult`; nếu `${Expected}` là `"LOI"` thì kiểm tra nhãn `lblError`.
  3. Thực thi toàn bộ bộ dữ liệu trong một phiên chạy tự động.
* **Yêu cầu nộp:**
  * File dữ liệu `BVA_TestData.xlsx`.
  * Mã nguồn kịch bản kiểm thử có cơ chế binding dữ liệu.
  * Báo cáo thực thi chi tiết thể hiện kết quả Pass/Fail cho từng dòng dữ liệu.

---

### BÀI TẬP 3 (Mức độ Nâng cao): Xử Lý Biến Động Giao Diện & Bảo Trì Kịch Bản
* **Thời lượng ước tính:** Bài tập về nhà / Nghiên cứu chuyên sâu.
* **Mục tiêu:** Rèn luyện tư duy thiết kế kịch bản bền vững và kỹ năng bảo trì — giải quyết bài toán "kịch bản dễ gãy" (fragile tests) khi phần mềm nâng cấp giao diện.
* **Tình huống giả định:** 
  * Nhà phát triển phát hành phiên bản cập nhật `MiniSum_v2.exe`. Trong phiên bản này, để chuẩn hóa mã nguồn, định danh của nút bấm tính tổng được đổi từ `btnSum` thành `btnCalculate`, đồng thời nhãn hiển thị chuyển từ `"Tổng"` sang `"Tính toán"`.
  * Hậu quả: Toàn bộ kịch bản kiểm thử xây dựng ở Bài tập 2 khi chạy trên bản v2 đều bị FAIL hàng loạt do lỗi không tìm thấy phần tử (*ElementNotFoundException*).
* **Nội dung yêu cầu:**
  1. Chạy kịch bản cũ trên bản v2, chụp lại log lỗi thực thi và phân tích nguyên nhân gốc của lỗi (Root Cause).
  2. Thực hiện **bảo trì và tái cấu trúc (Refactoring)** bộ định vị theo nguyên tắc tập trung:
     * *Nếu làm trên Katalon Studio:* Cập nhật lại thuộc tính của đối tượng trong *Object Repository* từ `btnSum` sang `btnCalculate` mà không sửa đổi bất kỳ dòng kịch bản nào trong Test Case.
     * *Nếu làm trên WinAppDriver:* Cập nhật lại biến locator trong lớp *Page Object* tương ứng.
  3. Thực thi lại toàn bộ kịch bản và chứng minh toàn bộ các ca kiểm thử PASS trở lại.
  4. Trả lời câu hỏi phân tích ngắn (khoảng 5-7 dòng): *Tại sao việc quản lý locator tập trung (Object Repository / Page Object Model) lại giúp giảm chi phí bảo trì so với việc gán cứng locator trực tiếp trong kịch bản? Liên hệ với nguyên lý kiểm thử "Nghịch lý thuốc trừ sâu".*
* **Yêu cầu nộp:**
  * Báo cáo phân tích lỗi ban đầu và ảnh chụp màn hình sau khi khắc phục thành công.
  * Đoạn trả lời câu hỏi phân tích lý thuyết bảo trì.

---

## 4 Barem đánh giá chi tiết

| Hạng mục | Tiêu chí đánh giá chi tiết | Điểm tối đa |
|---|---|:---:|
| **Bài tập 1** | - Mở được ứng dụng, thực thi đúng thao tác đăng nhập.<br>- Thiết lập Checkpoint đúng nhãn và chạy PASS.<br>- Có ca kiểm thử phụ cho trường hợp đăng nhập sai. | **3.0 điểm**<br>(1.0 đ)<br>(1.0 đ)<br>(1.0 đ) |
| **Bài tập 2** | - Thiết kế file dữ liệu Excel chuẩn lý thuyết BVA (đủ ca hợp lệ và biên lỗi).<br>- Tham số hóa và binding dữ liệu vào kịch bản thành công.<br>- Xử lý đúng điều kiện kiểm tra kết quả số và thông báo lỗi. | **4.0 điểm**<br>(1.5 đ)<br>(1.5 đ)<br>(1.0 đ) |
| **Bài tập 3** | - Phân tích đúng nguyên nhân lỗi khi đổi ID phần tử.<br>- Thực hiện cập nhật locator tập trung (Object Repository / Page Object).<br>- Câu trả lời phân tích lý thuyết bảo trì mạch lạc, đúng bản chất. | **3.0 điểm**<br>(1.0 đ)<br>(1.0 đ)<br>(1.0 đ) |
| **TỔNG CỘNG** | **Đánh giá toàn diện kỹ năng thực hành và tư duy lý thuyết** | **10.0 điểm** |
