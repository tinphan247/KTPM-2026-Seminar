using System;
using System.Threading;
using OpenQA.Selenium;
using OpenQA.Selenium.Appium.Windows;

namespace MiniSum.AiTests.PageObjects
{
    public class CalculatorPage
    {
        private readonly WindowsDriver<WindowsElement> driver;

        public CalculatorPage(WindowsDriver<WindowsElement> driver)
        {
            this.driver = driver ?? throw new ArgumentNullException(nameof(driver));
        }

        public WindowsElement TxtA
        {
            get
            {
                try { return driver.FindElementByAccessibilityId("txtA"); }
                catch { return driver.FindElementByName("So A:"); }
            }
        }

        public WindowsElement TxtB
        {
            get
            {
                try { return driver.FindElementByAccessibilityId("txtB"); }
                catch { return driver.FindElementByName("So B:"); }
            }
        }

        public WindowsElement BtnSum
        {
            get
            {
                try { return driver.FindElementByName("TINH TONG"); }
                catch { return driver.FindElementByAccessibilityId("btnSum"); }
            }
        }

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
            try
            {
                BtnSum.Click();
            }
            catch
            {
            }
            TxtB.SendKeys(Keys.Enter);
        }

        public string GetResultOrStatus()
        {
            Thread.Sleep(300);

            // 1. Ưu tiên kiểm tra nhanh bằng AccessibilityId "lblResult" (tốc độ cao)
            try
            {
                var lblRes = driver.FindElementByAccessibilityId("lblResult");
                if (lblRes != null)
                {
                    string text = lblRes.GetAttribute("Name");
                    if (string.IsNullOrEmpty(text))
                    {
                        text = lblRes.Text ?? string.Empty;
                    }

                    if (!string.IsNullOrWhiteSpace(text) && text.Contains("="))
                    {
                        return text.Split('=')[1].Trim();
                    }
                }
            }
            catch (WebDriverException)
            {
            }

            // 2. Ưu tiên kiểm tra nhanh nhãn lỗi bằng AccessibilityId "lblError" (v3)
            try
            {
                var lblErr = driver.FindElementByAccessibilityId("lblError");
                if (lblErr != null)
                {
                    string errText = lblErr.GetAttribute("Name");
                    if (string.IsNullOrEmpty(errText))
                    {
                        errText = lblErr.Text ?? string.Empty;
                    }

                    if (!string.IsNullOrWhiteSpace(errText))
                    {
                        return "LOI";
                    }
                }
            }
            catch (WebDriverException)
            {
            }

            // 3. Fallback: Bắt nhãn kết quả bằng XPath nếu cần
            try
            {
                var elem = driver.FindElementByXPath("//Text[contains(@Name, 'Ket qua:')]");
                if (elem != null)
                {
                    string text = elem.GetAttribute("Name") ?? elem.Text ?? string.Empty;
                    if (text.Contains("="))
                    {
                        return text.Split('=')[1].Trim();
                    }
                    return text.Trim();
                }
            }
            catch (WebDriverException)
            {
            }

            // 4. Fallback: Bắt thông báo lỗi qua XPath
            try
            {
                var errElem = driver.FindElementByXPath("//Text[contains(@Name, 'ngoai mien') or contains(@Name, 'khong hop le') or contains(@Name, 'Vui long')]");
                if (errElem != null)
                {
                    return "LOI";
                }
            }
            catch (WebDriverException)
            {
            }

            return string.Empty;
        }

        public void ClickLogout()
        {
            try
            {
                driver.FindElementByName("DANG XUAT").Click();
            }
            catch
            {
                driver.FindElementByAccessibilityId("btnLogout").Click();
            }
        }
    }
}
