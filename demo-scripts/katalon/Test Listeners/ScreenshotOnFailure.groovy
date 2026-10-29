/**
 * ScreenshotOnFailure.groovy — Test Listener
 * Tác giả: Kan
 *
 * Mục đích: Tự động chụp ảnh màn hình Desktop khi bất kỳ test step nào FAIL.
 *          Đây là cơ chế xây dựng Bug Report bằng chứng (evidence) cho seminar.
 *
 * Nguyên lý:
 *   - TestListener interface của Katalon có 4 hook:
 *       beforeTestSuite, afterTestSuite, beforeTestCase, afterTestCase
 *   - Trong afterTestCase, ta kiểm tra TestCaseContext.getTestStatus()
 *       nếu == FAILED → dùng WindowsBuiltinKeywords.takeScreenshot
 *
 * Cách cấu hình:
 *   - File này đặt tại: Test Listeners/ScreenshotOnFailure.groovy
 *   - Katalon tự động nhận diện và chạy cho mọi Test Suite
 */

import com.kms.katalon.core.annotation.AfterTestCase
import com.kms.katalon.core.annotation.BeforeTestCase
import com.kms.katalon.core.configuration.RunConfiguration
import com.kms.katalon.core.context.TestCaseContext
import com.kms.katalon.core.util.KeywordUtil
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows

class ScreenshotOnFailure {

    @BeforeTestCase
    def beforeTestCase(TestCaseContext testCaseContext) {
        KeywordUtil.logInfo("▶ Bắt đầu Test Case: ${testCaseContext.getTestCaseId()}")
        
        // Cấu hình URL WinAppDriver vào RunConfiguration (khắc phục lỗi MalformedURLException: spec is null trên Katalon v11+)
        try {
            Map winPref = ['desktopDriverUrl': 'http://127.0.0.1:4723', 'winAppDriverUrl': 'http://127.0.0.1:4723']
            Map execution = RunConfiguration.getExecutionProperties() ?: [:]
            Map drivers = execution.get('drivers') instanceof Map ? execution.get('drivers') : [:]
            Map preferences = drivers.get('preferences') instanceof Map ? drivers.get('preferences') : [:]
            preferences.put('Windows', winPref)
            drivers.put('preferences', preferences)
            execution.put('drivers', drivers)
            RunConfiguration.setExecutionSetting(['execution': execution])
        } catch (Throwable ignored) {
        }

        try {
            new java.net.Socket("127.0.0.1", 4723).close()
        } catch (Exception e) {
            KeywordUtil.logInfo("⚡ FlaUI.WebDriver chưa bật trên cổng 4723, đang tự động khởi động...")
            try {
                String flauiPath = "C:\\Users\\Admin\\.katalon\\packages\\KS-11.7.0\\configuration\\resources\\extensions\\FlaUIWebDriver\\FlaUI.WebDriver.exe"
                new ProcessBuilder(flauiPath, "--urls=http://127.0.0.1:4723").start()
                Thread.sleep(2000)
                KeywordUtil.logInfo("✔ FlaUI.WebDriver đã được khởi động trên cổng 4723.")
            } catch (Exception ex) {
                KeywordUtil.logWarning("Không thể khởi động FlaUI.WebDriver tự động: " + ex.getMessage())
            }
        }
    }

    @AfterTestCase
    def afterTestCase(TestCaseContext testCaseContext) {
        // Tương thích cả Katalon mới (getTestCaseStatus) và bản cũ (getTestStatus)
        String testStatus = ''
        try {
            testStatus = testCaseContext.getTestCaseStatus()
        } catch (Throwable t) {
            try {
                testStatus = testCaseContext.getTestStatus()
            } catch (Throwable t2) {
                testStatus = testCaseContext.toString()
            }
        }

        if ('FAILED'.equalsIgnoreCase(testStatus) || 'ERROR'.equalsIgnoreCase(testStatus)) {
            try {
                if (com.kms.katalon.core.windows.driver.WindowsDriverFactory.getWindowsSession() != null &&
                    com.kms.katalon.core.windows.driver.WindowsDriverFactory.getWindowsDriver() != null) {
                    String timestamp = new Date().format('yyyyMMdd_HHmmss')
                    String cleanCaseId = testCaseContext.getTestCaseId().replaceAll('[^a-zA-Z0-9]', '_')
                    String screenshotName = "FAIL_${cleanCaseId}_${timestamp}.png"

                    // Xác định thư mục lưu ảnh:
                    // 1. Nếu chạy qua Test Suite: lưu trực tiếp vào thư mục Report của Test Suite đó
                    // 2. Nếu chạy Test Case đơn lẻ: lưu vào Reports/Screenshots để gom gọn, tránh làm bẩn thư mục gốc
                    String reportFolder = RunConfiguration.getReportFolder()
                    File targetDir
                    if (reportFolder != null && !reportFolder.trim().isEmpty() && new File(reportFolder).exists()) {
                        targetDir = new File(reportFolder)
                    } else {
                        targetDir = new File(RunConfiguration.getProjectDir() + File.separator + 'Reports' + File.separator + 'Screenshots')
                        if (!targetDir.exists()) {
                            targetDir.mkdirs()
                        }
                    }

                    String fullScreenshotPath = new File(targetDir, screenshotName).getAbsolutePath()
                    Windows.takeScreenshot(fullScreenshotPath)
                    KeywordUtil.logInfo("📸 Đã lưu ảnh chụp lỗi tại: ${fullScreenshotPath}")
                }
            } catch (Throwable e) {
                KeywordUtil.logWarning("Không thể chụp ảnh: ${e.message}")
            }
        }
        KeywordUtil.logInfo("■ Kết thúc Test Case: ${testCaseContext.getTestCaseId()} — Status: ${testStatus}")
    }
}
