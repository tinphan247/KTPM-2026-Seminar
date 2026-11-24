using System;
using System.Threading;
using NUnit.Framework;
using MiniSum.AiTests.PageObjects;

namespace MiniSum.AiTests.Tests
{
    /// <summary>
    /// Test Suite tự động hóa kiểm thử BVA sinh bởi AI (Gemini / Claude / ChatGPT).
    /// Kế thừa BaseTest để quản lý vòng đời Session WinAppDriver và chuyển đổi cửa sổ.
    /// </summary>
    [TestFixture]
    public class AiGeneratedBvaTests : BaseTest
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

        // ======================================================================
        // 1. SMOKE TESTS: KIỂM TRA ĐĂNG NHẬP VÀ ĐIỀU HƯỚNG CỬA SỔ
        // ======================================================================
        [Test]
        [Category("Smoke")]
        [Description("Kiểm tra đăng nhập thành công và chuyển cảnh sang màn hình Tính tổng")]
        public void TC01_Login_Success()
        {
            loginPage.Login("admin", "1234");
            SwitchToCalculatorWindow();

            Assert.DoesNotThrow(() =>
            {
                var sumBtn = calculatorPage.BtnSum;
                Assert.IsNotNull(sumBtn, "Cửa sổ CalculatorForm không xuất hiện sau khi Login!");
            });
        }

        [Test]
        [Category("Negative")]
        [Description("Kiểm tra đăng nhập thất bại khi sai mật khẩu")]
        public void TC02_Login_Failed()
        {
            loginPage.Login("admin", "wrong_password");
            Thread.Sleep(500);

            string msg = loginPage.GetMessageText();
            Assert.AreEqual("Sai tai khoan hoac mat khau", msg);
        }

        // ======================================================================
        // 2. DATA-DRIVEN BVA TESTS: BỘ 12 CA KIỂM THỬ GIÁ TRỊ BIÊN CỐT LÕI
        // Tự động chuyển hóa trực tiếp từ Bảng Markdown ở Bước 1
        // ======================================================================
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
        public void TC03_Core_Bva_Tests(string a, string b, string expected)
        {
            // 1. Đăng nhập để mở form Tính tổng
            loginPage.Login("admin", "1234");
            
            // 2. Chuyển context sang cửa sổ CalculatorForm
            SwitchToCalculatorWindow();

            // 3. Nhập hai số A, B và kích hoạt tính toán
            calculatorPage.Calculate(a, b);
            Thread.Sleep(300);

            // 4. Đọc kết quả thực tế và so sánh với kỳ vọng
            string actual = calculatorPage.GetResultOrStatus();
            Assert.AreEqual(expected, actual, $"Lệch kết quả tại cặp giá trị ({a}, {b})");
        }

        // ======================================================================
        // 3. ROBUSTNESS & EXPLORATORY TESTS: CÁC CA ĐỘ BỀN VÀ BIÊN MỞ RỘNG
        // ======================================================================
        [TestCase("", "10", "LOI", TestName = "ROB_01_EmptyInputA")]
        [TestCase("12.5", "10", "LOI", TestName = "ROB_02_FloatNumberA")]
        [TestCase("!@#", "9", "LOI", TestName = "ROB_03_SpecialCharsA")]
        [TestCase("9999999999", "9", "LOI", TestName = "ROB_04_Int32OverflowA")]
        [TestCase("-99", "99", "0", TestName = "ROB_05_OppositeSymmetricEdges")]
        public void TC04_Robustness_Tests(string a, string b, string expected)
        {
            loginPage.Login("admin", "1234");
            SwitchToCalculatorWindow();

            calculatorPage.Calculate(a, b);
            Thread.Sleep(300);

            string actual = calculatorPage.GetResultOrStatus();
            Assert.AreEqual(expected, actual, $"Lệch kết quả ca độ bền ({a}, {b})");
        }
    }
}
