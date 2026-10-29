using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Appium.Windows;

namespace MiniSumTests.PageObjects
{
    public class CalculatorPage
    {
        private readonly WindowsDriver<WindowsElement> _driver;

        public CalculatorPage(WindowsDriver<WindowsElement> driver)
        {
            _driver = driver;
        }

        // 1. Ô nhập Số A: Thử tìm theo Name "So A:", nếu không có thì tìm thẻ Edit trong Pane "Số A"
        public WindowsElement TxtA
        {
            get
            {
                try
                {
                    return _driver.FindElementByName("So A:");
                }
                catch (WebDriverException)
                {
                    // Fallback: Tìm thẻ Edit bên trong Pane hoặc Edit đầu tiên trên form
                    return _driver.FindElementByXPath("//Pane[@Name='Số A']//Edit | //Edit[1]");
                }
            }
        }

        // 2. Ô nhập Số B: Tên chính xác theo inspect là "So B:"
        public WindowsElement TxtB => _driver.FindElementByName("So B:");

        // 3. Nút Tính tổng: Tên chính xác theo inspect là "TINH TONG"
        public WindowsElement BtnSum => _driver.FindElementByName("TINH TONG");

        // 4. Nhãn Kết quả: Bắt phần tử Text có chứa chuỗi "Ket qua:"
        public WindowsElement LblResult => _driver.FindElementByXPath("//Text[contains(@Name, 'Ket qua:')]");

        /// <summary>
        /// Thực hiện nhập hai số A, B và bấm nút TÍNH TỔNG
        /// </summary>
        public void CalculateSum(string a, string b)
        {
            TxtA.Clear();
            TxtA.SendKeys(a);

            TxtB.Clear();
            TxtB.SendKeys(b);

            BtnSum.Click();
        }

        /// <summary>
        /// Lấy toàn bộ chuỗi kết quả (Ví dụ: "Ket qua: 10 + 5 = 15")
        /// </summary>
        public string GetFullResultText()
        {
            return LblResult.Text;
        }

        /// <summary>
        /// Bóc tách lấy riêng giá trị số cuối cùng sau dấu '=' (Ví dụ: "15") để so sánh với file Excel BVA
        /// </summary>
        public string GetCalculatedValueOnly()
        {
            string fullText = GetFullResultText(); // "Ket qua: 10 + 5 = 15"
            if (fullText.Contains("="))
            {
                string[] parts = fullText.Split('=');
                return parts[1].Trim(); // Trả về "15"
            }
            return fullText.Trim();
        }
    }
}