# BÁO CÁO TOÀN VĂN CHUYÊN ĐỀ SEMINAR
# AUTOMATION TESTING FOR DESKTOP APPLICATIONS
## Kiểm Thử Tự Động Ứng Dụng Máy Tính Để Bàn

- **Học phần:** Kiểm thử Phần mềm
- **Đơn vị:** Khoa Công nghệ Thông tin — Bộ môn Kỹ thuật Phần mềm
- **Nhóm thực hiện:** Nhóm 02

---

## BẢNG PHÂN CÔNG CÔNG VIỆC VÀ TRÁCH NHIỆM

| Thành viên | Vai trò / Phân công | Nội dung chi tiết phụ trách | Sản phẩm bàn giao | Trạng thái |
|---|---|---|---|:---:|
| **Tín** | **Theory & Introduction (M1)** | - Bối cảnh, lý do chọn đề tài, mục tiêu và phạm vi.<br>- Cơ sở lý thuyết Automation Desktop, khó khăn đặc thù.<br>- 3 kỹ thuật cốt lõi (Record/Playback, Checkpoints, DDT).<br>- Khảo sát 9 tool, xây dựng bộ tiêu chí 6 nhóm (21 tiêu chí). | `01-introduction.md`<br>`02-theory.md`<br>`03-toolsurvey.md`<br>Slide M1 | **Hoàn thành** |
| **Kan** | **Tool A – Katalon Studio (M2)** | - Nghiên cứu nguyên lý hoạt động của Katalon Studio trên Desktop.<br>- Phân tích 3 năng lực cốt lõi theo lý thuyết.<br>- Đánh giá ưu/nhược điểm thực tế.<br>- Thiết lập kịch bản 3 nhóm demo trên ứng dụng mẫu. | `04-katalon-studio.md`<br>Kịch bản Demo Tool A<br>Slide Tool A | **Hoàn thành** |
| **Tùng** | **Tool B – WinAppDriver (M3)** | - Nghiên cứu nguyên lý WinAppDriver, chuẩn W3C WebDriver.<br>- Phân tích 3 năng lực cốt lõi bằng phương thức lập trình thuần.<br>- Đánh giá ưu/nhược điểm đối trọng với Tool A.<br>- Thiết lập kịch bản 3 nhóm demo dùng chung case study. | `05-winappdriver.md`<br>Kịch bản Demo Tool B<br>Slide Tool B | **Hoàn thành** |
| **Quang** | **AI + Comparison + Exercise (M4)** | - So sánh đối chiếu toàn diện Katalon Studio vs. WinAppDriver.<br>- Nghiên cứu chuyên đề ứng dụng AI trong Desktop Automation.<br>- Thiết kế hệ thống 3 bài tập thực hành theo phân tầng nhận thức.<br>- Tổng kết bài học và hoàn thiện báo cáo toàn văn. | `06-comparison.md`<br>`07-ai-desktop-automation.md`<br>`08-exercises.md`<br>`report.md`<br>Slide M4 | **Hoàn thành** |

---

## MỤC LỤC TOÀN VĂN

1. [Phần 1: Giới Thiệu & Bối Cảnh (Introduction)](#phần-1-giới-thiệu--bối-cảnh-introduction)
2. [Phần 2: Cơ Sở Lý Thuyết Kiểm Thử Tự Động Desktop (Theory)](#phần-2-cơ-sở-lý-thuyết-kiểm-thử-tự-động-desktop-theory)
3. [Phần 3: Khảo Sát Thị Trường & Bộ Tiêu Chí Đánh Giá (Tool Survey)](#phần-3-khảo-sát-thị-trường--bộ-tiêu-chí-đánh-giá-tool-survey)
4. [Phần 4: Nghiên Cứu Công Cụ Đại Diện A – Katalon Studio](#phần-4-nghiên-cứu-công-cụ-đại-diện-a--katalon-studio)
5. [Phần 5: Nghiên Cứu Công Cụ Đại Diện B – Microsoft WinAppDriver](#phần-5-nghiên-cứu-công-cụ-đại-diện-b--microsoft-winappdriver)
6. [Phần 6: So Sánh Đối Chiếu Hai Công Cụ (Comparison)](#phần-6-so-sánh-đối-chiếu-hai-công-cụ-comparison)
7. [Phần 7: Ứng Dụng Trí Tuệ Nhân Tạo (AI) Trong Desktop Automation](#phần-7-ứng-dụng-trí-tuệ-nhân-tạo-ai-trong-desktop-automation)
8. [Phần 8: Hệ Thống Bài Tập Thực Hành Đề Xuất (Exercise)](#phần-8-hệ-thống-bài-tập-thực-hành-đề-xuất-exercise)
9. [Phần 9: Kết Luận & Hướng Phát Triển (Conclusion)](#phần-9-kết-luận--hướng-phát-triển-conclusion)

---


# Phần 1: Giới Thiệu & Bối Cảnh (Introduction)

## 1. Bối cảnh

Phần mềm desktop vẫn chiếm vai trò đặc biệt quan trọng trong nhiều lĩnh vực: tài chính, ngân hàng, y tế, sản xuất công nghiệp, thiết kế đồ họa, kỹ thuật và quản trị nội bộ doanh nghiệp. Không giống như các ứng dụng web chạy trên nền trình duyệt, desktop app được cài đặt và vận hành trực tiếp trên hệ điều hành máy tính, tương tác sâu với tài nguyên phần cứng (file system, registry, drivers, thiết bị ngoại vi, GPU…) và đòi hỏi tiêu chuẩn rất cao về tính ổn định, độ bảo mật và hiệu năng.

Trong kỷ nguyên phát triển phần mềm theo các mô hình Agile/DevOps và CI/CD, chu kỳ phát hành phần mềm bị rút ngắn đáng kể. Các phương pháp kiểm thử thủ công (manual testing) thuần túy không còn đáp ứng kịp thời về tốc độ phản hồi lẫn độ phủ thử nghiệm, dễ dẫn đến hiện tượng trôi bug hoặc chậm tiến độ. Do đó, **Automation Testing** (Kiểm thử tự động) cho desktop applications trở thành một giải pháp tất yếu nhằm nâng cao chất lượng phần mềm và tối ưu chi phí kiểm thử dài hạn.

---

## 2. Lý do chọn đề tài

| Vấn đề thực tiễn | Lý do quan tâm nghiên cứu |
|---|---|
| **Vị trí của desktop app trong doanh nghiệp** | Nhiều hệ thống cốt lõi vẫn chạy trên desktop (ERP, SCADA, POS, ứng dụng xử lý dữ liệu nặng), nhu cầu kiểm thử chất lượng không suy giảm. |
| **Chi phí và hạn chế của kiểm thử thủ công** | Kiểm thử hồi quy bằng tay qua nhiều phiên bản tốn rất nhiều thời gian, công sức và dễ phát sinh sai sót do thao tác lặp lại. |
| **Độ phức tạp đặc thù của kiểm thử desktop** | Khác với web vốn chuẩn hóa theo DOM và HTML, desktop app phân mảnh sâu sắc theo framework UI (Win32, WPF, WinForms, Qt, Electron), đòi hỏi công cụ và kỹ thuật định danh chuyên biệt. |
| **Thách thức trong việc lựa chọn công cụ** | Hệ sinh thái công cụ automation desktop rất đa dạng (mã nguồn mở, thương mại, GUI-based, code-based), đội ngũ kiểm thử cần bộ tiêu chí rõ ràng để chọn đúng giải pháp. |
| **Xu hướng ứng dụng trí tuệ nhân tạo (AI)** | Các công nghệ GenAI và Computer Vision đang định hình lại cách sinh kịch bản kiểm thử, tự phục hồi selector (self-healing) và phân tích log lỗi. |

---

## 3. Mục tiêu seminar

```
┌─────────────────────────────────────────────────────────┐
│              MỤC TIÊU CỐT LÕI CỦA SEMINAR               │
│                                                         │
│  1. Làm chủ lý thuyết nền tảng về Automation Testing    │
│     dành riêng cho môi trường Desktop Applications      │
│                                                         │
│  2. Khảo sát thị trường và thiết lập bộ tiêu chí chuẩn  │
│     nhằm đánh giá, so sánh 2 công cụ đại diện           │
│                                                         │
│  3. Xây dựng kịch bản thực nghiệm và demo thực tế:      │
│     - Quy trình cài đặt môi trường                      │
│     - Kịch bản kiểm thử cơ bản (Record & Playback, DDT) │
│     - Kịch bản workflow phức tạp                        │
│                                                         │
│  4. Nghiên cứu tiềm năng ứng dụng AI trong hỗ trợ       │
│     tự động hóa kiểm thử desktop                        │
│                                                         │
│  5. Thiết kế bài tập thực hành ứng dụng cho lớp         │
└─────────────────────────────────────────────────────────┘
```

---

## 4. Phạm vi seminar

- **Hệ điều hành mục tiêu:** Môi trường Microsoft Windows (chiếm đa số các ứng dụng desktop doanh nghiệp).
- **Công nghệ ứng dụng thử nghiệm:** Ứng dụng xây dựng trên các nền tảng phổ biến như WinForms, WPF, Win32 hoặc Electron.
- **Kỹ thuật kiểm thử trọng tâm:**
  - Record & Playback (Ghi nhận và phát lại hành vi thao tác)
  - Data-Driven Testing (Kiểm thử điều khiển bằng dữ liệu)
  - Checkpoints & Assertions (Điểm kiểm tra trạng thái và dữ liệu)
  - Quản lý và xử lý đồng bộ hóa giao diện (Synchronization & Waits)
- **Mức độ nội dung:** Kết hợp từ cơ sở lý thuyết chuẩn mực đến thực hành triển khai mã nguồn demo và bài tập cụ thể.

---


# Phần 2: Cơ Sở Lý Thuyết Kiểm Thử Tự Động Desktop (Theory)

## Mục lục

1. [Automation Testing là gì?](#1-automation-testing-là-gì)
2. [Desktop Application Testing](#2-desktop-application-testing)
   - 2.1 [Phân loại Desktop Application](#21-phân-loại-desktop-application)
   - 2.2 [Các loại kiểm thử áp dụng cho Desktop App](#22-các-loại-kiểm-thử-áp-dụng-cho-desktop-app)
3. [Đặc điểm & Khó khăn đặc thù](#3-đặc-điểm--khó-khăn-đặc-thù)
   - 3.1 [Đặc điểm nổi bật](#31-đặc-điểm-nổi-bật)
   - 3.2 [Khó khăn đặc thù khi Automation](#32-khó-khăn-đặc-thù-khi-automation)
4. [Record & Playback](#4-record--playback)
   - 4.1 [Khái niệm](#41-khái-niệm)
   - 4.2 [Luồng hoạt động](#42-luồng-hoạt-động)
   - 4.3 [Ưu điểm & Nhược điểm](#43-ưu-điểm--nhược-điểm)
5. [Data-Driven Testing (DDT)](#5-data-driven-testing-ddt)
   - 5.1 [Khái niệm](#51-khái-niệm)
   - 5.2 [Ví dụ thực tế kịch bản đăng nhập](#52-ví-dụ-thực-tế-kịch-bản-đăng-nhập)
6. [Checkpoints & Assertions](#6-checkpoints--assertions)
   - 6.1 [Khái niệm](#61-khái-niệm)
   - 6.2 [Phân loại Checkpoint](#62-phân-loại-checkpoint)
   - 6.3 [Kiến trúc Assertion](#63-kiến-trúc-assertion)
7. [Fully vs Semi-Automated](#7-fully-vs-semi-automated)
   - 7.1 [Fully Automated](#71-fully-automated)
   - 7.2 [Semi-Automated](#72-semi-automated)
   - 7.3 [So sánh chi tiết](#73-so-sánh-chi-tiết)
8. [Ưu điểm & Nhược điểm của Automation Testing](#8-ưu-điểm--nhược-điểm-của-automation-testing)
9. [Khi nào nên dùng Automation Testing?](#9-khi-nào-nên-dùng-automation-testing)
10. [Bảng thuật ngữ chuyên ngành](#10-bảng-thuật-ngữ-chuyên-ngành)

---

## 1. Automation Testing là gì?

**Automation Testing** (Kiểm thử tự động) là quá trình áp dụng các công cụ phần mềm chuyên dụng nhằm thực thi tự động các kịch bản kiểm thử (test cases), tự động nhập dữ liệu đầu vào, tương tác với giao diện người dùng hoặc tầng API, và so sánh kết quả thực tế (actual results) với kết quả kỳ vọng (expected results) mà không cần sự can thiệp thủ công của con người trong quá trình chạy.

```
┌──────────────┐    Kịch bản kiểm thử    ┌──────────────────┐
│   Tester     │ ──────────────────────► │  Automation Tool │
│  (Thiết kế,  │                         │  (Thực thi test) │
│   Phân tích) │ ◄────────────────────── │                  │
└──────────────┘      Báo cáo kết quả    └────────┬─────────┘
                                                  │ Tương tác
                                                  ▼
                                         ┌──────────────────┐
                                         │  Ứng dụng cần    │
                                         │  kiểm thử (AUT)  │
                                         └──────────────────┘
```

> **Lưu ý:** Kiểm thử tự động không nhằm mục đích thay thế hoàn toàn con người. Tester vẫn giữ vai trò quyết định trong việc xây dựng chiến lược kiểm thử, thiết kế kịch bản kiểm thử biên/ngoại lệ, phân tích nguyên nhân lỗi và bảo trì bộ kịch bản tự động.

---

## 2. Desktop Application Testing

### 2.1 Phân loại Desktop Application

Khác với web applications chủ yếu dựa trên kiến trúc DOM HTML/CSS, các ứng dụng desktop được xây dựng trên nhiều kiến trúc và công nghệ giao diện khác nhau:

```
Desktop Applications
├── Ứng dụng bản địa thuần túy (Windows Native Apps)
│   ├── Win32 / MFC (C++, giao diện Windows truyền thống)
│   ├── WinForms (.NET Framework, mô hình hướng sự kiện)
│   ├── WPF (Windows Presentation Foundation - kiến trúc XAML, DirectX)
│   └── UWP (Universal Windows Platform - ứng dụng hiện đại từ Windows Store)
├── Ứng dụng đa nền tảng (Cross-Platform Native Apps)
│   ├── Qt (C++/QML, phổ biến trong hệ thống nhúng và công nghiệp)
│   └── JavaFX / Swing (Java Virtual Machine)
└── Ứng dụng lai (Hybrid / Embedded Web Apps)
    ├── Electron (Đóng gói Chromium + Node.js: VS Code, Slack, Teams)
    └── .NET MAUI / Blazor Hybrid (Kết hợp WebView2 và .NET)
```

Mỗi nền tảng UI trên đòi hỏi cơ chế nhận diện phần tử (Accessibility layer / UI Automation API) khác nhau, ảnh hưởng trực tiếp đến khả năng hỗ trợ của từng công cụ kiểm thử tự động.

### 2.2 Các loại kiểm thử áp dụng cho Desktop App

| Loại kiểm thử | Mục đích chính | Khả năng tự động hóa |
|---|---|---|
| **Functional Testing** | Xác minh các chức năng nghiệp vụ hoạt động đúng đặc tả | Rất phù hợp (Mức độ cao) |
| **Regression Testing** | Đảm bảo mã nguồn mới không làm hỏng tính năng đang chạy ổn định | Rất phù hợp (Mức độ rất cao) |
| **Smoke / Sanity Testing** | Kiểm tra nhanh các luồng cơ bản sau mỗi bản build mới | Rất phù hợp (Mức độ cao) |
| **UI Testing** | Kiểm tra bố cục, màu sắc, font chữ, trạng thái component | Phù hợp (Mức độ trung bình) |
| **Performance Testing** | Đo lường thời gian khởi động, mức chiếm dụng CPU, RAM, disk I/O | Rất phù hợp (Mức độ cao) |
| **Usability Testing** | Đánh giá độ thân thiện và trải nghiệm người dùng | Hạn chế (Cần con người đánh giá) |
| **Exploratory Testing** | Khám phá tự do nhằm tìm lỗi tiềm ẩn ngoài kịch bản định sẵn | Không khả thi (Đòi hỏi tư duy sáng tạo) |

---

## 3. Đặc điểm & Khó khăn đặc thù

### 3.1 Đặc điểm nổi bật

- **Tương tác sâu với hệ điều hành:** Desktop app chạy trực tiếp trên OS, truy cập trực tiếp vào hệ thống tệp tin, registry, tiến trình hệ thống, bộ nhớ và các dịch vụ nền.
- **Phụ thuộc cấu hình phần cứng và môi trường:** Độ phân giải màn hình, tỷ lệ co giãn DPI (DPI scaling), số lượng màn hình phụ (multi-monitor), card đồ họa, máy in, scanner... đều có thể làm thay đổi cách ứng dụng kết xuất giao diện.
- **Không có chuẩn DOM đồng nhất:** Mỗi công nghệ UI (Win32, WPF, Qt, Electron) dùng cây cấu trúc giao diện và thuộc tính nhận dạng hoàn toàn khác nhau.

### 3.2 Khó khăn đặc thù khi Automation

```
CÁC THÁCH THỨC CHÍNH TRONG DESKTOP AUTOMATION TESTING
───────────────────────────────────────────────────────────────
1. Nhận diện phần tử giao diện (Object Recognition)
   • Không có chuẩn CSS Selector hay thuộc tính ID nhất quán như web.
   • Nhiều control cũ (Win32 custom controls) không hỗ trợ UI Automation.
   • Giao diện bị ảnh hưởng bởi theme hệ điều hành, ngôn ngữ và DPI.

2. Đồng bộ hóa thời gian thực (Synchronization & Timing)
   • Không có sự kiện "Page Load" hay "Network Idle" rõ ràng như trình duyệt.
   • Dễ dẫn đến lỗi kịch bản chạy nhanh hơn tốc độ render của app (Flaky test).
   • Cần cơ chế chờ thông minh (Explicit Wait) thay vì thời gian chờ cố định (Sleep).

3. Quản lý cửa sổ và hộp thoại hệ thống
   • Các popup hệ điều hành (Open/Save File Dialog, Print Dialog) là tiến trình riêng.
   • Xử lý đa cửa sổ (MDI - Multiple Document Interface) đòi hỏi chuyển đổi ngữ cảnh.

4. Môi trường thực thi kịch bản (Execution Environment)
   • Khó chạy chế độ không màn hình (Headless mode) như web; cần Desktop Session thật.
   • Màn hình bị khóa (Lock screen) hoặc thu nhỏ (Minimize) có thể làm gián đoạn test.

5. Chi phí bảo trì kịch bản kiểm thử (Script Maintenance)
   • Khi nhà phát triển thay đổi giao diện, selector có thể bị đứt gãy hàng loạt.
   • Chi phí bảo trì nếu thiết kế kịch bản kém có thể vượt quá chi phí kiểm thử thủ công.
```

---

## 4. Record & Playback

### 4.1 Khái niệm

**Record & Playback** (Ghi và Phát lại) là kỹ thuật kiểm thử tự động trong đó công cụ lắng nghe và ghi nhận các thao tác chuột (click, drag-drop) và bàn phím (keystrokes) của người dùng trên ứng dụng cần kiểm thử. Sau đó, công cụ lưu lại chuỗi hành động này dưới dạng kịch bản để có thể tự động chạy lại nhiều lần.

```
GIAI ĐOẠN GHI (RECORD)               GIAI ĐOẠN PHÁT LẠI (PLAYBACK)
──────────────────────               ────────────────────────────
Tester thao tác trực tiếp            Công cụ tự động gửi tín hiệu
trên ứng dụng (AUT)       ──Script──► mô phỏng hành vi người dùng
                                     và kiểm tra kết quả kỳ vọng
Công cụ bắt đối tượng UI
và sinh mã kịch bản
```

### 4.2 Luồng hoạt động

```
[Bắt đầu quá trình Record]
            │
            ▼
[Tester thao tác các bước kiểm thử trên AUT]
            │
            ▼
[Công cụ bắt sự kiện: Control Name, AutomationId, Tọa độ, Thao tác nhập]
            │
            ▼
[Công cụ tự động sinh mã kịch bản (C#, Python, Groovy, VBScript...)]
            │
            ▼
[Tester bổ sung các Checkpoint / Assertion và tối ưu hóa selector]
            │
            ▼
[Chạy Playback: Công cụ điều khiển AUT và đối chiếu kết quả]
            │
            ▼
[Xuất báo cáo kết quả kiểm thử (Thành công / Thất bại)]
```

### 4.3 Ưu điểm & Nhược điểm

| Tiêu chí | Ưu điểm | Nhược điểm |
|---|---|---|
| **Độ dốc tiếp cận** | Rất dễ học, người kiểm thử không cần kiến thức lập trình sâu. | Dễ phụ thuộc vào công cụ, khó tùy biến luồng phức tạp. |
| **Thời gian tạo test** | Nhanh chóng tạo được kịch bản kiểm thử ban đầu. | Kịch bản sinh ra thường dài dòng, dư thừa nhiều thao tác thừa. |
| **Bảo trì** | Thích hợp tạo nhanh smoke test đơn giản ban đầu. | Rất dễ bị gãy (fragile) khi giao diện thay đổi dù chỉ một vị trí nhỏ. |
| **Xử lý dữ liệu** | Phù hợp với dữ liệu cố định trong kịch bản mẫu. | Không xử lý được dữ liệu động, logic phân nhánh hay vòng lặp. |

---

## 5. Data-Driven Testing (DDT)

### 5.1 Khái niệm

**Data-Driven Testing (DDT)** là phương pháp kiểm thử tự động tách rời hoàn toàn **logic của kịch bản kiểm thử** khỏi **tập dữ liệu kiểm thử**. Một kịch bản logic duy nhất được tham số hóa (parameterized) và thực thi lặp lại nhiều lần với từng dòng dữ liệu lấy từ nguồn lưu trữ bên ngoài (Excel, CSV, JSON, Database hoặc API).

```
┌────────────────────────┐      ┌──────────────────────────────────┐
│ Kịch bản kiểm thử      │◄─────│ Nguồn dữ liệu kiểm thử           │
│ (Logic kịch bản chung) │      │ (Excel / CSV / DB / JSON)        │
└───────────┬────────────┘      │                                  │
            │                   │ Dòng 1: admin / P@ssw0rd1        │
            │ Lần chạy 1        │ Dòng 2: user_01 / wrong_pass     │
            │ Lần chạy 2        │ Dòng 3: empty_user / 123456      │
            │ Lần chạy 3        └──────────────────────────────────┘
            ▼
┌────────────────────────┐
│ Báo cáo kết quả        │
│ (Kết quả chi tiết cho  │
│ từng bộ dữ liệu)       │
└────────────────────────┘
```

### 5.2 Ví dụ thực tế kịch bản đăng nhập

Kịch bản kiểm thử tổng quát cho chức năng đăng nhập:

```
HÀM KIỂM THỬ: test_login(username, password, expected_outcome)
───────────────────────────────────────────────────────────────────
Bước 1: Khởi chạy ứng dụng và điều hướng đến màn hình Đăng nhập
Bước 2: Xóa trường Username và nhập giá trị: {username}
Bước 3: Xóa trường Password và nhập giá trị: {password}
Bước 4: Nhấn nút "Đăng nhập"
Bước 5: Kiểm tra kết quả thực tế hiển thị phải khớp với: {expected_outcome}
```

Bảng dữ liệu đầu vào (tập tin `login_dataset.xlsx`):

| Trường hợp | username | password | expected_outcome |
|---|---|---|---|
| TC01: Đăng nhập hợp lệ | `admin_system` | `Secured#2026` | Chuyển đến màn hình Dashboard chính |
| TC02: Sai mật khẩu | `admin_system` | `wrong_pass` | Thông báo: "Mật khẩu không chính xác" |
| TC03: Để trống tài khoản | *(để trống)* | `12345678` | Thông báo: "Tên đăng nhập không được để trống" |
| TC04: Để trống mật khẩu | `admin_system` | *(để trống)* | Thông báo: "Mật khẩu không được để trống" |
| TC05: Tài khoản bị khóa | `locked_user` | `User@1234` | Thông báo: "Tài khoản hiện đang bị tạm khóa" |

---

## 6. Checkpoints & Assertions

### 6.1 Khái niệm

**Checkpoint** (hay **Assertion**) là điểm kiểm tra trong kịch bản tự động, tại đó công cụ lấy trạng thái/giá trị thực tế của ứng dụng (Actual Result) và đem so sánh với trạng thái/giá trị kỳ vọng (Expected Result).

> **Lưu ý:** Một kịch bản tự động thực hiện từ đầu đến cuối mà **không có checkpoint** thì chỉ là một đoạn script mô phỏng thao tác người dùng (bot tự động), không thể coi là kịch bản kiểm thử hợp lệ vì không có cơ chế kết luận PASS hay FAIL.

### 6.2 Phân loại Checkpoint

| Loại Checkpoint | Đối tượng kiểm tra | Ví dụ áp dụng trên Desktop App |
|---|---|---|
| **Text / Value Checkpoint** | Nội dung chuỗi ký tự hiển thị trên control | Kiểm tra nhãn trạng thái hiển thị "Đăng nhập thành công" |
| **Property Checkpoint** | Thuộc tính của thành phần giao diện | Nút "Lưu" chuyển từ Disabled sang Enabled sau khi điền đủ form |
| **Bitmap / Image Checkpoint** | So sánh ảnh chụp pixel hoặc vùng ảnh | Kiểm tra đồ thị phân tích hoặc hình vẽ kết xuất đúng chuẩn |
| **Table / DataGrid Checkpoint** | Toàn bộ dữ liệu hiển thị trong bảng | Đối chiếu danh sách 100 giao dịch hiển thị trên DataGridView |
| **File Checkpoint** | Tệp tin xuất ra từ ứng dụng | So sánh tệp báo cáo PDF/Excel xuất ra với tệp chuẩn mẫu |
| **Database Checkpoint** | Dữ liệu lưu xuống cơ sở dữ liệu ngầm | Kiểm tra sau khi nhấn Save, một bản ghi mới được thêm vào DB |

### 6.3 Kiến trúc Assertion

```
[Thực hiện hành động thao tác trên AUT]
                  │
                  ▼
[Trích xuất giá trị thực tế từ phần tử UI (Actual Value)]
                  │
                  ▼
[So sánh đối chiếu với giá trị kỳ vọng (Expected Value)]
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
  Khớp giá trị         Không khớp giá trị
(Test Case PASS)       (Test Case FAIL)
                            │
                            ▼
              [Chụp ảnh màn hình tại thời điểm lỗi]
              [Ghi log chi tiết thông số và stacktrace]
              [Đánh dấu trạng thái lỗi vào báo cáo]
```

---

## 7. Fully vs Semi-Automated

### 7.1 Fully Automated

Toàn bộ quy trình kiểm thử từ khâu thiết lập môi trường, chuẩn bị dữ liệu, mở ứng dụng, thực thi các bước, kiểm tra kết quả cho tới khâu xuất báo cáo và dọn dẹp môi trường đều diễn ra tự động hoàn toàn mà không cần sự can thiệp của con người.

```
Đường ống hoàn toàn tự động (Fully Automated Pipeline):
Kích hoạt CI/CD ──► Biên dịch mã ──► Triển khai build ──► Chạy Test Suite ──► Xuất báo cáo ──► Gửi thông báo
                                                              (Tự động 100%)
```

**Trường hợp áp dụng tối ưu:**
- Bộ kịch bản kiểm thử hồi quy (Regression Test Suite) đã ổn định
- Kiểm thử Smoke Test nhanh sau mỗi bản build mới
- Kịch bản chạy theo lịch định kỳ ban đêm (Nightly Builds)

### 7.2 Semi-Automated

Kết hợp giữa công cụ tự động và thao tác thủ công của kiểm thử viên. Công cụ sẽ đảm nhận các bước lặp lại tốn thời gian (như tạo tài khoản hàng loạt, nhập form dài, điều hướng đến màn hình cần kiểm tra), sau đó nhường quyền cho con người quan sát, đánh giá trực quan hoặc can thiệp các bước đặc biệt.

```
Quy trình bán tự động (Semi-Automated Flow):
[Tự động]: Tạo 50 bản ghi dữ liệu mẫu và mở sẵn form chỉnh sửa chi tiết
     │
     ▼
[Thủ công]: Tester kiểm tra độ mượt đồ họa, cảm quan giao diện và khả năng tương tác
     │
     ▼
[Tự động]: Công cụ lưu log, chụp ảnh màn hình và cập nhật kết quả vào hệ thống quản lý test
```

**Trường hợp áp dụng tối ưu:**
- Kiểm thử trải nghiệm người dùng (Usability Testing) đòi hỏi cảm nhận con người
- Kiểm thử khám phá (Exploratory Testing) cần công cụ hỗ trợ chuẩn bị dữ liệu
- Các trường hợp kiểm thử liên quan đến thiết bị phần cứng đặc biệt cần cắm/rút thủ công

### 7.3 So sánh chi tiết

| Tiêu chí | Fully Automated | Semi-Automated |
|---|---|---|
| **Chi phí đầu tư ban đầu** | Cao (cần thiết kế framework, wait thông minh, tích hợp CI) | Trung bình (script đơn giản hỗ trợ từng tác vụ) |
| **Tốc độ thực thi** | Rất nhanh, có thể chạy không cần giám sát | Phụ thuộc vào tốc độ thao tác của người kiểm thử |
| **Độ ổn định** | Cao nếu framework chuẩn, nhạy cảm với thay đổi UI | Linh hoạt cao vì con người xử lý được các tình huống bất ngờ |
| **Khả năng tích hợp CI/CD** | Tích hợp hoàn hảo vào đường ống tự động | Không tích hợp hoàn toàn được vì cần tương tác người |
| **Ứng dụng chính** | Regression Testing, Smoke Testing, Performance Testing | Usability Testing, Exploratory Testing, Phần cứng đặc thù |

---

## 8. Ưu điểm & Nhược điểm của Automation Testing

### Ưu điểm

| STT | Ưu điểm | Phân tích giá trị |
|---|---|---|
| 1 | **Tốc độ thực thi vượt trội** | Script thực hiện các thao tác nhập liệu và kiểm tra nhanh hơn con người nhiều lần. |
| 2 | **Độ bao phủ cao** | Có khả năng chạy hàng trăm kịch bản kiểm thử với hàng nghìn bộ dữ liệu khác nhau trong thời gian ngắn. |
| 3 | **Độ chính xác và tính nhất quán** | Loại bỏ hoàn toàn sự mệt mỏi, nhầm lẫn hay bỏ sót bước thường gặp ở con người khi làm việc lặp lại. |
| 4 | **Khả năng tái sử dụng (Reusability)** | Kịch bản sau khi xây dựng có thể tái sử dụng cho nhiều bản build, phiên bản phát hành và môi trường khác nhau. |
| 5 | **Phát hiện sớm lỗi hồi quy** | Tự động cảnh báo ngay lập tức nếu thay đổi code mới làm hỏng các tính năng cũ đã ổn định. |
| 6 | **Vận hành không giới hạn 24/7** | Có thể lên lịch chạy ngoài giờ làm việc hoặc trên các máy chủ tự động mà không cần nhân sự trực tiếp. |
| 7 | **Hỗ trợ tối đa cho CI/CD** | Cung cấp phản hồi tức thì (fast feedback loop) cho đội ngũ phát triển sau mỗi lần tích hợp mã nguồn. |

### Nhược điểm

| STT | Nhược điểm | Thách thức thực tế |
|---|---|---|
| 1 | **Chi phí đầu tư ban đầu lớn** | Tốn chi phí mua bản quyền công cụ (nếu dùng tool thương mại) và thời gian xây dựng framework ban đầu. |
| 2 | **Gánh nặng bảo trì (Maintenance Overhead)** | Khi giao diện phần mềm thay đổi, kịch bản kiểm thử cần cập nhật liên tục; nếu thiết kế kém có thể gây nợ kỹ thuật. |
| 3 | **Không thể thay thế kiểm thử thủ công hoàn toàn** | Không phát hiện được các lỗi về mặt thị giác tinh tế, trải nghiệm người dùng hoặc các kịch bản bất thường ngoài logic lập trình. |
| 4 | **Yêu cầu kỹ năng lập trình chuyên sâu** | Đòi hỏi kiểm thử viên phải có tư duy phát triển phần mềm, hiểu về cấu trúc ứng dụng và kỹ thuật viết mã sạch. |
| 5 | **Nguy cơ lỗi sai lệch (False Positives / Negatives)** | Kịch bản có thể báo lỗi do thời gian chờ không chuẩn (chứ không phải app lỗi), làm mất thời gian điều tra nguyên nhân. |
| 6 | **Thời gian hoàn vốn (ROI) cần độ trễ** | Không mang lại hiệu quả ngay lập tức cho các dự án ngắn hạn, quy mô nhỏ hoặc đang trong giai đoạn thử nghiệm ý tưởng. |

---

## 9. Khi nào nên dùng Automation Testing?

```
BẢNG QUYẾT ĐỊNH ÁP DỤNG KIỂM THỬ TỰ ĐỘNG
──────────────────────────────────────────────────────────────────────────
NÊN ÁP DỤNG AUTOMATION                      KHÔNG NÊN ÁP DỤNG AUTOMATION
──────────────────────────────────          ──────────────────────────────
• Kịch bản kiểm thử lặp đi lặp lại nhiều lần • Kịch bản chỉ chạy 1 đến 2 lần rồi bỏ
• Bộ kịch bản kiểm thử hồi quy quy mô lớn   • Ứng dụng có giao diện thay đổi liên tục
• Kiểm thử cần số lượng dữ liệu lớn (DDT)   • Kiểm thử đòi hỏi cảm nhận và phán đoán chủ quan
• Kịch bản cần chạy trên nhiều cấu hình OS   • Chi phí viết kịch bản lớn hơn thời gian tiết kiệm
• Cần kết quả kiểm tra nhanh trong CI/CD    • Dự án ngắn hạn, gấp rút về thời gian bàn giao
• Tính năng nghiệp vụ cốt lõi đã ổn định    • Tính năng đang trong giai đoạn thiết kế thử nghiệm
```

> **Quy tắc thực tế (Rule of Thumb):** Nếu một kịch bản kiểm thử dự kiến phải thực thi lặp lại **từ 3 lần trở lên** trong vòng đời sản phẩm, đó là ứng viên sáng giá để chuyển đổi sang kịch bản tự động hóa.

---

## 10. Bảng thuật ngữ chuyên ngành

| Thuật ngữ tiếng Anh | Viết tắt | Định nghĩa và giải thích ý nghĩa |
|---|---|---|
| **Automation Testing** | AT | Quá trình sử dụng phần mềm để thực thi kiểm thử và so sánh kết quả tự động |
| **Application Under Test** | AUT | Ứng dụng cụ thể đang được hướng tới để thực hiện kiểm thử |
| **Record & Playback** | R&P | Kỹ thuật ghi lại các hành vi tương tác và phát lại tự động |
| **Data-Driven Testing** | DDT | Phương pháp kiểm thử tách rời logic và dữ liệu kiểm thử |
| **Checkpoint / Assertion** | — | Điểm kiểm tra logic để kết luận kịch bản đạt (PASS) hay không đạt (FAIL) |
| **Regression Testing** | — | Kiểm thử hồi quy nhằm đảm bảo việc sửa lỗi hoặc thêm tính năng mới không làm hỏng tính năng cũ |
| **Smoke Testing** | — | Kiểm thử sơ bộ các luồng chức năng quan trọng nhất để quyết định chấp nhận bản build |
| **Continuous Integration / Continuous Delivery** | CI/CD | Phương pháp tích hợp và bàn giao mã nguồn tự động liên tục |
| **False Positive** | — | Hiện tượng kịch bản báo kiểm thử thất bại (FAIL) nhưng thực tế ứng dụng vẫn hoạt động đúng |
| **False Negative** | — | Hiện tượng kịch bản báo kiểm thử thành công (PASS) nhưng thực tế ứng dụng đang tồn tại lỗi |
| **Flaky Test** | — | Kịch bản kiểm thử không ổn định, cho kết quả khác nhau giữa các lần chạy dù mã nguồn không đổi |
| **Test Suite** | — | Tập hợp các kịch bản kiểm thử liên quan được gom nhóm để thực thi cùng nhau |
| **Page Object Model** | POM | Mẫu thiết kế phần mềm tách biệt giao diện màn hình khỏi logic các bước kiểm thử |
| **Keyword-Driven Testing** | KDT | Phương pháp kiểm thử dựa trên các từ khóa hành động được định nghĩa trước |
| **Windows Presentation Foundation** | WPF | Nền tảng phát triển giao diện Windows dựa trên ngôn ngữ XAML và DirectX |
| **Universal Windows Platform** | UWP | Nền tảng ứng dụng đa thiết bị hiện đại của Microsoft Windows |
| **UI Automation** | UIA | Bộ giao diện lập trình ứng dụng (API) của Windows cho phép đọc và điều khiển thành phần UI |
| **Return on Investment** | ROI | Tỷ số hoàn vốn đầu tư, đo lường hiệu quả kinh tế của việc áp dụng automation |

---

> **Phụ trách:** Tín  
> **Cập nhật lần cuối:** 02/10/2026  
> **Trạng thái:** Hoàn thành

---


# Phần 3: Khảo Sát Thị Trường & Bộ Tiêu Chí Đánh Giá (Tool Survey)

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

---


# Phần 4: Nghiên Cứu Công Cụ Đại Diện A – Katalon Studio

## 1. Tổng quan về Katalon Studio

### 1.1 Thông tin chung
* **Đơn vị phát triển:** Katalon Inc.
* **Mô hình bản quyền:** Freemium (Bản Free đáp ứng đầy đủ các tính năng cơ bản cho kiểm thử Desktop; các gói trả phí Enterprise/TestOps bổ sung tính năng nâng cao và báo cáo đám mây).
* **Phạm vi hỗ trợ:** Đa nền tảng kiểm thử (Web, API, Mobile và Windows Desktop). Đối với Desktop App, công cụ tập trung hỗ trợ nền tảng Windows.
* **Ngôn ngữ viết kịch bản:** Groovy / Java.
* **Chế độ soạn thảo kép (Dual-view):**
  * *Manual View:* Giao diện dạng bảng (Action - Object - Value) trực quan, cho phép xây dựng kịch bản kiểm thử mà không cần viết code.
  * *Script View:* Chế độ code Groovy thuần, cho phép tùy biến logic, xử lý điều kiện, vòng lặp phức tạp.

### 1.2 Lý do lựa chọn cho seminar
1. **Chi phí 0 đồng:** Bản Free không giới hạn thời gian dùng thử (loại bỏ rủi ro hết hạn bản quyền trong quá trình học tập và báo cáo).
2. **Tích hợp sẵn trọn bộ công cụ:** Có sẵn trình ghi kịch bản (Recorder), trình soi phần tử (Object Spy), kho lưu đối tượng tập trung (Object Repository) và hệ thống báo cáo (Reporting).
3. **Phù hợp với nhiều đối tượng:** Người chưa biết lập trình có thể tiếp cận qua Manual View; người muốn can thiệp kỹ thuật có thể viết mã qua Script View.

---

## 2. Nguyên lý hoạt động trên Desktop App

### 2.1 Kiến trúc thực thi
Katalon Studio kiểm thử ứng dụng Desktop Windows thông qua kiến trúc phân tầng chuẩn WebDriver:

```
┌──────────────────────────────────────────────┐
│  Katalon Studio (IDE / Test Engine)          │
│  - Test Cases, Object Repository, Test Data  │
└──────────────────────┬───────────────────────┘
                       │ HTTP / WebDriver Protocol (Port 4723)
                       ▼
┌──────────────────────────────────────────────┐
│  Microsoft WinAppDriver                      │
│  (Windows Application Driver Service)        │
└──────────────────────┬───────────────────────┘
                       │ Native API Calls
                       ▼
┌──────────────────────────────────────────────┐
│  Windows UI Automation (UIA) Engine          │
└──────────────────────┬───────────────────────┘
                       │ Điều khiển trực tiếp
                       ▼
┌──────────────────────────────────────────────┐
│  Application Under Test (AUT)                │
│  (WPF, WinForms, UWP, Win32)                 │
└──────────────────────────────────────────────┘
```

1. **Gửi lệnh:** Kịch bản kiểm thử trong Katalon sinh ra các yêu cầu HTTP theo chuẩn JSON Wire / W3C WebDriver.
2. **Thông dịch:** WinAppDriver (dịch vụ chạy nền ở cổng `4723`) tiếp nhận yêu cầu và chuyển đổi thành lời gọi hàm của Windows UI Automation (UIA).
3. **Tương tác:** Hệ điều hành Windows tương tác trực tiếp lên các thành phần giao diện (nhấp chuột, nhập văn bản, đọc giá trị).
4. **Phản hồi:** Trạng thái thực thi và dữ liệu giao diện được trả ngược về Katalon để đánh giá kết quả (Pass/Fail).

### 2.2 Nhận diện phần tử giao diện (Object Recognition)
* **Windows Object Spy:** Cho phép trỏ chuột vào phần tử giao diện để bóc tách các thuộc tính nhận dạng do Windows UIA cung cấp.
* **Object Repository:** Nơi lưu trữ tập trung các phần tử (Object). Mỗi test step chỉ tham chiếu đến Object này, giúp giảm chi phí bảo trì khi giao diện thay đổi (chỉ cần sửa locator tại một nơi duy nhất).
* **Độ ưu tiên của thuộc tính định vị (Locator):**
  1. `AutomationId`: Định danh duy nhất do lập trình viên gắn, độc lập với ngôn ngữ giao diện $\rightarrow$ **Ưu tiên số 1**.
  2. `Name`: Nhãn hiển thị của control $\rightarrow$ Dễ bị gãy kịch bản nếu ứng dụng đổi text hoặc đổi ngôn ngữ hiển thị.
  3. `ClassName` / `ControlType`: Loại phần tử giao diện $\rightarrow$ Kết hợp khi phần tử thiếu định danh duy nhất.
  4. `XPath`: Cấu trúc phân cấp cây giao diện $\rightarrow$ Thường dài và dễ vỡ khi bố cục màn hình cập nhật.

---

## 3. Ba Năng Lực Cốt Lõi (Theo Lý Thuyết Kiểm Thử)

### 3.1 Record & Playback (Ghi & Phát lại kịch bản)
* **Khái niệm:** Kỹ thuật ghi nhận chuỗi thao tác chuột và bàn phím của tester trên ứng dụng thật, sau đó tự động chuyển đổi thành mã kịch bản để thực thi lại.
* **Cách Katalon hỗ trợ:**
  * Tính năng **Windows Recorder** tự động mở ứng dụng, lắng nghe sự kiện người dùng và tự động lưu các control vào Object Repository.
  * Tự sinh ra các từ khóa hành động (`Start Application Window`, `Click`, `Set Text`).
* **Ưu điểm & Hạn chế:**
  * *Ưu điểm:* Xây dựng kịch bản kiểm thử ban đầu rất nhanh, không đòi hỏi kỹ năng lập trình sâu.
  * *Hạn chế:* Dữ liệu bị gán cứng (hard-coded); kịch bản dễ bị lỗi gián đoạn (flaky) nếu không bổ sung các bước chờ đồng bộ (Wait) và chuẩn hóa lại locator.

### 3.2 Checkpoints & Assertions (Điểm kiểm tra kết quả)
* **Khái niệm:** Điểm so sánh giữa kết quả thực tế (**Actual Result**) và kết quả kỳ vọng (**Expected Result**) nhằm tự động hóa vai trò của Test Oracle. Kịch bản không có Checkpoint chỉ là bot thao tác tự động, không thể coi là kịch bản kiểm thử.
* **Bộ từ khóa Verify trong Katalon:**
  * `Verify Element Text`: Kiểm tra nội dung chuỗi (ví dụ: thông báo lỗi, nhãn kết quả).
  * `Verify Element Attribute Value`: Kiểm tra trạng thái thuộc tính (ví dụ: nút bấm chuyển sang Disabled, ô nhập bị khóa).
  * `Verify Element Present`: Kiểm tra sự xuất hiện của cửa sổ mới, popup cảnh báo.
* **Cơ chế bắt lỗi:** Khi giá trị thực tế không khớp với giá trị kỳ vọng, kịch bản tự động dừng hoặc tiếp tục tùy cấu hình, chụp ảnh màn hình tại thời điểm lỗi và ghi log phục vụ báo cáo lỗi (Bug Report).

### 3.3 Data-Driven Testing (Kiểm thử hướng dữ liệu)
* **Khái niệm:** Tách rời kịch bản kiểm thử khỏi tập dữ liệu đầu vào. Một logic kiểm thử duy nhất được tham số hóa bằng các biến và chạy lặp qua nhiều bộ dữ liệu khác nhau.
* **Cách Katalon hỗ trợ:**
  * Hỗ trợ nguồn dữ liệu ngoài: File **Excel**, **CSV**, Database hoặc Internal Data.
  * Tab **Variables** trong Test Case định nghĩa các biến (ví dụ: `var_A`, `var_B`, `var_Expected`).
  * Cơ chế Data Binding trong Test Suite cho phép liên kết từng cột dữ liệu với biến của Test Case.
* **Ý nghĩa thực tế:**
  * Giúp thực thi nhanh chóng các kỹ thuật thiết kế ca kiểm thử hộp đen như **Phân hoạch tương đương (Equivalence Partitioning)** và **Phân tích giá trị biên (Boundary Value Analysis - BVA)**.
  * Mở rộng độ bao phủ kiểm thử mà không cần viết lại kịch bản (chỉ cần bổ sung các dòng dữ liệu vào file Excel).

---

## 4. Đánh Giá Ưu Điểm & Nhược Điểm

### 4.1 Ưu điểm
1. **Tiếp cận nhanh và dễ sử dụng:** Giao diện thân thiện, tài liệu hướng dẫn đầy đủ, cộng đồng người dùng đông đảo.
2. **Tích hợp toàn diện:** Cung cấp sẵn cơ chế quản lý dự án, Object Repository, Test Suite, quản lý dữ liệu và xuất báo cáo (HTML, JUnit) mà không cần cài thêm thư viện ngoài.
3. **Hỗ trợ bảo trì tốt:** Mô hình Object Repository giúp việc cập nhật locator khi phần mềm thay đổi diễn ra tập trung, tránh sửa hàng loạt script.
4. **Sẵn sàng tích hợp CI/CD:** Hỗ trợ chạy kịch bản thông qua dòng lệnh (Katalon Runtime Engine) để tích hợp vào Jenkins, GitHub Actions.

### 4.2 Nhược điểm & Rào cản kỹ thuật
1. **Phụ thuộc vào WinAppDriver:** Dự án WinAppDriver của Microsoft hiện đã ngừng phát triển tính năng mới (archive), điều này tiềm ẩn rủi ro dài hạn về khả năng tương thích với các bản cập nhật Windows tương lai.
2. **Khó nhận diện ứng dụng không chuẩn:** Đối với các ứng dụng desktop dựng bằng công nghệ tùy biến (Custom Controls, giao diện vẽ bằng Canvas/DirectX, Qt thuần không hỗ trợ UIA), Object Spy không thể bắt được control chi tiết.
3. **Tiêu tốn tài nguyên:** IDE tương đối nặng, thời gian khởi động lâu và yêu cầu kết nối mạng để xác thực tài khoản bản quyền khi khởi động.
4. **Hạn chế ở bản Free:** Các tính năng nâng cao như kiểm thử hình ảnh (Visual Testing), AI Self-healing và chạy kiểm thử song song bị giới hạn trong bản miễn phí.

---

## 5. Định Hướng Kịch Bản Demo Cho Nhóm

Để đảm bảo tính khách quan và có thể so sánh công bằng với Tool B, kịch bản demo được thiết kế theo 3 cấp độ:

```
[Demo 1: Thiết lập] ──► [Demo 2: Cơ bản] ──► [Demo 3: Nâng cao]
 Cấu hình môi trường    Record & Playback     Data-Driven (BVA)
 Nhận diện control      Gán Checkpoint        Chuyển trạng thái
```

### 5.1 Demo 1: Cài đặt và chuẩn bị môi trường
* **Mục tiêu:** Chứng minh tính dễ tiếp cận và khả năng kết nối của công cụ.
* **Các bước chính:**
  1. Kích hoạt *Developer Mode* trên Windows và khởi động `WinAppDriver.exe`.
  2. Tạo Project mới kiểu Windows trong Katalon Studio.
  3. Dùng *Windows Object Spy* soi vào ứng dụng mẫu (Calculator hoặc ứng dụng WPF) để kiểm tra các thuộc tính UIA (`AutomationId`, `Name`).

### 5.2 Demo 2: Thao tác cơ bản (Record & Playback + Checkpoint)
* **Mục tiêu:** Minh họa quy trình tự động hóa kịch bản kiểm thử chuẩn (ví dụ: Chức năng Đăng nhập).
* **Các bước chính:**
  1. Dùng *Windows Recorder* ghi lại thao tác nhập tài khoản, mật khẩu và bấm Submit.
  2. Chuẩn hóa lại các đối tượng đã ghi trong Object Repository.
  3. Thêm bước `Verify Element Text` để kiểm tra thông báo kết quả.
  4. Thực thi kịch bản (Playback) và minh họa trường hợp cố tình kiểm tra sai để xem cơ chế báo lỗi (chụp màn hình và xuất log).

### 5.3 Demo 3: Kịch bản nâng cao (Data-Driven BVA + Luồng nghiệp vụ)
* **Mục tiêu:** Minh họa khả năng chạy kiểm thử tự động với dữ liệu lớn theo kỹ thuật phân tích giá trị biên.
* **Các bước chính:**
  1. Chuẩn bị file Excel chứa tập dữ liệu biên (ví dụ: các giá trị biên hợp lệ và không hợp lệ của bài toán tính tổng 2 số nguyên).
  2. Tạo kịch bản tính toán có tham số hóa và thực hiện liên kết dữ liệu (Data Binding).
  3. Thực thi tự động toàn bộ danh sách dữ liệu trong một lần chạy và xem báo cáo kết quả chi tiết từng dòng dữ liệu.

---

## 6. Khi Nào Nên & Không Nên Chọn Katalon Studio

| Nên chọn Katalon Studio | Khi nào nên cân nhắc công cụ khác |
|---|---|
| Đội ngũ có cả nhân sự Manual Tester và Automation Tester (cần Dual-view). | Đội ngũ thuần Developer / SDET muốn viết code kiểm thử trực tiếp trong Visual Studio / VS Code (nên chọn WinAppDriver + C# hoặc PyWinAuto). |
| Cần triển khai nhanh mà không tốn thời gian xây dựng framework từ đầu. | Ứng dụng vẽ hoàn toàn bằng đồ họa custom hoặc công nghệ nhúng không hỗ trợ Windows UIA (cần công cụ so khớp hình ảnh như SikuliX). |
| Dự án có ngân sách hạn chế (cần bản miễn phí ổn định). | Dự án doanh nghiệp quy mô lớn đòi hỏi kiểm thử đa nền tảng (cả macOS, Linux) cho cùng một mã nguồn desktop. |

---


# Phần 5: Nghiên Cứu Công Cụ Đại Diện B – Microsoft WinAppDriver

## 1. Tổng quan về Microsoft WinAppDriver

### 1.1 Thông tin chung
* **Đơn vị phát triển:** Microsoft Corporation.
* **Mô hình bản quyền:** Mã nguồn mở (Open Source - Hoàn toàn miễn phí, không giới hạn tính năng hay thời gian sử dụng).
* **Chuẩn công nghệ:** Tuân thủ giao thức **W3C WebDriver** và chuẩn **Appium**.
* **Phạm vi hỗ trợ:** Kiểm thử tự động các ứng dụng chạy trên hệ điều hành Windows (UWP, WPF, WinForms, Win32).
* **Ngôn ngữ viết kịch bản:** Đa ngôn ngữ (C#/.NET, Python, Java, JavaScript/TypeScript...). Trong đó, **C#** và **Python** là hai ngôn ngữ phổ biến và tối ưu nhất.
* **Trường phái tiếp cận:** **Code-based / Developer-centric** (Kiểm thử thuần viết mã). Người kiểm thử làm việc trực tiếp trên các IDE tiêu chuẩn như Visual Studio, Rider hoặc VS Code.

### 1.2 Lý do lựa chọn làm Tool B đối trọng với Tool A
1. **Tạo ra sự đối lập rõ nét:** Nếu Katalon Studio đại diện cho trường phái *All-in-one GUI Tool* (có giao diện bọc ngoài, hỗ trợ kéo thả / low-code), thì WinAppDriver đại diện cho trường phái *Pure Code / SDK* (lập trình kiểm thử chuyên sâu cho Developer / SDET).
2. **Cùng chung nền tảng cốt lõi:** Cả hai công cụ đều sử dụng Windows UI Automation (UIA) để tương tác với ứng dụng. Điều này giúp việc so sánh giữa hai công cụ đạt tính khách quan tuyệt đối (chạy cùng đường đua, cùng case study).
3. **Chuẩn công nghiệp phổ biến:** Áp dụng cú pháp WebDriver quen thuộc (tương tự như Selenium trên Web và Appium trên Mobile), giúp người học dễ dàng kế thừa kỹ năng kiểm thử.

---

## 2. Nguyên lý hoạt động trên Desktop App

### 2.1 Kiến trúc thực thi
WinAppDriver hoạt động như một REST API Server độc lập đóng vai trò trung gian giữa kịch bản kiểm thử và hệ điều hành:

```
┌──────────────────────────────────────────────┐
│  Test Script (C# / NUnit hoặc Python/pytest) │
│  - Dùng Appium / Selenium Client Library     │
└──────────────────────┬───────────────────────┘
                       │ HTTP / JSON Wire / W3C WebDriver (Port 4723)
                       ▼
┌──────────────────────────────────────────────┐
│  Microsoft WinAppDriver.exe                  │
│  (Lắng nghe tại 127.0.0.1:4723)             │
└──────────────────────┬───────────────────────┘
                       │ Native API Calls (C++ / COM)
                       ▼
┌──────────────────────────────────────────────┐
│  Windows UI Automation (UIA) Engine          │
└──────────────────────┬───────────────────────┘
                       │ Tương tác sự kiện hệ điều hành
                       ▼
┌──────────────────────────────────────────────┐
│  Application Under Test (AUT)                │
│  (WPF, WinForms, UWP, Win32)                 │
└──────────────────────────────────────────────┘
```

1. **Khởi tạo phiên (Session):** Kịch bản kiểm thử khởi tạo một `WindowsDriver` với các thông số cấu hình (*DesiredCapabilities*) chỉ định đường dẫn ứng dụng (`app`), môi trường (`platformName: Windows`).
2. **Gửi lệnh WebDriver:** Các thao tác như tìm kiếm phần tử, click chuột, gửi phím được đóng gói thành các HTTP request gửi đến `http://127.0.0.1:4723`.
3. **Thông dịch UIA:** WinAppDriver tiếp nhận HTTP request và gọi trực tiếp các API của Windows UI Automation.
4. **Thực thi và phản hồi:** Windows thực thi thao tác trên ứng dụng đích và WinAppDriver đóng gói kết quả phản hồi (JSON) trả về cho Test Script.

### 2.2 Nhận diện phần tử giao diện (Object Recognition)
Do WinAppDriver không có giao diện đồ họa riêng, việc định danh phần tử dựa trên các công cụ inspect độc lập của Microsoft:
* **Công cụ hỗ trợ inspect:**
  * **Accessibility Insights for Windows:** Công cụ hiện đại được Microsoft khuyến nghị, hỗ trợ kiểm tra cấu trúc cây giao diện và phát hiện nhanh các thuộc tính định danh.
  * **Inspect.exe:** Công cụ truyền thống đi kèm Windows SDK.
* **Cơ chế định vị trong mã nguồn:**
  * `AccessibilityId`: Trỏ trực tiếp vào thuộc tính `AutomationId` của control $\rightarrow$ **Phương thức định vị chuẩn và bền vững nhất**.
  * `Name`: Tìm theo nhãn hiển thị hoặc tiêu đề nút bấm.
  * `ClassName`: Tìm theo loại control (ví dụ: `TextBox`, `Button`).
  * `XPath`: Tìm theo đường dẫn phân cấp trong cây UI $\rightarrow$ Tốc độ tìm kiếm qua XPath trên WinAppDriver tương đối chậm, nên hạn chế dùng trừ khi không có ID.

---

## 3. Ba Năng Lực Cốt Lõi (Theo Lý Thuyết Kiểm Thử)

### 3.1 Record & Playback (Ghi & Phát lại kịch bản)
* **Thực trạng hỗ trợ:**
  * Bản thân WinAppDriver **không tích hợp sẵn trình Record & Playback** như Katalon Studio.
  * Lập trình viên kiểm thử chủ yếu dùng kỹ thuật *Inspect & Code*: Dùng công cụ inspect để lấy ID $\rightarrow$ Tự viết mã kịch bản.
  * *Mở rộng:* Có thể kết hợp với các công cụ ghi của bên thứ ba (như Appium Desktop Inspector) để ghi lại thao tác, nhưng mã sinh ra thường thô và phải cấu trúc lại.
* **Đánh giá:**
  * *Nhược điểm:* Tốc độ tạo kịch bản ban đầu chậm hơn so với việc bấm Record.
  * *Ưu điểm:* Kịch bản tự viết có cấu trúc rõ ràng, không chứa các thao tác rác hay độ trễ thừa, dễ áp dụng ngay các mẫu thiết kế chuẩn như **Page Object Model (POM)**.

### 3.2 Checkpoints & Assertions (Điểm kiểm tra kết quả)
* **Khái niệm:** Tự động hóa Test Oracle thông qua việc so khớp giữa kết quả thực tế lấy từ ứng dụng (`element.Text`, `element.Enabled`) với kết quả kỳ vọng.
* **Cơ chế thực hiện:**
  * WinAppDriver tận dụng trực tiếp các thư viện Assertion mạnh mẽ của ngôn ngữ lập trình (NUnit, xUnit, FluentAssertions đối với C#; hoặc pytest, unittest đối với Python).
  * *Ví dụ kiểm tra Text:* `Assert.AreEqual("Đăng nhập thành công", lblMessage.Text);`
  * *Ví dụ kiểm tra trạng thái:* `Assert.IsTrue(btnSubmit.Enabled);`
* **Xử lý chụp ảnh màn hình khi lỗi:**
  * Khi Assertion thất bại, framework cho phép bắt ngoại lệ và gọi hàm `driver.GetScreenshot().SaveAsFile(...)` để lưu bằng chứng lỗi phục vụ lập Bug Report.

### 3.3 Data-Driven Testing (Kiểm thử hướng dữ liệu)
* **Cơ chế thực hiện:**
  * Tách rời hoàn toàn dữ liệu kiểm thử bằng cách tận dụng tính năng tham số hóa kịch bản (*Parameterized Testing*) của các Test Runner:
    * Trong **C# (NUnit):** Dùng thuộc tính `[TestCase]` cho dữ liệu nội tuyến hoặc `[TestCaseSource]` để đọc dữ liệu từ file Excel/CSV/JSON.
    * Trong **Python (pytest):** Dùng decorator `@pytest.mark.parametrize` kết hợp đọc file qua thư viện `pandas` hoặc `openpyxl`.
* **Ý nghĩa thực tế:**
  * Cho phép nạp trực tiếp danh sách **12 ca kiểm thử giá trị biên (BVA)** từ file Excel để chạy tự động qua cùng một kịch bản tính toán.
  * Dễ dàng tích hợp với các hệ thống quản trị cơ sở dữ liệu (SQL Server, MySQL) để kiểm thử các luồng dữ liệu lớn của doanh nghiệp.

---

## 4. Đánh Giá Ưu Điểm & Nhược Điểm

### 4.1 Ưu điểm
1. **Miễn phí và mã nguồn mở 100%:** Không chịu bất kỳ ràng buộc nào về chi phí bản quyền, số lượng máy chạy hay thời hạn dùng thử.
2. **Tuân thủ chuẩn W3C WebDriver:** Kỹ sư kiểm thử đã biết Selenium (Web) hoặc Appium (Mobile) có thể tiếp cận WinAppDriver gần như ngay lập tức mà không cần học một công cụ hoàn toàn mới.
3. **Tính linh hoạt và khả năng mở rộng vô hạn:**
   * Tự do lựa chọn cấu trúc dự án, áp dụng kiến trúc chuẩn như Page Object Model (POM) hoặc Screenplay.
   * Tự do tích hợp các thư viện xuất báo cáo chuyên nghiệp (Allure Report, ExtentReports, ReportPortal).
4. **Tối ưu cho quy trình DevOps & Git:** Mã kiểm thử là mã nguồn thuần (C#/Python), rất dễ kiểm soát phiên bản (VCS), giải quyết xung đột (conflict) và tích hợp vào pipeline CI/CD (GitHub Actions, Azure DevOps, Jenkins) thông qua lệnh build/test thông thường (`dotnet test` hoặc `pytest`).

### 4.2 Nhược điểm & Rào cản kỹ thuật
1. **Trạng thái phát triển của dự án (Archive status):** Dự án WinAppDriver trên GitHub chính thức của Microsoft đã chuyển sang chế độ lưu trữ (archive/ngừng cập nhật tính năng mới từ năm 2023). Dù hiện tại vẫn chạy rất ổn định trên Windows 10/11, sự phát triển trong tương lai đang dần dịch chuyển sang dự án cộng đồng *Appium Windows Driver*.
2. **Đòi hỏi kỹ năng lập trình:** Không có giao diện kéo thả hay chế độ Manual View; tester bắt buộc phải có tư duy phát triển phần mềm và thành thạo ngôn ngữ lập trình.
3. **Tốn thời gian xây dựng framework ban đầu:** Không có sẵn kho quản lý đối tượng (Object Repository) hay báo cáo tự động; nhóm phát triển phải tự tay viết code quản lý driver, cấu hình wait và cơ chế log/chụp màn hình.
4. **Phạm vi nền tảng hẹp:** Chỉ chạy trên hệ điều hành Windows, không hỗ trợ kiểm thử desktop trên macOS hay Linux.

---

## 5. Định Hướng Kịch Bản Demo Cho Nhóm (Dùng Chung Case Study Với Tool A)

Để đảm bảo tính đối chiếu công bằng với Katalon Studio, kịch bản của WinAppDriver sẽ thực hiện trên **cùng ứng dụng mẫu** và **cùng bộ dữ liệu**:

```
[Demo 1: Thiết lập] ──► [Demo 2: Cơ bản] ──► [Demo 3: Nâng cao]
 Khởi động driver        Viết code Test Case   Data-Driven BVA
 Soi ID bằng UIA         Assertion + Chụp ảnh  Đọc file Excel
```

### 5.1 Demo 1: Cài đặt và chuẩn bị môi trường
* **Mục tiêu:** Chứng minh cấu hình môi trường chuẩn mã nguồn mở.
* **Các bước chính:**
  1. Khởi chạy `WinAppDriver.exe` ở quyền Administrator (lắng nghe tại cổng 4723).
  2. Mở công cụ *Accessibility Insights for Windows* để bóc tách các `AutomationId` trên ứng dụng mẫu.
  3. Mở Visual Studio (hoặc VS Code), tạo dự án kiểm thử với thư viện `Appium.WebDriver` và `NUnit`.

### 5.2 Demo 2: Kịch bản cơ bản (Code-based + Checkpoint Assertion)
* **Mục tiêu:** Minh họa cách viết kịch bản kiểm thử chuẩn cấu trúc bằng mã nguồn (Chức năng Đăng nhập).
* **Các bước chính:**
  1. Khởi tạo phiên làm việc với ứng dụng qua `WindowsDriver<WindowsElement>`.
  2. Dùng lệnh `FindElementByAccessibilityId` để nhập tài khoản, mật khẩu và click nút Submit.
  3. Áp dụng Checkpoint bằng câu lệnh `Assert.AreEqual("Đăng nhập thành công", lblMessage.Text)`.
  4. Cố tình gây lỗi để minh họa cơ chế tự động chụp ảnh màn hình lưu vào thư mục dự án khi kiểm thử thất bại.

### 5.3 Demo 3: Kịch bản nâng cao (Data-Driven BVA với File Excel)
* **Mục tiêu:** Chứng minh năng lực kiểm thử dữ liệu lớn kết hợp kỹ thuật phân tích giá trị biên.
* **Các bước chính:**
  1. Sử dụng thư viện đọc Excel để nạp bộ dữ liệu **12 ca biên BVA** của bài toán tính tổng 2 số nguyên.
  2. Tham số hóa phương thức kiểm thử với `[TestCaseSource]`.
  3. Thực thi tự động 12 ca kiểm thử liên tiếp bằng lệnh `dotnet test`.
  4. Xem báo cáo kết quả thực thi chi tiết dạng XML/HTML qua công cụ Test Explorer.

---

## 6. Khi Nào Nên & Không Nên Chọn WinAppDriver

| Nên chọn Microsoft WinAppDriver | Khi nào nên cân nhắc công cụ khác (như Katalon Studio) |
|---|---|
| Đội ngũ kiểm thử là các kỹ sư SDET hoặc lập trình viên có kỹ năng viết code tốt. | Đội ngũ có nhiều Manual Tester, cần giao diện đồ họa và tính năng Record & Playback để làm quen nhanh. |
| Muốn tự do hoàn toàn trong việc thiết kế framework kiểm thử (áp dụng POM, Screenplay). | Cần một giải pháp trọn gói (All-in-one) có sẵn Object Repository và hệ thống báo cáo hoàn chỉnh ngay khi cài đặt. |
| Dự án yêu cầu 100% phần mềm mã nguồn mở, không có ngân sách mua license thương mại. | Cần một công cụ đang được nhà sản xuất cam kết hỗ trợ kỹ thuật dài hạn và cập nhật tính năng mới liên tục. |
| Muốn tích hợp sâu vào quy trình CI/CD nội bộ của nhóm phát triển phần mềm qua Git. | Dự án cần triển khai gấp trong thời gian ngắn mà không có thời gian lập trình khung framework. |

---


# Phần 6: So Sánh Đối Chiếu Hai Công Cụ (Comparison)

## 1. Phương Pháp So Sánh và Ngữ Cảnh Đánh Giá

Để việc so sánh đạt độ tin cậy và tính khoa học, hai công cụ được đối chiếu dựa trên các tiêu chuẩn kỹ thuật thống nhất:
* **Môi trường và ứng dụng thử nghiệm chung (Common Case Study):** Cùng tương tác trên ứng dụng Windows (WPF/WinForms) có đầy đủ luồng xác thực (Login), xử lý tính toán số học và bảng hiển thị lịch sử (DataGrid).
* **Bộ dữ liệu kiểm thử chuẩn hóa:** Cùng thực thi bộ **12 ca kiểm thử giá trị biên (BVA)** của bài toán tính tổng hai số nguyên $A, B \in [-99, 99]$ theo đúng lý thuyết thiết kế ca kiểm thử hộp đen.
* **Cơ chế tương tác nền tảng:** Cả hai công cụ đều dựa trên nền tảng **Windows UI Automation (UIA)** và chuẩn **WebDriver**, giúp việc đánh giá phản ánh chính xác sự khác biệt về mặt thiết kế công cụ thay vì sự chênh lệch về công nghệ hệ điều hành.

---

## 2. Bảng Tổng Hợp So Sánh Đa Tiêu Chí

| Nhóm tiêu chí | Katalon Studio (Tool A) | Microsoft WinAppDriver (Tool B) | Phân tích và Đánh giá |
|---|---|---|---|
| **Triết lý thiết kế** | Low-Code / All-in-One GUI Platform | Code-First / Developer-Centric SDK | Katalon đóng gói trọn gói; WinAppDriver cung cấp bộ khung lập trình mở. |
| **Yêu cầu kỹ năng** | Tiếp cận nhanh; hỗ trợ cả người chưa thành thạo lập trình. | Đòi hỏi kỹ năng lập trình hướng đối tượng (C# hoặc Python). | Katalon giảm thiểu rào cản kỹ thuật; WinAppDriver phát huy thế mạnh của kỹ sư SDET. |
| **Phương thức tạo test** | Hỗ trợ Record & Playback và giao diện Manual View dạng bảng. | Inspect phần tử thủ công và lập trình kịch bản trực tiếp trong IDE. | Katalon tạo kịch bản ban đầu nhanh hơn; WinAppDriver cho mã nguồn sạch và tối ưu hơn. |
| **Hiệu năng & Tài nguyên** | Nặng, khởi động chậm, chiếm dụng nhiều RAM/CPU do chạy trên nền Eclipse IDE. | Rất nhẹ, thực thi kịch bản nhanh, mức tiêu hao tài nguyên phần cứng không đáng kể. | WinAppDriver vượt trội về tốc độ thực thi kịch bản và tính ổn định trên máy chủ CI. |
| **Hệ thống báo cáo** | Tự động xuất báo cáo chi tiết (HTML, JUnit XML) kèm ảnh chụp màn hình khi lỗi. | Không có sẵn; phải tích hợp các thư viện bên ngoài (Allure, ExtentReports). | Katalon có sẵn hạ tầng báo cáo; WinAppDriver đòi hỏi công sức cấu hình ban đầu. |
| **Mô hình bản quyền** | Freemium: Bản Free đủ cho nhu cầu cơ bản; các tính năng nâng cao có tính phí. | Mã nguồn mở (Open Source) hoàn toàn, miễn phí bản quyền trọn đời. | WinAppDriver loại bỏ hoàn toàn chi phí đầu tư phần mềm; Katalon phụ thuộc chính sách hãng. |
| **Tích hợp CI/CD & VCS** | Quản lý theo cấu trúc dự án độc quyền; chạy dòng lệnh qua Katalon Runtime Engine. | Quản lý mã nguồn dạng text thuần qua Git; tích hợp trực tiếp qua CLI (`dotnet test`). | WinAppDriver tối ưu cho đường ống DevOps và dễ xử lý xung đột mã nguồn (merge conflict). |

---

## 3. So Sánh Chi Tiết Theo 3 Năng Lực Tự Động Hóa Cốt Lõi

### 3.1 Record & Playback (Ghi nhận và Phát lại)
* **Katalon Studio:**
  * Tích hợp sẵn trình *Windows Recorder*, tự động bắt các sự kiện bàn phím/chuột và ánh xạ trực tiếp thành các từ khóa thao tác (`Click`, `Set Text`).
  * Tự động trích xuất và lưu trữ các thuộc tính định danh vào kho đối tượng (*Object Repository*).
  * *Nhận xét:* Tối ưu hóa năng suất trong giai đoạn đầu xây dựng kịch bản, đặc biệt với các luồng nghiệp vụ dài. Tuy nhiên, kịch bản sinh ra có thể chứa các bước thừa và cần được chuẩn hóa thủ công để tránh lỗi gián đoạn (flaky).
* **Microsoft WinAppDriver:**
  * Không tích hợp tính năng ghi thao tác. 
  * Kiểm thử viên sử dụng công cụ thanh tra giao diện (*Accessibility Insights* hoặc *Inspect.exe*) để phân tích cây UIA, lấy thuộc tính `AutomationId` và tự viết mã kiểm thử.
  * *Nhận xét:* Tốn nhiều thời gian thiết lập ban đầu, nhưng mã nguồn được cấu trúc chặt chẽ, dễ áp dụng các mẫu thiết kế chuẩn ngay từ đầu.

### 3.2 Checkpoints & Assertions (Điểm kiểm tra kết quả)
* **Katalon Studio:**
  * Cung cấp các từ khóa kiểm tra có sẵn (`Verify Element Text`, `Verify Element Present`, `Verify Element Attribute Value`).
  * Thực thi kiểm tra trực quan, tự động ghi nhận trạng thái Pass/Fail vào cây báo cáo và tự động bắt ảnh màn hình khi phát hiện lỗi.
  * *Hạn chế:* Việc kiểm tra các cấu trúc dữ liệu phức tạp (như so sánh nhiều dòng trong bảng hoặc kiểm tra logic phụ thuộc) đòi hỏi phải chuyển sang chế độ Script View để viết mã Groovy.
* **Microsoft WinAppDriver:**
  * Kế thừa toàn bộ hệ thống Assertion mạnh mẽ của các khung kiểm thử tiêu chuẩn như NUnit, xUnit, FluentAssertions (C#) hoặc pytest (Python).
  * Cho phép xây dựng các điểm kiểm tra đa dạng: từ so sánh chuỗi, kiểm tra trạng thái thuộc tính, đến kiểm tra dữ liệu đối chiếu từ cơ sở dữ liệu ngầm.
  * *Nhận xét:* Khả năng kiểm tra không bị giới hạn bởi công cụ, đáp ứng hoàn hảo yêu cầu của các kịch bản kiểm thử nghiệp vụ chuyên sâu.

### 3.3 Data-Driven Testing (Kiểm thử điều khiển bằng dữ liệu)
* **Katalon Studio:**
  * Hỗ trợ đối tượng *Test Data* trực quan, cho phép import trực tiếp từ Excel, CSV hoặc cơ sở dữ liệu.
  * Việc liên kết (Data Binding) giữa các cột dữ liệu và biến của Test Case được thực hiện qua giao diện đồ họa của Test Suite.
  * *Nhận xét:* Dễ sử dụng, tách biệt rõ ràng giữa logic kịch bản và nguồn dữ liệu, phù hợp cho các bài kiểm tra phân tích giá trị biên (BVA).
* **Microsoft WinAppDriver:**
  * Tận dụng cơ chế tham số hóa kiểm thử (*Parameterized Testing*) thông qua mã nguồn: thuộc tính `[TestCaseSource]` trong NUnit hoặc `@pytest.mark.parametrize` trong pytest.
  * Đọc dữ liệu linh hoạt từ mọi định dạng (Excel, JSON, XML, Database) thông qua các thư viện lập trình chuẩn.
  * *Nhận xét:* Đòi hỏi viết code xử lý dữ liệu đầu vào, nhưng mang lại khả năng xử lý tiền kỳ (pre-processing) và biến đổi dữ liệu động trước khi thực thi kiểm thử.

---

## 4. Đánh Giá Về Kiến Trúc, Hiệu Năng và Khả Năng Bảo Trì

### 4.1 Tốc độ thực thi và mức độ chiếm dụng tài nguyên
* **Katalon Studio:** Do xây dựng trên nền tảng Eclipse RCP và máy ảo Java, công cụ tiêu tốn dung lượng RAM đáng kể (thường từ 1.5 GB - 3 GB trong quá trình chạy) và có độ trễ nhất định giữa các bước kiểm thử.
* **WinAppDriver:** Kịch bản được biên dịch thành mã thực thi nhị phân (.NET) hoặc script Python nhẹ, kết nối trực tiếp đến tiến trình WinAppDriver qua cổng 4723. Tốc độ gửi và nhận gói tin WebDriver đạt hiệu suất cao, mức chiếm dụng RAM dưới 200 MB, lý tưởng cho việc chạy hàng loạt trên các máy ảo kiểm thử.

### 4.2 Khả năng bảo trì kịch bản trong dự án dài hạn
* **Mô hình Object Repository (Katalon Studio):**
  * Các bộ định vị (locator) được quản lý tập trung trong cấu trúc thư mục dạng XML. Khi giao diện ứng dụng thay đổi, người kiểm thử chỉ cần cập nhật tại một vị trí mà không cần can thiệp vào mã kịch bản.
  * Phù hợp cho các dự án có quy mô vừa và đội ngũ có sự tham gia của manual tester.
* **Mẫu thiết kế Page Object Model - POM (WinAppDriver):**
  * Tách biệt hoàn toàn giao diện màn hình thành các lớp (Classes) trong mã nguồn hướng đối tượng, đóng gói hành vi và thuộc tính của từng màn hình.
  * Cung cấp khả năng tái sử dụng mã nguồn ở mức độ cao nhất, dễ bảo trì, dễ refactor khi mã nguồn ứng dụng phát triển lớn.

---

## 5. Bảng Tổng Hợp Ưu Điểm và Nhược Điểm Đối Đầu

| Khía cạnh | Katalon Studio | Microsoft WinAppDriver |
|---|---|---|
| **Thế mạnh cốt lõi** | - Triển khai nhanh, giao diện đồ họa hoàn chỉnh.<br>- Tích hợp sẵn Recorder, Spy và Báo cáo.<br>- Giảm thiểu chi phí đào tạo nhân sự ban đầu. | - Tốc độ thực thi cao, tài nguyên nhẹ.<br>- Mã nguồn mở hoàn toàn, không chi phí bản quyền.<br>- Tự do tối đa trong việc thiết kế framework (POM).<br>- Tối ưu hóa tuyệt đối cho quy trình Git và CI/CD. |
| **Hạn chế chính** | - Tiêu tốn nhiều tài nguyên hệ thống.<br>- Phụ thuộc vào chính sách giấy phép thương mại.<br>- Khó tùy biến sâu các tầng kiến trúc ngoài khuôn khổ tool. | - Không có giao diện đồ họa và tính năng Record.<br>- Đòi hỏi kỹ năng lập trình thành thạo.<br>- Phải tự cấu hình hạ tầng báo cáo và quản lý locator.<br>- Dự án GitHub gốc đang ở trạng thái lưu trữ (archive). |

---

## 6. Định Hướng và Ma Trận Lựa Chọn Công Cụ

Việc lựa chọn công cụ kiểm thử tự động cho desktop applications cần dựa trên sự cân đối giữa kỹ năng nhân sự, quy mô dự án và mục tiêu kiểm định chất lượng:

```
                             [BÀN CÂN LỰA CHỌN CÔNG CỤ]
                                         │
        ┌────────────────────────────────┴────────────────────────────────┐
        ▼                                                                 ▼
[CHỌN KATALON STUDIO]                                           [CHỌN WINAPPDRIVER]
- Đội ngũ kiểm thử chuyển tiếp từ manual.                       - Đội ngũ phát triển / SDET thành thạo code.
- Cần triển khai kịch bản nhanh chóng.                          - Cần xây dựng framework bài bản, dài hạn.
- Dự án ưu tiên giải pháp trọn gói (All-in-one).                 - Dự án yêu cầu tối ưu hóa tốc độ và CI/CD.
- Chấp nhận sử dụng phiên bản miễn phí cơ bản.                  - Dự án bắt buộc sử dụng chuẩn mã nguồn mở 100%.
```

### Kết luận đánh giá:
* **Katalon Studio** là giải pháp tối ưu cho bài toán **năng suất và tốc độ tiếp cận**, phù hợp với các dự án cần nhanh chóng đưa tự động hóa vào quy trình kiểm thử mà không yêu cầu đội ngũ phải có nền tảng phát triển phần mềm chuyên sâu.
* **Microsoft WinAppDriver** là lựa chọn tiêu chuẩn cho bài toán **chất lượng kỹ thuật và khả năng mở rộng**, cung cấp nền tảng vững chắc cho các kỹ sư kiểm thử tự động muốn tích hợp sâu kiểm thử vào vòng đời phát triển phần mềm hiện đại.

---


# Phần 7: Ứng Dụng Trí Tuệ Nhân Tạo (AI) Trong Desktop Automation

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

---


# Phần 8: Hệ Thống Bài Tập Thực Hành Đề Xuất (Exercise)

## 1. Mục Tiêu và Nguyên Tắc Xây Dựng Bài Tập

Hệ thống bài tập được thiết kế tuân thủ 3 nguyên tắc sư phạm và kỹ thuật:
1. **Bám sát chương trình lý thuyết:** Gắn kết trực tiếp với các bài học trong chương trình: Kỹ thuật phân tích giá trị biên (BVA - Bài 4), Chuyển trạng thái (State Transition - Bài 6), Cấu trúc Test Case (Bài 7) và Tái hiện lỗi trong Bug Report (Bài 8).
2. **Khả thi về công cụ và bản quyền:** Sinh viên có thể tự do lựa chọn thực hiện bằng **Katalon Studio (Bản Free)** hoặc **Microsoft WinAppDriver (C# / Python)** mà không chịu ràng buộc về chi phí giấy phép.
3. **Sử dụng ứng dụng mẫu chung (MiniSum):** Cung cấp sẵn file thực thi `.exe` chuẩn hóa về mặt định danh (`AutomationId`), giúp sinh viên tập trung rèn luyện tư duy kiểm thử thay vì mất thời gian sửa lỗi môi trường.

---

## 2. Thông Tin Ứng Dụng Mẫu (MiniSum)

Sinh viên tải file thực thi `MiniSum.exe` từ kho lưu trữ của nhóm. Các thuộc tính định danh chính được cung cấp sẵn:
* **Màn hình Đăng nhập (Login Window):**
  * Ô nhập tài khoản: `txtUser` (Tài khoản hợp lệ: `abc`)
  * Ô nhập mật khẩu: `txtPass` (Mật khẩu hợp lệ: `123`)
  * Nút đăng nhập: `btnSubmit`
  * Nhãn thông báo trạng thái: `lblMessage`
* **Màn hình Tính toán (Main Window):**
  * Ô nhập số A: `txtA` (Giới hạn số nguyên $A \in [-99, 99]$)
  * Ô nhập số B: `txtB` (Giới hạn số nguyên $B \in [-99, 99]$)
  * Nút tính tổng: `btnSum`
  * Nhãn kết quả hợp lệ: `lblResult`
  * Nhãn thông báo lỗi: `lblError`
  * Nút đăng xuất: `btnLogout`

---

## 3. Nội Dung Chi Tiết Bộ 3 Bài Tập

### BÀI TẬP 1 (Mức độ Cơ bản): Xây Dựng Kịch Bản Đăng Nhập & Checkpoint
* **Thời lượng ước tính:** 15 – 20 phút.
* **Mục tiêu:** Làm quen với cơ chế nhận diện phần tử (`AutomationId`), ghi thao tác (Record) hoặc viết mã kịch bản cơ bản, và thiết lập điểm kiểm tra kết quả kỳ vọng (Test Oracle).
* **Nội dung yêu cầu:**
  1. Khởi động ứng dụng `MiniSum.exe`.
  2. Thực hiện kịch bản kiểm thử ca hợp lệ: Nhập `txtUser = "abc"`, `txtPass = "123"`, nhấp chuột vào nút `btnSubmit`.
  3. Thêm một **Checkpoint (Assertion)** để xác minh nhãn `lblMessage` hiển thị đúng nội dung: `"Đăng nhập thành công"`.
  4. Tạo tiếp một ca kiểm thử phụ cho trường hợp đăng nhập thất bại (nhập sai mật khẩu) và xác minh nhãn hiển thị `"Sai tài khoản hoặc mật khẩu"`.
* **Yêu cầu nộp:**
  * File kịch bản kiểm thử (Test Case của Katalon hoặc file mã nguồn C#/Python).
  * Ảnh chụp màn hình kết quả chạy thực thi (Execution Report) thể hiện trạng thái PASS.

---

### BÀI TẬP 2 (Mức độ Vừa sức): Kiểm Thử Điều Khiển Bằng Dữ Liệu (Data-Driven BVA)
* **Thời lượng ước tính:** 30 – 45 phút.
* **Mục tiêu:** Vận dụng lý thuyết phân tích giá trị biên (BVA) để xây dựng bộ dữ liệu kiểm thử và áp dụng kỹ thuật Data-Driven Testing để kiểm thử tự động hàng loạt.
* **Nội dung yêu cầu:**
  1. **Thiết kế dữ liệu:** Tạo một file Excel (`BVA_TestData.xlsx`) chứa ít nhất **6 ca kiểm thử** cho chức năng tính tổng hai số nguyên $A, B \in [-99, 99]$:
     * 2 ca giá trị biên hợp lệ (ví dụ: $A = -99, B = 9 \rightarrow \text{Tổng} = -90$; $A = 99, B = 9 \rightarrow \text{Tổng} = 108$).
     * 2 ca giá trị ngoài biên dưới và trên (ví dụ: $A = -100, B = 9$; $A = 100, B = 9 \rightarrow$ Kỳ vọng xuất hiện `"Thông báo lỗi"`).
     * 1 ca giá trị không hợp lệ về kiểu dữ liệu (ví dụ: $A = \text{"xyz"}, B = 10 \rightarrow$ Kỳ vọng xuất hiện `"Thông báo lỗi"`).
     * 1 ca biên của toán tử thứ hai ($B = -99$).
  2. **Xây dựng kịch bản Data-Driven:**
     * Tham số hóa kịch bản tính tổng để nhận giá trị `${A}`, `${B}`, `${Expected}` từ file Excel.
     * Cấu hình logic kiểm tra: Nếu `${Expected}` là giá trị số thì kiểm tra nhãn `lblResult`; nếu `${Expected}` là `"LOI"` thì kiểm tra nhãn `lblError`.
  3. Thực thi toàn bộ bộ dữ liệu trong một phiên chạy tự động.
* **Yêu cầu nộp:**
  * File dữ liệu `BVA_TestData.xlsx`.
  * Mã nguồn kịch bản kiểm thử có cơ chế binding dữ liệu.
  * Báo cáo thực thi chi tiết thể hiện kết quả Pass/Fail cho từng dòng dữ liệu.

---

### BÀI TẬP 3 (Mức độ Nâng cao): Xử Lý Biến Động Giao Diện & Bảo Trì Kịch Bản
* **Thời lượng ước tính:** Bài tập về nhà / Nghiên cứu chuyên sâu.
* **Mục tiêu:** Rèn luyện tư duy thiết kế kịch bản bền vững và kỹ năng bảo trì — giải quyết bài toán "kịch bản dễ gãy" (fragile tests) khi phần mềm nâng cấp giao diện.
* **Tình huống giả định:** 
  * Nhà phát triển phát hành phiên bản cập nhật `MiniSum_v2.exe`. Trong phiên bản này, để chuẩn hóa mã nguồn, định danh của nút bấm tính tổng được đổi từ `btnSum` thành `btnCalculate`, đồng thời nhãn hiển thị chuyển từ `"Tổng"` sang `"Tính toán"`.
  * Hậu quả: Toàn bộ kịch bản kiểm thử xây dựng ở Bài tập 2 khi chạy trên bản v2 đều bị FAIL hàng loạt do lỗi không tìm thấy phần tử (*ElementNotFoundException*).
* **Nội dung yêu cầu:**
  1. Chạy kịch bản cũ trên bản v2, chụp lại log lỗi thực thi và phân tích nguyên nhân gốc của lỗi (Root Cause).
  2. Thực hiện **bảo trì và tái cấu trúc (Refactoring)** bộ định vị theo nguyên tắc tập trung:
     * *Nếu làm trên Katalon Studio:* Cập nhật lại thuộc tính của đối tượng trong *Object Repository* từ `btnSum` sang `btnCalculate` mà không sửa đổi bất kỳ dòng kịch bản nào trong Test Case.
     * *Nếu làm trên WinAppDriver:* Cập nhật lại biến locator trong lớp *Page Object* tương ứng.
  3. Thực thi lại toàn bộ kịch bản và chứng minh toàn bộ các ca kiểm thử PASS trở lại.
  4. Trả lời câu hỏi phân tích ngắn (khoảng 5-7 dòng): *Tại sao việc quản lý locator tập trung (Object Repository / Page Object Model) lại giúp giảm chi phí bảo trì so với việc gán cứng locator trực tiếp trong kịch bản? Liên hệ với nguyên lý kiểm thử "Nghịch lý thuốc trừ sâu".*
* **Yêu cầu nộp:**
  * Báo cáo phân tích lỗi ban đầu và ảnh chụp màn hình sau khi khắc phục thành công.
  * Đoạn trả lời câu hỏi phân tích lý thuyết bảo trì.

---

## 4 Barem đánh giá chi tiết

| Hạng mục | Tiêu chí đánh giá chi tiết | Điểm tối đa |
|---|---|:---:|
| **Bài tập 1** | - Mở được ứng dụng, thực thi đúng thao tác đăng nhập.<br>- Thiết lập Checkpoint đúng nhãn và chạy PASS.<br>- Có ca kiểm thử phụ cho trường hợp đăng nhập sai. | **3.0 điểm**<br>(1.0 đ)<br>(1.0 đ)<br>(1.0 đ) |
| **Bài tập 2** | - Thiết kế file dữ liệu Excel chuẩn lý thuyết BVA (đủ ca hợp lệ và biên lỗi).<br>- Tham số hóa và binding dữ liệu vào kịch bản thành công.<br>- Xử lý đúng điều kiện kiểm tra kết quả số và thông báo lỗi. | **4.0 điểm**<br>(1.5 đ)<br>(1.5 đ)<br>(1.0 đ) |
| **Bài tập 3** | - Phân tích đúng nguyên nhân lỗi khi đổi ID phần tử.<br>- Thực hiện cập nhật locator tập trung (Object Repository / Page Object).<br>- Câu trả lời phân tích lý thuyết bảo trì mạch lạc, đúng bản chất. | **3.0 điểm**<br>(1.0 đ)<br>(1.0 đ)<br>(1.0 đ) |
| **TỔNG CỘNG** | **Đánh giá toàn diện kỹ năng thực hành và tư duy lý thuyết** | **10.0 điểm** |

---


# Phần 9: Kết Luận & Hướng Phát Triển (Conclusion)

## 9.1 Tổng kết kết quả đạt được
1. **Làm chủ cơ sở lý thuyết:** Hệ thống hóa toàn diện các nguyên lý kiểm thử tự động trên desktop, phân loại các công nghệ giao diện và chỉ ra 5 thách thức kỹ thuật cốt lõi (nhận diện UI, đồng bộ Wait, xử lý popup OS, môi trường headless và chi phí bảo trì).
2. **Khảo sát và đối chiếu công bằng:** Nghiên cứu sâu sắc hai công cụ đại diện cho hai trường phái đối lập hoàn hảo: Katalon Studio (All-in-one GUI / Low-Code) và Microsoft WinAppDriver (Pure Code / Open Source SDK) trên cùng một case study ứng dụng và cùng bộ dữ liệu kiểm thử giá trị biên chuẩn mực.
3. **Tiếp cận công nghệ mới:** Nhận diện rõ vai trò đột phá của Trí tuệ nhân tạo (AI/GenAI) trong việc giải quyết bài toán tự phục hồi locator (Self-healing) và kiểm thử thị giác (Visual AI).
4. **Đóng gói sản phẩm thực hành:** Hoàn thiện bộ kịch bản kiểm thử mẫu và hệ thống bài tập thực hành 3 cấp độ chuẩn hóa phục vụ trực tiếp cho môn học.

## 9.2 Bài học kinh nghiệm (Lessons Learned)
* **Kiểm thử phụ thuộc ngữ cảnh:** Không có công cụ nào là tối ưu tuyệt đối cho mọi dự án. Việc chọn công cụ phụ thuộc chặt chẽ vào năng lực nhân sự, ngân sách và kiến trúc phần mềm (nguyên lý số 6 trong kiểm thử phần mềm).
* **Chi phí bảo trì là thách thức sống còn:** Viết kịch bản tự động ban đầu chỉ chiếm 30% công sức, 70% nỗ lực nằm ở khâu duy trì kịch bản khi phần mềm nâng cấp. Áp dụng các mẫu thiết kế chuẩn (Page Object Model / Object Repository) là điều kiện bắt buộc để tự động hóa bền vững.
* **Tầm quan trọng của Wait thông minh:** Cơ chế đồng bộ hóa (Explicit Wait) là chìa khóa then chốt để loại bỏ hiện tượng Flaky Test trong môi trường desktop.

## 9.3 Hướng phát triển trong giai đoạn tiếp theo
* Hoàn thiện mã nguồn ứng dụng mẫu MiniSum và đóng gói repository dùng chung cho nhóm.
* Thực hiện ghi hình và thử nghiệm thực tế 3 nhóm demo kịch bản trên cả hai công cụ.
* Triển khai thử nghiệm 1 kịch bản ứng dụng GenAI hỗ trợ sinh test script tự động cho buổi báo cáo chuyên sâu.
