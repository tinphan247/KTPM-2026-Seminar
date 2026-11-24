using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Appium.Windows;

namespace MiniSum.AiTests.PageObjects
{
    /// <summary>
    /// Page Object cho màn hình Đăng nhập (winLogin) - Sinh bởi Gemini / AI.
    /// </summary>
    public class LoginPage
    {
        private readonly WindowsDriver<WindowsElement> driver;

        public LoginPage(WindowsDriver<WindowsElement> driver)
        {
            this.driver = driver ?? throw new ArgumentNullException(nameof(driver));
        }

        public WindowsElement TxtUser => driver.FindElementByAccessibilityId("txtUser");
        public WindowsElement TxtPass => driver.FindElementByAccessibilityId("txtPass");
        public WindowsElement BtnLogin => driver.FindElementByAccessibilityId("btnLogin");
        public WindowsElement LblMessage => driver.FindElementByAccessibilityId("lblMessage");

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

        public void Login(string username, string password)
        {
            ClearAndType(TxtUser, username);
            ClearAndType(TxtPass, password);
            BtnLogin.Click();
        }

        public string GetMessageText()
        {
            return LblMessage.Text;
        }
    }
}
