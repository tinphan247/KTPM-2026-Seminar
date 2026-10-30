using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Appium.Windows;

namespace MiniSum.AiTests.PageObjects
{
    /// <summary>
    /// Page Object cho màn hình Tính tổng (winMain) - Đã xử lý nhãn kết quả và nhãn lỗi lblError.
    /// </summary>
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
        /// Lấy giá trị kết quả tính toán hoặc thông báo lỗi đã được chuẩn hóa.
        /// </summary>
        public string GetResultOrStatus()
        {
            // 1. Kiểm tra nhãn kết quả hợp lệ
            string resultText = LblResult.Text?.Trim() ?? string.Empty;
            if (!string.IsNullOrEmpty(resultText))
            {
                if (resultText.Contains("="))
                {
                    string[] parts = resultText.Split('=');
                    return parts[1].Trim();
                }
                return resultText;
            }

            // 2. Nếu nhãn kết quả rỗng (ở bản v3), kiểm tra banner lỗi màu đỏ lblError
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
                // Không có control lblError (app bản v1/v2)
            }

            return resultText;
        }

        public void ClickLogout()
        {
            BtnLogout.Click();
        }
    }
}
