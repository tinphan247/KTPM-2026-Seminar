package com.minisum.keywords

import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject

import com.kms.katalon.core.annotation.Keyword
import com.kms.katalon.core.util.KeywordUtil
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import org.openqa.selenium.Keys

/**
 * LoginKeyword.groovy
 * Custom Keyword trong Katalon Studio cho ung dung MiniSum (WPF Desktop AUT).
 *
 * Tuan thu mo hinh Keyword-Driven Testing & Page Object Model (POM):
 *   - Goi cac thao tac UI phuc tap thanh ham bieu cam, de doc, de tai su dung.
 *   - Ap dung Explicit Wait thay the hoan toan Thread.sleep cung.
 *   - Dong goi logic Checkpoint (Test Oracle) xac minh nhan thong bao va ket qua.
 *
 * Tac gia: Nguyen Le Quang Kan (MSSV: 23120279) - Chuyen trach Tool A: Katalon Studio
 */
class LoginKeyword {

    /**
     * Khoi dong MiniSum_v3.exe va thuc hien dang nhap voi thong tin tai khoan
     * @param appPath Duong dan tuyet doi toi file MiniSum_v3.exe
     * @param username Ten dang nhap (hop le: "admin")
     * @param password Mat khau (hop le: "1234")
     * @param timeoutSoGiay Thoi gian cho toi da (giay)
     */
    @Keyword
    def login(String appPath = 'D:\\KAN\\N4_1\\semina\\KTPM-2026-Seminar\\case-study-app\\MiniSum_v3.exe', String username = 'admin', String password = '1234', int timeoutSoGiay = 10) {
        if (!new File(appPath).exists()) {
            appPath = 'D:\\KAN\\N4_1\\semina\\Tool_A_Katalon_Artifacts\\MiniSum\\bin\\Release\\net6.0-windows\\MiniSum_v3.exe'
        }
        
        // Cấu hình URL WinAppDriver cho Katalon Studio v11+
        try {
            Map winPref = ['desktopDriverUrl': 'http://127.0.0.1:4723', 'winAppDriverUrl': 'http://127.0.0.1:4723']
            Map execution = com.kms.katalon.core.configuration.RunConfiguration.getExecutionProperties() ?: [:]
            Map drivers = execution.get('drivers') instanceof Map ? execution.get('drivers') : [:]
            Map preferences = drivers.get('preferences') instanceof Map ? drivers.get('preferences') : [:]
            preferences.put('Windows', winPref)
            drivers.put('preferences', preferences)
            execution.put('drivers', drivers)
            com.kms.katalon.core.configuration.RunConfiguration.setExecutionSetting(['execution': execution])
        } catch (Throwable ignored) {
        }

        KeywordUtil.logInfo(">>> [LoginKeyword] Khoi dong MiniSum tu: ${appPath}")
        Windows.startApplicationWithTitle(appPath, 'MiniSum - Dang nhap')
        Thread.sleep(1500)
        try {
            Windows.switchToWindowTitle('MiniSum - Dang nhap')
        } catch (Exception ignored) {
        }
        Thread.sleep(500)
        
        // Explicit wait: Cho den khi o nhap txtUser xuat hien tren giao dien
        Windows.waitForElementPresent(findWindowsObject('Object Repository/MiniSum/Login/txtUser'), timeoutSoGiay)
        
        KeywordUtil.logInfo(">>> [LoginKeyword] Nhap tai khoan='${username}', mat khau='${password}'")
        Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtUser'), username)
        Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Login/txtPass'), password)
        
        KeywordUtil.logInfo(">>> [LoginKeyword] Click nut DANG NHAP")
        try {
            Windows.click(findWindowsObject('Object Repository/MiniSum/Login/btnLogin'))
        } catch (Exception e) {
            Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Login/txtPass'), Keys.chord(Keys.ENTER))
        }
    }

    /**
     * Checkpoint xac minh nhan thong bao lblMessage tai man hinh Dang nhap
     * @param expectedMessage Chuoi ky vong (vi du: "Dang nhap thanh cong" hoac "Sai tai khoan hoac mat khau")
     * @return boolean true neu pass assertion
     */
    @Keyword
    def verifyLoginMessage(String expectedMessage) {
        KeywordUtil.logInfo(">>> [LoginKeyword] Checkpoint: Kiem tra lblMessage phai bang '${expectedMessage}'")
        
        // UIA doc noi dung TextBlock qua thuoc tinh 'Name' hoac fallback sang getText()
        String actualMsg = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'), 'Name')
        if (actualMsg == null || actualMsg.trim().isEmpty()) {
            actualMsg = Windows.getText(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'))
        }
        
        KeywordUtil.logInfo(">>> [LoginKeyword] Noi dung thuc te cua lblMessage: '${actualMsg}'")
        assert actualMsg == expectedMessage : "Checkpoint THAT BAI: Ky vong '${expectedMessage}', thuc te nhan '${actualMsg}'"
        KeywordUtil.markPassed("Checkpoint PASS: lblMessage hien thi dung '${expectedMessage}'")
        return true
    }

    /**
     * Explicit wait: Cho va chuyen sang man hinh Tinh toan (MainWindow)
     * @param timeoutSoGiay Thoi gian cho cua so moi xuat hien
     */
    @Keyword
    def switchToCalculator(int timeoutSoGiay = 10) {
        KeywordUtil.logInfo(">>> [LoginKeyword] Cho va chuyen sang cua so 'MiniSum - Tinh tong'...")
        Thread.sleep(1000) // Cho ung dung MiniSum delay 1s theo thiet ke
        Windows.switchToWindowTitle('MiniSum - Tinh tong')
        Windows.waitForElementPresent(findWindowsObject('Object Repository/MiniSum/Calculator/winMain'), timeoutSoGiay)
        KeywordUtil.markPassed("Da chuyen sang cua so Calculator thanh cong.")
    }

    /**
     * Nhap gia tri A va B roi bam nut TINH TONG
     * @param a Gia tri toan hang A (chuoi)
     * @param b Gia tri toan hang B (chuoi)
     */
    @Keyword
    def calculateSum(String a, String b) {
        KeywordUtil.logInfo(">>> [LoginKeyword] Nhap A='${a}', B='${b}' va bam nut TINH TONG")
        Windows.click(findWindowsObject('Object Repository/MiniSum/Calculator/txtA'))
        Windows.setText(findWindowsObject('Object Repository/MiniSum/Calculator/txtA'), a)
        
        Windows.click(findWindowsObject('Object Repository/MiniSum/Calculator/txtB'))
        Windows.setText(findWindowsObject('Object Repository/MiniSum/Calculator/txtB'), b)
        
        Windows.click(findWindowsObject('Object Repository/MiniSum/Calculator/btnSum'))
        Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Calculator/btnSum'), Keys.chord(Keys.ENTER))
        Thread.sleep(300)
    }

    /**
     * Checkpoint phan nhanh theo gia tri Expected (Data-Driven Test Oracle)
     * @param a Toan hang A
     * @param b Toan hang B
     * @param expected Gia tri ky vong ("LOI" hoac so nguyen ket qua)
     */
    @Keyword
    def verifyResultOrError(String a, String b, String expected) {
        if (expected.equalsIgnoreCase("LOI")) {
            KeywordUtil.logInfo(">>> [LoginKeyword] Ca kiem thu ngoai le: Kiem tra lblError phai hien thi thong bao loi")
            String err = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Calculator/lblError'), 'Name')
            if (err == null || err.trim().isEmpty()) {
                err = Windows.getText(findWindowsObject('Object Repository/MiniSum/Calculator/lblError'))
            }
            assert err != null && err.trim().length() > 0 : "Loi checkpoint: lblError khong co thong bao loi!"
            KeywordUtil.markPassed("Checkpoint PASS: lblError = '${err}'")
        } else {
            String expResult = "Ket qua: ${a} + ${b} = ${expected}"
            KeywordUtil.logInfo(">>> [LoginKeyword] Ca kiem thu hop le: Kiem tra lblResult == '${expResult}'")
            String actResult = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'), 'Name')
            if (actResult == null || actResult.trim().isEmpty()) {
                actResult = Windows.getText(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'))
            }
            assert actResult == expResult : "Checkpoint THAT BAI: Ky vong '${expResult}', nhung nhan '${actResult}'"
            KeywordUtil.markPassed("Checkpoint PASS: lblResult = '${expResult}'")
        }
    }

    /**
     * Dong ung dung MiniSum an toan sau khi hoan tat ca kiem thu
     */
    @Keyword
    def closeApp() {
        KeywordUtil.logInfo(">>> [LoginKeyword] Dong ung dung AUT")
        Windows.closeApplication()
    }
}
