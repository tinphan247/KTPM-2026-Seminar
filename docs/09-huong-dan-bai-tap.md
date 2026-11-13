# Bài Thực Hành Katalon Studio — Từ Clone Đến Hoàn Thành

**Seminar:** Automation Testing for Desktop Applications · **Nhóm 02 (ZipTool)**  
**Ứng dụng mẫu:** MiniSum (WinForms/C#, tài khoản demo `admin / 1234`)  
**Công cụ:** Katalon Studio 11.x — bản Free (track chính) · WinAppDriver (track B, tùy chọn)

| Hạng mục | Nội dung |
|---|---|
| Thời lượng trên lớp | 90 phút (15' chuẩn bị máy + 20' bài 1 + 45' bài 2 + 10' nộp) |
| Bài 3 | Làm ở nhà, nộp cùng đợt |
| Hình thức | Cá nhân, mỗi sinh viên một project Katalon |
| Nộp bài | 1 file `.zip` gồm project + HTML report + Excel (xem mục 9) |
| Cần chuẩn bị trước | Mục 1 — làm ở nhà, **không làm trong giờ lab** |

---

## 0. Bản đồ buổi lab

| Thời gian | Việc cần làm | Kết quả |
|---|---|---|
| Trước buổi | Cài .NET Runtime, Katalon, clone repo, tạo project, sửa đường dẫn | Mở được `TC01_Login_Success` và chạy PASS |
| 0–15' | Chạy thử `TC01` (bản demo) để xác nhận môi trường | Log có `TC01 PASSED` |
| 15–35' | **Bài 1** — TC01 của bạn + TC02 đăng nhập sai | 2 test case PASS |
| 35–75' | **Bài 2** — Excel 6 ca BVA + Data Binding | Suite chạy 6/6 PASS |
| 75–85' | Xuất report, nén bài, tự kiểm theo checklist | File `.zip` sẵn sàng nộp |
| Về nhà | **Bài 3** — bảo trì khi `btnSum` → `btnCalculate` | Report trước/sau + 5–7 dòng phân tích |

> **Quy tắc 5 phút:** kẹt một lỗi quá 5 phút thì giơ tay gọi trợ giảng. Trong 90 phút, thời gian dành cho tư duy kiểm thử quan trọng hơn thời gian dò lỗi môi trường.

---

## 1. Chuẩn bị máy (làm ở nhà, ~30 phút)

### 1.1. Yêu cầu

| Thứ cần | Chi tiết | Cách kiểm tra |
|---|---|---|
| Windows 10/11 64-bit | Bắt buộc — Katalon Windows engine chỉ chạy trên Windows | Settings → System → About |
| **.NET 8 Desktop Runtime (x64)** | Bắt buộc để chạy `MiniSum*.exe` | Nháy đúp `MiniSum_v3.exe`, thấy cửa sổ **MiniSum - Dang nhap** |
| Katalon Studio 11.x (Free) | Tải tại <https://katalon.com/download> | Help → About |
| Tài khoản Katalon | Miễn phí, kích hoạt online ở lần mở đầu tiên | Mở Katalon, đăng nhập thành công |
| Git (hoặc trình giải nén) | `git --version` | Chạy được lệnh ở mục 2 |
| Dung lượng trống | ≥ 5 GB | Ổ cài Katalon |

### 1.2. Cài .NET 8 Desktop Runtime

1. Vào <https://dotnet.microsoft.com/download/dotnet/8.0>.
2. Tải **.NET Desktop Runtime 8.x** → chọn **Windows x64** → cài.
3. Mở `MiniSum_v3.exe`. Nếu hiện hộp thoại *"To run this application, you must install .NET"* thì runtime chưa đúng — cài lại bản **Desktop** (không phải Console/ASP.NET).

> Đây là lỗi phổ biến nhất của buổi lab: `MiniSum.exe` chỉ nặng ~170 KB vì nó **không** mang theo runtime. Thiếu .NET 8 Desktop Runtime thì test case sẽ báo *application not found* hoặc ứng dụng không mở.

### 1.3. Cài Katalon Studio

1. Cài Katalon Studio 11.x (bản Free) với quyền mặc định — **không cần** quyền admin, **không cần** bật Developer Mode (khác WinAppDriver).
2. Mở Katalon → đăng nhập bằng tài khoản Katalon. Lần đầu cần mạng để kích hoạt; sau đó dùng offline được.
3. Nếu công ty/trường chặn tải file `.exe`, tải trước ở nhà rồi copy sang máy lab.

### 1.4. Checklist "máy đã sẵn sàng"

- [ ] `MiniSum_v3.exe` mở được, thấy tiêu đề **MiniSum - Dang nhap**
- [ ] Katalon Studio mở được, đã đăng nhập
- [ ] `git --version` chạy được
- [ ] Còn ≥ 5 GB đĩa trống
- [ ] Đường dẫn làm việc **không dấu, không khoảng trắng** (ví dụ `C:\KTPM\`) — tránh `C:\Users\Nguyễn Văn A\...`

---

## 2. Bước 1 — Clone repo và kiểm tra ứng dụng (5 phút)

Mở **PowerShell** tại thư mục bạn muốn làm việc (ví dụ `C:\KTPM`):

```powershell
git clone https://github.com/tinphan247/KTPM-2026-Seminar.git
cd KTPM-2026-Seminar
dir case-study-app\*.exe
```

Kết quả mong đợi — đúng **3 file**:

```text
MiniSum.exe       MiniSum_v2.exe    MiniSum_v3.exe
```

Kiểm tra nhanh: nháy đúp `MiniSum_v3.exe` → cửa sổ đăng nhập hiện ra → đóng lại.

| Phiên bản | Khác biệt | Dùng cho |
|---|---|---|
| `MiniSum.exe` (v1) | `btnSum`, không có `lblError` | Bài 1 (tùy chọn — màn hình Login giống hệt v3) |
| `MiniSum_v2.exe` | `btnSum` → **`btnCalculate`**, thêm màn hình Lịch sử | Bài 3 |
| `MiniSum_v3.exe` | giữ `btnSum`, thêm `lblError` + validation | Bài 1, Bài 2 |

> **Không dùng git?** Vào trang GitHub → **Code → Download ZIP** → giải nén ra `C:\KTPM\`. Đừng chạy `.exe` trực tiếp từ trong file ZIP — Windows sẽ giải nén vào thư mục tạm và Katalon không tìm thấy đường dẫn.

---

## 3. Bước 2 — Tạo project Katalon và nạp starter (10 phút)

### 3.1. Vì sao phải tạo project mới

Repo **không chứa** file `.project` / `.settings` của Katalon (đã bị `.gitignore` loại ra để tránh xung đột máy cá nhân). Vì vậy bạn không mở thẳng thư mục `demo-scripts/katalon/` bằng *Open Project* được. Cách chuẩn: tạo project rỗng rồi **copy các thư mục nội dung** vào.

### 3.2. Các bước

1. Katalon Studio → **File → New → Project…** (hoặc **Create new project** ở màn hình Welcome).
2. Điền:
   * **Name:** `MiniSumLab`
   * **Location:** `C:\KTPM\Katalon` (thư mục cha, không dấu)
   * Loại project: để mặc định (Blank/Generic) → **Create**.
3. Đóng các project mẫu Katalon tự mở (nếu có).
4. Mở thư mục project vừa tạo bằng File Explorer (chuột phải project → **Open Containing Folder**).
5. Copy **7 thư mục** dưới đây từ `KTPM-2026-Seminar\demo-scripts\katalon\` vào thư mục project, chọn **Replace/Merge** khi được hỏi:

| Thư mục | Nội dung nhận được |
|---|---|
| `Object Repository` | 13 đối tượng Windows của MiniSum (`txtUser`, `btnSubmit`, `lblMessage`, `txtA`, `btnSum`, `lblError`, …) |
| `Test Cases` | 3 test case mẫu `TC01`–`TC03` (dùng để đối chiếu, xem mục 5) |
| `Keywords` | Custom Keyword `LoginKeyword.groovy` (hàm đăng nhập/tính tổng có explicit wait) |
| `Test Suites` | `BVA_TestSuite` đã cấu hình Data Binding |
| `Test Data` | `BVA_TestData.xlsx` — 12 ca BVA mẫu |
| `Data Files` | `BVA_TestData.dat` — khai báo nguồn dữ liệu trỏ tới file Excel trên |
| `Test Listeners` | `ScreenshotOnFailure.groovy` — tự chụp ảnh khi test FAIL |

6. Quay lại Katalon, chọn project → nhấn **F5** (Refresh).
7. Kiểm tra cây thư mục: `Test Cases` có 3 file, `Object Repository/MiniSum` có 2 nhánh `Login` và `Calculator`.

> **Gặp lỗi khi mở project?** Xem mục 8 — "Katalon không nhận project".

### 3.3. Chạy thử bản demo để xác nhận môi trường

1. Mở `Test Cases/TC01_Login_Success`.
2. Bấm **▶ Run** và chọn platform **Windows** (không chọn Chrome/Firefox).
3. Lần chạy đầu mất 30–90 giây vì Katalon khởi động FlaUI WebDriver (cổng 4723).
4. Kết quả đúng: tab **Log** có dòng `TC01 PASSED: ...`, tab **Status** hiện **PASSED**.

Nếu bước này FAIL → **đừng làm bài 1**, xử lý theo mục 8 trước.

---

## 4. Bước 3 — Trỏ đường dẫn ứng dụng về máy bạn (5 phút)

Ba test case mẫu đang trỏ tới đường dẫn máy của người viết demo
(`D:\KAN\N4_1\...`), nên trên máy bạn chúng sẽ FAIL với lỗi không tìm thấy file.

Sửa dòng khai báo `String appPath = ...` ở đầu mỗi file:

| File cần sửa | Đổi thành |
|---|---|
| `Test Cases/TC01_Login_Success.groovy` | `MiniSum_v3.exe` (hoặc `MiniSum.exe`) |
| `Test Cases/TC02_Login_Failed.groovy` | `MiniSum_v3.exe` |
| `Test Cases/TC03_BVA_Calculation.groovy` | `MiniSum_v3.exe` |

Trước:

```groovy
String appPath = 'D:\\KAN\\N4_1\\semina\\KTPM-2026-Seminar\\case-study-app\\MiniSum_v3.exe'
```

Sau (dùng dấu `/` cho khỏi phải nhân đôi `\\`):

```groovy
String appPath = 'C:/KTPM/KTPM-2026-Seminar/case-study-app/MiniSum_v3.exe'
```

Nhấn **Ctrl + S** sau mỗi file, rồi chạy lại `TC01` để xác nhận PASS.

> Nếu vẫn dùng `\`, mỗi dấu phải viết đôi: `'C:\\KTPM\\KTPM-2026-Seminar\\case-study-app\\MiniSum_v3.exe'`. Sai chỗ này là nguyên nhân số 2 khiến test case không khởi động được ứng dụng.

---

## 5. Bài 1 — Đăng nhập và Checkpoint (20 phút)

### 5.1. Yêu cầu

Tạo **test case của bạn** (không nộp lại bản demo), tên có MSSV:

* `TC01_Login_<MSSV>`: đăng nhập thành công + checkpoint nhãn `lblMessage`.
* `TC02_LoginFail_<MSSV>`: đăng nhập sai mật khẩu + checkpoint thông báo lỗi.

### 5.2. Các bước

1. Chuột phải `Test Cases` → **New → Test Case**, đặt tên `TC01_Login_<MSSV>`.
2. Trong test case mới, thêm lần lượt các bước (Manual view hoặc Script view):

| # | Hành động | Đối tượng | Dữ liệu |
|---|---|---|---|
| 1 | Start Application With Title | — | `appPath` của bạn, title `MiniSum - Dang nhap` |
| 2 | Switch To Window Title | — | `MiniSum - Dang nhap` |
| 3 | Set Text | `Object Repository/MiniSum/Login/txtUser` | `admin` |
| 4 | Send Keys | `Object Repository/MiniSum/Login/txtPass` | `1234` |
| 5 | Click | `Object Repository/MiniSum/Login/btnLogin` | — |
| 6 | **Checkpoint** | `Object Repository/MiniSum/Login/lblMessage` | `Dang nhap thanh cong` |

3. Ở bước 6, dán đoạn checkpoint sau vào cuối Script view (đã kiểm chứng chạy được — UIA đọc chữ của Label qua thuộc tính `Name`):

```groovy
String msg = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'), 'Name') ?: Windows.getText(findWindowsObject('Object Repository/MiniSum/Login/lblMessage'))
assert msg == 'Dang nhap thanh cong' : "Kỳ vọng 'Dang nhap thanh cong', nhận '${msg}'"
```

Nếu Script view báo `unable to resolve class Windows`, thêm 2 dòng import lên đầu file:

```groovy
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
```

> **Manual view:** thêm keyword **Verify Element Text**, chọn object `lblMessage`, text `Dang nhap thanh cong`. Nếu bước này FAIL dù màn hình hiện đúng chữ, quay lại cách dán script ở trên — một số bản Katalon đọc text của WinForms Label không ổn định.

4. Chạy test case (▶ → **Windows**). Kết quả cần đạt: **PASSED**.

### 5.3. Tạo TC02 (đăng nhập sai)

1. Chuột phải `TC01_Login_<MSSV>` → **Duplicate** → đổi tên `TC02_LoginFail_<MSSV>`.
2. Sửa mật khẩu thành `wrong123`.
3. Sửa checkpoint: kỳ vọng `Sai tai khoan hoac mat khau` thay vì `Dang nhap thanh cong`.
4. Chạy → **PASSED**.

> Sau khi đăng nhập sai, ứng dụng **xoá trắng ô mật khẩu**. Đây là chi tiết UX có thể kiểm thêm (nếu làm được, ghi vào phần mở rộng — không bắt buộc).

### 5.4. Vì sao phải có checkpoint

Không có checkpoint, test chỉ chứng minh "đã bấm được nút", không chứng minh "hệ thống trả về đúng kết quả". Checkpoint chính là **Test Oracle** — phần quyết định một ca kiểm thử có ý nghĩa hay không.

### 5.5. Lưu ý về thời gian chuyển màn hình

Sau khi đăng nhập thành công, MiniSum giữ màn hình Login thêm **1 giây** (`SuccessDelayMs = 1000`) rồi mới mở cửa sổ Tính tổng. Vì vậy:

* Không dùng `Thread.sleep(5000)` cứng — vừa chậm vừa dễ flaky.
* Dùng `Windows.waitForElementPresent(..., 10)` hoặc `switchToWindowTitle('MiniSum - Tinh tong')` — Katalon tự chờ tối đa 10 giây.

### 5.6. Kết quả mong đợi của bài 1

| Kiểm tra | Đạt khi |
|---|---|
| `TC01_Login_<MSSV>` | PASSED, checkpoint đọc đúng `Dang nhap thanh cong` |
| `TC02_LoginFail_<MSSV>` | PASSED, checkpoint đọc đúng `Sai tai khoan hoac mat khau` |
| Bằng chứng | HTML report của lần chạy cuối, cả 2 case PASS |

---

## 6. Bài 2 — Data-Driven Testing với BVA (45 phút)

### 6.1. Yêu cầu

Trên `MiniSum_v3.exe`, kiểm thử chức năng tính tổng `A + B` với `A, B ∈ [-99, 99]` bằng bộ dữ liệu Excel, chạy tự động toàn bộ trong một lần.

**6 ca bắt buộc** (tối thiểu — có thể thêm):

| # | A | B | Expected | Loại ca | Kỳ vọng trên giao diện |
|---|---|---|---|---|---|
| 1 | `-99` | `9` | `-90` | Biên dưới hợp lệ của A | `Ket qua: -99 + 9 = -90` |
| 2 | `99` | `9` | `108` | Biên trên hợp lệ của A | `Ket qua: 99 + 9 = 108` |
| 3 | `-100` | `9` | `LOI` | Ngoài biên dưới của A | `A ngoai mien [-99, 99]` |
| 4 | `100` | `9` | `LOI` | Ngoài biên trên của A | `A ngoai mien [-99, 99]` |
| 5 | `xyz` | `10` | `LOI` | Sai kiểu dữ liệu | `Gia tri khong hop le: phai la so nguyen` |
| 6 | `10` | `-99` | `-89` | Biên dưới hợp lệ của B | `Ket qua: 10 + -99 = -89` |

Quy ước: `Expected` là **số** → kiểm tra `lblResult`; `Expected` là **`LOI`** → kiểm tra `lblError` khác rỗng.

### 6.2. Tạo file dữ liệu

**Cách nhanh (khuyến nghị):** mở `Test Data/BVA_TestData.xlsx` trong project, sửa sheet tên **`BVA_TestData`** (giữ nguyên tên sheet) thành 6 dòng của bạn, giữ nguyên dòng tiêu đề:

| TC_ID | A | B | Expected | Description |
|---|---|---|---|---|
| TC01 | -99 | 9 | -90 | Biên dưới A hợp lệ |
| TC02 | 99 | 9 | 108 | Biên trên A hợp lệ |
| TC03 | -100 | 9 | LOI | Ngoài biên dưới A |
| TC04 | 100 | 9 | LOI | Ngoài biên trên A |
| TC05 | xyz | 10 | LOI | Sai kiểu dữ liệu |
| TC06 | 10 | -99 | -89 | Biên dưới B hợp lệ |

Lưu ý khi nhập Excel:

* Cột `A`, `B`, `Expected` phải là **Text** (định dạng ô *Text* hoặc thêm dấu `'` đầu ô) để Excel không tự đổi `-99` thành công thức hay `10` thành `10.0`.
* **Đóng file Excel** trước khi chạy test — Katalon không đọc được file đang mở bởi Excel.
* Không đổi tên sheet nếu dùng lại `Data Files/BVA_TestData` (file `.dat` đã trỏ tới sheet `BVA_TestData`).

**Cách đầy đủ (nếu muốn giữ nguyên bộ 12 ca mẫu):** `Data Files` → chuột phải → **New → Test Data** → chọn **Excel File** → trỏ tới file Excel của bạn → đặt tên `MyBVA` → chọn sheet → sau đó thay nguồn dữ liệu trong Test Suite (bước 6.4).

### 6.3. Tạo test case có tham số

Cách nhanh nhất: **Duplicate** `TC03_BVA_Calculation` thành `TC03_BVA_<MSSV>` rồi sửa `appPath` (mục 4). Test case này đã khai báo 3 biến `A`, `B`, `Expected` và logic rẽ nhánh số/`LOI`.

Nếu tự viết, phần kiểm tra kết quả có dạng:

```groovy
if (Expected.toString().trim().equalsIgnoreCase('LOI')) {
    String err = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Calculator/lblError'), 'Name')
    assert err != null && !err.trim().isEmpty() : 'Kỳ vọng có thông báo lỗi nhưng lblError rỗng'
} else {
    String expected = "Ket qua: ${A} + ${B} = ${Expected}"
    String actual = Windows.getAttribute(findWindowsObject('Object Repository/MiniSum/Calculator/lblResult'), 'Name')
    assert actual == expected : "Kỳ vọng '${expected}', nhận '${actual}'"
}
```

Biến `A`, `B`, `Expected` khai báo ở tab **Variables** của Test Case (Add → name `A` / `B` / `Expected`, default `'0'`).

### 6.4. Cấu hình Data Binding trong Test Suite

1. Chuột phải `Test Suites` → **New → Test Suite**, đặt tên `BVA_<MSSV>`.  
   *(Hoặc chuột phải `BVA_TestSuite` → **Duplicate** → đổi tên, nhanh hơn.)*
2. Thêm test case `TC03_BVA_<MSSV>` vào suite.
3. Mở test suite, chuyển sang tab **Data Binding** (thanh dưới cùng cửa sổ) → **Add Test Data** → chọn `Data Files/BVA_TestData` (hoặc `MyBVA` nếu bạn tạo mới).
4. Ở bảng **Variable Binding**, map ba biến:

| Variable | Bind to column |
|---|---|
| `A` | `A` |
| `B` | `B` |
| `Expected` | `Expected` |

5. Nhấn **Ctrl + S**, sau đó chạy ở cấp **Test Suite**: **▶ Run → Windows**.

> Chạy ở cấp Test Case sẽ **không** áp dụng dữ liệu — chỉ chạy 1 lần với biến mặc định. Đây là lỗi phổ biến nhất của bài 2.

### 6.5. Đọc kết quả

| Nơi xem | Cần thấy |
|---|---|
| Tab **Log** | 6 dòng `PASS [A, B] -> ...` |
| Tab **Report** | 6 dòng dữ liệu, cột Status = PASSED |
| Thư mục `Reports/` | Thư mục có `report.html` + ảnh (nếu fail) |

Mở `report.html` bằng trình duyệt: header phải hiện **6 Test Cases / 6 Passed / 0 Failed**.

### 6.6. Phần mở rộng (cộng vào điểm trình bày, không bắt buộc)

Thêm 2 ca do bạn tự nghĩ, ví dụ:

| A | B | Expected | Ý tưởng |
|---|---|---|---|
| `99` | `-99` | `0` | Hai biên chéo nhau (tổng bằng 0) |
| `10` | `100` | `LOI` | Ngoài biên trên của B → `B ngoai mien [-99, 99]` |

> Tránh dùng ô **trống** trong Excel cho A hoặc B: Katalon trả về `null`, và dòng `A.toString()` trong test case sẽ lỗi `NullPointerException` — fail vì lý do kỹ thuật chứ không phải vì phát hiện lỗi. Nếu muốn kiểm ca bỏ trống, hãy viết một test case riêng, không dùng chung bộ dữ liệu này.

### 6.7. Kết quả mong đợi của bài 2

* File Excel của bạn có ≥ 6 ca, đúng cấu trúc cột.
* Test Suite chạy **6/6 PASSED** trong một lần bấm Run.
* HTML report thể hiện kết quả **từng dòng dữ liệu** (không phải một dòng tổng).

---

## 7. Bài 3 — Bảo trì kịch bản khi giao diện thay đổi (về nhà)

### 7.1. Tình huống

Nhà phát triển phát hành `MiniSum_v2.exe`: nút tính tổng đổi `AutomationId` từ `btnSum` sang **`btnCalculate`** (nhãn trên nút vẫn là `TINH TONG`), thêm màn hình Lịch sử. Không có thông báo trước.

### 7.2. Tái hiện lỗi

1. Đổi `appPath` trong `TC03_BVA_<MSSV>` sang `MiniSum_v2.exe`.
2. **Lưu ý dữ liệu:** v2 **không có** `lblError`, nên các ca `Expected = LOI` không thể PASS trên v2. Hãy sửa sheet `BVA_TestData` thành bộ **4 ca hợp lệ** (hoặc tạo Data File `BVA_v2_Valid` riêng):

| A | B | Expected |
|---|---|---|
| -99 | 9 | -90 |
| 99 | 9 | 108 |
| 0 | 0 | 0 |
| 10 | -99 | -89 |

3. Chạy suite → **FAIL toàn bộ** với lỗi dạng *element not found / no such element* tại bước click nút tính tổng.

> Chạy thêm `TC01`, `TC02` trên v2: cả hai vẫn **PASS** vì màn hình đăng nhập không đổi. Đây là bằng chứng cho thấy lỗi khu trú đúng ở locator nút tính tổng, không phải môi trường.

4. Chụp lại màn hình log lỗi và ghi rõ: bước nào fail, thông điệp gì.

### 7.3. Phân tích nguyên nhân gốc

| Câu hỏi | Trả lời cần đạt |
|---|---|
| Test fail ở bước nào? | Bước click nút `btnSum` |
| Vì sao? | `AutomationId` đổi thành `btnCalculate`, object cũ không còn tồn tại |
| Có phải lỗi logic kiểm thử? | Không — là **thay đổi giao diện**, test đúng nhưng locator cũ |
| Sửa ở đâu cho đúng? | Tại **một chỗ**: Object Repository, không sửa test case |

### 7.4. Sửa và chạy lại

1. Mở `Object Repository/MiniSum/Calculator/btnSum` (double-click).
2. Sửa giá trị **AutomationId** từ `btnSum` → **`btnCalculate`**.
3. **Không** sửa bất kỳ dòng nào trong test case. Lưu (Ctrl + S).
4. Chạy lại suite → **4/4 PASSED**.

> Nếu sửa file bằng tay: `Object Repository/MiniSum/Calculator/btnSum.wrs`, đổi `<value>btnSum</value>` thành `<value>btnCalculate</value>` trong khối `AutomationId`.
>
> **Nhớ đổi lại `btnSum` khi quay về `MiniSum_v3`.** Object Repository dùng chung cho cả project — đây chính là mặt trái của "một locator dùng nhiều nơi", và là lý do trong thực tế người ta tách OR theo phiên bản hoặc dùng locator động.

### 7.5. Câu hỏi lý thuyết (5–7 dòng)

> Vì sao quản lý locator tập trung (Object Repository / Page Object Model) giúp giảm chi phí bảo trì so với gán cứng locator trong từng kịch bản? Liên hệ với **"Nghịch lý thuốc trừ sâu"** (Pesticide Paradox).

Gợi ý ý chính: một thay đổi UI → một điểm sửa; gán cứng → sửa N kịch bản, dễ sót; Pesticide Paradox: bộ test lặp lại mãi sẽ hết khả năng phát hiện lỗi mới, nên bộ test cần được cập nhật — và cấu trúc locator tốt làm việc cập nhật đó rẻ đi.

### 7.6. Nộp gì cho bài 3

* Ảnh chụp log lỗi **trước** khi sửa (thấy rõ element not found).
* HTML report **sau** khi sửa: 4/4 PASSED.
* Đoạn trả lời 5–7 dòng.

---

## 8. Sự cố thường gặp

| Hiện tượng | Nguyên nhân | Cách xử lý |
|---|---|---|
| `Application not found` / không mở được MiniSum | Sai `appPath`, hoặc thiếu .NET 8 Desktop Runtime | Kiểm tra đường dẫn tồn tại; cài **.NET Desktop Runtime 8 x64** |
| `Unable to start... FlaUI` / timeout cổng 4723 | Windows driver chưa bật | Chạy lại Katalon; hoặc mở `Test Listeners/ScreenshotOnFailure.groovy` và sửa `flauiPath` theo máy bạn (`C:\Users\<TênBạn>\.katalon\packages\KS-<phiên bản>\configuration\resources\extensions\FlaUIWebDriver\FlaUI.WebDriver.exe`) |
| Test PASS nhưng không thấy ứng dụng | Cửa sổ MiniSum đang bị che / thu nhỏ | Để cửa sổ hiện trên màn hình khi chạy; không khoá màn hình |
| `Element not found: lblMessage` | Đọc text sai cách trên WinForms Label | Dùng `getAttribute(obj, 'Name')` như snippet mục 5.2 |
| Đăng nhập fail dù đúng mật khẩu | `Send Keys` gõ thiếu do ô password | Dùng `sendKeys` (không `setText`) cho `txtPass`, thêm `waitForElementPresent` trước |
| Suite chạy 1 lần, không lặp theo dữ liệu | Bind sai cấp (Test Case thay vì Test Suite) hoặc chưa map biến | Chạy ở cấp **Test Suite**, kiểm tra bảng **Variable Binding** |
| Report chỉ 1 dòng | Chưa bật Data Binding, hoặc file Excel chỉ có 1 dòng dữ liệu | Kiểm tra `Data Files` trỏ đúng file + sheet; đếm số dòng có dữ liệu |
| Lỗi đọc Excel / `NullPointerException` | File Excel đang mở, hoặc cột bị đổi định dạng | Đóng Excel; đặt cột A/B/Expected là Text |
| Katalon không nhận project (`Open Project` báo lỗi) | Thiếu `.project` (bị gitignore) | Tạo project mới rồi copy 7 thư mục (mục 3.2) |
| Mở project thấy thiếu test case | Chưa F5, hoặc copy sai cấp thư mục | Copy đúng `Object Repository`, `Test Cases`… vào **gốc** project, rồi F5 |
| Chạy lại v3 nhưng vẫn lỗi sau bài 3 | Đã đổi OR sang `btnCalculate` | Đổi lại `btnSum` hoặc tách OR cho từng phiên bản |

---

## 9. Nộp bài

### 9.1. Cấu trúc file nộp

Đặt tên: **`MSSV_HoTen_BaiTapKatalon.zip`**

```text
MSSV_HoTen_BaiTapKatalon/
├─ MiniSumLab/                  # thư mục project Katalon (đã có Test Cases, Object Repository, Test Suites)
├─ Reports/                     # copy từ MiniSumLab/Reports — HTML report của lần chạy cuối
├─ BVA_TestData.xlsx            # bản sao file dữ liệu bài 2
├─ bai3_truoc_khi_sua.png       # log lỗi trên MiniSum_v2
├─ bai3_sau_khi_sua.png         # report 4/4 PASS sau khi sửa OR
└─ bai3_phan_tich.md            # 5–7 dòng trả lời câu hỏi lý thuyết
```

Report nằm trong `<project>/Reports/<tên test suite>/<timestamp>/report.html` — mở bằng trình duyệt để kiểm tra trước khi nộp.

### 9.2. Quy định chấm

* Giảng viên **mở lại project và chạy** — report nộp kèm phải khớp với lần chạy lại; sai lệch tính là không đạt.
* Không nộp file Excel đang mở, không nộp report rỗng, không nộp test case mẫu `TC01`–`TC03` nguyên bản.
* Tên test case phải có MSSV để đối chiếu.

### 9.3. Barem tóm tắt

| Hạng mục | Điểm | Yêu cầu tối thiểu |
|---|---|---|
| Bài 1 | 3.0 | Mở app + đăng nhập đúng; checkpoint `lblMessage` PASS; có ca đăng nhập sai |
| Bài 2 | 4.0 | Excel ≥ 6 ca đúng BVA; binding và chạy 6/6; xử lý đúng cả nhánh số và `LOI` |
| Bài 3 | 3.0 | Phân tích đúng nguyên nhân; sửa locator tập trung; report trước/sau; trả lời lý thuyết |
| Track B (tùy chọn) | +0.5 | Cùng đề, làm bằng WinAppDriver + Page Object, chạy được `dotnet test`; tổng không vượt 10 |

---

## 10. Checklist trước khi nộp

- [ ] Project mở được trên máy khác (đã thử copy sang thư mục khác và mở lại)
- [ ] `TC01_Login_<MSSV>` PASS, checkpoint đọc đúng `Dang nhap thanh cong`
- [ ] `TC02_LoginFail_<MSSV>` PASS, checkpoint đọc đúng `Sai tai khoan hoac mat khau`
- [ ] Excel có ≥ 6 ca, cột `A`, `B`, `Expected` đúng định dạng
- [ ] Suite chạy 6/6 (hoặc nhiều hơn nếu thêm ca), report hiện từng dòng
- [ ] Bài 3: có ảnh log lỗi trước, report PASS sau, đoạn phân tích 5–7 dòng
- [ ] Không còn đường dẫn `D:\KAN\...` trong bất kỳ test case nào
- [ ] File `.zip` đặt đúng tên `MSSV_HoTen_BaiTapKatalon.zip`

---

## Phụ lục A — AutomationId và thông điệp của MiniSum

| Màn hình | Control | AutomationId | Ghi chú |
|---|---|---|---|
| Login | Window | `winLogin` | Title: `MiniSum - Dang nhap` |
| Login | Tài khoản | `txtUser` | `admin` |
| Login | Mật khẩu | `txtPass` | `1234`; dùng `sendKeys` |
| Login | Nút đăng nhập | `btnLogin` | OR đặt tên `btnSubmit` nhưng trỏ tới `btnLogin` |
| Login | Thông báo | `lblMessage` | Đọc qua `getAttribute(..., 'Name')` |
| Calculator | Window | `winMain` | Title: `MiniSum - Tinh tong` |
| Calculator | Số A / Số B | `txtA` / `txtB` | Số nguyên ∈ [-99, 99] |
| Calculator | Nút tính tổng | `btnSum` (v1, v3) / `btnCalculate` (v2) | Nhãn `TINH TONG` |
| Calculator | Kết quả | `lblResult` | Dạng `Ket qua: A + B = C` |
| Calculator | Lỗi | `lblError` | Chỉ có ở v3 |
| Calculator | Đăng xuất | `btnLogout` | Quay về màn hình Login |

Thông điệp (ASCII, không dấu — so sánh đúng từng ký tự):

| Tình huống | Chuỗi |
|---|---|
| Đăng nhập đúng | `Dang nhap thanh cong` |
| Sai tài khoản/mật khẩu | `Sai tai khoan hoac mat khau` |
| Bỏ trống cả hai | `Vui long nhap tai khoan va mat khau` |
| Bỏ trống tài khoản | `Ten dang nhap khong duoc de trong` |
| Bỏ trống mật khẩu | `Mat khau khong duoc de trong` |
| A/B ngoài miền | `A ngoai mien [-99, 99]` · `B ngoai mien [-99, 99]` |
| Không phải số nguyên | `Gia tri khong hop le: phai la so nguyen` |
| Bỏ trống A hoặc B | `Vui long nhap day du gia tri A va B` |

## Phụ lục B — Cấu trúc starter project

```text
demo-scripts/katalon/
├─ Object Repository/MiniSum/
│  ├─ Login/      winLogin, txtUser, txtPass, btnLogin, btnSubmit, lblMessage
│  └─ Calculator/ winMain, txtA, txtB, btnSum, lblResult, lblError, btnLogout
├─ Test Cases/    TC01_Login_Success, TC02_Login_Failed, TC03_BVA_Calculation
├─ Keywords/      com/minisum/keywords/LoginKeyword.groovy
├─ Test Suites/   BVA_TestSuite (đã bind Data Files/BVA_TestData)
├─ Test Data/     BVA_TestData.xlsx (12 ca mẫu)
├─ Data Files/    BVA_TestData.dat (trỏ tới Test Data/BVA_TestData.xlsx)
└─ Test Listeners/ ScreenshotOnFailure.groovy
```

`TC01`–`TC03` là **bản demo của nhóm** để bạn đối chiếu cách làm và kiểm tra môi trường — bài nộp phải là test case do bạn tạo, có MSSV trong tên.

## Phụ lục C — Keyword Windows hay dùng

| Keyword | Dùng khi nào |
|---|---|
| `startApplicationWithTitle(path, title)` | Mở ứng dụng desktop |
| `switchToWindowTitle(title)` | Chuyển giữa các cửa sổ |
| `setText(obj, text)` | Nhập vào TextBox thường |
| `sendKeys(obj, text)` | Nhập vào ô mật khẩu, hoặc gửi phím |
| `click(obj)` | Bấm nút |
| `getAttribute(obj, 'Name')` | Đọc chữ của Label (cách ổn định nhất cho WinForms/WPF) |
| `waitForElementPresent(obj, timeout)` | Chờ phần tử xuất hiện (thay `Thread.sleep`) |
| `verifyElementPresent(obj, timeout)` | Checkpoint phần tử tồn tại |
| `takeScreenshot(path)` | Chụp bằng chứng khi fail (đã có listener tự làm) |
| `closeApplication()` | Đóng ứng dụng cuối test case |
