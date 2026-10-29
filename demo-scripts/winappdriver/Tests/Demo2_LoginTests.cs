using NUnit.Framework;
using MiniSumTests.PageObjects;

namespace MiniSumTests.Tests
{
    [TestFixture]
    public class Demo2_LoginTests : BaseTest
    {
        [Test]
        [Description("W10 - Demo 2a: Đăng nhập hợp lệ với admin/1234 và kiểm tra checkpoint")]
        public void TC01_Login_Success()
        {
            var loginPage = new LoginPage(driver);
            loginPage.Login("admin", "1234");

            // Checkpoint kiểm tra thông báo đăng nhập thành công
            Assert.That(loginPage.GetMessage(), Is.EqualTo("Dang nhap thanh cong!"));
        }

        [Test]
        [Description("W11 - Demo 2b: Đăng nhập thất bại khi sai mật khẩu")]
        public void TC02_Login_Failed()
        {
            var loginPage = new LoginPage(driver);
            loginPage.Login("admin", "wrong_password");

            // Checkpoint kiểm tra thông báo lỗi
            Assert.That(loginPage.GetMessage(), Does.Contain("Sai tai khoan hoac mat khau").Or.Contain("Sai").Or.Not.Empty);
        }

        [Test]
        [Description("W12 - Demo 2c: Test case cố tình Fail để kích hoạt cơ chế chụp ảnh màn hình")]
        public void TC02c_Intentional_Fail_TestScreenshot()
        {
            var loginPage = new LoginPage(driver);
            loginPage.Login("admin", "1234");

            // Cố tình Assert sai để kích hoạt TearDown chụp ảnh màn hình
            // Bỏ comment dòng dưới khi muốn quay clip demo chụp màn hình tự động
            // Assert.That(loginPage.GetMessage(), Is.EqualTo("Chuỗi không bao giờ xuất hiện!"));
            
            Assert.Pass("Bỏ qua test này khi chạy chính thức; mở ra khi cần test chụp màn hình.");
        }
    }
}