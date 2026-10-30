// ==============================================================================
// FILE: chatgpt-script-output.cs
// ĐỀ TÀI: Automation Testing cho Desktop Applications (Nhóm 02)
// TÁC GIẢ THỰC NGHIỆM: Trần Vũ Quang (MSSV: 23120346)
// MÔ HÌNH THỰC HIỆN: OpenAI ChatGPT-4 (Prompt: script-gen-prompt.md)
// MỤC TIÊU: Mã nguồn C# NUnit + WinAppDriver tự động sinh theo mẫu thiết kế POM
// ==============================================================================

using System;
using System.IO;
using System.Threading;
using NUnit.Framework;
using OpenQA.Selenium.Appium;
using OpenQA.Selenium.Appium.Windows;

namespace MiniSum.Automation.AiGenerated
{
    // ==========================================================================
    // 1. PAGE OBJECT: LOGIN PAGE
    // ==========================================================================
    /// <summary>
    /// Đóng gói các phần tử và hành vi thao tác trên màn hình Đăng nhập (winLogin).
    /// Sinh tự động bởi ChatGPT-4 theo chuẩn Page Object Model.
    /// </summary>
    public class LoginPage
    {
        private readonly WindowsDriver<WindowsElement> driver;

        public LoginPage(WindowsDriver<WindowsElement> driver)
        {
            this.driver = driver ?? throw new ArgumentNullException(nameof(driver));
        }

        // --- Định danh các phần tử qua AccessibilityId ---
        public WindowsElement TxtUsername => driver.FindElementByAccessibilityId("txtUser");
        public WindowsElement TxtPassword => driver.FindElementByAccessibilityId("txtPass");
        public WindowsElement BtnLogin => driver.FindElementByAccessibilityId("btnLogin");
        public WindowsElement LblMessage => driver.FindElementByAccessibilityId("lblMessage");

        // --- Các hàm thao tác nghiệp vụ ---
        public void EnterUsername(string username)
        {
            TxtUsername.Clear();
            if (!string.IsNullOrEmpty(username))
            {
                TxtUsername.SendKeys(username);
            }
        }

        public void EnterPassword(string password)
        {
            TxtPassword.Clear();
            if (!string.IsNullOrEmpty(password))
            {
                TxtPassword.SendKeys(password);
            }
        }

        public void ClickLogin()
        {
            BtnLogin.Click();
        }

        public void Login(string username, string password)
        {
            EnterUsername(username);
            EnterPassword(password);
            ClickLogin();
        }

        public string GetMessageText()
        {
            return LblMessage.Text;
        }
    }

    // ==========================================================================
    // 2. PAGE OBJECT: CALCULATOR PAGE
    // ==========================================================================
    /// <summary>
    /// Đóng gói các phần tử và hành vi thao tác trên màn hình Tính tổng (winMain).
    /// </summary>
    public class CalculatorPage
    {
        private readonly WindowsDriver<WindowsElement> driver;

        public CalculatorPage(WindowsDriver<WindowsElement> driver)
        {
            this.driver = driver ?? throw new ArgumentNullException(nameof(driver));
        }

        // --- Định danh các phần tử qua AccessibilityId ---
        public WindowsElement TxtA => driver.FindElementByAccessibilityId("txtA");
        public WindowsElement TxtB => driver.FindElementByAccessibilityId("txtB");
        public WindowsElement BtnSum => driver.FindElementByAccessibilityId("btnSum");
        public WindowsElement LblResult => driver.FindElementByAccessibilityId("lblResult");
        public WindowsElement BtnLogout => driver.FindElementByAccessibilityId("btnLogout");

        // --- Các hàm thao tác nghiệp vụ ---
        public void EnterA(string a)
        {
            TxtA.Clear();
            if (!string.IsNullOrEmpty(a))
            {
                TxtA.SendKeys(a);
            }
        }

        public void EnterB(string b)
        {
            TxtB.Clear();
            if (!string.IsNullOrEmpty(b))
            {
                TxtB.SendKeys(b);
            }
        }

        public void ClickSum()
        {
            BtnSum.Click();
        }

        public void Calculate(string a, string b)
        {
            EnterA(a);
            EnterB(b);
            ClickSum();
        }

        public string GetResultText()
        {
            return LblResult.Text;
        }

        public void ClickLogout()
        {
            BtnLogout.Click();
        }
    }

    // ==========================================================================
    // 3. BASE TEST: QUẢN LÝ VÒNG ĐỜI SESSION WINAPPDRIVER
    // ==========================================================================
    /// <summary>
    /// Lớp cơ sở thiết lập WindowsDriver session với WinAppDriver tại cổng 4723.
    /// </summary>
    public abstract class BaseTest
    {
        protected WindowsDriver<WindowsElement> Driver;
        protected const string WinAppDriverUrl = "http://127.0.0.1:4723";
        protected string AppPath;

        [SetUp]
        public virtual void SetUp()
        {
            // Định vị đường dẫn file thực thi MiniSum.exe
            string baseDir = AppDomain.CurrentDomain.BaseDirectory;
            AppPath = Path.GetFullPath(Path.Combine(baseDir, @"..\..\..\..\..\case-study-app\MiniSum.exe"));

            if (!File.Exists(AppPath))
            {
                // Fallback nếu chạy trong cấu trúc thư mục khác
                AppPath = @"D:\university\n4hk1\test\seminar1\KTPM-2026-Seminar\case-study-app\MiniSum.exe";
            }

            var options = new AppiumOptions();
            options.AddAdditionalCapability("app", AppPath);
            options.AddAdditionalCapability("deviceName", "WindowsPC");

            Driver = new WindowsDriver<WindowsElement>(new Uri(WinAppDriverUrl), options);
            Driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(3);
        }

        [TearDown]
        public virtual void TearDown()
        {
            if (Driver != null)
            {
                try
                {
                    Driver.CloseApp();
                }
                catch
                {
                    // Tránh lỗi nếu app đã bị đóng trước đó
                }
                finally
                {
                    Driver.Quit();
                    Driver = null;
                }
            }
        }
    }

    // ==========================================================================
    // 4. TEST FIXTURE: THỰC THI KIỂM THỬ VỚI NUNIT
    // ==========================================================================
    [TestFixture]
    public class MiniSumAiGeneratedTests : BaseTest
    {
        private LoginPage loginPage;
        private CalculatorPage calculatorPage;

        [SetUp]
        public override void SetUp()
        {
            base.SetUp();
            loginPage = new LoginPage(Driver);
            calculatorPage = new CalculatorPage(Driver);
        }

        /// <summary>
        /// Test Case 1: Đăng nhập thành công với tài khoản chuẩn admin / 1234
        /// </summary>
        [Test]
        [Category("SmokeTest")]
        public void TC01_Login_Success_NavigatesToCalculator()
        {
            loginPage.Login("admin", "1234");
            
            // Đợi chuyển form (LoginForm có animation transition 1000ms)
            Thread.Sleep(1500);

            // Kiểm tra phần tử trên màn hình tính tổng xuất hiện
            Assert.IsNotNull(calculatorPage.BtnSum, "Nút Tính tổng trên winMain phải hiển thị sau khi login thành công");
        }

        /// <summary>
        /// Test Case 2: Đăng nhập thất bại với mật khẩu sai
        /// </summary>
        [Test]
        [Category("NegativeTest")]
        public void TC02_Login_Failed_ShowsErrorMessage()
        {
            loginPage.Login("admin", "wrong_password");
            
            Thread.Sleep(500);
            string message = loginPage.GetMessageText();
            Assert.AreEqual("Sai tài khoản hoặc mật khẩu!", message, "Thông báo lỗi sai mật khẩu không khớp đặc tả!");
        }

        /// <summary>
        /// Test Case 3: Kiểm thử điều khiển bằng dữ liệu (DDT) cho 12 ca kiểm thử BVA
        /// </summary>
        [TestCase("-99", "9", "-90", TestName = "TC_BVA_01_MinLowerA")]
        [TestCase("99", "9", "108", TestName = "TC_BVA_02_MaxUpperA")]
        [TestCase("-100", "9", "LOI", TestName = "TC_BVA_03_InvalidBelowMinA")]
        [TestCase("100", "9", "LOI", TestName = "TC_BVA_04_InvalidAboveMaxA")]
        [TestCase("xyz", "10", "LOI", TestName = "TC_BVA_05_InvalidTypeA")]
        [TestCase("10", "-99", "-89", TestName = "TC_BVA_06_MinLowerB")]
        [TestCase("10", "99", "109", TestName = "TC_BVA_07_MaxUpperB")]
        [TestCase("10", "-100", "LOI", TestName = "TC_BVA_08_InvalidBelowMinB")]
        [TestCase("10", "100", "LOI", TestName = "TC_BVA_09_InvalidAboveMaxB")]
        [TestCase("0", "0", "0", TestName = "TC_BVA_10_NominalCenter")]
        [TestCase("-99", "-99", "-198", TestName = "TC_BVA_11_ExtremeDualMin")]
        [TestCase("99", "99", "198", TestName = "TC_BVA_12_ExtremeDualMax")]
        public void TC03_Bva_Calculation_Tests(string a, string b, string expected)
        {
            // Bước 1: Login vào ứng dụng
            loginPage.Login("admin", "1234");
            Thread.Sleep(1500);

            // Bước 2: Nhập số và bấm tính tổng
            calculatorPage.Calculate(a, b);
            Thread.Sleep(300);

            // Bước 3: So khớp kết quả
            string actualResult = calculatorPage.GetResultText();
            Assert.AreEqual(expected, actualResult, $"Lỗi tính toán với A={a}, B={b}!");
        }
    }
}
