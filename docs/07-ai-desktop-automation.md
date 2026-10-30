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

## 4. Kết Quả Thực Nghiệm Thực Tế Tại Nhóm (Round 2)

Nhóm 02 đã hiện thực hóa trọn vẹn kịch bản ứng dụng AI vào thực tế dự án, lưu trữ toàn bộ minh chứng tại thư mục `ai/prompts/` và `ai/output/`:

### 4.1 Thực nghiệm sinh bộ Test Case BVA tự động (Few-shot Prompting)
- **Prompt:** [`ai/prompts/testcase-bva-prompt.md`](../ai/prompts/testcase-bva-prompt.md) kèm đặc tả [`ai/prompts/minisum-spec.md`](../ai/prompts/minisum-spec.md).
- **Kết quả thực nghiệm:** Cả ChatGPT-4 ([`ai/output/chatgpt-bva-output.md`](../ai/output/chatgpt-bva-output.md)) và Gemini Advanced ([`ai/output/gemini-bva-output.md`](../ai/output/gemini-bva-output.md)) đều sinh ra chính xác 12 ca kiểm thử biên đạt độ phủ 100% các điểm biên $\{-100, -99, -98, 0, 98, 99, 100\}$.
- **Xuất file dữ liệu thực tế:** File Excel [`ai/output/bva-testcases.xlsx`](../ai/output/bva-testcases.xlsx) đã được nạp trực tiếp vào kịch bản Data-driven của cả Katalon Studio và WinAppDriver NUnit.

### 4.2 Thực nghiệm sinh mã kiểm thử C# NUnit POM tự động
- **Prompt:** [`ai/prompts/script-gen-prompt.md`](../ai/prompts/script-gen-prompt.md) yêu cầu sinh script WinAppDriver theo mẫu thiết kế Page Object Model.
- **Mã nguồn sinh ra:** [`ai/output/chatgpt-script-output.cs`](../ai/output/chatgpt-script-output.cs) đã được biên dịch và chạy kiểm thử thực tế trên `MiniSum.exe`.
- **Hiệu quả định lượng:**
  - Thời gian viết kịch bản giảm từ **130 phút xuống 29 phút** (tiết kiệm **77.7% thời gian**).
  - Tỷ lệ dòng code tái sử dụng đạt **93.5%** (chỉ cần điều chỉnh đường dẫn tương đối và tên file exe).
  - Chi tiết đo đạc xem tại [`ai/output/loc-time-measurement.md`](../ai/output/loc-time-measurement.md).

---

## 5. Tổng Kết: Cơ Hội & Thách Thức (Bài Học Kinh Nghiệm)

* **Cơ hội:** 
  * Giảm tới 70–80% thời gian soạn thảo boilerplate code và thiết kế test case biên.
  * Tăng năng suất cho cả Manual Tester và Automation SDET.
* **Thách thức & Bài học rút ra (Human-in-the-loop):**
  * **Hiện tượng ảo giác (Hallucination):** Ở lần prompt đầu tiên, AI hay tự ý sinh kết quả có dấu tiếng Việt trong khi AUT chỉ hỗ trợ ASCII. Cần áp dụng kỹ thuật Few-shot Prompting để neo cứng định dạng đầu ra.
  * **Rủi ro sai lệch định vị (Locator Drift):** AI không thể tự đoán đúng AutomationId nếu không được cấp đặc tả chính xác (`minisum-spec.md`). Do đó, con người vẫn đóng vai trò quyết định trong việc rà soát và kiểm chứng kịch bản thực tế.
