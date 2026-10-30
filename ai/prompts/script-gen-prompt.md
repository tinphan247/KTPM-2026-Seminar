# Kỹ Thuật Prompt Engineering: Sinh Mã Nguồn Test Script C# NUnit & WinAppDriver Kèm Ràng Buộc Page Object Model (POM)
## Chuyên đề: Automation Testing cho Desktop Applications

- **Người thiết kế:** Trần Vũ Quang (MSSV: 23120346) - Nhóm 02
- **Mục tiêu:** Thiết kế prompt chuyên sâu dành cho kỹ sư SDET để các mô hình LLM sinh ra mã nguồn kiểm thử tự động hoàn chỉnh, tuân thủ kiến trúc Page Object Model (POM), tương thích với `Appium.WebDriver` và `NUnit` trên nền tảng WinAppDriver mà không bị lỗi deprecated API hoặc sai lệch locator.

---

## 1. Các Vấn Đề Thường Gặp Khi Để AI Tự Động Sinh Mã Desktop Test Script

Nếu không có prompt ràng buộc kỹ thuật (Unconstrained Prompting), các mô hình LLM thường mắc 4 lỗi nghiêm trọng:
1. **Dùng nhầm thư viện Selenium Web thay vì WindowsDriver:** Sinh ra `ChromeDriver` hoặc cú pháp web HTML không tương thích với Win32/WPF.
2. **Dùng API cũ bị Deprecated:** Sử dụng `DesiredCapabilities` (đã lỗi thời trong Appium .NET v4.x) thay vì `AppiumOptions`.
3. **Mã nguồn nguyên khối (Monolithic Spaghetti Script):** Nhồi nhét toàn bộ locator và assertion vào một hàm `[Test]` duy nhất thay vì tách Page Object Model (POM).
4. **Hardcode thời gian chờ (Sleep-based flaky test):** Dùng `Thread.Sleep(5000)` bừa bãi thay vì cơ chế chờ đợi văn minh (`DefaultWait` hoặc Timeout hợp lý).

---

## 2. Bản Đặc Tả Kỹ Thuật Prompt Sinh Script Chuẩn (Production-Ready Prompt)

Dưới đây là nội dung Prompt hoàn chỉnh được tối ưu hóa cho ChatGPT-4 / Claude / Gemini:

```markdown
[ROLE & PERSONA]
Bạn là một Senior SDET (Software Development Engineer in Test) chuyên gia về tự động hóa Desktop Applications trên hệ điều hành Windows sử dụng Microsoft WinAppDriver, C# (.NET 8/6 hoặc .NET Framework 4.8), NUnit 3 và Appium.WebDriver.

[CONTEXT & TARGET APPLICATION]
Ứng dụng mục tiêu: MiniSum Desktop Application (chạy tại đường dẫn `case-study-app/MiniSum.exe`).
Cổng kết nối WinAppDriver: `http://127.0.0.1:4723`.
Thông tin các phần tử giao diện (Inspect qua Accessibility Insights / UIA):
1. Cửa sổ Đăng nhập (LoginForm):
   - Window: Name = "winLogin" (Title: "MiniSum - Dang nhap")
   - Tài khoản: AutomationId = "txtUser"
   - Mật khẩu: AutomationId = "txtPass"
   - Nút Đăng nhập: AutomationId = "btnLogin"
   - Thông báo kết quả: AutomationId = "lblMessage"
2. Cửa sổ Tính toán (CalculatorForm):
   - Window: Name = "winMain" (Title: "MiniSum - Tinh tong")
   - Ô nhập số A: AutomationId = "txtA"
   - Ô nhập số B: AutomationId = "txtB"
   - Nút Tính tổng: AutomationId = "btnSum"
   - Nhãn kết quả: AutomationId = "lblResult"
   - Nút Đăng xuất: AutomationId = "btnLogout"

[ARCHITECTURAL REQUIREMENTS: PAGE OBJECT MODEL]
Hãy thiết kế mã nguồn theo đúng mẫu thiết kế Page Object Model (POM) gồm các thành phần sau:
1. `LoginPage.cs`:
   - Đóng gói các thuộc tính định vị (`WindowsElement`) bằng `driver.FindElementByAccessibilityId`.
   - Các phương thức hành động: `EnterUsername(string user)`, `EnterPassword(string pass)`, `ClickLogin()`, `Login(string user, string pass)`, `GetMessageText()`.
2. `CalculatorPage.cs`:
   - Đóng gói các phần tử: `txtA`, `txtB`, `btnSum`, `lblResult`, `btnLogout`.
   - Các phương thức hành động: `EnterA(string a)`, `EnterB(string b)`, `ClickSum()`, `Calculate(string a, string b)`, `GetResultText()`, `ClickLogout()`.
3. `BaseTest.cs`:
   - Khởi tạo `WindowsDriver<WindowsElement>` với `AppiumOptions` (đặt `app`, `deviceName = "WindowsPC"`).
   - `[SetUp]` mở app, `[TearDown]` đóng session và thoát ứng dụng.
4. `MiniSumAutomationTests.cs`:
   - Test Method 1: `Test_Login_Success()` -> Nhập "admin" / "1234", kiểm tra chuyển cảnh sang `winMain`.
   - Test Method 2: `Test_Login_Failed()` -> Nhập "admin" / "wrong", kiểm tra `lblMessage` hiển thị "Sai tài khoản hoặc mật khẩu!".
   - Test Method 3: `Test_Bva_Calculation(string a, string b, string expected)` -> Sử dụng `[TestCase]` hoặc `[TestCaseSource]` kiểm tra các ca biên tính toán.

[TECHNICAL CONSTRAINTS]
- Sử dụng cú pháp C# hiện đại, rõ ràng, có XML documentation comments bằng tiếng Việt.
- Sử dụng thư viện:
  * `OpenQA.Selenium.Appium`
  * `OpenQA.Selenium.Appium.Windows`
  * `NUnit.Framework`
- Tuyệt đối không dùng `DesiredCapabilities`. Phải dùng `AppiumOptions`.
- Xử lý thời gian chờ implicit wait 3-5 giây để đảm bảo không bị NoSuchElementException khi form đang khởi tạo.
```

---

## 3. Khung Đánh Giá Mã Nguồn Do AI Sinh Ra

| Tiêu chí | Trọng số | Yêu cầu đạt được |
|---|:---:|---|
| **Tính đúng đắn cú pháp** | 30% | Mã C# biên dịch được ngay không có lỗi ngữ pháp, đúng namespace. |
| **Tuân thủ mẫu POM** | 30% | Tách biệt hoàn toàn tầng Page Object (Locators & Actions) khỏi tầng Test Assertion. |
| **Chính xác Locator** | 20% | Đúng 100% `AccessibilityId` theo đặc tả `txtUser`, `txtPass`, `btnLogin`, `txtA`, `txtB`, `btnSum`. |
| **Vòng đời Session chuẩn** | 10% | Khởi tạo sạch sẽ trong SetUp và giải phóng tài nguyên trong TearDown (Quit driver). |
| **Chất lượng Assert** | 10% | Sử dụng đúng NUnit `Assert.AreEqual` với thông điệp giải thích rõ ràng khi fail. |
