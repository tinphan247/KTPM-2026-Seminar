# Prompt: Sinh Test Script WinAppDriver C# NUnit Áp Dụng POM

## System Prompt
Bạn là chuyên gia SDET thành thạo C#, NUnit 3, Appium/WinAppDriver và mẫu thiết kế Page Object Model (POM).

## User Prompt
Viết một bộ test script C# NUnit hoàn chỉnh để kiểm thử tự động ứng dụng desktop MiniSum.exe thông qua WinAppDriver:
1. Sử dụng Page Object Model:
   - LoginPage: đóng gói các trường 	xtUser, 	xtPass, tnLogin, lblMessage.
   - CalculatorPage: đóng gói 	xtA, 	xtB, tnSum, lblResult, lblError.
2. Hỗ trợ Data-Driven Testing (DDT) đọc dữ liệu từ file Excel hoặc TestCaseSource.
3. Tích hợp [TearDown] chụp màn hình tự động khi test fail (TestContext.CurrentContext.Result.Outcome.Status == TestStatus.Failed).
4. Khởi tạo session với AppiumOptions trỏ tới WindowsDriver<WindowsElement>.
