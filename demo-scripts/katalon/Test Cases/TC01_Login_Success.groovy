/**
 * TC01_Login_Success.groovy
 * Mục đích: Demo Record & Playback + Checkpoint cho trường hợp đăng nhập HỢP LỆ
 * Ứng dụng: MiniSum_v3.exe (Login Window)
 * Tác giả: Kan — Tool A: Katalon Studio (M2)
 */

import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.util.KeywordUtil
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows

// Đường dẫn ứng dụng MiniSum_v3.exe
String appPath = 'D:\\KAN\\N4_1\\semina\\KTPM-2026-Seminar\\case-study-app\\MiniSum_v3.exe'

// Bước 1: Khởi động ứng dụng
Windows.startApplicationWithTitle(appPath, 'MiniSum - Dang nhap')
Windows.switchToWindowTitle('MiniSum - Dang nhap')

// Bước 2: Nhập tài khoản hợp lệ
Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtUser'), 'admin')

// Bước 3: Nhập mật khẩu hợp lệ (dùng sendKeys cho ô password)
Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Login/txtPass'), '1234')

// Bước 4: Click nút Đăng nhập
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/btnSubmit'))

// Bước 5: Checkpoint #1 (K10) — Xác minh thông báo lblMessage = 'Dang nhap thanh cong'
String successMsg = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'), 'Name') ?: Windows.getText(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'))
assert successMsg == 'Dang nhap thanh cong' : "Kỳ vọng 'Dang nhap thanh cong', nhưng nhận được '${successMsg}'"

// Bước 6: Checkpoint #2 — Chuyển sang cửa sổ Calculator và xác minh xuất hiện
Windows.switchToWindowTitle('MiniSum - Tinh tong')
Windows.verifyElementPresent(findWindowsObject('Object Repository/MiniSum/Calculator/winMain'), 10)

// Bước 7: Đóng ứng dụng
Windows.closeApplication()

KeywordUtil.logInfo('TC01 PASSED: Đăng nhập thành công, đúng lblMessage và mở Calculator')
