/**
 * TC01_Login_Success.groovy
 * Mục đích: Demo Record & Playback + Checkpoint cho trường hợp đăng nhập HỢP LỆ
 * Ứng dụng: MiniSum.exe (Login Window)
 * Tác giả: Kan — Tool A: Katalon Studio (M2)
 *
 * Luồng kiểm thử:
 *   1. Khởi động WinAppDriver (yêu cầu môi trường)
 *   2. Mở MiniSum.exe qua Windows.startApplicationWithTitle
 *   3. Nhập username = "abc"
 *   4. Nhập password = "123"
 *   5. Click nút "DANG NHAP"
 *   6. Checkpoint: verifyElementText(lblMessage) == "Dang nhap thanh cong"
 *   7. Checkpoint: verifyElementPresent(winMain) — cửa sổ Calculator xuất hiện
 *   8. Đóng ứng dụng
 */

import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.util.KeywordUtil
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import org.openqa.selenium.Keys

// Đường dẫn tuyệt đối tới MiniSum.exe — điều chỉnh theo máy của bạn
String appPath = 'D:\\KAN\\N4_1\\semina\\Tool_A_Katalon_Artifacts\\MiniSum\\bin\\Release\\net6.0-windows\\MiniSum.exe'

// Bước 1: Khởi động ứng dụng (tìm chính xác theo tiêu đề cửa sổ)
Windows.startApplicationWithTitle(appPath, 'MiniSum - Dang nhap')
Thread.sleep(1000)

// Bước 2: Nhập tài khoản
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/txtUser'))
Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtUser'), 'abc')

// Bước 3: Nhập mật khẩu
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/txtPass'))
Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtPass'), '123')

// Bước 4: Click nút Đăng nhập & kích hoạt phím Enter
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/btnSubmit'))
Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Login/btnSubmit'), Keys.chord(Keys.ENTER))
Thread.sleep(500)

// Bước 5: CHECKPOINT #1 — Kiểm tra nhãn lblMessage hiển thị "Dang nhap thanh cong"
// WPF TextBlock lưu văn bản trong thuộc tính 'Name' của UI Automation
String actualMsg = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'), 'Name')
if (actualMsg == null || actualMsg.trim().isEmpty()) {
    actualMsg = Windows.getText(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'))
}
KeywordUtil.logInfo("Nội dung lblMessage nhận được: '${actualMsg}'")
assert actualMsg == 'Dang nhap thanh cong' : "Kỳ vọng 'Dang nhap thanh cong', nhưng nhận được '${actualMsg}'"

// Bước 6: CHECKPOINT #2 — Chuyển sang cửa sổ Calculator và kiểm tra xuất hiện
Thread.sleep(1000)
Windows.switchToWindowTitle('MiniSum - Tinh tong')
Windows.verifyElementPresent(
    findWindowsObject('Object Repository/MiniSum/Calculator/winMain'),
    10
)

// Bước 7: Đóng ứng dụng
Windows.closeApplication()

KeywordUtil.logInfo('TC01 PASSED: Đăng nhập hợp lệ chuyển sang màn hình Calculator')
