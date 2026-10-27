/**
 * TC03_BVA_Calculation.groovy
 * Mục đích: Demo DATA-DRIVEN TESTING với 12 ca kiểm thử giá trị biên (BVA)
 * Ứng dụng: MiniSum.exe (Login + Calculator Window)
 * Tác giả: Kan — Tool A: Katalon Studio (M2)
 *
 * Mô hình Data-Driven:
 *   - Biến A, B, Expected được khai báo trong tab Variables của Test Case
 *   - Test Suite thực hiện Data Binding với file Excel BVA_TestData.xlsx
 *   - Mỗi dòng dữ liệu → 1 lần chạy Test Case
 *
 * Luồng kiểm thử (thực thi cho mỗi dòng dữ liệu):
 *   1. Mở MiniSum.exe
 *   2. Login hợp lệ (abc / 123)
 *   3. Chuyển sang cửa sổ Calculator
 *   4. Nhập A = ${A}, B = ${B} (tham số hóa từ Excel)
 *   5. Click btnSum
 *   6. Phân nhánh CHECKPOINT theo Expected:
 *      - Nếu Expected = "LOI"  → kiểm tra lblError có nội dung lỗi
 *      - Nếu Expected là số    → kiểm tra lblResult có "Ket qua: A + B = Expected"
 *   7. Đóng ứng dụng
 */

import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.util.KeywordUtil
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import org.openqa.selenium.Keys

// ===== Đường dẫn ứng dụng =====
String appPath = 'D:\\KAN\\N4_1\\semina\\Tool_A_Katalon_Artifacts\\MiniSum\\bin\\Release\\net6.0-windows\\MiniSum.exe'

// ===== Biến Data-Driven (được bind từ Excel qua Test Suite) =====
// Khai báo trong tab Variables của Test Case:
//   A        | Type: String | Value: ${A}
//   B        | Type: String | Value: ${B}
//   Expected | Type: String | Value: ${Expected}
// Khi bind từ Excel, các biến này sẽ nhận giá trị theo từng dòng dữ liệu

String strA = A.toString().trim()
String strB = B.toString().trim()
String strExpected = Expected.toString().trim()

KeywordUtil.logInfo("BVA Test Case chạy với: A='${strA}', B='${strB}', Expected='${strExpected}'")

// ===== Bước 1: Mở ứng dụng & Đăng nhập hợp lệ (tìm theo tiêu đề cửa sổ) =====
Windows.startApplicationWithTitle(appPath, 'MiniSum - Dang nhap')
Thread.sleep(1000)
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/txtUser'))
Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtUser'), 'abc')
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/txtPass'))
Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtPass'), '123')
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/btnSubmit'))
Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Login/btnSubmit'), Keys.chord(Keys.ENTER))

// Đợi và chuyển sang cửa sổ Calculator (timeout 10s)
Thread.sleep(1000)
Windows.switchToWindowTitle('MiniSum - Tinh tong')
Windows.waitForElementPresent(
    findWindowsObject('Object Repository/MiniSum/Calculator/winMain'),
    10
)
Thread.sleep(500)

// ===== Bước 2: Nhập A và B từ dữ liệu =====
Windows.click(findWindowsObject('Object Repository/MiniSum/Calculator/txtA'))
Windows.setText(findWindowsObject('Object Repository/MiniSum/Calculator/txtA'), strA)
Windows.click(findWindowsObject('Object Repository/MiniSum/Calculator/txtB'))
Windows.setText(findWindowsObject('Object Repository/MiniSum/Calculator/txtB'), strB)

// ===== Bước 3: Click nút TINH TONG =====
Windows.click(findWindowsObject('Object Repository/MiniSum/Calculator/btnSum'))
Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Calculator/btnSum'), Keys.chord(Keys.ENTER))
Thread.sleep(500)

// ===== Bước 4: CHECKPOINT phân nhánh theo Expected =====
if (strExpected.equalsIgnoreCase("LOI")) {
    // Kỳ vọng ứng dụng báo lỗi → lblError phải có nội dung
    String errorText = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Calculator/lblError'), 'Name')
    if (errorText == null || errorText.trim().isEmpty()) {
        errorText = Windows.getText(findWindowsObject('Object Repository/MiniSum/Calculator/lblError'))
    }
    assert errorText != null && errorText.trim().length() > 0 :
        "Kỳ vọng lblError hiển thị lỗi, nhưng nhận được: '${errorText}'"
    KeywordUtil.logInfo("PASS: lblError hiển thị đúng lỗi = '${errorText}'")
} else {
    // Kỳ vọng kết quả hợp lệ → lblResult phải chứa "Ket qua: A + B = Expected"
    String expectedResult = "Ket qua: ${strA} + ${strB} = ${strExpected}"
    String actualResult = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'), 'Name')
    if (actualResult == null || actualResult.trim().isEmpty()) {
        actualResult = Windows.getText(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'))
    }
    assert actualResult == expectedResult : "Kỳ vọng '${expectedResult}', nhưng nhận được '${actualResult}'"
    KeywordUtil.logInfo("PASS: lblResult = '${expectedResult}'")
}

// ===== Bước 5: Đóng ứng dụng =====
Windows.closeApplication()
