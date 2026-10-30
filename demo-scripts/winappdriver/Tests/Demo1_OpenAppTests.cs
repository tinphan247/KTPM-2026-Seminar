using NUnit.Framework;
using MiniSumTests.Tests;

namespace MiniSumTests.Tests
{
    [TestFixture]
    public class Demo1_OpenAppTests : BaseTest
    {
        [Test]
        [Description("Demo 1: Kiểm tra khởi chạy và kết nối ứng dụng MiniSum qua WinAppDriver")]
        public void TC00_OpenApp_VerifyTitle()
        {
            // 1. Kiểm tra session WinAppDriver đã khởi tạo thành công
            Assert.That(driver, Is.Not.Null, "Không thể kết nối hoặc khởi tạo session tới WinAppDriver.");

            // 2. Kiểm tra cửa sổ chính của ứng dụng được hiển thị
            // Dùng FindElementByXPath để lấy Window/Pane chính thay vì gọi driver.Title
            var loginBtn = driver.FindElementByName("DANG NHAP");
            Assert.That(loginBtn.Displayed, Is.True, "Cửa sổ đăng nhập không hiển thị nút DANG NHAP.");
            System.Threading.Thread.Sleep(50000);
        }
    }
}