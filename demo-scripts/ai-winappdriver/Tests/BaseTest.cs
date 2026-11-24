using System;
using System.IO;
using NUnit.Framework;
using OpenQA.Selenium.Appium;
using OpenQA.Selenium.Appium.Windows;

namespace MiniSum.AiTests.Tests
{
    /// <summary>
    /// Base Test class quản lý kết nối và vòng đời session với WinAppDriver.
    /// </summary>
    public abstract class BaseTest
    {
        protected WindowsDriver<WindowsElement> Driver;
        protected const string WinAppDriverUrl = "http://127.0.0.1:4723";
        protected string AppPath;

        [SetUp]
        public virtual void SetUp()
        {
            string baseDir = AppDomain.CurrentDomain.BaseDirectory;
            // Tìm đường dẫn tới bản build MiniSum_v3.exe hoặc MiniSum.exe
            AppPath = Path.GetFullPath(Path.Combine(baseDir, @"..\..\..\..\..\case-study-app\MiniSum_v3.exe"));

            if (!File.Exists(AppPath))
            {
                AppPath = Path.GetFullPath(Path.Combine(baseDir, @"..\..\..\..\..\case-study-app\MiniSum.exe"));
            }

            if (!File.Exists(AppPath))
            {
                AppPath = @"D:\university\n4hk1\test\seminar1\KTPM-2026-Seminar\case-study-app\MiniSum_v3.exe";
            }

            var options = new AppiumOptions();
            options.AddAdditionalCapability("app", AppPath);
            options.AddAdditionalCapability("deviceName", "WindowsPC");

            Driver = new WindowsDriver<WindowsElement>(new Uri(WinAppDriverUrl), options);
            Driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(3);
        }

        public void SwitchToCalculatorWindow()
        {
            // Chờ 1.5s để timer chuyển cảnh LoginForm hoàn tất
            System.Threading.Thread.Sleep(1500);

            var handles = Driver.WindowHandles;
            if (handles != null && handles.Count > 0)
            {
                for (int i = handles.Count - 1; i >= 0; i--)
                {
                    try
                    {
                        Driver.SwitchTo().Window(handles[i]);
                        // Xác nhận window này có thể thao tác được
                        if (Driver.Title.Contains("Tinh tong") || Driver.Title.Contains("MiniSum"))
                        {
                            return;
                        }
                    }
                    catch
                    {
                    }
                }
                // Fallback nếu Title không match
                try { Driver.SwitchTo().Window(handles[0]); } catch { }
            }
        }

        [TearDown]
        public virtual void TearDown()
        {
            if (Driver != null)
            {
                try
                {
                    Driver.CloseApp();
                }
                catch
                {
                }
                finally
                {
                    try
                    {
                        Driver.Quit();
                        Driver.Dispose();
                    }
                    catch
                    {
                    }
                    Driver = null;
                }
            }

            // Dọn dẹp triệt để mọi tiến trình MiniSum mồ côi
            try
            {
                foreach (var p in System.Diagnostics.Process.GetProcessesByName("MiniSum_v3"))
                {
                    try { p.Kill(); } catch { }
                }
                foreach (var p in System.Diagnostics.Process.GetProcessesByName("MiniSum"))
                {
                    try { p.Kill(); } catch { }
                }
            }
            catch
            {
            }
        }
    }
}
