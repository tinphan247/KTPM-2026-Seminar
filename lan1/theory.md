# Automation Testing for Desktop Applications
## Phần 2: Theory

> **Seminar – Phụ trách:** Tín  
> **Nội dung:** Khái niệm cốt lõi · Kỹ thuật tự động hóa · Thách thức đặc thù · Thuật ngữ  
> **Cập nhật lần cuối:** 02/10/2026  
> **Trạng thái:** Hoàn thành  

---

## Mục lục

1. [Automation Testing là gì?](#1-automation-testing-là-gì)
2. [Desktop Application Testing](#2-desktop-application-testing)
   - 2.1 [Phân loại Desktop Application](#21-phân-loại-desktop-application)
   - 2.2 [Các loại kiểm thử áp dụng cho Desktop App](#22-các-loại-kiểm-thử-áp-dụng-cho-desktop-app)
3. [Đặc điểm & Khó khăn đặc thù](#3-đặc-điểm--khó-khăn-đặc-thù)
   - 3.1 [Đặc điểm nổi bật](#31-đặc-điểm-nổi-bật)
   - 3.2 [Khó khăn đặc thù khi Automation](#32-khó-khăn-đặc-thù-khi-automation)
4. [Record & Playback](#4-record--playback)
   - 4.1 [Khái niệm](#41-khái-niệm)
   - 4.2 [Luồng hoạt động](#42-luồng-hoạt-động)
   - 4.3 [Ưu điểm & Nhược điểm](#43-ưu-điểm--nhược-điểm)
5. [Data-Driven Testing (DDT)](#5-data-driven-testing-ddt)
   - 5.1 [Khái niệm](#51-khái-niệm)
   - 5.2 [Ví dụ thực tế kịch bản đăng nhập](#52-ví-dụ-thực-tế-kịch-bản-đăng-nhập)
6. [Checkpoints & Assertions](#6-checkpoints--assertions)
   - 6.1 [Khái niệm](#61-khái-niệm)
   - 6.2 [Phân loại Checkpoint](#62-phân-loại-checkpoint)
   - 6.3 [Kiến trúc Assertion](#63-kiến-trúc-assertion)
7. [Fully vs Semi-Automated](#7-fully-vs-semi-automated)
   - 7.1 [Fully Automated](#71-fully-automated)
   - 7.2 [Semi-Automated](#72-semi-automated)
   - 7.3 [So sánh chi tiết](#73-so-sánh-chi-tiết)
8. [Ưu điểm & Nhược điểm của Automation Testing](#8-ưu-điểm--nhược-điểm-của-automation-testing)
9. [Khi nào nên dùng Automation Testing?](#9-khi-nào-nên-dùng-automation-testing)
10. [Bảng thuật ngữ chuyên ngành](#10-bảng-thuật-ngữ-chuyên-ngành)

---

## 1. Automation Testing là gì?

**Automation Testing** (Kiểm thử tự động) là quá trình áp dụng các công cụ phần mềm chuyên dụng nhằm thực thi tự động các kịch bản kiểm thử (test cases), tự động nhập dữ liệu đầu vào, tương tác với giao diện người dùng hoặc tầng API, và so sánh kết quả thực tế (actual results) với kết quả kỳ vọng (expected results) mà không cần sự can thiệp thủ công của con người trong quá trình chạy.

```
┌──────────────┐    Kịch bản kiểm thử    ┌──────────────────┐
│   Tester     │ ──────────────────────► │  Automation Tool │
│  (Thiết kế,  │                         │  (Thực thi test) │
│   Phân tích) │ ◄────────────────────── │                  │
└──────────────┘      Báo cáo kết quả    └────────┬─────────┘
                                                  │ Tương tác
                                                  ▼
                                         ┌──────────────────┐
                                         │  Ứng dụng cần    │
                                         │  kiểm thử (AUT)  │
                                         └──────────────────┘
```

> **Lưu ý:** Kiểm thử tự động không nhằm mục đích thay thế hoàn toàn con người. Tester vẫn giữ vai trò quyết định trong việc xây dựng chiến lược kiểm thử, thiết kế kịch bản kiểm thử biên/ngoại lệ, phân tích nguyên nhân lỗi và bảo trì bộ kịch bản tự động.

---

## 2. Desktop Application Testing

### 2.1 Phân loại Desktop Application

Khác với web applications chủ yếu dựa trên kiến trúc DOM HTML/CSS, các ứng dụng desktop được xây dựng trên nhiều kiến trúc và công nghệ giao diện khác nhau:

```
Desktop Applications
├── Ứng dụng bản địa thuần túy (Windows Native Apps)
│   ├── Win32 / MFC (C++, giao diện Windows truyền thống)
│   ├── WinForms (.NET Framework, mô hình hướng sự kiện)
│   ├── WPF (Windows Presentation Foundation - kiến trúc XAML, DirectX)
│   └── UWP (Universal Windows Platform - ứng dụng hiện đại từ Windows Store)
├── Ứng dụng đa nền tảng (Cross-Platform Native Apps)
│   ├── Qt (C++/QML, phổ biến trong hệ thống nhúng và công nghiệp)
│   └── JavaFX / Swing (Java Virtual Machine)
└── Ứng dụng lai (Hybrid / Embedded Web Apps)
    ├── Electron (Đóng gói Chromium + Node.js: VS Code, Slack, Teams)
    └── .NET MAUI / Blazor Hybrid (Kết hợp WebView2 và .NET)
```

Mỗi nền tảng UI trên đòi hỏi cơ chế nhận diện phần tử (Accessibility layer / UI Automation API) khác nhau, ảnh hưởng trực tiếp đến khả năng hỗ trợ của từng công cụ kiểm thử tự động.

### 2.2 Các loại kiểm thử áp dụng cho Desktop App

| Loại kiểm thử | Mục đích chính | Khả năng tự động hóa |
|---|---|---|
| **Functional Testing** | Xác minh các chức năng nghiệp vụ hoạt động đúng đặc tả | Rất phù hợp (Mức độ cao) |
| **Regression Testing** | Đảm bảo mã nguồn mới không làm hỏng tính năng đang chạy ổn định | Rất phù hợp (Mức độ rất cao) |
| **Smoke / Sanity Testing** | Kiểm tra nhanh các luồng cơ bản sau mỗi bản build mới | Rất phù hợp (Mức độ cao) |
| **UI Testing** | Kiểm tra bố cục, màu sắc, font chữ, trạng thái component | Phù hợp (Mức độ trung bình) |
| **Performance Testing** | Đo lường thời gian khởi động, mức chiếm dụng CPU, RAM, disk I/O | Rất phù hợp (Mức độ cao) |
| **Usability Testing** | Đánh giá độ thân thiện và trải nghiệm người dùng | Hạn chế (Cần con người đánh giá) |
| **Exploratory Testing** | Khám phá tự do nhằm tìm lỗi tiềm ẩn ngoài kịch bản định sẵn | Không khả thi (Đòi hỏi tư duy sáng tạo) |

---

## 3. Đặc điểm & Khó khăn đặc thù

### 3.1 Đặc điểm nổi bật

- **Tương tác sâu với hệ điều hành:** Desktop app chạy trực tiếp trên OS, truy cập trực tiếp vào hệ thống tệp tin, registry, tiến trình hệ thống, bộ nhớ và các dịch vụ nền.
- **Phụ thuộc cấu hình phần cứng và môi trường:** Độ phân giải màn hình, tỷ lệ co giãn DPI (DPI scaling), số lượng màn hình phụ (multi-monitor), card đồ họa, máy in, scanner... đều có thể làm thay đổi cách ứng dụng kết xuất giao diện.
- **Không có chuẩn DOM đồng nhất:** Mỗi công nghệ UI (Win32, WPF, Qt, Electron) dùng cây cấu trúc giao diện và thuộc tính nhận dạng hoàn toàn khác nhau.

### 3.2 Khó khăn đặc thù khi Automation

```
CÁC THÁCH THỨC CHÍNH TRONG DESKTOP AUTOMATION TESTING
───────────────────────────────────────────────────────────────
1. Nhận diện phần tử giao diện (Object Recognition)
   • Không có chuẩn CSS Selector hay thuộc tính ID nhất quán như web.
   • Nhiều control cũ (Win32 custom controls) không hỗ trợ UI Automation.
   • Giao diện bị ảnh hưởng bởi theme hệ điều hành, ngôn ngữ và DPI.

2. Đồng bộ hóa thời gian thực (Synchronization & Timing)
   • Không có sự kiện "Page Load" hay "Network Idle" rõ ràng như trình duyệt.
   • Dễ dẫn đến lỗi kịch bản chạy nhanh hơn tốc độ render của app (Flaky test).
   • Cần cơ chế chờ thông minh (Explicit Wait) thay vì thời gian chờ cố định (Sleep).

3. Quản lý cửa sổ và hộp thoại hệ thống
   • Các popup hệ điều hành (Open/Save File Dialog, Print Dialog) là tiến trình riêng.
   • Xử lý đa cửa sổ (MDI - Multiple Document Interface) đòi hỏi chuyển đổi ngữ cảnh.

4. Môi trường thực thi kịch bản (Execution Environment)
   • Khó chạy chế độ không màn hình (Headless mode) như web; cần Desktop Session thật.
   • Màn hình bị khóa (Lock screen) hoặc thu nhỏ (Minimize) có thể làm gián đoạn test.

5. Chi phí bảo trì kịch bản kiểm thử (Script Maintenance)
   • Khi nhà phát triển thay đổi giao diện, selector có thể bị đứt gãy hàng loạt.
   • Chi phí bảo trì nếu thiết kế kịch bản kém có thể vượt quá chi phí kiểm thử thủ công.
```

---

## 4. Record & Playback

### 4.1 Khái niệm

**Record & Playback** (Ghi và Phát lại) là kỹ thuật kiểm thử tự động trong đó công cụ lắng nghe và ghi nhận các thao tác chuột (click, drag-drop) và bàn phím (keystrokes) của người dùng trên ứng dụng cần kiểm thử. Sau đó, công cụ lưu lại chuỗi hành động này dưới dạng kịch bản để có thể tự động chạy lại nhiều lần.

```
GIAI ĐOẠN GHI (RECORD)               GIAI ĐOẠN PHÁT LẠI (PLAYBACK)
──────────────────────               ────────────────────────────
Tester thao tác trực tiếp            Công cụ tự động gửi tín hiệu
trên ứng dụng (AUT)       ──Script──► mô phỏng hành vi người dùng
                                     và kiểm tra kết quả kỳ vọng
Công cụ bắt đối tượng UI
và sinh mã kịch bản
```

### 4.2 Luồng hoạt động

```
[Bắt đầu quá trình Record]
            │
            ▼
[Tester thao tác các bước kiểm thử trên AUT]
            │
            ▼
[Công cụ bắt sự kiện: Control Name, AutomationId, Tọa độ, Thao tác nhập]
            │
            ▼
[Công cụ tự động sinh mã kịch bản (C#, Python, Groovy, VBScript...)]
            │
            ▼
[Tester bổ sung các Checkpoint / Assertion và tối ưu hóa selector]
            │
            ▼
[Chạy Playback: Công cụ điều khiển AUT và đối chiếu kết quả]
            │
            ▼
[Xuất báo cáo kết quả kiểm thử (Thành công / Thất bại)]
```

### 4.3 Ưu điểm & Nhược điểm

| Tiêu chí | Ưu điểm | Nhược điểm |
|---|---|---|
| **Độ dốc tiếp cận** | Rất dễ học, người kiểm thử không cần kiến thức lập trình sâu. | Dễ phụ thuộc vào công cụ, khó tùy biến luồng phức tạp. |
| **Thời gian tạo test** | Nhanh chóng tạo được kịch bản kiểm thử ban đầu. | Kịch bản sinh ra thường dài dòng, dư thừa nhiều thao tác thừa. |
| **Bảo trì** | Thích hợp tạo nhanh smoke test đơn giản ban đầu. | Rất dễ bị gãy (fragile) khi giao diện thay đổi dù chỉ một vị trí nhỏ. |
| **Xử lý dữ liệu** | Phù hợp với dữ liệu cố định trong kịch bản mẫu. | Không xử lý được dữ liệu động, logic phân nhánh hay vòng lặp. |

---

## 5. Data-Driven Testing (DDT)

### 5.1 Khái niệm

**Data-Driven Testing (DDT)** là phương pháp kiểm thử tự động tách rời hoàn toàn **logic của kịch bản kiểm thử** khỏi **tập dữ liệu kiểm thử**. Một kịch bản logic duy nhất được tham số hóa (parameterized) và thực thi lặp lại nhiều lần với từng dòng dữ liệu lấy từ nguồn lưu trữ bên ngoài (Excel, CSV, JSON, Database hoặc API).

```
┌────────────────────────┐      ┌──────────────────────────────────┐
│ Kịch bản kiểm thử      │◄─────│ Nguồn dữ liệu kiểm thử           │
│ (Logic kịch bản chung) │      │ (Excel / CSV / DB / JSON)        │
└───────────┬────────────┘      │                                  │
            │                   │ Dòng 1: admin / P@ssw0rd1        │
            │ Lần chạy 1        │ Dòng 2: user_01 / wrong_pass     │
            │ Lần chạy 2        │ Dòng 3: empty_user / 123456      │
            │ Lần chạy 3        └──────────────────────────────────┘
            ▼
┌────────────────────────┐
│ Báo cáo kết quả        │
│ (Kết quả chi tiết cho  │
│ từng bộ dữ liệu)       │
└────────────────────────┘
```

### 5.2 Ví dụ thực tế kịch bản đăng nhập

Kịch bản kiểm thử tổng quát cho chức năng đăng nhập:

```
HÀM KIỂM THỬ: test_login(username, password, expected_outcome)
───────────────────────────────────────────────────────────────────
Bước 1: Khởi chạy ứng dụng và điều hướng đến màn hình Đăng nhập
Bước 2: Xóa trường Username và nhập giá trị: {username}
Bước 3: Xóa trường Password và nhập giá trị: {password}
Bước 4: Nhấn nút "Đăng nhập"
Bước 5: Kiểm tra kết quả thực tế hiển thị phải khớp với: {expected_outcome}
```

Bảng dữ liệu đầu vào (tập tin `login_dataset.xlsx`):

| Trường hợp | username | password | expected_outcome |
|---|---|---|---|
| TC01: Đăng nhập hợp lệ | `admin_system` | `Secured#2026` | Chuyển đến màn hình Dashboard chính |
| TC02: Sai mật khẩu | `admin_system` | `wrong_pass` | Thông báo: "Mật khẩu không chính xác" |
| TC03: Để trống tài khoản | *(để trống)* | `12345678` | Thông báo: "Tên đăng nhập không được để trống" |
| TC04: Để trống mật khẩu | `admin_system` | *(để trống)* | Thông báo: "Mật khẩu không được để trống" |
| TC05: Tài khoản bị khóa | `locked_user` | `User@1234` | Thông báo: "Tài khoản hiện đang bị tạm khóa" |

---

## 6. Checkpoints & Assertions

### 6.1 Khái niệm

**Checkpoint** (hay **Assertion**) là điểm kiểm tra trong kịch bản tự động, tại đó công cụ lấy trạng thái/giá trị thực tế của ứng dụng (Actual Result) và đem so sánh với trạng thái/giá trị kỳ vọng (Expected Result).

> **Lưu ý:** Một kịch bản tự động thực hiện từ đầu đến cuối mà **không có checkpoint** thì chỉ là một đoạn script mô phỏng thao tác người dùng (bot tự động), không thể coi là kịch bản kiểm thử hợp lệ vì không có cơ chế kết luận PASS hay FAIL.

### 6.2 Phân loại Checkpoint

| Loại Checkpoint | Đối tượng kiểm tra | Ví dụ áp dụng trên Desktop App |
|---|---|---|
| **Text / Value Checkpoint** | Nội dung chuỗi ký tự hiển thị trên control | Kiểm tra nhãn trạng thái hiển thị "Đăng nhập thành công" |
| **Property Checkpoint** | Thuộc tính của thành phần giao diện | Nút "Lưu" chuyển từ Disabled sang Enabled sau khi điền đủ form |
| **Bitmap / Image Checkpoint** | So sánh ảnh chụp pixel hoặc vùng ảnh | Kiểm tra đồ thị phân tích hoặc hình vẽ kết xuất đúng chuẩn |
| **Table / DataGrid Checkpoint** | Toàn bộ dữ liệu hiển thị trong bảng | Đối chiếu danh sách 100 giao dịch hiển thị trên DataGridView |
| **File Checkpoint** | Tệp tin xuất ra từ ứng dụng | So sánh tệp báo cáo PDF/Excel xuất ra với tệp chuẩn mẫu |
| **Database Checkpoint** | Dữ liệu lưu xuống cơ sở dữ liệu ngầm | Kiểm tra sau khi nhấn Save, một bản ghi mới được thêm vào DB |

### 6.3 Kiến trúc Assertion

```
[Thực hiện hành động thao tác trên AUT]
                  │
                  ▼
[Trích xuất giá trị thực tế từ phần tử UI (Actual Value)]
                  │
                  ▼
[So sánh đối chiếu với giá trị kỳ vọng (Expected Value)]
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
  Khớp giá trị         Không khớp giá trị
(Test Case PASS)       (Test Case FAIL)
                            │
                            ▼
              [Chụp ảnh màn hình tại thời điểm lỗi]
              [Ghi log chi tiết thông số và stacktrace]
              [Đánh dấu trạng thái lỗi vào báo cáo]
```

---

## 7. Fully vs Semi-Automated

### 7.1 Fully Automated

Toàn bộ quy trình kiểm thử từ khâu thiết lập môi trường, chuẩn bị dữ liệu, mở ứng dụng, thực thi các bước, kiểm tra kết quả cho tới khâu xuất báo cáo và dọn dẹp môi trường đều diễn ra tự động hoàn toàn mà không cần sự can thiệp của con người.

```
Đường ống hoàn toàn tự động (Fully Automated Pipeline):
Kích hoạt CI/CD ──► Biên dịch mã ──► Triển khai build ──► Chạy Test Suite ──► Xuất báo cáo ──► Gửi thông báo
                                                              (Tự động 100%)
```

**Trường hợp áp dụng tối ưu:**
- Bộ kịch bản kiểm thử hồi quy (Regression Test Suite) đã ổn định
- Kiểm thử Smoke Test nhanh sau mỗi bản build mới
- Kịch bản chạy theo lịch định kỳ ban đêm (Nightly Builds)

### 7.2 Semi-Automated

Kết hợp giữa công cụ tự động và thao tác thủ công của kiểm thử viên. Công cụ sẽ đảm nhận các bước lặp lại tốn thời gian (như tạo tài khoản hàng loạt, nhập form dài, điều hướng đến màn hình cần kiểm tra), sau đó nhường quyền cho con người quan sát, đánh giá trực quan hoặc can thiệp các bước đặc biệt.

```
Quy trình bán tự động (Semi-Automated Flow):
[Tự động]: Tạo 50 bản ghi dữ liệu mẫu và mở sẵn form chỉnh sửa chi tiết
     │
     ▼
[Thủ công]: Tester kiểm tra độ mượt đồ họa, cảm quan giao diện và khả năng tương tác
     │
     ▼
[Tự động]: Công cụ lưu log, chụp ảnh màn hình và cập nhật kết quả vào hệ thống quản lý test
```

**Trường hợp áp dụng tối ưu:**
- Kiểm thử trải nghiệm người dùng (Usability Testing) đòi hỏi cảm nhận con người
- Kiểm thử khám phá (Exploratory Testing) cần công cụ hỗ trợ chuẩn bị dữ liệu
- Các trường hợp kiểm thử liên quan đến thiết bị phần cứng đặc biệt cần cắm/rút thủ công

### 7.3 So sánh chi tiết

| Tiêu chí | Fully Automated | Semi-Automated |
|---|---|---|
| **Chi phí đầu tư ban đầu** | Cao (cần thiết kế framework, wait thông minh, tích hợp CI) | Trung bình (script đơn giản hỗ trợ từng tác vụ) |
| **Tốc độ thực thi** | Rất nhanh, có thể chạy không cần giám sát | Phụ thuộc vào tốc độ thao tác của người kiểm thử |
| **Độ ổn định** | Cao nếu framework chuẩn, nhạy cảm với thay đổi UI | Linh hoạt cao vì con người xử lý được các tình huống bất ngờ |
| **Khả năng tích hợp CI/CD** | Tích hợp hoàn hảo vào đường ống tự động | Không tích hợp hoàn toàn được vì cần tương tác người |
| **Ứng dụng chính** | Regression Testing, Smoke Testing, Performance Testing | Usability Testing, Exploratory Testing, Phần cứng đặc thù |

---

## 8. Ưu điểm & Nhược điểm của Automation Testing

### Ưu điểm

| STT | Ưu điểm | Phân tích giá trị |
|---|---|---|
| 1 | **Tốc độ thực thi vượt trội** | Script thực hiện các thao tác nhập liệu và kiểm tra nhanh hơn con người nhiều lần. |
| 2 | **Độ bao phủ cao** | Có khả năng chạy hàng trăm kịch bản kiểm thử với hàng nghìn bộ dữ liệu khác nhau trong thời gian ngắn. |
| 3 | **Độ chính xác và tính nhất quán** | Loại bỏ hoàn toàn sự mệt mỏi, nhầm lẫn hay bỏ sót bước thường gặp ở con người khi làm việc lặp lại. |
| 4 | **Khả năng tái sử dụng (Reusability)** | Kịch bản sau khi xây dựng có thể tái sử dụng cho nhiều bản build, phiên bản phát hành và môi trường khác nhau. |
| 5 | **Phát hiện sớm lỗi hồi quy** | Tự động cảnh báo ngay lập tức nếu thay đổi code mới làm hỏng các tính năng cũ đã ổn định. |
| 6 | **Vận hành không giới hạn 24/7** | Có thể lên lịch chạy ngoài giờ làm việc hoặc trên các máy chủ tự động mà không cần nhân sự trực tiếp. |
| 7 | **Hỗ trợ tối đa cho CI/CD** | Cung cấp phản hồi tức thì (fast feedback loop) cho đội ngũ phát triển sau mỗi lần tích hợp mã nguồn. |

### Nhược điểm

| STT | Nhược điểm | Thách thức thực tế |
|---|---|---|
| 1 | **Chi phí đầu tư ban đầu lớn** | Tốn chi phí mua bản quyền công cụ (nếu dùng tool thương mại) và thời gian xây dựng framework ban đầu. |
| 2 | **Gánh nặng bảo trì (Maintenance Overhead)** | Khi giao diện phần mềm thay đổi, kịch bản kiểm thử cần cập nhật liên tục; nếu thiết kế kém có thể gây nợ kỹ thuật. |
| 3 | **Không thể thay thế kiểm thử thủ công hoàn toàn** | Không phát hiện được các lỗi về mặt thị giác tinh tế, trải nghiệm người dùng hoặc các kịch bản bất thường ngoài logic lập trình. |
| 4 | **Yêu cầu kỹ năng lập trình chuyên sâu** | Đòi hỏi kiểm thử viên phải có tư duy phát triển phần mềm, hiểu về cấu trúc ứng dụng và kỹ thuật viết mã sạch. |
| 5 | **Nguy cơ lỗi sai lệch (False Positives / Negatives)** | Kịch bản có thể báo lỗi do thời gian chờ không chuẩn (chứ không phải app lỗi), làm mất thời gian điều tra nguyên nhân. |
| 6 | **Thời gian hoàn vốn (ROI) cần độ trễ** | Không mang lại hiệu quả ngay lập tức cho các dự án ngắn hạn, quy mô nhỏ hoặc đang trong giai đoạn thử nghiệm ý tưởng. |

---

## 9. Khi nào nên dùng Automation Testing?

```
BẢNG QUYẾT ĐỊNH ÁP DỤNG KIỂM THỬ TỰ ĐỘNG
──────────────────────────────────────────────────────────────────────────
NÊN ÁP DỤNG AUTOMATION                      KHÔNG NÊN ÁP DỤNG AUTOMATION
──────────────────────────────────          ──────────────────────────────
• Kịch bản kiểm thử lặp đi lặp lại nhiều lần • Kịch bản chỉ chạy 1 đến 2 lần rồi bỏ
• Bộ kịch bản kiểm thử hồi quy quy mô lớn   • Ứng dụng có giao diện thay đổi liên tục
• Kiểm thử cần số lượng dữ liệu lớn (DDT)   • Kiểm thử đòi hỏi cảm nhận và phán đoán chủ quan
• Kịch bản cần chạy trên nhiều cấu hình OS   • Chi phí viết kịch bản lớn hơn thời gian tiết kiệm
• Cần kết quả kiểm tra nhanh trong CI/CD    • Dự án ngắn hạn, gấp rút về thời gian bàn giao
• Tính năng nghiệp vụ cốt lõi đã ổn định    • Tính năng đang trong giai đoạn thiết kế thử nghiệm
```

> **Quy tắc thực tế (Rule of Thumb):** Nếu một kịch bản kiểm thử dự kiến phải thực thi lặp lại **từ 3 lần trở lên** trong vòng đời sản phẩm, đó là ứng viên sáng giá để chuyển đổi sang kịch bản tự động hóa.

---

## 10. Bảng thuật ngữ chuyên ngành

| Thuật ngữ tiếng Anh | Viết tắt | Định nghĩa và giải thích ý nghĩa |
|---|---|---|
| **Automation Testing** | AT | Quá trình sử dụng phần mềm để thực thi kiểm thử và so sánh kết quả tự động |
| **Application Under Test** | AUT | Ứng dụng cụ thể đang được hướng tới để thực hiện kiểm thử |
| **Record & Playback** | R&P | Kỹ thuật ghi lại các hành vi tương tác và phát lại tự động |
| **Data-Driven Testing** | DDT | Phương pháp kiểm thử tách rời logic và dữ liệu kiểm thử |
| **Checkpoint / Assertion** | — | Điểm kiểm tra logic để kết luận kịch bản đạt (PASS) hay không đạt (FAIL) |
| **Regression Testing** | — | Kiểm thử hồi quy nhằm đảm bảo việc sửa lỗi hoặc thêm tính năng mới không làm hỏng tính năng cũ |
| **Smoke Testing** | — | Kiểm thử sơ bộ các luồng chức năng quan trọng nhất để quyết định chấp nhận bản build |
| **Continuous Integration / Continuous Delivery** | CI/CD | Phương pháp tích hợp và bàn giao mã nguồn tự động liên tục |
| **False Positive** | — | Hiện tượng kịch bản báo kiểm thử thất bại (FAIL) nhưng thực tế ứng dụng vẫn hoạt động đúng |
| **False Negative** | — | Hiện tượng kịch bản báo kiểm thử thành công (PASS) nhưng thực tế ứng dụng đang tồn tại lỗi |
| **Flaky Test** | — | Kịch bản kiểm thử không ổn định, cho kết quả khác nhau giữa các lần chạy dù mã nguồn không đổi |
| **Test Suite** | — | Tập hợp các kịch bản kiểm thử liên quan được gom nhóm để thực thi cùng nhau |
| **Page Object Model** | POM | Mẫu thiết kế phần mềm tách biệt giao diện màn hình khỏi logic các bước kiểm thử |
| **Keyword-Driven Testing** | KDT | Phương pháp kiểm thử dựa trên các từ khóa hành động được định nghĩa trước |
| **Windows Presentation Foundation** | WPF | Nền tảng phát triển giao diện Windows dựa trên ngôn ngữ XAML và DirectX |
| **Universal Windows Platform** | UWP | Nền tảng ứng dụng đa thiết bị hiện đại của Microsoft Windows |
| **UI Automation** | UIA | Bộ giao diện lập trình ứng dụng (API) của Windows cho phép đọc và điều khiển thành phần UI |
| **Return on Investment** | ROI | Tỷ số hoàn vốn đầu tư, đo lường hiệu quả kinh tế của việc áp dụng automation |

---

> **Phụ trách:** Tín  
> **Cập nhật lần cuối:** 02/10/2026  
> **Trạng thái:** Hoàn thành
