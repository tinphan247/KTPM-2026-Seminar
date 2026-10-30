using System;
using System.Threading;
using NUnit.Framework;
using MiniSum.AiTests.PageObjects;

namespace MiniSum.AiTests.Tests
{
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
        // PHẦN 1: SMOKE & FUNCTIONAL LOGIN TESTS
        // ======================================================================
        [Test]
        [Category("Smoke")]
        public void TC01_Login_Success()
        {
            loginPage.Login("admin", "1234");
            Thread.Sleep(1200);

            Assert.DoesNotThrow(() =>
            {
                var sumBtn = calculatorPage.BtnSum;
                Assert.IsNotNull(sumBtn, "Cửa sổ Tính tổng không hiển thị sau khi đăng nhập thành công!");
            });
        }

        [Test]
        [Category("Negative")]
        public void TC02_Login_Failed()
        {
            loginPage.Login("admin", "wrong_password");
            Thread.Sleep(500);

            string msg = loginPage.GetMessageText();
            Assert.AreEqual("Sai tai khoan hoac mat khau", msg);
        }

        // ======================================================================
        // PHẦN 2: BỘ 12 CA KIỂM THỬ GIÁ TRỊ BIÊN CỐT LÕI (CORE 12 BVA CASES)
        // Đồng bộ dữ liệu với file Excel bva-testcases.xlsx dùng cho cả nhóm
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
            loginPage.Login("admin", "1234");
            Thread.Sleep(1200);

            calculatorPage.Calculate(a, b);
            Thread.Sleep(300);

            string actual = calculatorPage.GetResultOrStatus();
            Assert.AreEqual(expected, actual, $"Lệch kết quả tại ca ({a}, {b})");
        }

        // ======================================================================
        // PHẦN 3: CÁC CA KIỂM THỬ MỞ RỘNG DO AI PHÁT HIỆN (AI EXPLORATORY TESTS)
        // Minh họa khả năng phát hiện biên đặc biệt khi không bị giới hạn cứng
        // ======================================================================
        [TestCase("", "10", "LOI", TestName = "AI_EXP_01_EmptyInputA")]
        [TestCase("12.5", "10", "LOI", TestName = "AI_EXP_02_FloatNumberA")]
        [TestCase("!@#", "9", "LOI", TestName = "AI_EXP_03_SpecialCharsA")]
        [TestCase("9999999999", "9", "LOI", TestName = "AI_EXP_04_Int32OverflowA")]
        [TestCase("98", "9", "107", TestName = "AI_EXP_05_ValidJustBelowMaxA")]
        public void TC04_Ai_Exploratory_Robustness_Tests(string a, string b, string expected)
        {
            loginPage.Login("admin", "1234");
            Thread.Sleep(1200);

            calculatorPage.Calculate(a, b);
            Thread.Sleep(300);

            string actual = calculatorPage.GetResultOrStatus();
            Assert.AreEqual(expected, actual, $"Lệch kết quả ca mở rộng ({a}, {b})");
        }
    }
}
