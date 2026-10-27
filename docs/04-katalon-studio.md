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

### 2.2 Cơ chế Object Repository và Nhận diện Locator (Object Recognition)

#### 2.2.1 Khái niệm và Vai trò của Object Repository
* **Bản chất:** Object Repository (OR) là kho lưu trữ tập trung toàn bộ các định danh phần tử giao diện (Test Objects). Thay vì gắn cứng locator (hard-coding) trực tiếp trong từng dòng lệnh kiểm thử, kịch bản chỉ gọi đối tượng qua từ khóa tham chiếu:
  ```groovy
  findWindowsObject('Object Repository/MiniSum/Login/txtUser')
  ```
* **Ý nghĩa thực tế đối với chi phí bảo trì (Maintenance Cost):**
  * Trong vòng đời phần mềm, giao diện người dùng (UI) biến đổi liên tục (đổi ID, tái cấu trúc layout, thay nhãn hiển thị). Nếu gắn cứng locator trong script, tester phải rà soát và sửa hàng chục đến hàng trăm test case riêng lẻ (hiện tượng *Kịch bản dễ gãy - Flaky Tests*).
  * Với Object Repository, tester chỉ cần cập nhật locator tại một file duy nhất trong kho lưu trữ, toàn bộ các Test Case liên quan sẽ tự động nhận diện theo thông số mới. Đây là sự hiện thực hóa triết lý **Page Object Model (POM)** ở mức công cụ không mã nguồn (Codeless/Low-code), giúp hạn chế nguyên lý *"Nghịch lý thuốc trừ sâu" (Pesticide Paradox)* khi kiểm thử tự động dài hạn.

#### 2.2.2 Cấu trúc lưu trữ nội bộ của Object Repository trên Desktop (.wrs)
Khác với kiểm thử Web sử dụng định dạng file `.rs` (`WebElementEntity`), kiểm thử Windows Desktop trong Katalon Studio quy định cấu trúc đối tượng nghiêm ngặt:
* **Định dạng file:** Mỗi đối tượng kiểm thử Desktop được lưu dưới dạng một file XML có đuôi mở rộng là **`.wrs`** (`WindowsElementEntity`).
* **Cấu trúc XML chuẩn:**
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <WindowsElementEntity>
     <description>Ô nhập tài khoản</description>
     <name>txtUser</name>
     <tag></tag>
     <locator>txtUser</locator>
     <locatorStrategy>ACCESSIBILITY_ID</locatorStrategy>
     <properties>
        <isSelected>true</isSelected>
        <matchCondition>equals</matchCondition>
        <name>AutomationId</name>
        <type>Main</type>
        <value>txtUser</value>
     </properties>
  </WindowsElementEntity>
  ```
* **Lưu ý kỹ thuật quan trọng:** Nếu tạo nhầm file định dạng Web (`.rs`) hoặc đường dẫn không đúng, hàm `findWindowsObject()` sẽ trả về `null` trong thời gian chạy, gây ra lỗi ngoại lệ `java.lang.IllegalArgumentException: Test object cannot be null`.

#### 2.2.3 Các chiến lược nhận diện Locator (Locator Strategies) trên Windows Desktop
Katalon Studio phối hợp với WinAppDriver để phân giải các thuộc tính UI Automation thành 4 chiến lược định vị chính theo thứ bậc ưu tiên:

| Chiến lược (Locator Strategy) | Thuộc tính UIA tương ứng | Độ ưu tiên | Đặc điểm kỹ thuật & Đánh giá |
|---|---|:---:|---|
| **ACCESSIBILITY_ID** | `AutomationProperties.AutomationId` (WPF) / `AccessibleName` (WinForms) | **Số 1 (Khuyên dùng)** | Định danh bất biến do lập trình viên gắn trong mã nguồn. Hoàn toàn độc lập với ngôn ngữ hiển thị (Localization) và nội dung text. Tốc độ tìm kiếm nhanh nhất. |
| **NAME** | `Name` attribute (Tiêu đề, Text hiển thị của Control) | **Số 2** | Dễ đọc, nhận diện trực quan theo mắt người dùng. Tuy nhiên rất dễ gãy kịch bản khi ứng dụng hỗ trợ đa ngôn ngữ (i18n) hoặc nội dung nhãn thay đổi. |
| **CLASS_NAME / CONTROL_TYPE** | `ClassName` (WPF/Win32) / `ControlType` (`Button`, `Edit`, `Text`) | **Số 3** | Thường không mang tính duy nhất trên màn hình; chỉ dùng làm điều kiện lọc kết hợp khi phần tử thiếu `AutomationId`. |
| **XPATH** | Vị trí cây phân cấp UIA (e.g., `//Window/Grid/StackPanel/Button[1]`) | **Số 4 (Hạn chế)** | Chuỗi XPath trên Windows Desktop rất phức tạp, tốc độ phân giải qua WinAppDriver chậm gấp 3-5 lần; cực kỳ dễ gãy khi lập trình viên thay đổi cấu trúc thẻ bố cục (Grid, StackPanel). |

#### 2.2.4 Các bẫy kỹ thuật thực tế đúc kết từ quá trình thực nghiệm
Qua quá trình triển khai automation thực tế trên ứng dụng WPF `MiniSum.exe`, nhóm đúc kết được 3 bài học kỹ thuật đặc thù:
1. **Bẫy đọc Text trên thẻ WPF `<TextBlock>`:** Thẻ hiển thị văn bản tĩnh `<TextBlock>` trong WPF không hỗ trợ mẫu thuộc tính `ValuePattern`. Khi gọi lệnh `Windows.getText(object)`, WinAppDriver sẽ trả về chuỗi rỗng `""`. Cách xử lý chuẩn là truy xuất thông qua thuộc tính UIA `Name`: `Windows.getAttribute(object, 'Name')`.
2. **Bẫy tương tác nút bấm (Mouse Click Miss vs. Keyboard Activation):** Trong một số layout WPF (như `StackPanel`), lệnh click chuột ảo `Windows.click(btn)` có thể bị trượt tọa độ do sai lệch tỉ lệ co giãn màn hình (DPI Scaling). Giải pháp tối ưu là bổ sung `IsDefault="True"` cho Button trong XAML và gửi kèm phím `ENTER` (`Keys.chord(Keys.ENTER)`) qua `Windows.sendKeys` để kích hoạt sự kiện chắc chắn 100%.
3. **Bẫy chuyển ngữ cảnh cửa sổ (Window Switching):** Khi ứng dụng đóng cửa sổ cha (`LoginWindow.Close()`) để mở cửa sổ con (`MainWindow.Show()`), session của WinAppDriver bị mất ngữ cảnh cũ. Cần sử dụng lệnh `Windows.switchToWindowTitle('Tiêu đề cửa sổ mới')` để cập nhật handle trước khi thao tác tiếp.

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
  * `Kiểm tra văn bản (Text Verification)`: Trên WebUI, Katalon cung cấp `WebUI.verifyElementText()`. Riêng trên nền tảng **Windows Desktop**, do đặc thù WinAppDriver, việc xác minh văn bản được thực hiện tối ưu qua `Windows.getAttribute(object, 'Name')` hoặc `Windows.getText(object)` kết hợp với lệnh `assert` của ngôn ngữ Groovy.
  * `Windows.verifyElementAttributeValue`: Kiểm tra trạng thái thuộc tính (ví dụ: nút bấm chuyển sang Disabled, ô nhập bị khóa).
  * `Windows.verifyElementPresent`: Kiểm tra sự xuất hiện của cửa sổ mới, popup cảnh báo (hỗ trợ chỉ định timeout).
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
