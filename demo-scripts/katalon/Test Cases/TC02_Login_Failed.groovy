/**
 * TC02_Login_Failed.groovy
 * Mục đích: Demo Checkpoint cho trường hợp đăng nhập SAI mật khẩu (Negative Test)
 * Ứng dụng: MiniSum_v3.exe (Login Window)
 * Tác giả: Kan — Tool A: Katalon Studio (M2)
 */

import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.configuration.RunConfiguration
import com.kms.katalon.core.util.KeywordUtil
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows

// Tự động xác định đường dẫn MiniSum_v3.exe từ repo được clone từ GitHub
String projectDir = RunConfiguration.getProjectDir()
String appPath = ''
for (String candidate : [
    projectDir + '/../../case-study-app/MiniSum_v3.exe',
    projectDir + '/../case-study-app/MiniSum_v3.exe',
    projectDir + '/case-study-app/MiniSum_v3.exe',
    'case-study-app/MiniSum_v3.exe'
]) {
    if (new File(candidate).exists()) {
        appPath = new File(candidate).getCanonicalPath()
        break
    }
}
if (!appPath || !new File(appPath).exists()) {
    appPath = projectDir + '/case-study-app/MiniSum_v3.exe'
}

// Bước 1: Khởi động ứng dụng
Windows.startApplicationWithTitle(appPath, 'MiniSum - Dang nhap')
Windows.switchToWindowTitle('MiniSum - Dang nhap')

// Bước 2: Nhập tài khoản và mật khẩu sai
Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtUser'), 'admin')
Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Login/txtPass'), 'wrong_pass')

// Bước 3: Click nút Đăng nhập
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/btnSubmit'))

// Bước 4: Checkpoint #1 — Xác minh hiển thị thông báo lỗi chính xác
String actualMsg = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'), 'Name') ?: Windows.getText(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'))
assert actualMsg == 'Sai tai khoan hoac mat khau' : "Kỳ vọng 'Sai tai khoan hoac mat khau', nhưng nhận được '${actualMsg}'"

// Bước 5: Checkpoint #2 — Xác minh vẫn ở màn hình Đăng nhập (không bị chuyển trang)
Windows.verifyElementPresent(findWindowsObject('Object Repository/MiniSum/Login/winLogin'), 5)

// Bước 6: Bonus Checkpoint #3 — Xác minh trường mật khẩu đã bị xóa tự động (UX pattern)
String passValue = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Login/txtPass'), 'Value')
assert passValue == '' || passValue == null : "Kỳ vọng trường mật khẩu rỗng sau khi đăng nhập thất bại"

// Bước 7: Đóng ứng dụng
Windows.closeApplication()

KeywordUtil.logInfo('TC02 PASSED: Đăng nhập sai hiển thị đúng thông báo lỗi và xóa mật khẩu')
