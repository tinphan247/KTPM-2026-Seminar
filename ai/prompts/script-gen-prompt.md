# Kỹ Thuật Prompt Engineering: Sinh Mã Nguồn Test Script C# NUnit & WinAppDriver Kèm Ràng Buộc Page Object Model (POM)
## Chuyên đề: Automation Testing cho Desktop Applications

- **Người thiết kế:** Trần Vũ Quang (MSSV: 23120346) - Nhóm 02
- **Mục tiêu:** Thiết kế prompt chuyên sâu dành cho kỹ sư SDET để các mô hình LLM (Gemini 1.5 Pro / ChatGPT-4 / Claude) chuyển hóa trực tiếp danh sách ca kiểm thử BVA thành mã nguồn C# NUnit hoàn chỉnh, tuân thủ Page Object Model (POM), xử lý triệt để các đặc thù của Desktop WinForms (chuyển cửa sổ, dọn dẹp tiến trình, định vị UIA) và chạy pass 100% trên WinAppDriver.

---

## 1. Quy Trình Khép Kín 2 Bước (Seamless 2-Stage Automation Workflow)

Để thực hiện từ đầu đến cuối kịch bản demo cho buổi Seminar hoặc video minh họa:

```
┌────────────────────────────────────────────────────────────────────────┐
│ BƯỚC 1: SINH BỘ TEST CASES BVA (Từ Yêu Cầu Nghiệp Vụ)                  │
│ • Sử dụng: ai/prompts/testcase-bva-prompt.md (Pha 1 hoặc Pha 2)        │
│ • Kết quả AI trả về: Bảng Markdown chứa danh sách Test Cases (A, B, Exp)│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (Copy bảng Markdown)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ BƯỚC 2: CHUYỂN HÓA THÀNH SCRIPT AUTOMATION C# (Script Generation)      │
│ • Sử dụng: ai/prompts/script-gen-prompt.md                             │
│ • Dán bảng Markdown từ Bước 1 vào mục [INPUT TEST CASES TABLE]         │
│ • Kết quả AI trả về: Bộ mã C# NUnit + Page Object Model hoàn chỉnh     │
│ • Chạy thực thi: dotnet test .\demo-scripts\ai-winappdriver\           │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Các Cạm Bẫy Kỹ Thuật Đặc Thù Của Desktop WinForms Cần Ràng Buộc AI

Nếu không đưa các ràng buộc thực tế vào prompt, mã nguồn AI sinh ra sẽ gặp các lỗi "chết người" sau:
1. **Lỗi 404 Không tìm thấy phần tử sau Login (Window Handle Transition):**
   - WinForms `LoginForm` sau khi đăng nhập thành công sẽ đếm lùi 1000ms rồi gọi `Hide()`, đồng thời mở `CalculatorForm` (`winMain`) mới.
   - WinAppDriver Session mặc định **vẫn gắn vào cửa sổ Login cũ đã bị ẩn**.
   - **Ràng buộc:** Bắt buộc AI sinh hàm `SwitchToCalculatorWindow()` chờ 1.5s và duyệt `Driver.WindowHandles` để chuyển context sang `CalculatorForm`.
2. **Lỗi xóa TextBox bị sót ký tự hoặc dính dấu âm `-`:**
   - Trong WinForms, hàm `.Clear()` của Selenium thường không kích hoạt sự kiện TextChanged hoặc bị dính dấu trừ khi nhập số âm `-99`.
   - **Ràng buộc:** Yêu cầu dùng phương pháp gõ phím tiêu chuẩn: `element.Click()` $\rightarrow$ `Ctrl + A` $\rightarrow$ `Backspace` $\rightarrow$ `SendKeys(text)`.
3. **Lỗi không kích hoạt được nút tính toán qua click chuột:**
   - Các nút giao diện bo góc GDI+ FlatStyle có thể bị trượt điểm click chuột của WinAppDriver.
   - **Ràng buộc:** Kết hợp `BtnSum.Click()` và gửi phím `Enter` vào ô B (do form cài `AcceptButton = btnSum`).
4. **Lỗi đọc nhãn kết quả và nhãn lỗi trong Windows Forms:**
   - WinForms Label không hỗ trợ `TextPattern` chuẩn của UIA; chuỗi hiển thị được lưu trong thuộc tính UIA `Name`.
   - Thuộc tính `.Text` trong Selenium có thể rỗng trong khi `.GetAttribute("Name")` mới chứa chuỗi kết quả `"Ket qua: {A} + {B} = {Sum}"`.
   - **Ràng buộc:** Bắt buộc đọc `GetAttribute("Name")` trước, sau đó bóc tách số sau dấu `=`; nếu gặp nhãn lỗi (`lblError` hoặc từ khóa "ngoai mien", "khong hop le") thì trả về `"LOI"`.
5. **Tiến trình mồ côi (Zombie Processes):**
   - Form bị `Hide()` sẽ giữ tiến trình `MiniSum_v3.exe` chạy ngầm mãi mãi nếu không kill.
   - **Ràng buộc:** Trong `[TearDown]`, bắt buộc thêm vòng lặp kill mọi tiến trình `MiniSum*`.

---

## 3. Nội Dung Prompt Chuẩn Dùng Để Sinh Script (Production-Ready Prompt)

> **Hướng dẫn người dùng:** Copy toàn bộ đoạn prompt bên dưới. Tại mục `[INPUT TEST CASES TABLE]`, hãy dán bảng test case mà bạn vừa nhận được từ Prompt BVA ở Bước 1. Sau đó gửi cho AI (Gemini hoặc ChatGPT).

```markdown
[ROLE & PERSONA]
Bạn là một Senior SDET (Software Development Engineer in Test) chuyên sâu về tự động hóa ứng dụng Desktop Windows bằng Microsoft WinAppDriver, C# (.NET 8), NUnit 3 và Appium.WebDriver (v4.x).

[TARGET APPLICATION SPECIFICATION]
Ứng dụng mục tiêu: MiniSum Calculator Desktop App (WinForms .NET 8).
Đường dẫn ứng dụng: `case-study-app/MiniSum_v3.exe` (hoặc `MiniSum.exe`).
URL WinAppDriver: `http://127.0.0.1:4723`.

Cấu trúc định vị giao diện (Inspect qua UI Automation):
1. Cửa sổ Đăng nhập (LoginForm):
   - Window Name / Title: "MiniSum - Dang nhap"
   - Ô tài khoản: AutomationId = "txtUser" (Tài khoản chuẩn: "admin")
   - Ô mật khẩu: AutomationId = "txtPass" (Mật khẩu chuẩn: "1234")
   - Nút Đăng nhập: AutomationId = "btnLogin"
   - Nhãn thông báo: AutomationId = "lblMessage"
2. Cửa sổ Tính tổng (CalculatorForm):
   - Window Title: "MiniSum - Tinh tong"
   - Ô nhập số A: AutomationId = "txtA" (AccessibleName = "So A:")
   - Ô nhập số B: AutomationId = "txtB" (AccessibleName = "So B:")
   - Nút tính tổng: AutomationId = "btnSum" (Name = "TINH TONG")
   - Nhãn kết quả: AutomationId = "lblResult" (Định dạng: "Ket qua: {A} + {B} = {Sum}")
   - Nhãn báo lỗi: AutomationId = "lblError" (Hiển thị khi vi phạm biên hoặc sai định dạng)
   - Nút đăng xuất: AutomationId = "btnLogout"

[INPUT TEST CASES TABLE]
Dưới đây là bảng dữ liệu kiểm thử giá trị biên (BVA) cần tự động hóa:
| TC_ID | A | B | Expected | Description |
|---|---|---|---|---|
| BVA_01_MinLowerA | -99 | 9 | -90 | Biên dưới A hợp lệ |
| BVA_02_MaxUpperA | 99 | 9 | 108 | Biên trên A hợp lệ |
| BVA_03_InvalidBelowMinA | -100 | 9 | LOI | Biên dưới A ngoài miền |
| BVA_04_InvalidAboveMaxA | 100 | 9 | LOI | Biên trên A ngoài miền |
| BVA_05_InvalidTypeA | xyz | 10 | LOI | Sai kiểu dữ liệu A |
| BVA_06_MinLowerB | 10 | -99 | -89 | Biên dưới B hợp lệ |
| BVA_07_MaxUpperB | 10 | 99 | 109 | Biên trên B hợp lệ |
| BVA_08_InvalidBelowMinB | 10 | -100 | LOI | Biên dưới B ngoài miền |
| BVA_09_InvalidAboveMaxB | 10 | 100 | LOI | Biên trên B ngoài miền |
| BVA_10_NominalCenter | 0 | 0 | 0 | Giá trị danh định trung tâm |
| BVA_11_ExtremeDualMin | -99 | -99 | -198 | Cực biên dưới đồng thời A và B |
| BVA_12_ExtremeDualMax | 99 | 99 | 198 | Cực biên trên đồng thời A và B |

[ARCHITECTURAL & IMPLEMENTATION REQUIREMENTS]
Hãy sinh toàn bộ mã nguồn C# NUnit hoàn chỉnh theo mô hình Page Object Model (POM), chia rõ các lớp:

1. `BaseTest.cs`:
   - Khởi tạo `WindowsDriver<WindowsElement>` dùng `AppiumOptions` (không dùng DesiredCapabilities đã cũ).
   - Thiết lập `ImplicitWait = TimeSpan.FromSeconds(3)`.
   - Hàm tiện ích chuyển cửa sổ `SwitchToCalculatorWindow()`:
     * Sau khi Login, dừng 1500ms để hiệu ứng timer 1000ms của LoginForm kết thúc.
     * Duyệt qua `Driver.WindowHandles` và switch driver sang cửa sổ có tiêu đề "Tinh tong" hoặc chứa `txtA`.
   - Hàm `[TearDown]`: CloseApp, Quit driver, và kill triệt để tiến trình `MiniSum_v3` / `MiniSum` chạy ngầm.

2. `LoginPage.cs`:
   - Khai báo các WindowsElement: `TxtUser`, `TxtPass`, `BtnLogin`, `LblMessage`.
   - Phương thức xóa và gõ an toàn: `ClearAndType(element, text)` bằng tổ hợp phím `Ctrl + A` + `Backspace` + `SendKeys`.
   - Phương thức `Login(user, pass)`.

3. `CalculatorPage.cs`:
   - Khai báo các WindowsElement: `TxtA`, `TxtB`, `BtnSum`, `LblResult`, `LblError`.
   - Phương thức `Calculate(a, b)`: Xóa và gõ A, B, sau đó bấm `BtnSum` và gửi phím `Enter` vào ô B để đảm bảo kích hoạt tính toán 100%.
   - Phương thức `GetResultOrStatus()`:
     * Đọc `GetAttribute("Name")` từ `lblResult`, nếu có dấu `=` thì lấy giá trị số phía sau.
     * Nếu không có kết quả hợp lệ, kiểm tra `lblError` (hoặc text lỗi "ngoai mien", "khong hop le") và trả về `"LOI"`.

4. `AiGeneratedBvaTests.cs`:
   - Kế thừa `BaseTest`.
   - Chuyển hóa toàn bộ các dòng trong bảng `[INPUT TEST CASES TABLE]` thành các attribute `[TestCase(a, b, expected, TestName = "...")]` của NUnit.
   - Trong hàm test `TC03_Core_Bva_Tests(string a, string b, string expected)`:
     * Gọi `loginPage.Login("admin", "1234")`.
     * Gọi `SwitchToCalculatorWindow()`.
     * Gọi `calculatorPage.Calculate(a, b)`.
     * So sánh `Assert.AreEqual(expected, calculatorPage.GetResultOrStatus())`.

[OUTPUT REQUIREMENTS]
- Mã nguồn C# sạch, đầy đủ using directive, không cắt ngắn code (không dùng "// TODO: ...").
- Biên dịch 0 warning, 0 error với .NET 8.
```

---

## 4. Hướng Dẫn Nhanh Cho Quang Khi Quay Video Demo

1. **Cảnh 1 (Prompt BVA):**
   - Mở file `ai/prompts/testcase-bva-prompt.md`.
   - Copy nội dung mục **3.2 (Core Regression Standardization)**.
   - Dán vào Gemini (trên Antigravity IDE) hoặc ChatGPT.
   - Quay cảnh AI suy luận theo chuỗi Chain-of-Thought và xuất ra bảng 12 ca kiểm thử Markdown.
2. **Cảnh 2 (Prompt Script Gen):**
   - Mở file `ai/prompts/script-gen-prompt.md`.
   - Copy nội dung mục **3 (Nội Dung Prompt Chuẩn)**.
   - Nhấn mạnh trước ống kính: *"Tôi lấy bảng kết quả BVA vừa sinh ở Cảnh 1 đưa vào mục [INPUT TEST CASES TABLE] của Prompt sinh mã WinAppDriver"*.
   - Gửi cho AI. AI sẽ xuất ra toàn bộ code C# Page Object Model hoàn chỉnh.
3. **Cảnh 3 (Thực thi kiểm thử tự động):**
   - Code này đã được đặt sẵn và xác minh hoàn hảo trong thư mục `demo-scripts/ai-winappdriver/`.
   - Mở terminal chạy lệnh:
     ```powershell
     dotnet test .\demo-scripts\ai-winappdriver\MiniSumAiTests.csproj --logger:"console;verbosity=normal"
     ```
   - Quay cảnh ứng dụng MiniSum tự động bật lên, đăng nhập, nhảy sang form Tính tổng, tự động gõ từng cặp biên và kiểm tra kết quả pass xanh lá 100%.
