# Ứng Dụng Trí Tuệ Nhân Tạo (AI) Trong Desktop Automation Testing
## Chuyên đề: Automation Testing cho Desktop Applications

- **Người thực hiện:** Quang 
- **Mục tiêu báo cáo:** Nghiên cứu các xu hướng ứng dụng AI/GenAI trong kiểm thử tự động ứng dụng desktop, giải quyết các điểm nghẽn truyền thống và đề xuất phương án demo cho giai đoạn sau.

---

## 1. Bối Cảnh: Vì Sao AI Là Bước Tiến Tất Yếu Trong Desktop Automation?

Kiểm thử tự động ứng dụng Desktop truyền thống luôn đối mặt với 3 thách thức lớn:
1. **Chi phí bảo trì kịch bản quá cao (Maintenance Overhead):** Chỉ cần nhà phát triển thay đổi nhỏ về giao diện, các định danh (`AutomationId`, `XPath`) bị đứt gãy, khiến hàng loạt test case bị FAIL hàng loạt (Flaky Test).
2. **Hạn chế trong kiểm thử thị giác (Visual Testing):** Cây cấu trúc Windows UI Automation (UIA) chỉ đọc được thuộc tính logic, hoàn toàn không phát hiện được các lỗi như: tràn chữ, chữ bị che khuất, lệch màu sắc, vỡ giao diện trên các độ phân giải màn hình khác nhau.
3. **Tốn nhiều công sức chuẩn bị dữ liệu:** Việc thiết kế thủ công các bộ dữ liệu kiểm thử giá trị biên (BVA) và phân hoạch tương đương (EP) cho các form nhập liệu phức tạp tốn rất nhiều thời gian.

$\longrightarrow$ **Trí tuệ nhân tạo (AI)**, bao gồm Machine Learning, Computer Vision và Generative AI (LLMs), xuất hiện như một lời giải đột phá nhằm chuyển đổi kiểm thử từ **tự động hóa cơ học (Automated)** sang **tự động hóa thông minh (Autonomous)**.

---

## 2. Năm (5) Hướng Ứng Dụng AI Trọng Tâm Trong Desktop Automation

```
┌────────────────────────────────────────────────────────────────────────┐
│             5 HƯỚNG ỨNG DỤNG AI TRONG DESKTOP AUTOMATION               │
├───────────────────────────────────┬────────────────────────────────────┤
│ 1. AI Tự phục hồi Selector       │ 2. Kiểm thử trực quan (Visual AI)  │
│    (Self-Healing Locators)        │    (Computer Vision / OpenCV)      │
├───────────────────────────────────┼────────────────────────────────────┤
│ 3. AI Sinh kịch bản kiểm thử     │ 4. AI Sinh dữ liệu kiểm thử        │
│    (Test Script Generation)       │    (Synthetic Test Data)           │
├───────────────────────────────────┴────────────────────────────────────┤
│ 5. Phân tích nguyên nhân lỗi tự động (Root Cause Analysis)             │
└────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Tự phục hồi phần tử định vị (AI-powered Self-Healing Locators)
* **Vấn đề giải quyết:** Khắc phục tình trạng script bị gãy khi lập trình viên đổi tên ID, thay đổi cấu trúc cây giao diện hoặc cập nhật phiên bản app mới.
* **Nguyên lý hoạt động:**
  * Khi bộ định vị chính (`AutomationId` hoặc `XPath`) không tìm thấy phần tử, thay vì dừng kịch bản và báo lỗi ngay, thuật toán AI sẽ kích hoạt cơ chế tự phục hồi.
  * AI phân tích một tập hợp trọng số bao gồm: văn bản hiển thị, kích thước, vị trí tương đối so với các phần tử lân cận, hình ảnh chụp control và loại control.
  * Tự động chọn phần tử có độ tương đồng cao nhất (Confidence Score > 90%) để tiếp tục thực thi kịch bản, đồng thời ghi log đề xuất cập nhật locator mới cho tester.

### 2.2 Kiểm thử thị giác thông minh bằng Thị giác máy tính (Visual AI Testing)
* **Vấn đề giải quyết:** Thay thế kỹ thuật Bitmap Checkpoint truyền thống (vốn so sánh pixel cứng nhắc, dễ fail khi đổi độ phân giải màn hình hoặc font hệ thống).
* **Nguyên lý hoạt động:**
  * Sử dụng mạng nơ-ron tích chập (Convolutional Neural Networks - CNN) và Computer Vision (như Applitools Eyes hoặc OpenCV) để "nhìn" giao diện giống như mắt người.
  * Phân biệt được sự khác biệt không mong muốn (lỗi vỡ layout, tràn chữ, nút bấm bị che khuất) với các thay đổi bình thường (đổi độ phân giải, khử răng cưa font chữ).

### 2.3 AI tự động sinh kịch bản kiểm thử (Automated Test Script Generation)
* **Vấn đề giải quyết:** Rút ngắn thời gian viết mã kịch bản từ tài liệu yêu cầu.
* **Nguyên lý hoạt động:**
  * Sử dụng các mô hình ngôn ngữ lớn (LLMs như GPT-4, Claude) được tinh chỉnh (fine-tuned) trên các tập dữ liệu kiểm thử.
  * Nhận đầu vào là kịch bản kiểm thử viết bằng ngôn ngữ tự nhiên hoặc cú pháp BDD/Gherkin (ví dụ: *"Khi nhập A = 99 và B = 9, kết quả phải hiển thị 108"*).
  * Tự động sinh ra mã nguồn kiểm thử hoàn chỉnh: script Groovy cho Katalon Studio hoặc mã C# / NUnit cho WinAppDriver.

### 2.4 AI tự động sinh dữ liệu kiểm thử (Synthetic Test Data Generation)
* **Vấn đề giải quyết:** Tự động hóa quá trình thiết kế ca kiểm thử hộp đen.
* **Nguyên lý hoạt động:**
  * Dựa trên đặc tả miền giá trị (ví dụ: $A, B \in [-99, 99]$), AI tự động tính toán và sinh ra ma trận dữ liệu bao gồm:
    * Các ca biên hợp lệ: `[-99, 9]`, `[99, 9]`, `[10, -99]`, `[10, 99]`.
    * Các ca biên không hợp lệ (ngoại lệ): `[-100, 9]`, `[100, 9]`, chuỗi ký tự, giá trị rỗng.
  * Tự động xuất ra file Excel/CSV chuẩn để nạp trực tiếp vào kịch bản Data-Driven Testing.

### 2.5 Phân tích nguyên nhân lỗi và phân loại tự động (Root Cause Analysis)
* **Vấn đề giải quyết:** Giảm thời gian điều tra lỗi thủ công khi chạy hàng trăm test case trong CI/CD.
* **Nguyên lý hoạt động:**
  * AI đọc log thực thi, thông tin stack trace và ảnh chụp màn hình lúc FAIL.
  * Phân loại lỗi tự động: Đâu là lỗi do phần mềm (Product Bug), đâu là lỗi do môi trường mạng/treo máy (Environment Issue), đâu là kịch bản không ổn định (Flaky Script).
  * Tự động gom nhóm các ca thất bại có cùng nguyên nhân gốc để lập một báo cáo lỗi duy nhất lên hệ thống quản lý (Jira/Azure DevOps).

---

## 3. Hiện Trạng Hỗ Trợ AI Trên 2 Công Cụ Khảo Sát

| Tính năng AI | Hệ sinh thái Katalon Studio | Hệ sinh thái Microsoft WinAppDriver |
|---|---|---|
| **Sinh mã kịch bản (Code Generation)** | Tích hợp **Katalon StudioAssist** (dùng GenAI giải thích mã và sinh mã Groovy trực tiếp trong IDE). | Tích hợp các trợ lý lập trình chuẩn trong IDE: **GitHub Copilot**, **Cursor** hoặc ChatGPT trong Visual Studio. |
| **Tự phục hồi Locator (Self-Healing)** | Có sẵn cơ chế **Smart XPath & Self-Healing** (thử nghiệm các locator dự phòng theo thứ tự ưu tiên). | Không có sẵn trong core driver; có thể kết hợp thư viện ngoài (như Healenium) hoặc tự viết thuật toán fallback. |
| **Kiểm thử trực quan (Visual Testing)** | Tích hợp thông qua nền tảng đám mây **Katalon TestOps Visual Testing**. | Tích hợp với SDK của các nền tảng Visual AI chuyên dụng: **Applitools Eyes SDK for Windows**. |
| **Phân tích lỗi thông minh** | Nền tảng TestOps tự động gom nhóm lỗi và phân tích độ ổn định của test case. | Tận dụng các plugin phân tích log AI trên các nền tảng báo cáo (ReportPortal, Allure Report AI). |

---

## 4. Đề Xuất Kế Hoạch Demo AI (Dự Kiến Cho Giai Đoạn Sau)

Nhằm biến lý thuyết AI thành sản phẩm trực quan, nhóm dự kiến triển khai **2 kịch bản demo ứng dụng AI** ở giai đoạn thực hành chuyên sâu:

### Kịch bản Demo 1: GenAI tự động sinh bộ Test Script & Dữ liệu BVA từ đặc tả
* **Đầu vào:** Đưa vào tài liệu đặc tả chức năng bài toán tính tổng của ứng dụng mẫu MiniSum (mô tả yêu cầu đăng nhập và giới hạn số nguyên $[-99, 99]$).
* **Ứng dụng AI:** Dùng mô hình ngôn ngữ lớn (GenAI) với prompt chuyên biệt cho kiểm thử phần mềm.
* **Kết quả đầu ra:** 
  1. Tự động sinh ra file Excel chứa đúng danh sách 12 ca kiểm thử giá trị biên (BVA).
  2. Tự động sinh ra khung mã nguồn kiểm thử hoàn chỉnh (viết bằng C# cho WinAppDriver hoặc Groovy cho Katalon Studio).
* **Đánh giá:** Đo lường thời gian viết kịch bản giảm từ vài giờ xuống còn vài phút.

### Kịch bản Demo 2: Minh họa cơ chế tự phục hồi (Self-Healing) khi ứng dụng đổi giao diện
* **Tình huống:** Nhà phát triển cập nhật phiên bản mới của ứng dụng mẫu MiniSum, cố tình đổi `AutomationId` của nút bấm từ `btnSum` thành `btnCalculate`.
* **Kịch bản kiểm thử:**
  * *Kịch bản truyền thống:* Bị gãy và dừng ngay lập tức do lỗi `ElementNotFoundException`.
  * *Kịch bản ứng dụng AI / Self-healing:* Thuật toán phát hiện sự biến mất của ID cũ, quét cấu trúc lân cận và tự động bắt vào nút bấm mới dựa trên nhãn hiển thị và tọa độ form $\rightarrow$ Kịch bản tiếp tục chạy PASS thành công.

---

## 5. Tổng Kết: Cơ Hội & Thách Thức

* **Cơ hội:** 
  * Giảm tới 60–70% thời gian bảo trì kịch bản kiểm thử khi phần mềm thay đổi liên tục.
  * Xóa nhòa rào cản kỹ thuật giữa Manual Tester và Automation Tester thông qua ngôn ngữ tự nhiên.
* **Thách thức cần lưu ý:**
  * Hiện tượng "ảo giác" (Hallucination) của GenAI có thể sinh ra các ca kiểm thử hoặc mã code không chính xác.
  * Chi phí token bản quyền API của các mô hình AI thương mại.
  * Vấn đề bảo mật dữ liệu: Tránh đưa mã nguồn và dữ liệu nghiệp vụ nhạy cảm của doanh nghiệp lên các mô hình AI công cộng.
