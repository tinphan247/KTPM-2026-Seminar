# Hướng Dẫn Thực Hành Katalon Studio — Bài Tập Cá Nhân 30 Phút Tại Lớp

**Chuyên đề:** Automation Testing cho Desktop Applications · **Nhóm 02**  
**Ứng dụng mẫu:** `MiniSum.exe` (WinForms C# .NET 8, tài khoản demo: `admin / 1234`)  
**Công cụ:** Katalon Studio (phiên bản Free 11.x)  
**Kho mã nguồn GitHub:** [https://github.com/tinphan247/KTPM-2026-Seminar.git](https://github.com/tinphan247/KTPM-2026-Seminar.git)

---

## 0. Bản Đồ Thời Gian Thực Hành 30 Phút

| Mốc thời gian | Hoạt động chính | Mục tiêu đạt được |
|---|---|---|
| **00 – 05'** | Clone repo từ GitHub, mở `MiniSum.exe` và Katalon Studio | Ứng dụng chạy lên, nạp thành công Object Repository |
| **05 – 17'** | **Bài 1:** Tạo `TC_Login_<MSSV>` (Login đúng + sai + Checkpoint) | 2 ca kiểm thử Đăng nhập báo **PASSED** (màu xanh) |
| **17 – 27'** | **Bài 2:** Tạo `TC_Calculate_<MSSV>` (Tính $A+B$ + Checkpoint BVA) | Ca tính tổng và 2 ca biên báo **PASSED** |
| **27 – 30'** | Xuất báo cáo HTML / Chụp màn hình và nộp bài | Hoàn thành và nộp bài đúng hạn |
| *(Tùy chọn)* | **Bonus:** Kiểm thử bắt lỗi ngoài biên trên `MiniSum_v3.exe` | Nhận thêm **+1.0 điểm thưởng** |

<p class="table-caption"><b>Bảng 9.1:</b> <i>Bảng phân bổ các mốc thời gian thực hiện bài tập thực hành cá nhân tại lớp</i></p>


>  **Mẹo tiết kiệm thời gian (Quy tắc 3 phút):** Kho đối tượng (*Object Repository*) của `MiniSum` đã được tạo sẵn trong thư mục `demo-scripts/katalon/` của repository. Sinh viên không cần dùng Object Spy để dò lại các phần tử mà có thể tái sử dụng ngay!

---

## 1. Chuẩn Bị Môi Trường

### 1.1. Yêu cầu hệ thống
1. **Hệ điều hành:** Windows 10 hoặc Windows 11 (64-bit).
2. **.NET 8 Desktop Runtime (x64):** Nếu máy chưa có, tải nhanh bộ cài chính thức từ Microsoft: [dotnet.microsoft.com/download/dotnet/8.0](https://dotnet.microsoft.com/download/dotnet/8.0) (chọn *Run desktop apps* $\to$ *Download x64*).
3. **Katalon Studio Free:** Tải tại [katalon.com/download](https://katalon.com/download) và đăng nhập bằng tài khoản cá nhân miễn phí.

### 1.2. Lấy tài nguyên từ GitHub về máy tính cá nhân
Mở **PowerShell** hoặc **Command Prompt** tại thư mục bạn muốn lưu bài (ví dụ `C:\KTPM` hoặc `D:\Testing`):

```powershell
# Bước 1: Clone kho mã nguồn từ GitHub
git clone https://github.com/tinphan247/KTPM-2026-Seminar.git

# Bước 2: Di chuyển vào thư mục dự án
cd KTPM-2026-Seminar

# Bước 3: Kiểm tra các phiên bản ứng dụng mẫu
dir case-study-app\*.exe
```

>  **Nếu máy bạn không có Git:**
> - Truy cập trực tiếp link GitHub: [https://github.com/tinphan247/KTPM-2026-Seminar](https://github.com/tinphan247/KTPM-2026-Seminar)
> - Bấm nút màu xanh **Code** $\to$ Chọn **Download ZIP**.
> - Giải nén file ZIP vào thư mục không dấu (ví dụ `C:\KTPM\KTPM-2026-Seminar`).

---

## 2. Kiểm Tra Ứng Dụng Mẫu (AUT)

Vào thư mục `case-study-app/`:
- Nháy đúp file `MiniSum.exe` (hoặc `MiniSum_v3.exe`).
- Cửa sổ **"MiniSum - Dang nhap"** xuất hiện trên màn hình $\to$ Ứng dụng hoạt động bình thường! Đóng ứng dụng lại để chuẩn bị tự động hóa.

```text
Cấu trúc thư mục ứng dụng trong repo:
KTPM-2026-Seminar/
├── case-study-app/
│   ├── MiniSum.exe          # Bản v1 (dùng cho Bài 1, Bài 2)
│   ├── MiniSum_v2.exe       # Bản v2 (đổi nút thành btnCalculate)
│   └── MiniSum_v3.exe       # Bản v3 (có nhãn lỗi lblError dùng cho bài Bonus)
└── demo-scripts/
    └── katalon/             # Thư mục starter kit của nhóm
        ├── Object Repository/MiniSum/  # Chứa sẵn 13 locator giao diện
        └── Test Cases/                 # Các test case mẫu tham khảo
```

---

## 3. Khởi Tạo Dự Án Katalon Studio

1. Khởi động **Katalon Studio**.
2. Chọn **File $\to$ New $\to$ Project**:
   - **Name:** `MiniSum_Lab_<MSSV>` (ví dụ: `MiniSum_Lab_23120001`).
   - **Type:** Chọn **Generic** hoặc để mặc định.
   - **Location:** Chọn thư mục trên máy bạn (ví dụ: `C:\KTPM\Projects`).
   - Bấm **OK** để tạo dự án mới.
3. **Nạp kho đối tượng có sẵn (Tiết kiệm thời gian dò locator):**
   - Mở File Explorer, copy thư mục `Object Repository` từ thư mục repo vừa clone (`KTPM-2026-Seminar\demo-scripts\katalon\Object Repository`) dán đè vào thư mục dự án Katalon bạn vừa tạo.
   - Quay lại Katalon Studio, bấm chuột phải vào thư mục gốc dự án $\to$ Chọn **Refresh (F5)**.
   - Kiểm tra nhánh `Object Repository/MiniSum/` đã xuất hiện đầy đủ:
     - Nhánh `Login`: `txtUser`, `txtPass`, `btnLogin`, `lblMessage`.
     - Nhánh `Calculator`: `txtA`, `txtB`, `btnSum`, `lblResult`, `lblError`.

---

## 4. Hướng Dẫn Chi Tiết BÀI TẬP 1: Tự Động Hóa Đăng Nhập (12 Phút)

### 4.1. Tạo Test Case mới
- Chuột phải vào thư mục `Test Cases` $\to$ **New $\to$ Test Case**.
- Đặt tên: `TC_Login_<MSSV>` (ví dụ: `TC_Login_23120001`).

### 4.2. Thêm các bước kiểm thử (Manual Mode hoặc Script Mode)

#### Cách làm bằng Script Mode (Khuyên dùng để nhanh nhất):
Chuyển sang tab **Script** ở góc dưới màn hình soạn thảo và dán đoạn mã sau:

```groovy
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import com.kms.katalon.core.util.KeywordUtil

// BƯỚC 1: ĐIỀN ĐƯỜNG DẪN ỨNG DỤNG TRÊN MÁY BẠN
// (Chỉ cần copy đường dẫn tuyệt đối của file MiniSum.exe trong thư mục repo bạn vừa clone)
String appPath = 'C:/KTPM/KTPM-2026-Seminar/case-study-app/MiniSum.exe'

// Khởi động ứng dụng MiniSum
Windows.startApplicationWithTitle(appPath, 'MiniSum - Dang nhap')
Windows.switchToWindowTitle('MiniSum - Dang nhap')

// ==========================================
// CA 1: ĐĂNG NHẬP THÀNH CÔNG (admin / 1234)
// ==========================================
// Nhập thông tin đăng nhập
Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtUser'), 'admin')
Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Login/txtPass'), '1234')

// Nhấp nút Đăng nhập
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/btnLogin'))

// CHECKPOINT 1: Xác minh nhãn lblMessage hiển thị đúng thông báo thành công
String msgSuccess = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'), 'Name') ?: Windows.getText(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'))
assert msgSuccess == 'Dang nhap thanh cong' : "Kỳ vọng 'Dang nhap thanh cong', thực tế nhận: '${msgSuccess}'"
KeywordUtil.logInfo(" Checkpoint Ca 1 PASS: ${msgSuccess}")

// Đóng ứng dụng để chuẩn bị cho Ca 2
Windows.closeApplication()

// ==========================================
// CA 2: ĐĂNG NHẬP THẤT BẠI (admin / sai pass)
// ==========================================
Windows.startApplicationWithTitle(appPath, 'MiniSum - Dang nhap')
Windows.switchToWindowTitle('MiniSum - Dang nhap')

Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtUser'), 'admin')
Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Login/txtPass'), 'wrongpass')
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/btnLogin'))

// CHECKPOINT 2: Xác minh nhãn lblMessage báo lỗi đăng nhập
String msgError = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'), 'Name') ?: Windows.getText(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'))
assert msgError == 'Sai tai khoan hoac mat khau' : "Kỳ vọng báo lỗi 'Sai tai khoan hoac mat khau', thực tế nhận: '${msgError}'"
KeywordUtil.logInfo(" Checkpoint Ca 2 PASS: ${msgError}")

Windows.closeApplication()
KeywordUtil.logInfo(" HOÀN THÀNH BÀI 1 - TẤT CẢ CHECKPOINT ĐÃ PASS!")
```

### 4.3. Chạy thử nghiệm Bài 1
1. Nhấn nút mũi tên cạnh biểu tượng **Run ** trên thanh công cụ $\to$ Chọn **Windows**.
2. Quan sát ứng dụng tự động mở lên, điền `admin/1234`, kiểm tra thông báo, đóng và lặp lại với trường hợp sai mật khẩu.
3. Tab **Log Viewer** bên dưới hiển thị màu xanh lá cây với thông báo `PASSED` $\to$ **Đạt 4.0 điểm!**

---

## 5. Hướng Dẫn Chi Tiết BÀI TẬP 2: Tự Động Hóa Tính Tổng & Giá Trị Biên (10 Phút)

### 5.1. Tạo Test Case mới
- Chuột phải `Test Cases` $\to$ **New $\to$ Test Case**.
- Đặt tên: `TC_Calculate_<MSSV>`.

### 5.2. Nội dung kịch bản kiểm thử tính toán và biên
Chuyển sang tab **Script** và dán đoạn mã kịch bản:

```groovy
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import com.kms.katalon.core.util.KeywordUtil

// Đường dẫn file MiniSum.exe trên máy bạn
String appPath = 'C:/KTPM/KTPM-2026-Seminar/case-study-app/MiniSum.exe'

// Khởi động và đăng nhập vào màn hình tính toán
Windows.startApplicationWithTitle(appPath, 'MiniSum - Dang nhap')
Windows.switchToWindowTitle('MiniSum - Dang nhap')
Windows.setText(findWindowsObject('Object Repository/MiniSum/Login/txtUser'), 'admin')
Windows.sendKeys(findWindowsObject('Object Repository/MiniSum/Login/txtPass'), '1234')
Windows.click(findWindowsObject('Object Repository/MiniSum/Login/btnLogin'))

// Chờ chuyển sang cửa sổ 'MiniSum - Tinh tong'
Windows.switchToWindowTitle('MiniSum - Tinh tong')
Windows.verifyElementPresent(findWindowsObject('Object Repository/MiniSum/Calculator/winMain'), 5)

// ==========================================
// 1. TÍNH TỔNG THÔNG THƯỜNG (A = 15, B = 25)
// ==========================================
Windows.setText(findWindowsObject('Object Repository/MiniSum/Calculator/txtA'), '15')
Windows.setText(findWindowsObject('Object Repository/MiniSum/Calculator/txtB'), '25')
Windows.click(findWindowsObject('Object Repository/MiniSum/Calculator/btnSum'))

// Checkpoint kiểm tra nhãn lblResult
String resNominal = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'), 'Name') ?: Windows.getText(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'))
assert resNominal == 'Ket qua: 15 + 25 = 40' : "Sai kết quả, thực tế: ${resNominal}"
KeywordUtil.logInfo(" Ca thông thường PASS: ${resNominal}")

// ==========================================
// 2. KIỂM THỬ BIÊN TRÊN (A = 99, B = 0)
// ==========================================
Windows.setText(findWindowsObject('Object Repository/MiniSum/Calculator/txtA'), '99')
Windows.setText(findWindowsObject('Object Repository/MiniSum/Calculator/txtB'), '0')
Windows.click(findWindowsObject('Object Repository/MiniSum/Calculator/btnSum'))

String resUpper = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'), 'Name') ?: Windows.getText(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'))
assert resUpper == 'Ket qua: 99 + 0 = 99' : "Sai kết quả biên trên: ${resUpper}"
KeywordUtil.logInfo(" Ca biên trên PASS: ${resUpper}")

// ==========================================
// 3. KIỂM THỬ BIÊN DƯỚI (A = -99, B = 0)
// ==========================================
Windows.setText(findWindowsObject('Object Repository/MiniSum/Calculator/txtA'), '-99')
Windows.setText(findWindowsObject('Object Repository/MiniSum/Calculator/txtB'), '0')
Windows.click(findWindowsObject('Object Repository/MiniSum/Calculator/btnSum'))

String resLower = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'), 'Name') ?: Windows.getText(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'))
assert resLower == 'Ket qua: -99 + 0 = -99' : "Sai kết quả biên dưới: ${resLower}"
KeywordUtil.logInfo(" Ca biên dưới PASS: ${resLower}")

Windows.closeApplication()
KeywordUtil.logInfo(" HOÀN THÀNH BÀI 2 - ĐẠT ĐIỂM TỐI ĐA BVA!")
```

### 5.3. Chạy kiểm thử Bài 2
- Nhấn **Run  (Windows)**.
- Quan sát kịch bản tự động thực thi 3 phép tính liên tiếp và xác minh các giá trị biên.
- Log báo **PASSED** $\to$ **Đạt trọn vẹn 6.0 điểm!**

---

## 6. Phần Mở Rộng: Bắt Lỗi Ngoài Biên (Bonus +1.0 Điểm)

* Mở file kịch bản mới `TC_Bonus_<MSSV>`.
* Đổi đường dẫn sang bản `MiniSum_v3.exe` (phiên bản có ràng buộc kiểm tra phạm vi $[-99, 99]$):
  `String appPath = 'C:/KTPM/KTPM-2026-Seminar/case-study-app/MiniSum_v3.exe'`
* Nhập giá trị vượt ngưỡng biên:
  - Nhập $A = 100$, $B = 0$.
  - Nhấp nút `btnSum`.
* **Thêm Checkpoint xác minh nhãn báo lỗi:**
  ```groovy
  String errText = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Calculator/lblError'), 'Name') ?: Windows.getText(findWindowsObject('Object Repository/MiniSum/Calculator/lblError'))
  assert errText == 'A ngoai mien [-99, 99]' : "Lỗi không đúng: ${errText}"
  KeywordUtil.logInfo(" Bonus Checkpoint PASS: ${errText}")
  ```

---

## 7. Hướng Dẫn Xuất Báo Cáo & Nộp Bài (3 Phút)

Sinh viên nộp minh chứng kết quả bằng 1 trong 2 cách đơn giản sau:

### Cách 1: Chụp màn hình kết quả PASSED (Nhanh nhất)
1. Trên giao diện Katalon Studio, mở tab **Log Viewer** sau khi chạy xong Bài 1 và Bài 2 (hiện chữ **PASSED màu xanh**).
2. Chụp toàn bộ màn hình desktop bao gồm:
   - Cây thư mục bên trái thấy rõ tên Test Case mang MSSV của bạn (`TC_Login_<MSSV>`).
   - Màn hình Log Viewer hiển thị các dòng ` Checkpoint PASS`.
3. Lưu ảnh với tên `<MSSV>_Katalon_Lab.png` và gửi nộp.

### Cách 2: Xuất HTML Report từ Katalon
1. Trong cửa sổ dự án Katalon, mở thư mục `Reports/`.
2. Mở file `report.html` gần nhất bằng trình duyệt Chrome/Edge.
3. Xuất file PDF hoặc nén file HTML nộp cho Trợ giảng.

---

## 8. Bảng Xử Lý Sự Cố Thường Gặp (Troubleshooting)

| Vấn đề gặp phải | Nguyên nhân | Cách khắc phục ngay lập tức |
|---|---|---|
| **Lỗi `Application not found`** | Đường dẫn `appPath` bị sai hoặc không tồn tại trên máy bạn. | Copy chính xác đường dẫn file `MiniSum.exe` trên máy bạn. Dùng dấu gạch chéo `/` (ví dụ `C:/KTPM/.../MiniSum.exe`) thay vì `\` để tránh lỗi escape. |
| **Lỗi `Cannot find element...`** | Chưa copy đủ thư mục `Object Repository` hoặc tên đối tượng bị lệch. | Kiểm tra cây `Object Repository/MiniSum` trong Katalon. Đảm bảo đã copy từ `demo-scripts/katalon/Object Repository` của repo đã clone. |
| **Ứng dụng không bật lên được** | Máy thiếu thư viện nền tảng .NET 8 Desktop Runtime. | Cài đặt nhanh **.NET 8 Desktop Runtime (x64)** từ link Microsoft mục 1.1. |
| **Katalon báo lỗi cổng 4723** | FlaUI WebDriver đang bị kẹt tiến trình cũ trong bộ nhớ. | Mở Task Manager (Ctrl + Shift + Esc) $\to$ Tìm tiến trình `FlaUI.WebDriver.exe` hoặc `WinAppDriver.exe` $\to$ End Task $\to$ Chạy lại Katalon. |

<p class="table-caption"><b>Bảng 9.2:</b> <i>Bảng tổng hợp các lỗi kỹ thuật thường gặp và hướng xử lý nhanh tại lớp</i></p>

