// ==============================================================================
// FILE: verified-script-output.cs
// ĐỀ TÀI: Automation Testing cho Desktop Applications (Nhóm 02)
// TÁC GIẢ: Trần Vũ Quang (MSSV: 23120346)
// TRẠNG THÁI: ĐÃ DEBUG & XÁC MINH CHẠY PASS 100% TRÊN MÔI TRƯỜNG THẬT (Task Q10)
// KIẾN TRÚC: Page Object Model (POM) + WinAppDriver + C# NUnit 3
// ==============================================================================

using System;
using System.IO;
using System.Threading;
using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Appium;
using OpenQA.Selenium.Appium.Windows;
using OpenQA.Selenium.Support.UI;

namespace MiniSum.Automation.Verified
{
    // ==========================================================================
    // 1. PAGE OBJECT: LOGIN PAGE (ĐÃ TỐI ƯU HÓA PHÍM & XỬ LÝ TEXTBOX)
    // ==========================================================================
    public class LoginPage
    {
        private readonly WindowsDriver<WindowsElement> driver;

        public LoginPage(WindowsDriver<WindowsElement> driver)
        {
            this.driver = driver ?? throw new ArgumentNullException(nameof(driver));
        }

        public WindowsElement TxtUsername => driver.FindElementByAccessibilityId("txtUser");
        public WindowsElement TxtPassword => driver.FindElementByAccessibilityId("txtPass");
        public WindowsElement BtnLogin => driver.FindElementByAccessibilityId("btnLogin");
        public WindowsElement LblMessage => driver.FindElementByAccessibilityId("lblMessage");

        public void ClearAndType(WindowsElement element, string text)
        {
            element.Click();
            // Sử dụng tổ hợp phím Ctrl+A + Backspace để đảm bảo sạch TextBox trong WinForms
            element.SendKeys(Keys.Control + "a");
            element.SendKeys(Keys.Backspace);
            if (!string.IsNullOrEmpty(text))
            {
                element.SendKeys(text);
            }
        }

        public void Login(string username, string password)
        {
            ClearAndType(TxtUsername, username);
            ClearAndType(TxtPassword, password);
            BtnLogin.Click();
        }

        public string GetMessageText()
        {
            return LblMessage.Text;
        }
    }

    // ==========================================================================
    // 2. PAGE OBJECT: CALCULATOR PAGE (HỖ TRỢ NHÃN LỖI LBLERROR CỦA V3)
    // ==========================================================================
    public class CalculatorPage
    {
        private readonly WindowsDriver<WindowsElement> driver;

        public CalculatorPage(WindowsDriver<WindowsElement> driver)
        {
            this.driver = driver ?? throw new ArgumentNullException(nameof(driver));
        }

        public WindowsElement TxtA => driver.FindElementByAccessibilityId("txtA");
        public WindowsElement TxtB => driver.FindElementByAccessibilityId("txtB");
        public WindowsElement BtnSum => driver.FindElementByAccessibilityId("btnSum");
        public WindowsElement LblResult => driver.FindElementByAccessibilityId("lblResult");
        public WindowsElement BtnLogout => driver.FindElementByAccessibilityId("btnLogout");

        public void ClearAndType(WindowsElement element, string text)
        {
            element.Click();
            element.SendKeys(Keys.Control + "a");
            element.SendKeys(Keys.Backspace);
            if (!string.IsNullOrEmpty(text))
            {
                element.SendKeys(text);
            }
        }

        public void Calculate(string a, string b)
        {
            ClearAndType(TxtA, a);
            ClearAndType(TxtB, b);
            BtnSum.Click();
        }

        /// <summary>
        /// Đọc kết quả tính toán. Nếu kết quả rỗng do vi phạm biên, kiểm tra nhãn lblError
        /// và trả về chuỗi "LOI" để khớp với bộ test case BVA chuẩn.
        /// </summary>
        public string GetResultOrStatus()
        {
            string res = LblResult.Text?.Trim() ?? string.Empty;
            if (!string.IsNullOrEmpty(res))
            {
                return res;
            }

            try
            {
                var lblError = driver.FindElementByAccessibilityId("lblError");
                if (lblError != null && !string.IsNullOrWhiteSpace(lblError.Text))
                {
                    return "LOI";
                }
            }
            catch (WebDriverException)
            {
                // Phiên bản app không có nhãn lblError
            }

            return res;
        }

        public void ClickLogout()
        {
            BtnLogout.Click();
        }
    }

    // ==========================================================================
    // 3. BASE TEST: ATTACH CỬA SỔ & QUẢN LÝ TIẾN TRÌNH WINAPPHANDLER
    // ==========================================================================
    public abstract class BaseTest
    {
        protected WindowsDriver<WindowsElement> Driver;
        protected const string WinAppDriverUrl = "http://127.0.0.1:4723";
        protected string AppPath;

        [SetUp]
        public virtual void SetUp()
        {
            string baseDir = AppDomain.CurrentDomain.BaseDirectory;
            AppPath = Path.GetFullPath(Path.Combine(baseDir, @"..\..\..\..\..\case-study-app\MiniSum.exe"));

            if (!File.Exists(AppPath))
            {
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
    // 4. TEST SUITE CHUẨN XÁC ĐÃ VERIFY
    // ==========================================================================
    [TestFixture]
    public class MiniSumVerifiedTests : BaseTest
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

        [Test]
        public void TC01_Login_Success()
        {
            loginPage.Login("admin", "1234");
            Thread.Sleep(1200); // Đợi timer chuyển cảnh 1000ms hoàn tất

            Assert.DoesNotThrow(() =>
            {
                var sumBtn = calculatorPage.BtnSum;
                Assert.IsNotNull(sumBtn);
            }, "Màn hình CalculatorForm không hiển thị sau khi đăng nhập!");
        }

        [Test]
        public void TC02_Login_Failed()
        {
            loginPage.Login("admin", "wrong_pass");
            Thread.Sleep(500);

            string msg = loginPage.GetMessageText();
            Assert.AreEqual("Sai tài khoản hoặc mật khẩu!", msg);
        }

        [TestCase("-99", "9", "-90", TestName = "BVA_01_MinLowerA")]
        [TestCase("99", "9", "108", TestName = "BVA_02_MaxUpperA")]
        [TestCase("-100", "9", "LOI", TestName = "BVA_03_InvalidBelowMinA")]
        [TestCase("100", "9", "LOI", TestName = "BVA_04_InvalidAboveMaxA")]
        [TestCase("xyz", "10", "LOI", TestName = "BVA_05_InvalidTypeA")]
        [TestCase("10", "-99", "-89", TestName = "BVA_06_MinLowerB")]
        [TestCase("10", "99", "109", TestName = "BVA_07_MaxUpperB")]
        [TestCase("10", "-100", "LOI", TestName = "BVA_08_InvalidBelowMinB")]
        [TestCase("10", "100", "LOI", TestName = "BVA_09_InvalidAboveMaxB")]
        [TestCase("0", "0", "0", TestName = "BVA_10_NominalCenter")]
        [TestCase("-99", "-99", "-198", TestName = "BVA_11_ExtremeDualMin")]
        [TestCase("99", "99", "198", TestName = "BVA_12_ExtremeDualMax")]
        public void TC03_Bva_DataDriven(string a, string b, string expected)
        {
            loginPage.Login("admin", "1234");
            Thread.Sleep(1200);

            calculatorPage.Calculate(a, b);
            Thread.Sleep(300);

            string actual = calculatorPage.GetResultOrStatus();
            Assert.AreEqual(expected, actual, $"Sai lệch kết quả BVA tại cặp ({a}, {b})");
        }
    }
}
