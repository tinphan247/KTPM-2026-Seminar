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
import com.kms.katalon.core.context.TestCaseContext
import com.kms.katalon.core.util.KeywordUtil
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows

class ScreenshotOnFailure {

    @BeforeTestCase
    def beforeTestCase(TestCaseContext testCaseContext) {
        KeywordUtil.logInfo("▶ Bắt đầu Test Case: ${testCaseContext.getTestCaseId()}")
        try {
            new java.net.Socket("127.0.0.1", 4723).close()
        } catch (Exception e) {
            KeywordUtil.logInfo("⚡ WinAppDriver chưa bật trên cổng 4723, đang tự động khởi động...")
            try {
                new ProcessBuilder("powershell.exe", "-WindowStyle", "Hidden", "-Command", "Start-Process 'C:\\Program Files\\Windows Application Driver\\WinAppDriver.exe' -ArgumentList '4723' -Verb RunAs").start()
                Thread.sleep(3000)
                KeywordUtil.logInfo("✔ WinAppDriver đã được khởi động tự động với quyền Administrator.")
            } catch (Exception ex) {
                KeywordUtil.logWarning("Không thể khởi động WinAppDriver tự động: " + ex.getMessage())
            }
        }
    }

    @AfterTestCase
    def afterTestCase(TestCaseContext testCaseContext) {
        if (testCaseContext.getTestStatus() == TestCaseContext.FAILED) {
            try {
                String timestamp = new Date().format('yyyyMMdd_HHmmss')
                String screenshotName = "FAIL_${testCaseContext.getTestCaseId().replaceAll('[^a-zA-Z0-9]', '_')}_${timestamp}.png"
                Windows.takeScreenshot(screenshotName)
                KeywordUtil.logInfo("📸 Đã chụp ảnh lỗi: ${screenshotName}")
            } catch (Exception e) {
                KeywordUtil.logInfo("Không thể chụp ảnh (có thể app đã đóng): ${e.message}")
            }
        }
        KeywordUtil.logInfo("■ Kết thúc Test Case: ${testCaseContext.getTestCaseId()} — Status: ${testCaseContext.getTestStatus()}")
    }
}
