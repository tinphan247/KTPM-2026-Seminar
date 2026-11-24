using System;
using System.Collections.Generic;
using System.IO;
using NUnit.Framework;
using MiniSumTests.Helpers;
using MiniSumTests.PageObjects;

namespace MiniSumTests.Tests
{
    [TestFixture]
    public class Demo3_BvaTests : BaseTest
    {
        private static string GetExcelDataPath()
        {
            string baseDir = AppDomain.CurrentDomain.BaseDirectory;
            string directPath = Path.Combine(baseDir, "Data", "bva-testcases.xlsx");
            
            if (File.Exists(directPath)) return directPath;

            // Thử tên file BVA_TestData.xlsx
            string altPath = Path.Combine(baseDir, "Data", "BVA_TestData.xlsx");
            if (File.Exists(altPath)) return altPath;

            return directPath;
        }

        public static IEnumerable<TestCaseData> GetBvaTestCases()
        {
            return ExcelHelper.ReadBvaData(GetExcelDataPath());
        }

        [Test, TestCaseSource(nameof(GetBvaTestCases))]
        [Description("W14/W17 - Demo 3: Data-Driven Testing đọc 12 ca kiểm thử biên (BVA) từ Excel và dùng POM")]
        public void TC03_BVA_Calculation_DataDriven(string a, string b, string expectedResult)
        {
            // 1. Đăng nhập để vào màn hình Calculator
            var loginPage = new LoginPage(driver);
            loginPage.Login("admin", "1234");

            // Chờ chuyển cảnh LoginForm -> CalculatorForm và switch window
            System.Threading.Thread.Sleep(1500);
            var handles = driver.WindowHandles;
            if (handles != null && handles.Count > 0)
            {
                driver.SwitchTo().Window(handles[0]);
            }

            // 2. Nhập A, B và tính tổng qua Page Object CalculatorPage
            var calcPage = new CalculatorPage(driver);
            calcPage.CalculateSum(a, b);

            // 3. Checkpoint kiểm tra kết quả tính tổng với Expected từ Excel
            Assert.That(calcPage.GetResult(), Is.EqualTo(expectedResult));
        }
    }
}