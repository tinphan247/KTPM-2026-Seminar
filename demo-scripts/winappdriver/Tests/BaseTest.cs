using System;
using System.IO;
using NUnit.Framework;
using NUnit.Framework.Interfaces;
using OpenQA.Selenium;
using OpenQA.Selenium.Appium;
using OpenQA.Selenium.Appium.Windows;

namespace MiniSumTests.Tests
{
    public class BaseTest
    {
        protected WindowsDriver<WindowsElement> driver;
        protected const string WinAppDriverUrl = "http://127.0.0.1:4723";

        protected virtual string GetAppPath()
        {
            string baseDir = AppDomain.CurrentDomain.BaseDirectory;
            string solutionDir = Path.GetFullPath(Path.Combine(baseDir, @"..\..\..\..\..\"));
            string appPath = Path.Combine(solutionDir, "case-study-app", "MiniSum", "MiniSum_v3.exe");

            if (!File.Exists(appPath))
            {
                appPath = Path.Combine(solutionDir, "case-study-app", "MiniSum_v3.exe");
            }
            return appPath;
        }

        [SetUp]
        public virtual void SetUp()
        {
            var options = new AppiumOptions();
            string appPath = GetAppPath();

            options.AddAdditionalCapability("app", appPath);
            options.AddAdditionalCapability("deviceName", "WindowsPC");
            options.AddAdditionalCapability("platformName", "Windows");

            driver = new WindowsDriver<WindowsElement>(new Uri(WinAppDriverUrl), options);
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(3);
        }

        [TearDown]
        public virtual void TearDown()
        {
            if (TestContext.CurrentContext.Result.Outcome.Status == TestStatus.Failed)
            {
                try
                {
                    string testName = TestContext.CurrentContext.Test.Name;
                    foreach (char c in Path.GetInvalidFileNameChars())
                    {
                        testName = testName.Replace(c, '_');
                    }

                    string timestamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
                    string screenshotDir = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Screenshots");
                    Directory.CreateDirectory(screenshotDir);

                    string filePath = Path.Combine(screenshotDir, $"{testName}_FAIL_{timestamp}.png");
                    Screenshot screenshot = driver.GetScreenshot();
                    screenshot.SaveAsFile(filePath, ScreenshotImageFormat.Png);

                    TestContext.AddTestAttachment(filePath, "Minh chứng lỗi lúc kiểm thử thất bại");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Không thể chụp ảnh lỗi: {ex.Message}");
                }
            }

            if (driver != null)
            {
                try
                {
                    driver.CloseApp();
                }
                catch
                {
                }

                driver.Quit();
                driver.Dispose();
                driver = null;
            }
        }
    }
}