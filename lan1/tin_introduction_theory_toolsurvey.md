# Automation Testing for Desktop Applications
> **Seminar – Phần phụ trách: Tín**
> Nội dung: Introduction · Theory · Tool Survey (Tiêu chí đánh giá)

---

## Mục lục

1. [Introduction](#1-introduction)
2. [Theory](#2-theory)
   - 2.1 [Automation Testing là gì?](#21-automation-testing-là-gì)
   - 2.2 [Desktop Application Testing](#22-desktop-application-testing)
   - 2.3 [Đặc điểm & Khó khăn đặc thù](#23-đặc-điểm--khó-khăn-đặc-thù)
   - 2.4 [Record & Playback](#24-record--playback)
   - 2.5 [Data-Driven Testing](#25-data-driven-testing)
   - 2.6 [Checkpoints & Assertions](#26-checkpoints--assertions)
   - 2.7 [Fully vs Semi-Automated](#27-fully-vs-semi-automated)
   - 2.8 [Ưu điểm & Nhược điểm](#28-ưu-điểm--nhược-điểm)
   - 2.9 [Khi nào nên dùng Automation?](#29-khi-nào-nên-dùng-automation)
3. [Tool Survey – Tiêu chí đánh giá](#3-tool-survey--tiêu-chí-đánh-giá)
4. [Bảng thuật ngữ](#4-bảng-thuật-ngữ)
5. [Tài liệu tham khảo](#5-tài-liệu-tham-khảo)

---

## 1. Introduction

### 1.1 Bối cảnh

Phần mềm desktop vẫn chiếm vai trò quan trọng trong nhiều lĩnh vực: tài chính, y tế, công nghiệp, giáo dục, v.v. Không giống ứng dụng web, desktop app chạy trực tiếp trên hệ điều hành, tương tác sâu với tài nguyên máy tính (file system, registry, driver, GPU…) và đòi hỏi độ ổn định cao.

Trong bối cảnh phát triển phần mềm ngày càng nhanh (Agile/CI-CD), kiểm thử thủ công không còn đáp ứng kịp yêu cầu về tốc độ và độ phủ. **Automation Testing** ra đời như một giải pháp tất yếu.

### 1.2 Lý do chọn đề tài

| Vấn đề thực tiễn | Lý do quan tâm |
|---|---|
| Desktop app vẫn được dùng rộng rãi trong môi trường doanh nghiệp | Nhu cầu kiểm thử không giảm |
| Kiểm thử thủ công tốn thời gian, dễ sai sót | Cần tự động hóa |
| Automation cho desktop khó hơn web | Cần nghiên cứu tool chuyên biệt |
| Nhiều tool trên thị trường, khó chọn | Cần bộ tiêu chí đánh giá rõ ràng |
| AI đang thay đổi cách viết test | Cần cập nhật xu hướng mới |

### 1.3 Mục tiêu seminar

```
┌─────────────────────────────────────────────────────────┐
│              MỤC TIÊU SEMINAR                           │
│                                                         │
│  1. Hiểu lý thuyết nền tảng Automation Testing         │
│     cho Desktop Application                             │
│                                                         │
│  2. Khảo sát & so sánh các tool phổ biến               │
│     (Tool A & Tool B)                                   │
│                                                         │
│  3. Demo thực tế: Record & Playback,                   │
│     Data-driven, Workflow phức tạp                      │
│                                                         │
│  4. Tìm hiểu ứng dụng AI trong Desktop Automation      │
│                                                         │
│  5. Thực hành: bài tập cho lớp                         │
└─────────────────────────────────────────────────────────┘
```

### 1.4 Phạm vi seminar

- **Đối tượng ứng dụng:** Desktop app trên Windows (WinForms, WPF, Win32, Electron…)
- **Kỹ thuật:** Record & Playback, Data-Driven, Checkpoints/Assertions
- **Mức độ:** Từ cơ bản đến workflow phức tạp; có demo minh họa

---

## 2. Theory

### 2.1 Automation Testing là gì?

**Automation Testing** (Kiểm thử tự động) là quá trình sử dụng **công cụ phần mềm** để thực thi các ca kiểm thử (test case) một cách tự động, so sánh kết quả thực tế với kết quả kỳ vọng mà không cần (hoặc chỉ cần rất ít) sự can thiệp thủ công.

```
┌──────────────┐    Test Script    ┌──────────────────┐
│   Tester     │ ─────────────── ► │  Automation Tool  │
│  (Lập lịch, │                   │  (Thực thi test)  │
│   Phân tích) │ ◄─────────────── │                   │
└──────────────┘    Test Report    └──────────┬────────┘
                                              │ Tương tác
                                              ▼
                                   ┌──────────────────┐
                                   │  Ứng dụng cần    │
                                   │  kiểm thử (AUT)  │
                                   └──────────────────┘
```

> **Kiểm thử tự động ≠ Loại bỏ tester.** Con người vẫn cần để thiết kế test case, phân tích kết quả, bảo trì script và đánh giá rủi ro.

---

### 2.2 Desktop Application Testing

#### 2.2.1 Phân loại Desktop Application

```
Desktop Applications
├── Native Apps
│   ├── Win32 / MFC
│   ├── WinForms (.NET)
│   ├── WPF (Windows Presentation Foundation)
│   └── UWP (Universal Windows Platform)
├── Cross-Platform Native
│   ├── Qt
│   └── JavaFX / Swing
└── Hybrid / Embedded Web
    ├── Electron (Chromium + Node.js)
    └── .NET MAUI / Blazor Hybrid
```

#### 2.2.2 Các loại kiểm thử áp dụng cho Desktop App

| Loại kiểm thử | Mô tả | Khả năng tự động hóa |
|---|---|---|
| **Functional Testing** | Kiểm tra chức năng đúng yêu cầu | Rất phù hợp (Mức độ cao) |
| **Regression Testing** | Đảm bảo tính năng cũ không bị hỏng | Rất phù hợp (Mức độ rất cao) |
| **Smoke Testing** | Kiểm tra nhanh sau build mới | Rất phù hợp (Mức độ cao) |
| **UI Testing** | Kiểm tra giao diện người dùng | Phù hợp (Mức độ trung bình) |
| **Performance Testing** | Đo tốc độ, tài nguyên sử dụng | Rất phù hợp (Mức độ cao) |
| **Usability Testing** | Trải nghiệm người dùng | Hạn chế (Cần đánh giá thủ công) |
| **Exploratory Testing** | Khám phá lỗi sáng tạo | Không khả thi (Đòi hỏi tư duy con người) |

---

### 2.3 Đặc điểm & Khó khăn đặc thù

#### 2.3.1 Đặc điểm nổi bật của Desktop App Testing

- **Phụ thuộc OS:** App chạy khác nhau trên Win 10 vs Win 11, 32-bit vs 64-bit.
- **Tương tác trực tiếp với phần cứng:** Máy in, scanner, camera, thiết bị đặc thù.
- **Quản lý tài nguyên:** Kiểm soát bộ nhớ, CPU, file lock.
- **Không có DOM chuẩn:** Không như web, giao diện desktop không có cấu trúc thống nhất.

#### 2.3.2 Khó khăn đặc thù khi Automation

```
KHÓ KHĂN TRONG DESKTOP AUTOMATION TESTING
──────────────────────────────────────────
① Nhận diện phần tử UI
   • Không có ID/CSS selector như web
   • Phụ thuộc vào framework: Win32, WPF, WinForms mỗi loại khác nhau
   • UI thay đổi theo theme, DPI, ngôn ngữ hệ thống

② Đồng bộ hóa (Synchronization)
   • Desktop app không có event "page load" rõ ràng
   • Cần wait thông minh (không chỉ sleep cứng)

③ Quản lý cửa sổ & hộp thoại
   • Dialog, popup hệ thống (Save As, Print...) khó kiểm soát
   • Multi-window, MDI (Multiple Document Interface)

④ Môi trường thực thi
   • Cần môi trường có màn hình (không dễ chạy headless)
   • Độ phân giải màn hình ảnh hưởng đến vị trí phần tử

⑤ Bảo trì script
   • Giao diện thay đổi → script cần cập nhật liên tục
   • Chi phí bảo trì có thể vượt chi phí viết mới
```

---

### 2.4 Record & Playback

#### 2.4.1 Khái niệm

**Record & Playback** là kỹ thuật trong đó công cụ ghi lại toàn bộ thao tác của người dùng trên ứng dụng (click, nhập liệu, navigation…), sau đó phát lại chính xác các thao tác đó để kiểm thử.

```
RECORD PHASE                    PLAYBACK PHASE
─────────────                   ──────────────
Tester thao tác                 Tool tự động thực thi
trên AUT           ──Script──►  lại các bước đã ghi
                                và kiểm tra kết quả
Tool ghi lại
từng hành động
```

#### 2.4.2 Luồng hoạt động

```
[Bắt đầu Record]
      │
      ▼
[Tester thực hiện test case thủ công]
      │
      ▼
[Tool capture: tên phần tử UI, hành động, dữ liệu nhập]
      │
      ▼
[Tool sinh script (VBScript, Python, Groovy...)]
      │
      ▼
[Tester chỉnh sửa/bổ sung script nếu cần]
      │
      ▼
[Chạy Playback – so sánh kết quả thực vs kỳ vọng]
      │
      ▼
[Báo cáo PASS / FAIL]
```

#### 2.4.3 Ưu & Nhược điểm

| | Ưu điểm | Nhược điểm |
|---|---|---|
| **Record & Playback** | Dễ dùng, không cần kỹ năng lập trình | Script cứng nhắc, khó bảo trì |
| | Nhanh tạo test ban đầu | Không xử lý được dữ liệu động |
| | Phù hợp cho người mới | Script thường dài và lặp lại |

---

### 2.5 Data-Driven Testing

#### 2.5.1 Khái niệm

**Data-Driven Testing (DDT)** là kỹ thuật tách biệt **logic test** và **dữ liệu test**. Một test script duy nhất được chạy nhiều lần với nhiều bộ dữ liệu khác nhau lấy từ nguồn bên ngoài (Excel, CSV, database, JSON…).

```
┌─────────────────┐      ┌──────────────────────┐
│   Test Script   │◄─────│   Data Source        │
│  (Logic chung)  │      │  (Excel/CSV/DB/JSON) │
└────────┬────────┘      │                      │
         │               │  Row 1: admin/123456 │
         │ Chạy lần 1    │  Row 2: user/abc@123 │
         │ Chạy lần 2    │  Row 3: guest/guest  │
         │ Chạy lần 3    └──────────────────────┘
         ▼
┌─────────────────┐
│   Test Results  │
│  (Per-row PASS/ │
│   FAIL report)  │
└─────────────────┘
```

#### 2.5.2 Ví dụ thực tế: Kiểm thử đăng nhập

```
TEST SCRIPT: login_test(username, password, expected_result)
─────────────────────────────────────────────────────────────
Bước 1: Mở app
Bước 2: Nhập {username}
Bước 3: Nhập {password}
Bước 4: Click Login
Bước 5: Assert kết quả == {expected_result}

DATA FILE (login_data.xlsx):
┌──────────────┬──────────────┬──────────────────┐
│  username    │  password    │  expected_result  │
├──────────────┼──────────────┼──────────────────┤
│  admin       │  Admin@123   │  Dashboard        │
│  user01      │  wrongpass   │  Error message    │
│  (empty)     │  123456      │  Validation error │
│  admin       │  (empty)     │  Validation error │
└──────────────┴──────────────┴──────────────────┘
```

---

### 2.6 Checkpoints & Assertions

#### 2.6.1 Khái niệm

**Checkpoint** (hay **Assertion**) là điểm kiểm tra trong test script, nơi công cụ so sánh **trạng thái thực tế** của ứng dụng với **giá trị kỳ vọng**. Đây là yếu tố quyết định test PASS hay FAIL.

> **Lưu ý:** Một automation script **không có checkpoint** chỉ đơn giản là "thao tác robot" – không phải kiểm thử thực sự.

#### 2.6.2 Phân loại Checkpoint

| Loại | Mô tả | Ví dụ |
|---|---|---|
| **Text Checkpoint** | Kiểm tra text hiển thị | Label "Đăng nhập thành công" |
| **Object/Property Checkpoint** | Kiểm tra thuộc tính UI | Button enabled/disabled |
| **Bitmap Checkpoint** | So sánh ảnh chụp màn hình | UI rendering |
| **Table Checkpoint** | Kiểm tra dữ liệu trong bảng | DataGrid, ListView |
| **File Checkpoint** | Kiểm tra file đầu ra | Export PDF, CSV |
| **Database Checkpoint** | So sánh dữ liệu với DB | Sau thao tác CRUD |

#### 2.6.3 Kiến trúc Assertion

```
[Thực hiện hành động]
         │
         ▼
[Lấy giá trị thực tế (Actual Value)]
         │
         ▼
[So sánh với giá trị kỳ vọng (Expected Value)]
         │
    ┌────┴────┐
    ▼         ▼
 MATCH?    NO MATCH?
  PASS       FAIL
             │
             ▼
   [Chụp màn hình, ghi log, báo cáo]
```

---

### 2.7 Fully vs Semi-Automated

#### 2.7.1 Fully Automated

Toàn bộ quy trình từ **khởi chạy → thực thi → kiểm tra → báo cáo** diễn ra tự động, không cần con người can thiệp trong quá trình thực thi.

```
Fully Automated Pipeline:
CI/CD Trigger ──► Build ──► Deploy ──► Run Tests ──► Report ──► Notify
                                          (Auto)
```

**Phù hợp với:** Regression test suite ổn định; Smoke test sau mỗi build; Test chạy qua đêm (nightly build).

#### 2.7.2 Semi-Automated

Kết hợp giữa tự động hóa và thao tác thủ công. Công cụ xử lý phần lặp đi lặp lại, con người xử lý phần cần phán đoán.

```
Semi-Automated Flow:
Auto: Chuẩn bị dữ liệu → Điều hướng đến màn hình
Manual: Tester kiểm tra giao diện trực quan
Auto: Ghi nhận kết quả, sinh báo cáo
```

**Phù hợp với:** Usability testing (cần đánh giá chủ quan); Exploratory testing hỗ trợ; Test liên quan đến thiết bị vật lý.

#### 2.7.3 So sánh

|  | Fully Automated | Semi-Automated |
|---|---|---|
| Chi phí setup | Cao | Trung bình |
| Tốc độ thực thi | Rất nhanh | Chậm hơn |
| Độ tin cậy | Cao | Phụ thuộc người |
| Linh hoạt | Thấp | Cao |
| Phù hợp với | Regression, Smoke test | Exploratory, Usability |

---

### 2.8 Ưu điểm & Nhược điểm

#### Ưu điểm của Automation Testing

| STT | Ưu điểm | Giải thích |
|---|---|---|
| 1 | **Tốc độ cao** | Script chạy nhanh hơn kiểm thử thủ công nhiều lần |
| 2 | **Độ phủ rộng** | Có thể chạy hàng trăm test case trong một lần |
| 3 | **Nhất quán** | Thực thi chính xác cùng một kịch bản, không bị ảnh hưởng bởi tâm lý |
| 4 | **Reusable** | Script có thể tái sử dụng cho các version khác nhau |
| 5 | **Regression hiệu quả** | Phát hiện ngay lỗi hồi quy sau mỗi thay đổi code |
| 6 | **Chạy 24/7** | Không bị giới hạn giờ làm việc |
| 7 | **Tích hợp CI/CD** | Tự động hóa trong pipeline phát triển |

#### Nhược điểm của Automation Testing

| STT | Nhược điểm | Giải thích |
|---|---|---|
| 1 | **Chi phí ban đầu cao** | Đầu tư công cụ, thời gian viết script |
| 2 | **Bảo trì script** | UI thay đổi → script cần cập nhật |
| 3 | **Không phát hiện được mọi lỗi** | Không thay thế được exploratory testing |
| 4 | **Đòi hỏi kỹ năng kỹ thuật** | Tester cần biết lập trình |
| 5 | **False positive/negative** | Script có thể báo sai nếu thiết kế kém |
| 6 | **Khởi đầu chậm** | Tốn thời gian setup trước khi có ROI |

---

### 2.9 Khi nào nên dùng Automation?

| Nên dùng Automation khi | Không nên khi |
|---|---|
| Test case lặp lại nhiều lần | Test case chỉ chạy 1–2 lần |
| Regression test suite lớn | UI thay đổi liên tục |
| Dữ liệu test đa dạng (DDT) | Test cần phán đoán chủ quan |
| Test chạy nhiều môi trường | Thời gian setup > thời gian tiết kiệm |
| Cần kết quả nhanh (CI/CD) | Dự án nhỏ, deadline gấp |
| Kiểm tra tính năng ổn định | Tính năng đang thay đổi thiết kế |

> **Quy tắc ngón tay cái:** Nếu một test case sẽ được thực thi **hơn 3 lần**, đó là ứng viên tốt cho automation.

---

## 3. Tool Survey – Tiêu chí đánh giá

### 3.1 Các tool phổ biến trên thị trường

| Tool | Hãng | Giấy phép | Ngôn ngữ Script | Nổi bật |
|---|---|---|---|---|
| **WinAppDriver** | Microsoft | Open Source | C#, Java, Python | Tích hợp VS, hỗ trợ UWP/WPF/Win32 |
| **TestComplete** | SmartBear | Commercial | Python, VBScript, JS | Hỗ trợ nhiều loại app, AI-powered |
| **Ranorex** | Ranorex | Commercial | C#, VB.NET | Record & Playback mạnh |
| **UFT (Unified Functional Testing)** | OpenText | Commercial | VBScript | Doanh nghiệp lớn |
| **Katalon Studio** | Katalon | Freemium | Groovy, Java | Dễ dùng, hỗ trợ desktop |
| **PyAutoGUI** | Cộng đồng | Open Source | Python | Image-based, đơn giản |
| **Sikuli/Sikulix** | Cộng đồng | Open Source | Python/Java | Nhận diện ảnh |
| **AutoIt** | AutoIt | Freeware | AutoIt Script | Windows-only, nhẹ |
| **Robot Framework** | Cộng đồng | Open Source | Robot DSL | Keyword-driven |

### 3.2 Bộ tiêu chí đánh giá Tool

#### 3.2.1 Sơ đồ tổng quan tiêu chí

```
BỘ TIÊU CHÍ ĐÁNH GIÁ TOOL AUTOMATION TESTING
══════════════════════════════════════════════

  ① KỸ THUẬT                ② KHẢ NĂNG SỬ DỤNG
  ──────────────────         ──────────────────────
  • Hỗ trợ UI tech           • Độ dốc học (learning curve)
  • Object recognition       • Tài liệu & cộng đồng
  • Record & Playback        • IDE / Editor hỗ trợ
  • Data-driven              • Record & Playback dễ dùng?
  • Checkpoints/Assertions
  • Reporting / CI/CD

  ③ HIỆU NĂNG               ④ CHI PHÍ
  ─────────────              ──────────
  • Tốc độ thực thi          • Giấy phép (free/paid)
  • Độ ổn định               • Chi phí training
  • Scalability              • Chi phí bảo trì
  • Xử lý đồng thời          • ROI

  ⑤ BẢO TRÌ & LINH HOẠT    ⑥ HỆ SINH THÁI
  ──────────────────────     ─────────────────
  • Kháng thay đổi UI        • Plugin/extension
  • Cấu trúc script          • Tích hợp framework
  • Reusability              • Community support
  • Version control          • AI/Smart features
```

#### 3.2.2 Tiêu chí chi tiết – Nhóm 1: Kỹ thuật

| # | Tiêu chí | Mô tả | Trọng số (1–5) |
|---|---|---|---|
| T1 | **Hỗ trợ công nghệ UI** | Win32, WPF, WinForms, UWP, Electron, Java Swing… | 5 |
| T2 | **Object Recognition** | Nhận diện phần tử UI (XPath, AutomationId, Name, ClassName, Image-based…) | 5 |
| T3 | **Record & Playback** | Chất lượng ghi và phát lại thao tác | 4 |
| T4 | **Data-Driven Testing** | Hỗ trợ đọc dữ liệu từ Excel, CSV, DB, API… | 4 |
| T5 | **Checkpoints/Assertions** | Loại và chất lượng điểm kiểm tra | 5 |
| T6 | **Reporting** | Báo cáo: log, screenshot, video, trend | 4 |
| T7 | **CI/CD Integration** | Jenkins, GitHub Actions, Azure DevOps… | 4 |
| T8 | **Cross-platform** | Hỗ trợ nhiều OS | 3 |
| T9 | **Script Language** | Python, C#, Java, Groovy… | 4 |
| T10 | **Parallel Execution** | Chạy nhiều test đồng thời | 3 |

#### 3.2.3 Tiêu chí chi tiết – Nhóm 2: Khả năng sử dụng

| # | Tiêu chí | Mô tả | Trọng số (1–5) |
|---|---|---|---|
| U1 | **Learning Curve** | Mức độ dễ học và làm quen | 5 |
| U2 | **Tài liệu chính thức** | Chất lượng docs, tutorial, ví dụ | 4 |
| U3 | **Cộng đồng người dùng** | Forum, Stack Overflow, GitHub issues | 4 |
| U4 | **IDE Integration** | Plugin cho VS Code, IntelliJ, Visual Studio | 3 |
| U5 | **Giao diện GUI** | Tool có GUI trực quan hay chỉ CLI | 3 |

#### 3.2.4 Tiêu chí chi tiết – Nhóm 3: Hiệu năng

| # | Tiêu chí | Mô tả | Trọng số (1–5) |
|---|---|---|---|
| P1 | **Tốc độ thực thi** | Script chạy nhanh không? | 4 |
| P2 | **Độ ổn định** | Script có bị flaky không? | 5 |
| P3 | **Xử lý đồng bộ hóa** | Cơ chế wait thông minh | 5 |
| P4 | **Tiêu thụ tài nguyên** | RAM, CPU khi chạy test | 3 |

#### 3.2.5 Tiêu chí chi tiết – Nhóm 4: Chi phí

| # | Tiêu chí | Mô tả | Trọng số (1–5) |
|---|---|---|---|
| C1 | **Giấy phép** | Free / Open Source / Freemium / Commercial | 5 |
| C2 | **Chi phí setup** | Cài đặt và cấu hình ban đầu | 4 |
| C3 | **Chi phí training** | Thời gian học, khóa đào tạo | 4 |
| C4 | **ROI** | Thời gian bắt đầu sinh lợi | 4 |

#### 3.2.6 Tiêu chí chi tiết – Nhóm 5: Bảo trì & Linh hoạt

| # | Tiêu chí | Mô tả | Trọng số (1–5) |
|---|---|---|---|
| M1 | **UI Change Resistance** | Script có bị hỏng khi UI thay đổi nhỏ không? | 5 |
| M2 | **Cấu trúc script** | Hỗ trợ Page Object Model, Keyword-driven? | 4 |
| M3 | **Reusability** | Tái sử dụng component, function, test data | 4 |
| M4 | **Version Control** | Script có dễ quản lý bằng Git không? | 4 |

#### 3.2.7 Tiêu chí chi tiết – Nhóm 6: Hệ sinh thái

| # | Tiêu chí | Mô tả | Trọng số (1–5) |
|---|---|---|---|
| E1 | **Plugin/Extension** | Khả năng mở rộng | 4 |
| E2 | **Framework Integration** | TestNG, JUnit, pytest, NUnit… | 4 |
| E3 | **Community Support** | Mức độ hỗ trợ từ cộng đồng | 5 |
| E4 | **Vendor Support** | Hỗ trợ thương mại, SLA | 3 |
| E5 | **AI/Smart features** | Tích hợp AI để sinh test, nhận diện UI | 4 |

### 3.3 Ma trận đánh giá (Template – M2 & M3 điền vào)

| Tiêu chí | Trọng số | Tool A | Tool B |
|---|---|---|---|
| **NHÓM KỸ THUẬT** | | | |
| T1. Hỗ trợ UI tech | 5 | /5 | /5 |
| T2. Object Recognition | 5 | /5 | /5 |
| T3. Record & Playback | 4 | /5 | /5 |
| T4. Data-Driven | 4 | /5 | /5 |
| T5. Checkpoints/Assertions | 5 | /5 | /5 |
| T6. Reporting | 4 | /5 | /5 |
| T7. CI/CD Integration | 4 | /5 | /5 |
| T9. Script Language | 4 | /5 | /5 |
| **NHÓM KHẢ NĂNG SỬ DỤNG** | | | |
| U1. Learning Curve | 5 | /5 | /5 |
| U2. Tài liệu | 4 | /5 | /5 |
| U3. Cộng đồng | 4 | /5 | /5 |
| **NHÓM HIỆU NĂNG** | | | |
| P1. Tốc độ thực thi | 4 | /5 | /5 |
| P2. Độ ổn định | 5 | /5 | /5 |
| P3. Đồng bộ hóa | 5 | /5 | /5 |
| **NHÓM CHI PHÍ** | | | |
| C1. Giấy phép | 5 | /5 | /5 |
| C2. Chi phí setup | 4 | /5 | /5 |
| **NHÓM BẢO TRÌ** | | | |
| M1. UI Change Resistance | 5 | /5 | /5 |
| M2. Cấu trúc script | 4 | /5 | /5 |
| **NHÓM HỆ SINH THÁI** | | | |
| E3. Community | 5 | /5 | /5 |
| E5. AI Features | 4 | /5 | /5 |
| **TỔNG ĐIỂM** | | **/100** | **/100** |

### 3.4 Lý do chọn 2 Tool để nghiên cứu sâu

> *(Sẽ được điền sau khi M2 và M3 hoàn thành khảo sát sơ bộ)*

Tiêu chí ưu tiên khi lựa chọn 2 tool để demo:

1. **Đại diện cho 2 trường phái khác nhau** (ví dụ: commercial vs open source; GUI-based vs code-based)
2. **Cùng hỗ trợ được case study chung** để so sánh công bằng
3. **Có cộng đồng đủ lớn** để dễ tìm tài liệu hỗ trợ
4. **Có thể cài đặt và demo** trong điều kiện học thuật

---

## 4. Bảng thuật ngữ

| Thuật ngữ | Viết tắt | Định nghĩa |
|---|---|---|
| Automation Testing | AT | Kiểm thử tự động bằng công cụ phần mềm |
| Application Under Test | AUT | Ứng dụng đang được kiểm thử |
| Record & Playback | R&P | Ghi lại thao tác và phát lại |
| Data-Driven Testing | DDT | Kiểm thử dựa trên dữ liệu bên ngoài |
| Checkpoint / Assertion | — | Điểm kiểm tra kết quả trong script |
| Regression Testing | — | Kiểm thử hồi quy, đảm bảo tính năng cũ không hỏng |
| Smoke Testing | — | Kiểm thử nhanh sau build mới |
| CI/CD | — | Tích hợp và triển khai liên tục |
| False Positive | — | Test báo PASS nhưng thực ra có lỗi |
| False Negative | — | Test báo FAIL nhưng ứng dụng hoạt động đúng |
| Flaky Test | — | Test không ổn định, khi PASS khi FAIL |
| Test Suite | — | Tập hợp các test case liên quan |
| Page Object Model | POM | Mô hình thiết kế script dựa trên cấu trúc màn hình |
| Keyword-Driven | KDT | Kiểm thử hướng từ khóa |
| Windows Presentation Foundation | WPF | Framework UI của Microsoft (.NET) |
| Universal Windows Platform | UWP | Nền tảng ứng dụng Windows đa thiết bị |
| UI Automation | UIA | API của Windows để tương tác với UI |
| Return on Investment | ROI | Tỷ suất hoàn vốn |

---

## 5. Tài liệu tham khảo

1. Myers, G. J., Sandler, C., & Badgett, T. (2011). *The Art of Software Testing* (3rd ed.). Wiley.
2. Fewster, M., & Graham, D. (1999). *Software Test Automation*. Addison-Wesley.
3. Microsoft. (2024). *UI Automation Overview*. https://learn.microsoft.com/en-us/dotnet/framework/ui-automation/
4. SmartBear. (2024). *TestComplete Documentation*. https://support.smartbear.com/testcomplete/
5. ISTQB. (2023). *ISTQB Glossary*. https://glossary.istqb.org/
6. Crispin, L., & Gregory, J. (2009). *Agile Testing*. Addison-Wesley.

---

> **Phụ trách:** Tín  
> **Cập nhật lần cuối:** 02/10/2026  
> **Trạng thái:** Hoàn thành
