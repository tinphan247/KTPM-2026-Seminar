# Automation Testing for Desktop Applications
## Phần 2: Theory

> **Seminar – Phụ trách:** Tín  
> **Nội dung:** Khái niệm cốt lõi · Kỹ thuật tự động hóa · Thách thức đặc thù · Thuật ngữ  
> **Cập nhật lần cuối:** 27/10/2026 (bổ sung Lần 2: POM, Flaky Test, Wait, Test Oracle, Recovery Testing)  
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
7. [Page Object Model (POM)](#7-page-object-model-pom)
   - 7.1 [Khái niệm](#71-khái-niệm)
   - 7.2 [Ví dụ trên MiniSum](#72-ví-dụ-trên-minisum)
   - 7.3 [POM trong Katalon Studio và WinAppDriver](#73-pom-trong-katalon-studio-và-winappdriver)
   - 7.4 [Ưu điểm, nhược điểm và nguyên tắc áp dụng](#74-ưu-điểm-nhược-điểm-và-nguyên-tắc-áp-dụng)
8. [Flaky Test](#8-flaky-test)
   - 8.1 [Khái niệm và biểu hiện](#81-khái-niệm-và-biểu-hiện)
   - 8.2 [Nguyên nhân gốc rễ](#82-nguyên-nhân-gốc-rễ)
   - 8.3 [Cách phát hiện](#83-cách-phát-hiện)
   - 8.4 [Cách xử lý](#84-cách-xử-lý)
9. [Wait Strategy – Implicit, Explicit và Fluent Wait](#9-wait-strategy--implicit-explicit-và-fluent-wait)
   - 9.1 [Vì sao phải chờ](#91-vì-sao-phải-chờ)
   - 9.2 [Implicit Wait](#92-implicit-wait)
   - 9.3 [Explicit Wait](#93-explicit-wait)
   - 9.4 [Fluent Wait](#94-fluent-wait)
   - 9.5 [So sánh và cách chọn](#95-so-sánh-và-cách-chọn)
10. [Test Oracle](#10-test-oracle)
   - 10.1 [Khái niệm](#101-khái-niệm)
   - 10.2 [Phân loại Test Oracle](#102-phân-loại-test-oracle)
   - 10.3 [Test Oracle trong kiểm thử tự động](#103-test-oracle-trong-kiểm-thử-tự-động)
   - 10.4 [Bài toán Oracle và giới hạn](#104-bài-toán-oracle-và-giới-hạn)
11. [Recovery Testing](#11-recovery-testing)
   - 11.1 [Khái niệm](#111-khái-niệm)
   - 11.2 [Kịch bản sự cố thường gặp](#112-kịch-bản-sự-cố-thường-gặp)
   - 11.3 [Cơ chế phục hồi trong automation](#113-cơ-chế-phục-hồi-trong-automation)
   - 11.4 [Checklist kiểm tra khả năng phục hồi](#114-checklist-kiểm-tra-khả-năng-phục-hồi)
12. [Fully vs Semi-Automated](#12-fully-vs-semi-automated)
   - 12.1 [Fully Automated](#121-fully-automated)
   - 12.2 [Semi-Automated](#122-semi-automated)
   - 12.3 [So sánh chi tiết](#123-so-sánh-chi-tiết)
13. [Ưu điểm & Nhược điểm của Automation Testing](#13-ưu-điểm--nhược-điểm-của-automation-testing)
14. [Khi nào nên dùng Automation Testing?](#14-khi-nào-nên-dùng-automation-testing)
15. [Bảng thuật ngữ chuyên ngành](#15-bảng-thuật-ngữ-chuyên-ngành)

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

## 7. Page Object Model (POM)

### 7.1 Khái niệm

**Page Object Model (POM)** là mẫu thiết kế (design pattern) trong kiểm thử tự động, trong đó **mỗi màn hình hoặc cửa sổ của ứng dụng được biểu diễn bằng một lớp (class) riêng**. Lớp này đóng gói ba thành phần:

1. **Locator** – định danh các phần tử giao diện (`AutomationId`, `Name`, `XPath`…).
2. **Hành động** – các thao tác người dùng thực hiện được trên màn hình (nhập liệu, nhấn nút, chuyển màn hình).
3. **Truy vấn trạng thái** – các hàm đọc dữ liệu phục vụ checkpoint (lấy nội dung nhãn, kiểm tra nút đang Enabled hay Disabled).

Kịch bản kiểm thử **không thao tác trực tiếp lên control**, mà gọi các phương thức nghiệp vụ do page object cung cấp. Nhờ vậy khi giao diện thay đổi, chỉ cần sửa **một chỗ** trong page object thay vì sửa toàn bộ kịch bản.

```
        Không dùng POM                        Dùng POM
┌───────────────────────────┐        ┌───────────────────────────┐
│ TC01_Login                │        │ TC01_Login                │
│  find("txtUser").sendKeys│        │  loginPage.Login(u, p)    │
│  find("txtPass").sendKeys│        │  Assert(lblMessage)       │
│  find("btnLogin").click  │        └─────────────┬─────────────┘
│  find("lblMessage")...   │                      │ gọi
└───────────────────────────┘        ┌─────────────▼─────────────┐
   Locator rải khắp test case        │ LoginPage                 │
   → đổi UI phải sửa nhiều nơi       │  locator + Login()        │
                                     └───────────────────────────┘
                                        Locator tập trung một nơi
```

### 7.2 Ví dụ trên MiniSum

Giả sử cần kiểm thử màn hình đăng nhập của `MiniSum.exe`. Cách viết **không có POM** lặp lại locator trong từng test case:

```csharp
// TC01 - lặp locator ngay trong test
driver.FindElementByAccessibilityId("txtUser").SendKeys("admin");
driver.FindElementByAccessibilityId("txtPass").SendKeys("1234");
driver.FindElementByAccessibilityId("btnLogin").Click();
Assert.AreEqual("Dang nhap thanh cong",
    driver.FindElementByAccessibilityId("lblMessage").Text);
```

Cách viết **có POM** – tách thành `LoginPage` và `CalculatorPage`:

```csharp
// PageObjects/LoginPage.cs
public class LoginPage
{
    private readonly WindowsDriver<WindowsElement> driver;

    public LoginPage(WindowsDriver<WindowsElement> driver) => this.driver = driver;

    private WindowsElement TxtUser => driver.FindElementByAccessibilityId("txtUser");
    private WindowsElement TxtPass => driver.FindElementByAccessibilityId("txtPass");
    private WindowsElement BtnLogin => driver.FindElementByAccessibilityId("btnLogin");
    private WindowsElement LblMessage => driver.FindElementByAccessibilityId("lblMessage");

    public void Login(string user, string pass)
    {
        TxtUser.Clear();
        TxtUser.SendKeys(user);
        TxtPass.SendKeys(pass);
        BtnLogin.Click();
    }

    public string Message => LblMessage.Text;
}
```

```csharp
// TC01_Login_Success.cs - test case chỉ còn nghiệp vụ
var loginPage = new LoginPage(driver);
loginPage.Login("admin", "1234");

Assert.AreEqual("Dang nhap thanh cong", loginPage.Message);
var calculatorPage = new CalculatorPage(driver);
Assert.IsTrue(calculatorPage.IsDisplayed());
```

Khi bản **v2** đổi `btnSum` thành `btnCalculate`, chỉ `CalculatorPage` phải sửa; toàn bộ test case dùng lại vẫn giữ nguyên. Đây chính là kịch bản **maintenance & self-healing** được demo trong seminar.

### 7.3 POM trong Katalon Studio và WinAppDriver

| Công cụ | Cách hiện thực POM | Ghi chú |
|---|---|---|
| **Katalon Studio** | **Object Repository** đóng vai trò kho locator dùng chung; mỗi màn hình là một thư mục (`MiniSum/Login`, `MiniSum/Calculator`). Test case tham chiếu `findWindowsObject('Object Repository/...')` thay vì khai báo locator trực tiếp. Có thể bọc thêm **Custom Keyword** để tạo lớp hành vi (`LoginKeyword.login()`) | POM ở mức “locator tập trung”, chưa phải class đầy đủ |
| **WinAppDriver + C# NUnit** | Tạo thư mục `PageObjects/` với `LoginPage.cs`, `CalculatorPage.cs`; test case chỉ gọi phương thức | POM đầy đủ theo hướng lập trình hướng đối tượng |

### 7.4 Ưu điểm, nhược điểm và nguyên tắc áp dụng

| Ưu điểm | Nhược điểm |
|---|---|
| Locator tập trung → bảo trì nhanh khi UI đổi | Tốn công thiết kế ban đầu, nhiều file hơn |
| Test case đọc như tài liệu nghiệp vụ, giảm trùng lặp | Với ứng dụng rất nhỏ, POM có thể là over-engineering |
| Tái sử dụng hành động giữa nhiều test case | Dễ phình to nếu nhồi cả logic kiểm thử vào page object |
| Hỗ trợ phân công: người viết page object và người viết test case độc lập | Cần kỷ luật đặt tên, nếu không sẽ thành “God class” |

**Nguyên tắc áp dụng:**
- Page object **chỉ mô tả giao diện**, **không chứa assertion**; assertion thuộc về test case.
- Một page object tương ứng một màn hình (hoặc một thành phần tái sử dụng như dialog, toolbar).
- Phương thức nên diễn đạt **ý định nghiệp vụ** (`Login`, `Calculate`, `OpenHistory`) thay vì `ClickButton1`.
- Trả về page object tiếp theo khi hành động làm chuyển màn hình (`Login()` trả về `CalculatorPage`) để test case mô tả đúng luồng.

---

## 8. Flaky Test

### 8.1 Khái niệm và biểu hiện

**Flaky Test** là kịch bản kiểm thử cho kết quả **không ổn định giữa các lần chạy dù mã nguồn ứng dụng và mã kiểm thử không thay đổi**: lần chạy PASS, lần chạy FAIL, có khi FAIL rồi PASS khi chạy lại ngay lập tức.

Flaky test là vấn đề nghiêm trọng hơn việc “không có test”, vì:

- Đội phát triển **mất niềm tin** vào bộ kiểm thử: khi test báo FAIL, không ai biết là ứng dụng lỗi thật hay test lỗi.
- Tốn thời gian điều tra lại các lỗi “ma”, làm chậm pipeline CI/CD.
- Che giấu lỗi thật: một khi nhóm đã quen với việc “chạy lại là PASS”, lỗi thật sẽ bị bỏ qua.

**Biểu hiện thường gặp trên desktop automation:**

| Biểu hiện | Ví dụ với MiniSum |
|---|---|
| PASS/FAIL xen kẽ trên cùng máy | `TC03_BVA` lúc đọc được `lblResult`, lúc đọc được chuỗi rỗng |
| Chỉ FAIL trên máy CI hoặc máy chậm hơn | Máy yếu nên cửa sổ Calculator xuất hiện sau khi script đã tìm control |
| Phụ thuộc thứ tự chạy | Chạy riêng thì PASS, chạy cả suite thì FAIL do cửa sổ cũ còn mở |
| FAIL khi màn hình bị khoá / đổi độ phân giải | Toạ độ click sai khi scale 125% hoặc khi RDP |

### 8.2 Nguyên nhân gốc rễ

| Nhóm nguyên nhân | Mô tả | Ví dụ |
|---|---|---|
| **Timing / bất đồng bộ** | Script chạy nhanh hơn tốc độ ứng dụng phản hồi | Đọc `lblMessage` trước khi ứng dụng kịp cập nhật sau khi click |
| **Locator không ổn định** | Dùng locator sinh động (XPath theo index, toạ độ) | `//Button[3]` đổi vị trí khi thêm nút mới |
| **Trạng thái dùng chung** | Test này để lại dữ liệu/cửa sổ ảnh hưởng test khác | Test trước không đóng app, test sau mở thêm instance |
| **Dữ liệu test không cô lập** | Dùng chung file Excel/DB, không reset trước mỗi lần chạy | Lịch sử tính toán (v2) tích luỹ qua nhiều test |
| **Môi trường** | DPI, độ phân giải, ngôn ngữ, focus, phần mềm diệt virus | Windows scale 150% làm toạ độ click lệch |
| **Tài nguyên / session** | WinAppDriver session chết, port 4723 bị chiếm | Chạy song song nhiều test trên cùng session |

### 8.3 Cách phát hiện

1. **Chạy lặp**: thực thi cùng test N lần (ví dụ 10–20 lần) và thống kê tỉ lệ PASS. Test có tỉ lệ PASS < 100% là flaky.
2. **Ghi log đầy đủ**: timestamp từng bước, ảnh chụp màn hình tại thời điểm FAIL, giá trị Actual/Expected.
3. **Đo “flaky rate”** theo từng test case để ưu tiên sửa: test FAIL 1/20 lần vẫn phải xử lý.
4. **Chạy trên nhiều cấu hình**: máy nhanh/chậm, độ phân giải khác nhau, có/không có màn hình phụ.

### 8.4 Cách xử lý

| Biện pháp | Cách làm | Lưu ý |
|---|---|---|
| **Chờ tường minh (Explicit Wait)** | Chờ *điều kiện* cụ thể thay vì chờ cố định: `waitForElementPresent`, `WebDriverWait.Until(...)` | Ưu tiên số 1, xem mục 9 – Wait Strategy |
| **Locator ổn định** | Dùng `AutomationId` do đội phát triển đặt, tránh XPath theo index/toạ độ | MiniSum đặt sẵn `txtUser`, `btnLogin`, `lblResult`… |
| **Cô lập test** | Mỗi test tự chuẩn bị trạng thái đầu vào và dọn dẹp ở `finally`/`TearDown` | Không phụ thuộc test chạy trước |
| **Dữ liệu riêng** | Sinh dữ liệu cho từng lần chạy hoặc reset file test data | Tránh ghi đè chéo giữa các test |
| **Retry có kiểm soát** | Chỉ retry test đã được xác định là flaky, có ghi log số lần retry | Không dùng retry để “che” lỗi thật |
| **Quarantine** | Tách test flaky khỏi suite chính, theo dõi riêng cho tới khi sửa xong | Giữ suite chính luôn “xanh” và đáng tin |

**Phân biệt flaky test và lỗi thật:**

| Tiêu chí | Flaky Test | Lỗi thật của ứng dụng |
|---|---|---|
| Chạy lại nhiều lần | Kết quả thay đổi | Luôn FAIL |
| Thay đổi môi trường | Có thể PASS/FAIL khác nhau | FAIL ở mọi môi trường |
| Log/ảnh chụp | Thường cho thấy script thao tác sai thời điểm | Cho thấy giá trị thực tế sai so với đặc tả |
| Hành động | Sửa script (wait, locator, isolation) | Báo lỗi cho đội phát triển |

> **Liên hệ MiniSum:** sau khi đăng nhập thành công, ứng dụng cố ý **giữ màn hình Login thêm 1 giây** trước khi mở cửa sổ Calculator. Nếu script không chờ mà đọc `lblMessage` hoặc tìm `winMain` ngay lập tức, test sẽ flaky. Đây là tình huống được dùng để minh hoạ wait strategy ở mục tiếp theo.

---

## 9. Wait Strategy – Implicit, Explicit và Fluent Wait

### 9.1 Vì sao phải chờ

Trong desktop app, giao diện **không cập nhật đồng bộ với thao tác của script**: cửa sổ cần thời gian khởi tạo handle, hiệu ứng chuyển màn hình có animation, xử lý nghiệp vụ chạy trên UI thread, dữ liệu được tải từ đĩa/dịch vụ. Nếu script tìm control hoặc đọc giá trị ngay sau khi click, nó có thể chạy *trước* khi ứng dụng kịp phản hồi → sinh ra flaky test.

Có ba cơ chế chờ phổ biến trong automation desktop, đều được hỗ trợ bởi WinAppDriver/Appium và Katalon Studio.

### 9.2 Implicit Wait

**Implicit Wait** là thời gian chờ mặc định được cấu hình **một lần cho toàn bộ driver**. Mỗi khi gọi tìm phần tử, driver sẽ thử lại liên tục trong khoảng thời gian này trước khi ném `NoSuchElementException`.

```csharp
// C# – WinAppDriver: chờ tối đa 10 giây cho MỌI lệnh tìm phần tử
driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
```

- **Ưu điểm:** cấu hình một dòng, áp dụng cho mọi locator, script gọn.
- **Nhược điểm:** không phân biệt được “phần tử chưa xuất hiện” với “phần tử không bao giờ xuất hiện” → test chậm và khó chẩn đoán; không kiểm tra được điều kiện phức tạp (text đã đổi chưa, nút đã Enabled chưa). Khi một phần tử thật sự không tồn tại, mỗi lần tìm đều phải chờ hết timeout.

### 9.3 Explicit Wait

**Explicit Wait** chờ **một điều kiện cụ thể** trên **một phần tử cụ thể**, với timeout riêng cho từng bước. Đây là cách được khuyến nghị.

```csharp
// C# – WinAppDriver: chờ cửa sổ Calculator xuất hiện (tối đa 10 giây)
var wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));
wait.Until(d => d.FindElementByAccessibilityId("winMain").Displayed);

// Chờ nhãn kết quả có nội dung mong đợi
var result = wait.Until(d =>
{
    var text = d.FindElementByAccessibilityId("lblResult").Text;
    return text == "Ket qua: 5 + 7 = 12" ? text : null;
});
```

```groovy
// Katalon Studio (Windows Desktop) – chờ cửa sổ và phần tử
Windows.waitForElementPresent(
    findWindowsObject('Object Repository/MiniSum/Calculator/winMain'), 10)
Windows.switchToWindowTitle('MiniSum - Tinh tong')
Windows.waitForElementPresent(
    findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'), 10)
```

- **Ưu điểm:** rõ ràng về mặt ý định, chỉ chờ đúng nơi cần, timeout ngắn và dễ chẩn đoán khi FAIL, có thể chờ điều kiện phức tạp.
- **Nhược điểm:** phải viết thêm code; nếu quên ở một bước vẫn có thể flaky.

### 9.4 Fluent Wait

**Fluent Wait** là dạng mở rộng của Explicit Wait, cho phép cấu hình **tần suất kiểm tra (polling interval)** và **danh sách exception được bỏ qua** trong lúc chờ.

```csharp
var fluentWait = new DefaultWait<WindowsDriver<WindowsElement>>(driver)
{
    Timeout = TimeSpan.FromSeconds(15),
    PollingInterval = TimeSpan.FromMilliseconds(500)
};
fluentWait.IgnoreExceptionTypes(typeof(NoSuchElementException), typeof(StaleElementReferenceException));

string message = fluentWait.Until(d =>
{
    var el = d.FindElementByAccessibilityId("lblMessage");
    return string.IsNullOrWhiteSpace(el.Text) ? null : el.Text;
});
```

- **Ưu điểm:** kiểm soát chi tiết nhịp kiểm tra, bỏ qua các lỗi tạm thời (phần tử bị dựng lại → `StaleElementReference`), phù hợp với ứng dụng khởi động chậm hoặc có animation dài.
- **Nhược điểm:** cấu hình phức tạp, dễ lạm dụng thành “chờ vô tội vạ” làm test chậm.

### 9.5 So sánh và cách chọn

| Tiêu chí | Implicit Wait | Explicit Wait | Fluent Wait |
|---|---|---|---|
| Phạm vi | Toàn bộ driver | Từng bước | Từng bước |
| Điều kiện chờ | Chỉ “tìm thấy phần tử” | Mọi điều kiện tự định nghĩa | Mọi điều kiện + polling + ignore exception |
| Cấu hình | Một lần | Mỗi lần gọi | Mỗi lần gọi, nhiều tham số |
| Khả năng chẩn đoán khi FAIL | Thấp (chỉ biết timeout) | Cao | Cao |
| Khuyến nghị | Chỉ dùng làm lưới an toàn, timeout nhỏ (3–5s) | **Mặc định nên dùng** | Khi cần kiểm soát chi tiết |

**Nguyên tắc thực hành:**
- **Không dùng `Thread.Sleep`/`delay` cố định** làm cơ chế chờ chính: máy nhanh thì lãng phí, máy chậm vẫn flaky. Chỉ dùng khi thật sự cần (ví dụ chờ animation ngắn) và phải ghi chú lý do.
- Mỗi bước chờ nên gắn với **một điều kiện nghiệp vụ** (“cửa sổ Calculator đã mở”, “lblResult đã có nội dung”) thay vì “chờ 2 giây”.
- Đặt timeout theo **thời gian phản hồi thực tế đo được × 2–3**, không đặt quá lớn.
- Tránh trộn Implicit Wait với Explicit Wait trong cùng session vì thời gian chờ thực tế sẽ khó dự đoán.

> **Áp dụng cho MiniSum:** sau khi đăng nhập thành công, ứng dụng giữ màn hình Login 1 giây rồi mới mở Calculator. Script nên dùng `waitForElementPresent(winMain, 10)` / `WebDriverWait` thay vì `Thread.Sleep(1000)`; cách này vừa nhanh hơn khi máy khoẻ, vừa không flaky khi máy chậm.

---

## 10. Test Oracle

### 10.1 Khái niệm

**Test Oracle** là **cơ chế hoặc nguồn thông tin dùng để xác định một kết quả kiểm thử là ĐÚNG hay SAI**. Nói cách khác, oracle trả lời câu hỏi: *“Làm sao biết giá trị ứng dụng trả về là chấp nhận được?”*

Một test case không có oracle chỉ là chuỗi thao tác mô phỏng người dùng; nó không thể kết luận PASS/FAIL. Oracle tồn tại **độc lập với công cụ kiểm thử**: Katalon, WinAppDriver hoặc một script PowerShell đều chỉ là phương tiện thực thi, còn tính đúng/sai do oracle quyết định.

```
Test Case: nhập A = 5, B = 7, nhấn TINH TONG
                     │
                     ▼
        Giá trị thực tế: lblResult = "Ket qua: 5 + 7 = 12"
                     │
        ┌────────────┴─────────────┐
        ▼                          ▼
   Oracle: đặc tả quy tắc      So sánh
   "lblResult = Ket qua: A + B = A+B"
        │
        ▼
   Khớp → PASS  |  Không khớp → FAIL
```

### 10.2 Phân loại Test Oracle

| Loại oracle | Nguồn xác định kết quả đúng | Ví dụ trên MiniSum |
|---|---|---|
| **Specified oracle** (theo đặc tả) | Yêu cầu/tài liệu đặc tả của hệ thống | Đặc tả ghi: đăng nhập sai phải hiển thị `Sai tai khoan hoac mat khau` |
| **Derived oracle** (suy dẫn) | Tính toán từ công thức, bảng quyết định, giá trị biên | Với A = -99, B = 99 → kỳ vọng `Ket qua: -99 + 99 = 0` |
| **Implicit oracle** (ngầm định) | Kỳ vọng hiển nhiên: không crash, không treo, không rò rỉ | Sau khi nhấn TINH TONG, ứng dụng vẫn phản hồi và không hiện hộp thoại lỗi .NET |
| **Consistency oracle** (nhất quán) | So sánh giữa hai lần chạy / hai phiên bản / hai môi trường | Cùng bộ dữ liệu BVA, kết quả của v1 và v3 phải giống nhau ở miền hợp lệ |
| **Human oracle** (con người) | Chuyên gia/người dùng đánh giá bằng mắt | Kiểm tra bố cục, màu sắc, thông báo lỗi có dễ hiểu không |
| **Metamorphic oracle** (biến đổi) | So sánh quan hệ giữa các lần chạy có dữ liệu biến đổi | Đổi chỗ A và B thì tổng không đổi: `f(a,b) = f(b,a)` |

### 10.3 Test Oracle trong kiểm thử tự động

Trong automation, oracle được **hiện thực hoá bằng checkpoint/assertion**. Mỗi assertion cần trả lời rõ ba câu hỏi:

1. **Kiểm tra cái gì?** – phần tử nào, thuộc tính nào (`lblResult.Text`, `btnLogin.Enabled`…).
2. **Giá trị kỳ vọng là bao nhiêu?** – lấy từ nguồn oracle nào (đặc tả, công thức, dữ liệu chuẩn).
3. **Khi lệch thì kết luận gì?** – FAIL kèm thông điệp chứa Actual và Expected để điều tra.

```csharp
// Oracle dạng specified/derived: công thức A + B và định dạng chuỗi theo đặc tả
int a = 5, b = 7;
string expected = $"Ket qua: {a} + {b} = {a + b}";
string actual = calculatorPage.Result;

Assert.AreEqual(expected, actual,
    $"Sai ket qua hien thi. Expected='{expected}', Actual='{actual}'");
```

**Lưu ý chất lượng oracle:**
- Oracle **quá yếu** (“chỉ cần không crash”) sẽ cho PASS giả, không phát hiện lỗi nghiệp vụ.
- Oracle **quá chặt** vào chi tiết giao diện (toạ độ, font, màu) sẽ FAIL oan mỗi khi đổi UI.
- Kỳ vọng phải được tính **độc lập với cách ứng dụng tính** — nếu lấy chính kết quả của app làm kỳ vọng thì test không có giá trị.

### 10.4 Bài toán Oracle và giới hạn

**Oracle problem** là tình huống rất khó hoặc rất tốn kém để xác định đâu là kết quả đúng, ví dụ:

- Giao diện phức tạp, kết quả là hình ảnh/đồ thị → khó so sánh tự động.
- Ứng dụng có nhiều kết quả “đúng” tương đương (thứ tự hiển thị không quan trọng).
- Không có đặc tả rõ ràng, hoặc đặc tả lỗi thời.

**Cách giảm nhẹ:**
- Ưu tiên dữ liệu kiểm thử có **kỳ vọng tính được bằng công thức** (BVA, bảng quyết định) như bộ 12 ca của MiniSum.
- Kết hợp nhiều loại oracle (specified + implicit + consistency) trong cùng một test.
- Với phần giao diện khó so sánh, dùng **human oracle** hoặc **bitmap checkpoint** có ngưỡng sai lệch hợp lý.

> **Liên hệ MiniSum:** bộ dữ liệu BVA gồm 12 ca là ví dụ của **derived oracle** – kỳ vọng được tính từ quy tắc `A + B` và miền giá trị `[-99, 99]`, hoàn toàn độc lập với cách ứng dụng hiển thị.

---

## 11. Recovery Testing

### 11.1 Khái niệm

**Recovery Testing** (kiểm thử phục hồi) là loại kiểm thử đánh giá khả năng của hệ thống **tự phục hồi sau sự cố** và **tiếp tục hoạt động đúng**: ứng dụng bị treo/crash, mất kết nối, tiến trình bị kill, dữ liệu bị hỏng hoặc tài nguyên bị chiếm dụng.

Trong bối cảnh automation, khái niệm này có hai tầng:

1. **Kiểm thử khả năng phục hồi của AUT** – AUT có tự khôi phục trạng thái, có báo lỗi rõ ràng, có giữ dữ liệu đã nhập không?
2. **Cơ chế tự phục hồi của bộ test** – khi một test hoặc session automation gặp sự cố, suite có dọn dẹp đúng cách và tiếp tục chạy các test còn lại không?

Tầng thứ hai đặc biệt quan trọng với desktop automation vì WinAppDriver/Katalon **giữ session gắn với tiến trình ứng dụng**: chỉ cần một cửa sổ “ma” còn sót lại là các test sau có thể FAIL hàng loạt.

### 11.2 Kịch bản sự cố thường gặp

| Sự cố | Hậu quả nếu không xử lý | Cách phát hiện |
|---|---|---|
| Ứng dụng crash giữa chừng | Script treo tới hết timeout, các test sau FAIL dây chuyền | Tiến trình biến mất, `NoSuchWindowException` |
| Ứng dụng treo (Not Responding) | Lệnh click chờ vô hạn, suite bị block | Cửa sổ không phản hồi, timeout liên tiếp |
| Session WinAppDriver chết / port bị chiếm | Không mở được app ở test kế tiếp | `WebDriverException`, lỗi kết nối `127.0.0.1:4723` |
| Popup/dialog bất ngờ | Click trúng sai phần tử, kết quả sai | Ảnh chụp màn hình cho thấy dialog lạ |
| Cửa sổ cũ còn mở | Mở thêm instance, đọc nhầm window | Nhiều cửa sổ cùng title trong danh sách |
| Dữ liệu bẩn từ lần chạy trước | Kết quả phụ thuộc lịch sử (ví dụ danh sách lịch sử v2) | Kết quả khác nhau giữa lần chạy đầu và lần sau |

### 11.3 Cơ chế phục hồi trong automation

**a) Dọn dẹp trong `TearDown` / `finally` (bắt buộc)**

```csharp
[TestFixture]
public class MiniSumTests
{
    private WindowsDriver<WindowsElement> driver;

    [SetUp]
    public void StartApp()
    {
        var options = new AppiumOptions();
        options.AddAdditionalCapability("app", MiniSumPath);
        driver = new WindowsDriver<WindowsElement>(new Uri("http://127.0.0.1:4723"), options);
    }

    [TearDown]
    public void CloseApp()
    {
        try
        {
            if (driver != null)
            {
                // Nếu test FAIL, chụp ảnh trước khi đóng để còn bằng chứng
                if (TestContext.CurrentContext.Result.Outcome.Status == NUnit.Framework.Interfaces.TestStatus.Failed)
                {
                    ScreenshotHelper.Capture(driver, TestContext.CurrentContext.Test.Name);
                }
                driver.Quit();
            }
        }
        catch (Exception ex)
        {
            // Không để lỗi dọn dẹp che mất kết quả test
            TestContext.Progress.WriteLine($"Cleanup warning: {ex.Message}");
        }
        finally
        {
            driver = null;
        }
    }
}
```

**b) Khởi tạo lại session khi session chết**

```csharp
private void EnsureSessionAlive()
{
    try
    {
        _ = driver.SessionId;          // truy cập nhẹ để kiểm tra session
    }
    catch (WebDriverException)
    {
        driver = CreateDriver();       // tạo session mới thay vì bỏ cả suite
    }
}
```

**c) Test Listener của Katalon Studio**

Katalon cho phép can thiệp vào vòng đời test qua **Test Listener**, ví dụ `ScreenshotOnFailure` đã dùng trong dự án:

```groovy
class ScreenshotOnFailure {
    @AfterTestCase
    def afterTestCase(TestCaseContext testCaseContext) {
        if (testCaseContext.getTestCaseStatus() == 'FAILED') {
            WebUI.takeScreenshot("Reports/screenshots/${testCaseContext.getTestCaseId()}.png")
        }
        // Dọn dẹp: đóng ứng dụng nếu còn mở
        Windows.closeApplication()
    }
}
```

**d) Nguyên tắc chung**
- Mỗi test phải để hệ thống ở trạng thái sạch khi kết thúc, **kể cả khi test FAIL**.
- Không “nuốt” exception trong `catch` mà không ghi log.
- Chụp ảnh + log ngay tại thời điểm lỗi, trước khi dọn dẹp.
- Với suite chạy dài, tách **test độc lập** để một test hỏng không kéo theo cả suite.

### 11.4 Checklist kiểm tra khả năng phục hồi

- [ ] Ứng dụng bị kill giữa lúc chạy test → suite vẫn tiếp tục được test kế tiếp.
- [ ] Sau mỗi test, không còn tiến trình `MiniSum*.exe` hay cửa sổ nào sót lại.
- [ ] Test FAIL có ảnh chụp màn hình và log giá trị Actual/Expected.
- [ ] Session WinAppDriver được tạo mới nếu kết nối cũ không còn.
- [ ] Dữ liệu test (file Excel, lịch sử trong bộ nhớ) được reset trước mỗi lần chạy.
- [ ] Khi AUT báo lỗi nghiệp vụ (ví dụ `lblError`), test kết luận FAIL/PASS đúng chứ không crash.

> **Liên hệ MiniSum:** ứng dụng không lưu dữ liệu xuống đĩa, lịch sử tính toán (v2) chỉ nằm trong bộ nhớ nên mỗi lần khởi động lại là trạng thái sạch. Tuy vậy, script vẫn phải đóng ứng dụng trong `TearDown`; nếu để sót cửa sổ, lần chạy sau sẽ mở thêm instance và test sẽ đọc nhầm cửa sổ cũ.

---

## 12. Fully vs Semi-Automated

### 12.1 Fully Automated

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

### 12.2 Semi-Automated

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

### 12.3 So sánh chi tiết

| Tiêu chí | Fully Automated | Semi-Automated |
|---|---|---|
| **Chi phí đầu tư ban đầu** | Cao (cần thiết kế framework, wait thông minh, tích hợp CI) | Trung bình (script đơn giản hỗ trợ từng tác vụ) |
| **Tốc độ thực thi** | Rất nhanh, có thể chạy không cần giám sát | Phụ thuộc vào tốc độ thao tác của người kiểm thử |
| **Độ ổn định** | Cao nếu framework chuẩn, nhạy cảm với thay đổi UI | Linh hoạt cao vì con người xử lý được các tình huống bất ngờ |
| **Khả năng tích hợp CI/CD** | Tích hợp hoàn hảo vào đường ống tự động | Không tích hợp hoàn toàn được vì cần tương tác người |
| **Ứng dụng chính** | Regression Testing, Smoke Testing, Performance Testing | Usability Testing, Exploratory Testing, Phần cứng đặc thù |

---

## 13. Ưu điểm & Nhược điểm của Automation Testing

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

## 14. Khi nào nên dùng Automation Testing?

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

## 15. Bảng thuật ngữ chuyên ngành

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
