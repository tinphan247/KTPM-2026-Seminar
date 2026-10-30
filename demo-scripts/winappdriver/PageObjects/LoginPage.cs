using OpenQA.Selenium.Appium.Windows;
using OpenQA.Selenium;

namespace MiniSumTests.PageObjects
{
    public class LoginPage
    {
        private readonly WindowsDriver<WindowsElement> _driver;

        public LoginPage(WindowsDriver<WindowsElement> driver)
        {
            _driver = driver;
        }

        public WindowsElement TxtUser => _driver.FindElementByName("Tai khoan:");
        public WindowsElement TxtPass => _driver.FindElementByName("Mat khau:");
        
        public WindowsElement BtnLogin => _driver.FindElementByName("DANG NHAP");

        // Nhãn thông báo kết quả/lỗi: 
        // Có thể tìm theo Name hoặc bắt theo loại TextBlock/Label trong cửa sổ
      public WindowsElement LblMessage => _driver.FindElementByXPath(
    "//Text[contains(@Name, 'Sai') or contains(@Name, 'tai khoan') or contains(@Name, 'thanh cong') or contains(@Name, 'thành công')]"
);

        public void EnterUsername(string username)
        {
            TxtUser.Clear();
            TxtUser.SendKeys(username);
        }

        public void EnterPassword(string password)
        {
            TxtPass.Clear();
            TxtPass.SendKeys(password);
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

        public string GetMessage()
        {
            try
            {
                return LblMessage.Text;
            }
            catch
            {
                // Fallback nếu thông báo dạng MessageBox popup
                var alert = _driver.SwitchTo().Alert();
                string text = alert.Text;
                alert.Accept();
                return text;
            }
        }
    }
}