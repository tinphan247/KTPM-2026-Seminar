/**
 * TC02_Login_Failed.groovy
 * Mục đích: Demo Checkpoint cho trường hợp đăng nhập SAI mật khẩu
 *         (kịch bản Negative Test Case)
 * Ứng dụng: MiniSum.exe (Login Window)
 * Tác giả: Kan — Tool A: Katalon Studio (M2)
 *
 * Luồng kiểm thử:
 *   1. Mở MiniSum.exe
 *   2. Nhập username hợp lệ "abc"
 *   3. Nhập password sai "wrong_pass"
 *   4. Click nút "DANG NHAP"
 *   5. CHECKPOINT: verifyElementText(lblMessage) == "Sai tai khoan hoac mat khau"
 *   6. CHECKPOINT phụ: verifyElementPresent(winLogin) — vẫn ở màn Login (không chuyển)
 *   7. Đóng ứng dụng
 */

import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.util.KeywordUtil
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import org.openqa.selenium.Keys

String appPath = 'D:\\KAN\\N4_1\\semina\\Tool_A_Katalon_Artifacts\\MiniSum\\bin\\Release\\net6.0-windows\\MiniSum.exe'

// Khởi động ứng dụng (tìm chính xác theo tiêu đề cửa sổ)
Windows.startApplicationWithTitle(appPath, 'MiniSum - Dang nhap')
Thread.sleep(1000)

// Nhập thông tin sai (negative test case)
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/txtUser'))
Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtUser'), 'abc')
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/txtPass'))
Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtPass'), 'wrong_pass')

// Click nút Đăng nhập & kích hoạt phím Enter
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/btnSubmit'))
Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Login/btnSubmit'), Keys.chord(Keys.ENTER))
Thread.sleep(500)

// CHECKPOINT #1 — Nhãn lỗi phải hiển thị thông báo chính xác
String actualMsg = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'), 'Name')
if (actualMsg == null || actualMsg.trim().isEmpty()) {
    actualMsg = Windows.getText(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'))
}
KeywordUtil.logInfo("Nội dung lblMessage lỗi nhận được: '${actualMsg}'")
assert actualMsg == 'Sai tai khoan hoac mat khau' : "Kỳ vọng 'Sai tai khoan hoac mat khau', nhưng nhận được '${actualMsg}'"

// CHECKPOINT #2 — Vẫn ở cửa sổ Login (không chuyển sang Calculator)
Windows.verifyElementPresent(
    findWindowsObject('Object Repository/MiniSum/Login/winLogin'),
    5
)

// BONUS CHECKPOINT #3 — Trường mật khẩu phải bị xóa (để sẵn cho lần nhập tiếp theo)
String passValue = Windows.getAttribute(
    findWindowsObject('Object Repository/MiniSum/Login/txtPass'),
    'Value'
)
assert passValue == '' || passValue == null : 'Password field phải rỗng sau khi đăng nhập thất bại'

Windows.closeApplication()

KeywordUtil.logInfo('TC02 PASSED: Đăng nhập sai mật khẩu hiển thị thông báo lỗi đúng')
