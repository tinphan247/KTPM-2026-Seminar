# Nghiên Cứu Công Cụ: Katalon Studio
## Chuyên đề: Automation Testing cho Desktop Applications

- **Người thực hiện:** Kan (Tool A)
- **Mục tiêu báo cáo tuần:** Tổng quan công cụ, nguyên lý hoạt động trên Desktop, 3 năng lực cốt lõi (Record & Playback, Data-Driven, Checkpoints), ưu/nhược điểm và định hướng kịch bản demo.

---

## 1. Tổng quan về Katalon Studio

### 1.1 Thông tin chung
* **Đơn vị phát triển:** Katalon Inc.
* **Mô hình bản quyền:** Freemium (Bản Free đáp ứng đầy đủ các tính năng cơ bản cho kiểm thử Desktop; các gói trả phí Enterprise/TestOps bổ sung tính năng nâng cao và báo cáo đám mây).
* **Phạm vi hỗ trợ:** Đa nền tảng kiểm thử (Web, API, Mobile và Windows Desktop). Đối với Desktop App, công cụ tập trung hỗ trợ nền tảng Windows.
* **Ngôn ngữ viết kịch bản:** Groovy / Java.
* **Chế độ soạn thảo kép (Dual-view):**
  * *Manual View:* Giao diện dạng bảng (Action - Object - Value) trực quan, cho phép xây dựng kịch bản kiểm thử mà không cần viết code.
  * *Script View:* Chế độ code Groovy thuần, cho phép tùy biến logic, xử lý điều kiện, vòng lặp phức tạp.

### 1.2 Lý do lựa chọn cho seminar
1. **Chi phí 0 đồng:** Bản Free không giới hạn thời gian dùng thử (loại bỏ rủi ro hết hạn bản quyền trong quá trình học tập và báo cáo).
2. **Tích hợp sẵn trọn bộ công cụ:** Có sẵn trình ghi kịch bản (Recorder), trình soi phần tử (Object Spy), kho lưu đối tượng tập trung (Object Repository) và hệ thống báo cáo (Reporting).
3. **Phù hợp với nhiều đối tượng:** Người chưa biết lập trình có thể tiếp cận qua Manual View; người muốn can thiệp kỹ thuật có thể viết mã qua Script View.

---

## 2. Nguyên lý hoạt động trên Desktop App

### 2.1 Kiến trúc thực thi
Katalon Studio kiểm thử ứng dụng Desktop Windows thông qua kiến trúc phân tầng chuẩn WebDriver:

```
┌──────────────────────────────────────────────┐
│  Katalon Studio (IDE / Test Engine)          │
│  - Test Cases, Object Repository, Test Data  │
└──────────────────────┬───────────────────────┘
                       │ HTTP / WebDriver Protocol (Port 4723)
                       ▼
┌──────────────────────────────────────────────┐
│  Microsoft WinAppDriver                      │
│  (Windows Application Driver Service)        │
└──────────────────────┬───────────────────────┘
                       │ Native API Calls
                       ▼
┌──────────────────────────────────────────────┐
│  Windows UI Automation (UIA) Engine          │
└──────────────────────┬───────────────────────┘
                       │ Điều khiển trực tiếp
                       ▼
┌──────────────────────────────────────────────┐
│  Application Under Test (AUT)                │
│  (WPF, WinForms, UWP, Win32)                 │
└──────────────────────────────────────────────┘
```

1. **Gửi lệnh:** Kịch bản kiểm thử trong Katalon sinh ra các yêu cầu HTTP theo chuẩn JSON Wire / W3C WebDriver.
2. **Thông dịch:** WinAppDriver (dịch vụ chạy nền ở cổng `4723`) tiếp nhận yêu cầu và chuyển đổi thành lời gọi hàm của Windows UI Automation (UIA).
3. **Tương tác:** Hệ điều hành Windows tương tác trực tiếp lên các thành phần giao diện (nhấp chuột, nhập văn bản, đọc giá trị).
4. **Phản hồi:** Trạng thái thực thi và dữ liệu giao diện được trả ngược về Katalon để đánh giá kết quả (Pass/Fail).

### 2.2 Nhận diện phần tử giao diện (Object Recognition)
* **Windows Object Spy:** Cho phép trỏ chuột vào phần tử giao diện để bóc tách các thuộc tính nhận dạng do Windows UIA cung cấp.
* **Object Repository:** Nơi lưu trữ tập trung các phần tử (Object). Mỗi test step chỉ tham chiếu đến Object này, giúp giảm chi phí bảo trì khi giao diện thay đổi (chỉ cần sửa locator tại một nơi duy nhất).
* **Độ ưu tiên của thuộc tính định vị (Locator):**
  1. `AutomationId`: Định danh duy nhất do lập trình viên gắn, độc lập với ngôn ngữ giao diện $\rightarrow$ **Ưu tiên số 1**.
  2. `Name`: Nhãn hiển thị của control $\rightarrow$ Dễ bị gãy kịch bản nếu ứng dụng đổi text hoặc đổi ngôn ngữ hiển thị.
  3. `ClassName` / `ControlType`: Loại phần tử giao diện $\rightarrow$ Kết hợp khi phần tử thiếu định danh duy nhất.
  4. `XPath`: Cấu trúc phân cấp cây giao diện $\rightarrow$ Thường dài và dễ vỡ khi bố cục màn hình cập nhật.

---

## 3. Ba Năng Lực Cốt Lõi (Theo Lý Thuyết Kiểm Thử)

### 3.1 Record & Playback (Ghi & Phát lại kịch bản)
* **Khái niệm:** Kỹ thuật ghi nhận chuỗi thao tác chuột và bàn phím của tester trên ứng dụng thật, sau đó tự động chuyển đổi thành mã kịch bản để thực thi lại.
* **Cách Katalon hỗ trợ:**
  * Tính năng **Windows Recorder** tự động mở ứng dụng, lắng nghe sự kiện người dùng và tự động lưu các control vào Object Repository.
  * Tự sinh ra các từ khóa hành động (`Start Application Window`, `Click`, `Set Text`).
* **Ưu điểm & Hạn chế:**
  * *Ưu điểm:* Xây dựng kịch bản kiểm thử ban đầu rất nhanh, không đòi hỏi kỹ năng lập trình sâu.
  * *Hạn chế:* Dữ liệu bị gán cứng (hard-coded); kịch bản dễ bị lỗi gián đoạn (flaky) nếu không bổ sung các bước chờ đồng bộ (Wait) và chuẩn hóa lại locator.

### 3.2 Checkpoints & Assertions (Điểm kiểm tra kết quả)
* **Khái niệm:** Điểm so sánh giữa kết quả thực tế (**Actual Result**) và kết quả kỳ vọng (**Expected Result**) nhằm tự động hóa vai trò của Test Oracle. Kịch bản không có Checkpoint chỉ là bot thao tác tự động, không thể coi là kịch bản kiểm thử.
* **Bộ từ khóa Verify trong Katalon:**
  * `Verify Element Text`: Kiểm tra nội dung chuỗi (ví dụ: thông báo lỗi, nhãn kết quả).
  * `Verify Element Attribute Value`: Kiểm tra trạng thái thuộc tính (ví dụ: nút bấm chuyển sang Disabled, ô nhập bị khóa).
  * `Verify Element Present`: Kiểm tra sự xuất hiện của cửa sổ mới, popup cảnh báo.
* **Cơ chế bắt lỗi:** Khi giá trị thực tế không khớp với giá trị kỳ vọng, kịch bản tự động dừng hoặc tiếp tục tùy cấu hình, chụp ảnh màn hình tại thời điểm lỗi và ghi log phục vụ báo cáo lỗi (Bug Report).

### 3.3 Data-Driven Testing (Kiểm thử hướng dữ liệu)
* **Khái niệm:** Tách rời kịch bản kiểm thử khỏi tập dữ liệu đầu vào. Một logic kiểm thử duy nhất được tham số hóa bằng các biến và chạy lặp qua nhiều bộ dữ liệu khác nhau.
* **Cách Katalon hỗ trợ:**
  * Hỗ trợ nguồn dữ liệu ngoài: File **Excel**, **CSV**, Database hoặc Internal Data.
  * Tab **Variables** trong Test Case định nghĩa các biến (ví dụ: `var_A`, `var_B`, `var_Expected`).
  * Cơ chế Data Binding trong Test Suite cho phép liên kết từng cột dữ liệu với biến của Test Case.
* **Ý nghĩa thực tế:**
  * Giúp thực thi nhanh chóng các kỹ thuật thiết kế ca kiểm thử hộp đen như **Phân hoạch tương đương (Equivalence Partitioning)** và **Phân tích giá trị biên (Boundary Value Analysis - BVA)**.
  * Mở rộng độ bao phủ kiểm thử mà không cần viết lại kịch bản (chỉ cần bổ sung các dòng dữ liệu vào file Excel).

---

## 4. Đánh Giá Ưu Điểm & Nhược Điểm

### 4.1 Ưu điểm
1. **Tiếp cận nhanh và dễ sử dụng:** Giao diện thân thiện, tài liệu hướng dẫn đầy đủ, cộng đồng người dùng đông đảo.
2. **Tích hợp toàn diện:** Cung cấp sẵn cơ chế quản lý dự án, Object Repository, Test Suite, quản lý dữ liệu và xuất báo cáo (HTML, JUnit) mà không cần cài thêm thư viện ngoài.
3. **Hỗ trợ bảo trì tốt:** Mô hình Object Repository giúp việc cập nhật locator khi phần mềm thay đổi diễn ra tập trung, tránh sửa hàng loạt script.
4. **Sẵn sàng tích hợp CI/CD:** Hỗ trợ chạy kịch bản thông qua dòng lệnh (Katalon Runtime Engine) để tích hợp vào Jenkins, GitHub Actions.

### 4.2 Nhược điểm & Rào cản kỹ thuật
1. **Phụ thuộc vào WinAppDriver:** Dự án WinAppDriver của Microsoft hiện đã ngừng phát triển tính năng mới (archive), điều này tiềm ẩn rủi ro dài hạn về khả năng tương thích với các bản cập nhật Windows tương lai.
2. **Khó nhận diện ứng dụng không chuẩn:** Đối với các ứng dụng desktop dựng bằng công nghệ tùy biến (Custom Controls, giao diện vẽ bằng Canvas/DirectX, Qt thuần không hỗ trợ UIA), Object Spy không thể bắt được control chi tiết.
3. **Tiêu tốn tài nguyên:** IDE tương đối nặng, thời gian khởi động lâu và yêu cầu kết nối mạng để xác thực tài khoản bản quyền khi khởi động.
4. **Hạn chế ở bản Free:** Các tính năng nâng cao như kiểm thử hình ảnh (Visual Testing), AI Self-healing và chạy kiểm thử song song bị giới hạn trong bản miễn phí.

---

## 5. Định Hướng Kịch Bản Demo Cho Nhóm

Để đảm bảo tính khách quan và có thể so sánh công bằng với Tool B, kịch bản demo được thiết kế theo 3 cấp độ:

```
[Demo 1: Thiết lập] ──► [Demo 2: Cơ bản] ──► [Demo 3: Nâng cao]
 Cấu hình môi trường    Record & Playback     Data-Driven (BVA)
 Nhận diện control      Gán Checkpoint        Chuyển trạng thái
```

### 5.1 Demo 1: Cài đặt và chuẩn bị môi trường
* **Mục tiêu:** Chứng minh tính dễ tiếp cận và khả năng kết nối của công cụ.
* **Các bước chính:**
  1. Kích hoạt *Developer Mode* trên Windows và khởi động `WinAppDriver.exe`.
  2. Tạo Project mới kiểu Windows trong Katalon Studio.
  3. Dùng *Windows Object Spy* soi vào ứng dụng mẫu (Calculator hoặc ứng dụng WPF) để kiểm tra các thuộc tính UIA (`AutomationId`, `Name`).

### 5.2 Demo 2: Thao tác cơ bản (Record & Playback + Checkpoint)
* **Mục tiêu:** Minh họa quy trình tự động hóa kịch bản kiểm thử chuẩn (ví dụ: Chức năng Đăng nhập).
* **Các bước chính:**
  1. Dùng *Windows Recorder* ghi lại thao tác nhập tài khoản, mật khẩu và bấm Submit.
  2. Chuẩn hóa lại các đối tượng đã ghi trong Object Repository.
  3. Thêm bước `Verify Element Text` để kiểm tra thông báo kết quả.
  4. Thực thi kịch bản (Playback) và minh họa trường hợp cố tình kiểm tra sai để xem cơ chế báo lỗi (chụp màn hình và xuất log).

### 5.3 Demo 3: Kịch bản nâng cao (Data-Driven BVA + Luồng nghiệp vụ)
* **Mục tiêu:** Minh họa khả năng chạy kiểm thử tự động với dữ liệu lớn theo kỹ thuật phân tích giá trị biên.
* **Các bước chính:**
  1. Chuẩn bị file Excel chứa tập dữ liệu biên (ví dụ: các giá trị biên hợp lệ và không hợp lệ của bài toán tính tổng 2 số nguyên).
  2. Tạo kịch bản tính toán có tham số hóa và thực hiện liên kết dữ liệu (Data Binding).
  3. Thực thi tự động toàn bộ danh sách dữ liệu trong một lần chạy và xem báo cáo kết quả chi tiết từng dòng dữ liệu.

---

## 6. Khi Nào Nên & Không Nên Chọn Katalon Studio

| Nên chọn Katalon Studio | Khi nào nên cân nhắc công cụ khác |
|---|---|
| Đội ngũ có cả nhân sự Manual Tester và Automation Tester (cần Dual-view). | Đội ngũ thuần Developer / SDET muốn viết code kiểm thử trực tiếp trong Visual Studio / VS Code (nên chọn WinAppDriver + C# hoặc PyWinAuto). |
| Cần triển khai nhanh mà không tốn thời gian xây dựng framework từ đầu. | Ứng dụng vẽ hoàn toàn bằng đồ họa custom hoặc công nghệ nhúng không hỗ trợ Windows UIA (cần công cụ so khớp hình ảnh như SikuliX). |
| Dự án có ngân sách hạn chế (cần bản miễn phí ổn định). | Dự án doanh nghiệp quy mô lớn đòi hỏi kiểm thử đa nền tảng (cả macOS, Linux) cho cùng một mã nguồn desktop. |
