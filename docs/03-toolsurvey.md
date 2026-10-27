# Automation Testing for Desktop Applications
## Phần 3: Tool Survey & Selection Criteria

> **Seminar – Phụ trách:** Tín  
> **Nội dung:** Khảo sát công cụ thị trường · Bộ tiêu chí đánh giá · Ma trận đối chiếu · Tài liệu tham khảo  
> **Cập nhật lần cuối:** 02/10/2026  
> **Trạng thái:** Hoàn thành  

---

## Mục lục

1. [Khảo sát các công cụ phổ biến trên thị trường](#1-khảo-sát-các-công-cụ-phổ-biến-trên-thị-trường)
2. [Bộ tiêu chí đánh giá công cụ Desktop Automation](#2-bộ-tiêu-chí-đánh-giá-công-cụ-desktop-automation)
   - 2.1 [Sơ đồ cấu trúc 6 nhóm tiêu chí](#21-sơ-đồ-cấu-trúc-6-nhóm-tiêu-chí)
   - 2.2 [Nhóm 1: Tiêu chí Kỹ thuật (Technical Capabilities)](#22-nhóm-1-tiêu-chí-kỹ-thuật-technical-capabilities)
   - 2.3 [Nhóm 2: Khả năng sử dụng (Usability & Learning Curve)](#23-nhóm-2-khả-năng-sử-dụng-usability--learning-curve)
   - 2.4 [Nhóm 3: Hiệu năng & Tính ổn định (Performance & Reliability)](#24-nhóm-3-hiệu-năng--tính-ổn-định-performance--reliability)
   - 2.5 [Nhóm 4: Chi phí & Giá trị đầu tư (Cost & ROI)](#25-nhóm-4-chi-phí--giá-trị-đầu-tư-cost--roi)
   - 2.6 [Nhóm 5: Khả năng bảo trì & Tính linh hoạt (Maintainability)](#26-nhóm-5-khả-năng-bảo-trì--tính-linh-hoạt-maintainability)
   - 2.7 [Nhóm 6: Hệ sinh thái & Khả năng mở rộng (Ecosystem)](#27-nhóm-6-hệ-sinh-thái--khả-năng-mở-rộng-ecosystem)
3. [Ma trận đánh giá so sánh (Biểu mẫu Template)](#3-ma-trận-đánh-giá-so-sánh-biểu-mẫu-template)
4. [Định hướng lựa chọn 2 công cụ nghiên cứu chuyên sâu](#4-định-hướng-lựa-chọn-2-công-cụ-nghiên-cứu-chuyên-sâu)
5. [Tài liệu tham khảo](#5-tài-liệu-tham-khảo)

---

## 1. Khảo sát các công cụ phổ biến trên thị trường

Hiện nay, thị trường kiểm thử tự động cho ứng dụng desktop được chia thành nhiều phân khúc: giải pháp mã nguồn mở của Microsoft, phần mềm thương mại trọn gói cho doanh nghiệp lớn, và các thư viện lập trình tự động hóa dựa trên đồ họa/tọa độ.

| Tên công cụ | Đơn vị phát triển | Mô hình bản quyền | Ngôn ngữ viết kịch bản | Đặc điểm và thế mạnh nổi bật |
|---|---|---|---|---|
| **WinAppDriver** | Microsoft | Mã nguồn mở (Free) | C#, Java, Python, JavaScript | Hỗ trợ chuẩn WebDriver (Appium), tương thích hoàn hảo với UWP, WPF, Win32 trên Windows 10/11. |
| **TestComplete** | SmartBear | Thương mại (Commercial) | Python, JavaScript, VBScript | Nhận diện đối tượng thông minh, tích hợp AI nhận dạng thành phần giao diện, hỗ trợ Record & Playback mạnh mẽ. |
| **Ranorex Studio** | Ranorex | Thương mại (Commercial) | C#, VB.NET | Công cụ nhận diện RanoreXPath cực kỳ chuẩn xác, giao diện chuyên nghiệp, hỗ trợ đa dạng framework desktop. |
| **OpenText UFT One** | OpenText (Micro Focus) | Thương mại (Commercial) | VBScript | Giải pháp lâu đời, phù hợp cho hệ thống doanh nghiệp lớn tích hợp phức tạp (SAP, Oracle, mainframe, desktop). |
| **Katalon Studio** | Katalon | Freemium (Miễn phí / Trả phí) | Groovy, Java | Giao diện đồ họa thân thiện, tích hợp sẵn Record & Playback cho desktop (dựa trên WinAppDriver engine). |
| **PyAutoGUI** | Cộng đồng | Mã nguồn mở (Free) | Python | Điều khiển chuột và bàn phím dựa trên tọa độ màn hình và so khớp hình ảnh mẫu; đơn giản, dễ tiếp cận. |
| **SikuliX** | Cộng đồng | Mã nguồn mở (Free) | Python (Jython), Java | Cơ chế nhận diện đối tượng dựa trên thị giác máy tính (OpenCV), kiểm thử được các giao diện không thể inspect bằng UIA. |
| **AutoIt** | AutoIt Team | Miễn phí (Freeware) | Ngôn ngữ script AutoIt | Rất nhẹ, chuyên dùng tự động hóa các tác vụ hệ thống Windows và xử lý popup/dialog hệ điều hành. |
| **Robot Framework** | Cộng đồng | Mã nguồn mở (Free) | Robot DSL (Python backend) | Kiến trúc kiểm thử hướng từ khóa (Keyword-Driven), có thể mở rộng qua WhiteLibrary hoặc FlaUI library. |

---

## 2. Bộ tiêu chí đánh giá công cụ Desktop Automation

### 2.1 Sơ đồ cấu trúc 6 nhóm tiêu chí

```
BỘ TIÊU CHÍ ĐÁNH GIÁ CÔNG CỤ AUTOMATION TESTING CHO DESKTOP
═══════════════════════════════════════════════════════════════════════════════

  ┌────────────────────────────────────────────────────────────────────────┐
  │                 6 NHÓM TIÊU CHÍ ĐÁNH GIÁ CỐT LÕI                       │
  └────────────────────────────────────────────────────────────────────────┘

  1. NĂNG LỰC KỸ THUẬT                  2. KHẢ NĂNG SỬ DỤNG
  ─────────────────────────────────     ───────────────────────────────────────
  • Hỗ trợ các công nghệ UI desktop     • Độ dốc học tập (Learning Curve)
  • Năng lực nhận diện đối tượng (UIA)   • Chất lượng tài liệu và hướng dẫn
  • Tính năng Record & Playback         • Độ lớn cộng đồng hỗ trợ
  • Khả năng Data-Driven Testing        • Khả năng tích hợp IDE (VS Code, VS)
  • Hệ thống Checkpoint & Báo cáo       • Độ tiện dụng của giao diện công cụ

  3. HIỆU NĂNG & TÍNH ỔN ĐỊNH           4. CHI PHÍ & GIÁ TRỊ ĐẦU TƯ
  ─────────────────────────────────     ───────────────────────────────────────
  • Tốc độ thực thi kịch bản            • Bản quyền phần mềm (Free/Commercial)
  • Độ ổn định (chống flaky test)       • Chi phí thiết lập môi trường ban đầu
  • Cơ chế đồng bộ hóa (Wait handling)  • Chi phí đào tạo nhân sự
  • Mức tiêu hao tài nguyên hệ thống    • Khả năng thu hồi vốn đầu tư (ROI)

  5. BẢO TRÌ & TÍNH LINH HOẠT           6. HỆ SINH THÁI & MỞ RỘNG
  ─────────────────────────────────     ───────────────────────────────────────
  • Khả năng chịu biến động UI          • Khả năng mở rộng qua Plugin
  • Hỗ trợ mô hình thiết kế (POM)       • Tích hợp thư viện kiểm thử phổ biến
  • Tái sử dụng thành phần kịch bản     • Khả năng tích hợp CI/CD Pipelines
  • Tương thích quản lý mã nguồn (Git)  • Tính năng ứng dụng AI/Smart Testing
```

---

### 2.2 Nhóm 1: Tiêu chí Kỹ thuật (Technical Capabilities)

| Mã số | Tiêu chí đánh giá | Nội dung mô tả chi tiết | Trọng số (1–5) |
|---|---|---|---|
| T1 | **Hỗ trợ công nghệ UI** | Khả năng tương thích với các framework phổ biến: Win32, WinForms, WPF, UWP, Electron, Qt, Java Swing. | 5 |
| T2 | **Nhận diện đối tượng (Object Recognition)** | Hỗ trợ bắt thuộc tính qua Microsoft UI Automation (AutomationId, Name, ClassName, XPath) hoặc Image Matching. | 5 |
| T3 | **Chất lượng Record & Playback** | Cơ chế tự động ghi nhận hành vi, lọc nhiễu thao tác và phát lại ổn định trên ứng dụng thật. | 4 |
| T4 | **Hỗ trợ Data-Driven Testing** | Khả năng kết nối và đọc trực tiếp từ các nguồn dữ liệu bên ngoài: Excel, CSV, JSON, XML, Database, REST API. | 4 |
| T5 | **Đa dạng Checkpoints & Assertions** | Hỗ trợ phong phú các loại kiểm tra: Text, Thuộc tính đối tượng, Ảnh chụp, Bảng dữ liệu, File xuất ra, Database. | 5 |
| T6 | **Hệ thống Báo cáo (Reporting)** | Tự động xuất báo cáo chi tiết: thời gian thực thi, log từng bước, ảnh chụp màn hình khi lỗi, video quay phiên test. | 4 |
| T7 | **Tích hợp đường ống CI/CD** | Hỗ trợ chạy kịch bản qua dòng lệnh (CLI), dễ tích hợp vào Jenkins, GitHub Actions, Azure DevOps, GitLab CI. | 4 |
| T8 | **Khả năng đa nền tảng (Cross-platform)** | Khả năng kiểm thử các ứng dụng desktop trên các hệ điều hành khác ngoài Windows (macOS, Linux). | 3 |
| T9 | **Ngôn ngữ lập trình kịch bản** | Hỗ trợ các ngôn ngữ phổ biến trong ngành: C#, Python, Java, JavaScript/TypeScript, Groovy. | 4 |
| T10 | **Thực thi song song (Parallel Execution)** | Năng lực chạy đồng thời nhiều kịch bản trên các máy ảo hoặc phiên desktop khác nhau để rút ngắn thời gian. | 3 |

---

### 2.3 Nhóm 2: Khả năng sử dụng (Usability & Learning Curve)

| Mã số | Tiêu chí đánh giá | Nội dung mô tả chi tiết | Trọng số (1–5) |
|---|---|---|---|
| U1 | **Độ dốc tiếp cận (Learning Curve)** | Mức độ dễ dàng làm quen cho người mới bắt đầu hoặc người kiểm thử chuyển từ manual sang automation. | 5 |
| U2 | **Chất lượng tài liệu chính thức** | Hệ thống tài liệu (Documentation), cẩm nang hướng dẫn (Tutorials), ví dụ mẫu và API reference rõ ràng, cập nhật. | 4 |
| U3 | **Cộng đồng và diễn đàn hỗ trợ** | Số lượng câu hỏi và giải đáp trên Stack Overflow, GitHub Issues, Reddit hoặc diễn đàn chính thức của hãng. | 4 |
| U4 | **Tích hợp môi trường lập trình (IDE)** | Khả năng tích hợp trực tiếp vào các IDE phổ biến như Visual Studio, Visual Studio Code, IntelliJ, PyCharm. | 3 |
| U5 | **Giao diện người dùng trực quan (GUI)** | Cung cấp giao diện đồ họa trực quan để theo dõi cây đối tượng (Object Spy/Inspector), quản lý test suite. | 3 |

---

### 2.4 Nhóm 3: Hiệu năng & Tính ổn định (Performance & Reliability)

| Mã số | Tiêu chí đánh giá | Nội dung mô tả chi tiết | Trọng số (1–5) |
|---|---|---|---|
| P1 | **Tốc độ thực thi** | Tốc độ gửi sự kiện và phản hồi kiểm tra trên phần tử UI; không bị trễ thời gian vô lý giữa các thao tác. | 4 |
| P2 | **Độ ổn định của kịch bản** | Kịch bản chạy ổn định qua nhiều lần thực thi, hạn chế tối đa hiện tượng Flaky Test (khi pass khi fail không lý do). | 5 |
| P3 | **Cơ chế đồng bộ hóa (Synchronization)** | Cung cấp các hàm chờ thông minh (Explicit Wait, Fluent Wait) dựa trên trạng thái thật của đối tượng UI thay vì sleep cứng. | 5 |
| P4 | **Mức tiêu hao tài nguyên** | Mức độ chiếm dụng bộ nhớ RAM và xung nhịp CPU của công cụ khi đang vận hành trong phiên kiểm thử. | 3 |

---

### 2.5 Nhóm 4: Chi phí & Giá trị đầu tư (Cost & ROI)

| Mã số | Tiêu chí đánh giá | Nội dung mô tả chi tiết | Trọng số (1–5) |
|---|---|---|---|
| C1 | **Chi phí bản quyền phần mềm** | Thuộc diện Mã nguồn mở miễn phí, Freemium, hay Thương mại tính phí theo người dùng (Per-user/Node-locked/Floating). | 5 |
| C2 | **Chi phí cấu hình và thiết lập ban đầu** | Thời gian và độ phức tạp cần thiết để cài đặt driver, runtime, chứng chỉ số và môi trường vận hành. | 4 |
| C3 | **Chi phí đào tạo nhân sự** | Thời gian và chi phí cần bỏ ra để đội ngũ kiểm thử làm chủ được công cụ và quy trình làm việc. | 4 |
| C4 | **Khả năng thu hồi vốn đầu tư (ROI)** | Mức độ tiết kiệm thời gian và nguồn lực kiểm thử đạt được so với tổng chi phí bỏ ra sau chu kỳ 6-12 tháng. | 4 |

---

### 2.6 Nhóm 5: Khả năng bảo trì & Tính linh hoạt (Maintainability)

| Mã số | Tiêu chí đánh giá | Nội dung mô tả chi tiết | Trọng số (1–5) |
|---|---|---|---|
| M1 | **Kháng biến động giao diện (UI Resilience)** | Cơ chế nhận diện có bị gãy đổ khi lập trình viên thay đổi nhỏ về tọa độ, màu sắc hay vị trí thứ tự hay không. | 5 |
| M2 | **Hỗ trợ kiến trúc thiết kế chuẩn** | Khả năng triển khai các mẫu thiết kế hướng cấu trúc như Page Object Model (POM), Screenplay Pattern, Keyword-Driven. | 4 |
| M3 | **Khả năng tái sử dụng (Reusability)** | Cho phép đóng gói các hàm thao tác dùng chung, thư viện dùng chung và bộ dữ liệu kiểm thử dùng chung dễ dàng. | 4 |
| M4 | **Quản lý phiên bản mã nguồn (VCS / Git)** | Định dạng tệp kịch bản là text thuần (code) dễ merge/diff bằng Git, hay là tệp nhị phân độc quyền khó kiểm soát xung đột. | 4 |

---

### 2.7 Nhóm 6: Hệ sinh thái & Khả năng mở rộng (Ecosystem)

| Mã số | Tiêu chí đánh giá | Nội dung mô tả chi tiết | Trọng số (1–5) |
|---|---|---|---|
| E1 | **Khả năng mở rộng qua Plugin** | Hỗ trợ cài đặt hoặc tự phát triển các extension/plugin bổ sung khi phát sinh yêu cầu đặc thù. | 4 |
| E2 | **Tương thích Framework kiểm thử chuẩn** | Tương thích mượt mà với các test runner và assertion framework chuẩn: NUnit, xUnit, MSTest, pytest, JUnit, TestNG. | 4 |
| E3 | **Mức độ hỗ trợ từ cộng đồng** | Tần suất cập nhật phiên bản mới, tính thường xuyên của các bản vá lỗi và sự tích cực đóng góp từ cộng đồng. | 5 |
| E4 | **Chất lượng hỗ trợ từ hãng (Vendor Support)** | Cam kết hỗ trợ kỹ thuật trực tiếp từ nhà cung cấp (SLA, hỗ trợ qua ticket, tư vấn giải pháp kỹ thuật). | 3 |
| E5 | **Tính năng ứng dụng trí tuệ nhân tạo (AI)** | Tích hợp tính năng AI tự động nhận diện control khi thuộc tính đổi (Self-healing), tự sinh kịch bản từ ngôn ngữ tự nhiên. | 4 |

---

## 3. Ma trận đánh giá so sánh (Biểu mẫu Template)

> **Hướng dẫn dành cho thành viên phụ trách Tool A (Kan) và Tool B (Tùng):**  
> Mỗi tiêu chí chấm theo thang điểm từ **1 đến 5** (1 = Kém / Không hỗ trợ, 5 = Xuất sắc / Hoàn thiện).  
> Điểm có trọng số = Điểm đánh giá × Trọng số tiêu chí. Điểm tối đa chuẩn hóa về thang **100 điểm**.

| Nhóm tiêu chí | Tiêu chí đánh giá | Trọng số (W) | Điểm Tool A (1-5) | Điểm Tool B (1-5) | Ghi chú đánh giá thực tế |
|---|---|---|---|---|---|
| **Kỹ thuật** | T1. Hỗ trợ công nghệ UI | 5 | /5 | /5 | |
| | T2. Năng lực Object Recognition | 5 | /5 | /5 | |
| | T3. Tính năng Record & Playback | 4 | /5 | /5 | |
| | T4. Hỗ trợ Data-Driven Testing | 4 | /5 | /5 | |
| | T5. Đa dạng Checkpoint / Assertion | 5 | /5 | /5 | |
| | T6. Hệ thống Báo cáo kết quả | 4 | /5 | /5 | |
| | T7. Khả năng tích hợp CI/CD | 4 | /5 | /5 | |
| | T9. Ngôn ngữ lập trình hỗ trợ | 4 | /5 | /5 | |
| **Khả năng sử dụng** | U1. Độ dốc tiếp cận (Learning curve) | 5 | /5 | /5 | |
| | U2. Chất lượng tài liệu hướng dẫn | 4 | /5 | /5 | |
| | U3. Độ lớn cộng đồng hỗ trợ | 4 | /5 | /5 | |
| **Hiệu năng & Ổn định** | P1. Tốc độ thực thi kịch bản | 4 | /5 | /5 | |
| | P2. Độ ổn định (Chống Flaky test) | 5 | /5 | /5 | |
| | P3. Cơ chế chờ đồng bộ (Waits) | 5 | /5 | /5 | |
| **Chi phí & Đầu tư** | C1. Bản quyền phần mềm | 5 | /5 | /5 | |
| | C2. Độ phức tạp thiết lập ban đầu | 4 | /5 | /5 | |
| **Bảo trì & Linh hoạt** | M1. Kháng biến động giao diện UI | 5 | /5 | /5 | |
| | M2. Hỗ trợ thiết kế chuẩn (POM) | 4 | /5 | /5 | |
| **Hệ sinh thái** | E3. Mức độ hỗ trợ từ cộng đồng | 5 | /5 | /5 | |
| | E5. Tính năng thông minh / AI | 4 | /5 | /5 | |
| **TỔNG KẾT** | **Tổng điểm đánh giá chuẩn hóa** | **--** | **/100** | **/100** | |

---

## 4. Định hướng lựa chọn 2 công cụ nghiên cứu chuyên sâu

Nhằm đảm bảo tính khách quan và chiều sâu khoa học cho buổi seminar, việc lựa chọn 2 công cụ đại diện (Tool A và Tool B) cần tuân thủ 4 nguyên tắc định hướng sau:

1. **Đại diện cho 2 trường phái giải pháp đối lập:**
   - *Lựa chọn gợi ý 1:* Một công cụ **Mã nguồn mở hướng lập trình (Code-based / Open Source)** đối trọng với một công cụ **Thương mại trọn gói có giao diện đồ họa (GUI-based / All-in-one Commercial)**.
   - *Ví dụ tiêu biểu:* **WinAppDriver** (hoặc FlaUI) đối chiếu với **TestComplete** (hoặc Katalon Studio / Ranorex).
2. **Cùng có khả năng thực thi trên một ứng dụng mẫu chung (Common Case Study):**
   - Hai công cụ phải cùng tương tác được trên một phần mềm thử nghiệm cụ thể (ví dụ: ứng dụng máy tính Windows Calculator, ứng dụng quản lý nhân sự WPF, hoặc ứng dụng POS) để đối chiếu trực tiếp độ phức tạp khi viết test, độ ổn định và thời gian chạy.
3. **Có tài liệu đầy đủ và môi trường khả thi trong điều kiện học tập:**
   - Công cụ phải cho phép cài đặt, cấp giấy phép dùng thử (Trial) hoặc mã nguồn mở miễn phí để các thành viên có thể dựng môi trường và ghi hình demo thực tế.
4. **Có cộng đồng và tiềm năng ứng dụng cao trong công nghiệp:**
   - Giúp sinh viên nắm bắt được những kỹ năng thực tế mà các doanh nghiệp phần mềm đang sử dụng.

---

## 5. Tài liệu tham khảo

1. Myers, G. J., Sandler, C., & Badgett, T. (2011). *The Art of Software Testing* (3rd ed.). John Wiley & Sons.
2. Fewster, M., & Graham, D. (1999). *Software Test Automation: Effective Use of Test Execution Tools*. ACM Press / Addison-Wesley.
3. Microsoft Corporation. (2024). *UI Automation Overview & Windows Application Driver Documentation*. Microsoft Learn. https://learn.microsoft.com/en-us/dotnet/framework/ui-automation/
4. SmartBear Software. (2024). *TestComplete Documentation & Automated UI Testing Best Practices*. SmartBear Documentation Portal. https://support.smartbear.com/testcomplete/
5. International Software Testing Qualifications Board (ISTQB). (2023). *Certified Tester Foundation Level (CTFL) Syllabus & Specialist Test Automation Engineer*. ISTQB Guidelines. https://www.istqb.org/
6. Crispin, L., & Gregory, J. (2009). *Agile Testing: A Practical Guide for Testers and Agile Teams*. Addison-Wesley Professional.

---

> **Phụ trách:** Tín  
> **Cập nhật lần cuối:** 02/10/2026  
> **Trạng thái:** Hoàn thành
