/**
 * TC03_BVA_Calculation.groovy
 * Mục đích: Demo Data-Driven Testing (DDT) với 12 ca kiểm thử giá trị biên (BVA)
 * Ứng dụng: MiniSum_v3.exe (Calculator Window)
 * Tác giả: Kan — Tool A: Katalon Studio (M2)
 */

import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.model.FailureHandling
import com.kms.katalon.core.util.KeywordUtil
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows

String appPath = 'D:\\KAN\\N4_1\\semina\\KTPM-2026-Seminar\\case-study-app\\MiniSum_v3.exe'

// Bước 1: Khởi động và đăng nhập nếu màn hình Calculator chưa mở (Tái sử dụng phiên cho DDT)
boolean isCalcOpen = false
try {
    Windows.switchToWindowTitle('MiniSum - Tinh tong', FailureHandling.OPTIONAL)
    isCalcOpen = Windows.verifyElementPresent(findWindowsObject('Object Repository/MiniSum/Calculator/winMain'), 1, FailureHandling.OPTIONAL)
} catch (Exception ignored) {}

if (!isCalcOpen) {
    Windows.startApplicationWithTitle(appPath, 'MiniSum - Dang nhap')
    Windows.switchToWindowTitle('MiniSum - Dang nhap')
    Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtUser'), 'admin')
    Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Login/txtPass'), '1234')
    Windows.click(findWindowsObject('Object Repository/MiniSum/Login/btnSubmit'))
    Windows.switchToWindowTitle('MiniSum - Tinh tong')
    Windows.verifyElementPresent(findWindowsObject('Object Repository/MiniSum/Calculator/winMain'), 10)
}

// Bước 2: Lấy dữ liệu kiểm thử (A, B, Expected được bind từ file Excel qua Test Suite)
String strA = A.toString().trim()
String strB = B.toString().trim()
String strExpected = Expected.toString().trim()

// Bước 3: Nhập A, B và thực hiện tính tổng
Windows.setText(findWindowsObject('Object Repository/MiniSum/Calculator/txtA'), strA)
Windows.setText(findWindowsObject('Object Repository/MiniSum/Calculator/txtB'), strB)
Windows.click(findWindowsObject('Object Repository/MiniSum/Calculator/btnSum'))

// Bước 4: Checkpoint phân nhánh theo kết quả kỳ vọng
if (strExpected.equalsIgnoreCase('LOI')) {
    String errorText = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Calculator/lblError'), 'Name') ?: Windows.getText(findWindowsObject('Object Repository/MiniSum/Calculator/lblError'))
    assert errorText != null && !errorText.trim().isEmpty() : 'Kỳ vọng hiển thị lỗi nhưng lblError rỗng'
    KeywordUtil.logInfo("PASS [${strA}, ${strB}] -> Báo lỗi: ${errorText}")
} else {
    String expectedResult = "Ket qua: ${strA} + ${strB} = ${strExpected}"
    String actualResult = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'), 'Name') ?: Windows.getText(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'))
    assert actualResult == expectedResult : "Kỳ vọng '${expectedResult}', nhưng nhận được '${actualResult}'"
    KeywordUtil.logInfo("PASS [${strA}, ${strB}] -> ${actualResult}")
}
