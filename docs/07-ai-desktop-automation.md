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

---

## 4. Kết Quả Thực Nghiệm Thực Tế Của Nhóm (Group Experimental Results)

Nhóm 02 đã hiện thực hóa toàn bộ các định hướng lý thuyết thành **2 chuỗi thực nghiệm thực tế** trên ứng dụng MiniSum:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   CHUỖI THỰC NGHIỆM AI AUTOMATION CỦA NHÓM                       │
├──────────────────────────────────────────────────────────────────────────────────┤
│ [AI DEMO 1: SINH TEST CASE & DỮ LIỆU BVA]                                        │
│   Tài liệu đặc tả               Prompt Few-Shot              12 Test Cases BVA   │
│ (minisum-spec.md)   ───────► (testcase-bva-prompt.md) ───────► (bva-testcases.xlsx)│
├──────────────────────────────────────────────────────────────────────────────────┤
│ [AI DEMO 2: SINH MÃ NGUỒN C# NUNIT & XÁC MINH TRÊN WINAPPDRIVER]                 │
│   Prompt kiến trúc POM          Script C# GenAI              Xác minh chạy PASS  │
│ (script-gen-prompt.md) ───► (chatgpt-script-output.cs) ───► (verified-script.cs)│
└──────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 AI Demo 1: Tự động hóa thiết kế ca kiểm thử hộp đen BVA
* **Đầu vào:** Đặc tả kỹ thuật chi tiết tại [`ai/prompts/minisum-spec.md`](../ai/prompts/minisum-spec.md) mô tả quy tắc hai màn hình và miền giới hạn $[-99, 99]$.
* **Kỹ thuật áp dụng:** Prompt Few-shot kết hợp Chain-of-Thought tại [`ai/prompts/testcase-bva-prompt.md`](../ai/prompts/testcase-bva-prompt.md).
* **Kết quả đối chiếu liên mô hình (Multi-model Benchmark):**
  * **ChatGPT-4:** Phản hồi sắc bén sau 2 vòng tinh chỉnh, sinh đủ 12 ca kiểm thử ([`ai/output/chatgpt-bva-output.md`](../ai/output/chatgpt-bva-output.md)).
  * **Gemini 1.5 Pro & Claude 3.5 Sonnet:** Tốc độ sinh nhanh (3.2s), độ chính xác toán học số âm đạt 100% ngay từ vòng 1 ([`ai/output/gemini-bva-output.md`](../ai/output/gemini-bva-output.md)).
* **Bàn giao:** Xuất file Excel chuẩn hóa [`ai/output/bva-testcases.xlsx`](../ai/output/bva-testcases.xlsx) làm dữ liệu đầu vào cho kịch bản Data-Driven Testing của cả hai nhánh Katalon và WinAppDriver.

### 4.2 AI Demo 2: Tự động sinh kịch bản C# NUnit POM & Debug trên môi trường thật
* **Đầu vào:** Bộ thuộc tính định vị UIA và yêu cầu thiết kế mẫu Page Object Model (POM) tại [`ai/prompts/script-gen-prompt.md`](../ai/prompts/script-gen-prompt.md).
* **Mã sinh tự động ban đầu:** Mã nguồn C# NUnit 215 dòng tại [`ai/output/chatgpt-script-output.cs`](../ai/output/chatgpt-script-output.cs).
* **Quy trình Debug & Xác minh (Verification on Real Environment):**
  * Nhóm đã đưa mã nguồn vào thực thi trực tiếp với tiến trình `WinAppDriver.exe` và `MiniSum.exe`.
  * **4 phát hiện quan trọng được xử lý:**
    1. *Window handle transition:* Chuyển context driver từ `LoginForm` sang `CalculatorForm` bằng `WebDriverWait`.
    2. *Xử lý trạng thái lỗi v3:* Tự động ánh xạ `lblError` thành mã `"LOI"` khi kiểm thử giá trị biên ngoại lệ.
    3. *Làm sạch TextBox:* Thay thế lệnh `.Clear()` bằng tổ hợp phím `Ctrl+A + Backspace`.
    4. *Loại bỏ Sleep tĩnh:* Chuyển sang cơ chế Explicit Wait linh hoạt.
* **Kết quả cuối cùng:** File kịch bản [`ai/output/verified-script-output.cs`](../ai/output/verified-script-output.cs) chạy **PASS 14/14 test cases (100%)** với tổng thời gian thực thi chỉ 18.2 giây!

---

## 5. Bài Học Thực Tế & Best Practices Khi Áp Dụng AI Trong Desktop Automation

Từ kết quả thực nghiệm thực tế, nhóm đúc kết 5 bài học cốt lõi cho các kỹ sư kiểm thử tự động:

### 5.1 Quy tắc "Rác vào - Rác ra" (Garbage In - Garbage Out)
AI chỉ sinh ra mã nguồn và dữ liệu kiểm thử chuẩn xác khi và chỉ khi tài liệu đặc tả cung cấp cho nó có tính cấu trúc và tường minh. Việc cung cấp thiếu một chi tiết nhỏ (ví dụ: không nêu rõ có nhãn `lblError` ở v3) sẽ khiến AI sinh ra mã đọc nhầm trường dữ liệu.

### 5.2 Kỹ thuật Few-shot là chìa khóa chặn đứng ảo giác toán học
Mô hình ngôn ngữ có xu hướng thực hiện phép cộng tự nhiên thay vì tuân theo luật chặn của phần mềm. Việc đưa vào ít nhất **1 ca biên hợp lệ** và **1 ca biên ngoại lệ có kèm Expected: "LOI"** là điều kiện tiên quyết để ép AI tuân thủ luật nghiệp vụ kiểm thử.

### 5.3 Nguyên tắc "Con người giữ vô-lăng" (Human-in-the-Loop)
Mặc dù AI đạt tỷ lệ sinh mã giữ nguyên lên tới **84.6%**, nhưng **15.4% mã nguồn cần sửa chữa** lại quyết định 100% sự thành bại của kịch bản kiểm thử (liên quan đến cơ chế đa cửa sổ của hệ điều hành Windows, xử lý focus và timing). Không bao giờ tin tưởng tuyệt đối vào mã AI sinh ra mà không chạy thử nghiệm (dry-run).

### 5.4 Cấu trúc Prompt theo mẫu POM để dễ bảo trì
Khi yêu cầu AI sinh mã, luôn ép mô hình tách riêng:
- Tầng định danh phần tử (`FindElementByAccessibilityId`).
- Tầng hành động người dùng (`Click`, `SendKeys`).
- Tầng Assertions và Data-Driven runner.
Cách làm này giúp mã nguồn sinh ra có thể tái sử dụng ngay trong các dự án doanh nghiệp lớn mà không cần đập đi xây lại.

---

## 6. Tổng Kết: Cơ Hội, Thách Thức & Tương Lai

* **Cơ hội vượt trội:**
  * Giảm **75% tổng thời gian** xây dựng một bộ kiểm thử tự động hoàn chỉnh (từ 2 giờ xuống dưới 30 phút).
  * Giảm tải gánh nặng viết code boilerplate lặp đi lặp lại cho kỹ sư SDET.
  * Tự động hóa khâu sinh test case vốn là khâu tốn nhiều năng lượng nhận thức nhất của tester.
* **Thách thức cần quản trị:**
  * Nguy cơ rò rỉ dữ liệu khi gửi đặc tả ứng dụng nội bộ lên các dịch vụ AI công cộng (cần sử dụng các mô hình Private / On-Premise LLM).
  * Đòi hỏi kỹ sư kiểm thử phải nâng cao năng lực Prompt Engineering và năng lực review code thay vì chỉ viết code đơn thuần.

