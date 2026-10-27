# Kịch Bản & Nội Dung Slide: Introduction, Theory & Tool Survey
## Chuyên đề: Automation Testing for Desktop Applications

> **Người soạn thảo:** Tín  
> **Phần phụ trách:** Phần 1 (Introduction) · Phần 2 (Theory) · Phần 3 (Tiêu chí Tool Survey)  
> **Cập nhật lần cuối:** 02/10/2026  
> **Trạng thái:** Hoàn thành  

---

## Slide 1: Trang tiêu đề (Title Slide)

- **Tiêu đề chính:** AUTOMATION TESTING FOR DESKTOP APPLICATIONS
- **Tiêu đề phụ:** Cơ sở lý thuyết, thách thức đặc thù và bộ tiêu chí lựa chọn công cụ
- **Môn học:** Kiểm thử phần mềm chuyên sâu (Software Testing Seminar)
- **Thành viên thuyết trình:** Tín (Phụ trách: Giới thiệu, Cơ sở lý thuyết & Tiêu chí khảo sát)
- **Nhóm nghiên cứu:** Tín, Kan, Tùng, Quang

**Ghi chú thuyết trình (Speaker Notes):**
> Kính chào thầy và các bạn. Hôm nay nhóm chúng mình xin trình bày seminar chuyên đề: "Automation Testing cho ứng dụng Desktop". Phần đầu tiên do mình phụ trách sẽ cung cấp cái nhìn tổng quan về bối cảnh, các thách thức kỹ thuật cốt lõi khi tự động hóa trên desktop và bộ tiêu chí khoa học để đánh giá, lựa chọn công cụ phù hợp.

---

## Slide 2: Mục lục nội dung (Agenda)

- **Phần 1: Giới thiệu (Introduction)**
  - Bối cảnh và lý do chọn đề tài
  - Mục tiêu và phạm vi nghiên cứu
- **Phần 2: Cơ sở lý thuyết (Theory)**
  - Bản chất của Automation Testing trên desktop
  - Phân loại công nghệ UI desktop và các loại kiểm thử khả thi
  - 5 Thách thức đặc thù trong Desktop Automation
  - Các kỹ thuật trọng tâm: Record & Playback, Data-Driven Testing, Checkpoints
  - Fully Automated vs Semi-Automated: Lựa chọn chiến lược
  - Ưu nhược điểm và nguyên tắc áp dụng
- **Phần 3: Bộ tiêu chí đánh giá công cụ (Tool Survey Criteria)**
  - Tổng quan thị trường công cụ desktop
  - 6 nhóm tiêu chí đánh giá (21 tiêu chí chuẩn hóa)
  - Ma trận đối chiếu và định hướng chọn công cụ cho Tool A / Tool B

**Ghi chú thuyết trình (Speaker Notes):**
> Bài thuyết trình phần 1 được chia làm 3 chặng rõ ràng: Đi từ lý do vì sao desktop app vẫn cần test tự động, đi sâu vào bản chất kỹ thuật để giải quyết các khó khăn, và kết thúc bằng việc đặt ra khung tiêu chí chuẩn để hai bạn tiếp theo (Kan và Tùng) đánh giá cụ thể từng tool.

---

## Slide 3: Bối cảnh & Thực trạng (Context)

- **Vị thế của Desktop App trong thực tế:**
  - Vẫn là nền tảng cốt lõi trong tài chính, ngân hàng, công nghiệp, y tế, hệ thống bán lẻ (POS).
  - Tận dụng tối đa phần cứng, bảo mật cục bộ, xử lý dữ liệu lớn không phụ thuộc mạng.
- **Sự chuyển dịch của quy trình phát triển:**
  - Áp dụng mô hình Agile, DevOps và đường ống CI/CD.
  - Chu kỳ phát hành tính bằng tuần/ngày thay vì tháng/quý.
- **Nghịch lý hiện tại:**
  - Web và Mobile đã tự động hóa mạnh mẽ.
  - Desktop testing ở nhiều doanh nghiệp vẫn phụ thuộc vào kiểm thử thủ công (Manual Testing).

**Ghi chú thuyết trình (Speaker Notes):**
> Nhiều người nghĩ desktop app đã lỗi thời, nhưng thực tế trong các lĩnh vực tài chính hay sản xuất, desktop app vẫn là sống còn. Vấn đề là trong khi Web/Mobile đã tích hợp CI/CD tự động chạy test hàng ngày, thì desktop app vẫn bị kiểm thử thủ công nặng nề, tạo ra nút thắt cổ chai lớn trong khâu phát hành.

---

## Slide 4: Tại sao cần Automation Testing cho Desktop?

| Kiểm thử thủ công (Manual) | Kiểm thử tự động (Automation) |
|---|---|
| Tốn nhiều thời gian và nhân lực lặp lại | Chạy nhanh gấp hàng chục lần, chạy 24/7 |
| Dễ bỏ sót lỗi do mệt mỏi, thao tác nhàm chán | Nhất quán 100%, thực thi chuẩn xác từng bước |
| Khó lặp lại hàng trăm bộ dữ liệu đầu vào | Dễ dàng áp dụng Data-Driven Testing |
| Kiểm thử hồi quy (Regression) kéo dài chu kỳ | Phản hồi ngay lập tức sau mỗi lần build mới |
| Chi phí nhân sự tăng dần theo thời gian | Đầu tư ban đầu cao, nhưng hoàn vốn dài hạn (ROI) |

**Ghi chú thuyết trình (Speaker Notes):**
> Bảng này so sánh trực diện giữa việc kiểm thử bằng tay và tự động. Mục đích của automation không phải là thay thế tester, mà là giải phóng tester khỏi các bài test hồi quy lặp đi lặp lại để họ tập trung vào kiểm thử khám phá và trải nghiệm người dùng.

---

## Slide 5: Mục tiêu & Phạm vi buổi Seminar

- **5 Mục tiêu chính:**
  1. Nắm vững nền tảng lý thuyết và thuật ngữ chuẩn quốc tế.
  2. Xây dựng bộ tiêu chí đánh giá công cụ khách quan, có trọng số.
  3. Trực quan hóa qua 3 nhóm demo thực tế: Cài đặt - Cơ bản - Workflow phức tạp.
  4. Tiếp cận xu hướng ứng dụng AI trong kiểm thử tự động.
  5. Cung cấp bài tập thực hành áp dụng ngay cho lớp.
- **Phạm vi kiểm thử:**
  - Hệ điều hành: Microsoft Windows (nền tảng phổ biến nhất cho desktop doanh nghiệp).
  - Công nghệ UI: WinForms, WPF, Win32, Electron.
  - Kỹ thuật: Record & Playback, Data-Driven Testing, Checkpoint/Assertion, Smart Waits.

**Ghi chú thuyết trình (Speaker Notes):**
> Seminar này không chỉ dừng lại ở lý thuyết suông. Mục tiêu là trang bị cả công cụ tư duy (bộ tiêu chí), kỹ năng thực hành (qua 3 nhóm demo của hai tool đại diện) và bài tập cho các bạn tự tay thực hiện.

---

## Slide 6: Automation Testing là gì?

- **Định nghĩa:** Áp dụng phần mềm chuyên dụng để điều khiển việc thực thi kịch bản kiểm thử, so khớp kết quả thực tế với kỳ vọng.
- **Sơ đồ vận hành:**

```
Kịch bản kiểm thử ──► [Công cụ Automation] ──Tương tác──► [Ứng dụng Desktop (AUT)]
                            │                                     │
                 Báo cáo ◄──┴────────── Đọc trạng thái & Giá trị ◄┘
```

- **Nguyên tắc quan trọng:**
  - Automation Test = Logic kịch bản + Cơ chế mô phỏng hành vi + Điểm kiểm tra (Assertions).
  - Kiểm thử tự động không tự thông minh nếu người viết kịch bản không cài đặt đúng checkpoint.

**Ghi chú thuyết trình (Speaker Notes):**
> Điểm mấu chốt: Một kịch bản chỉ click từ đầu đến cuối mà không có kiểm tra thì chỉ là bot tự động thao tác, chưa phải là testing. Testing bắt buộc phải có assertion: lấy giá trị thực tế đối chiếu với kết quả mong đợi.

---

## Slide 7: Phân loại ứng dụng Desktop & Khả năng kiểm thử

- **Cây phân loại công nghệ UI:**
  - **Native truyền thống:** Win32, MFC, WinForms (.NET)
  - **Native hiện đại:** WPF (XAML), UWP
  - **Đa nền tảng:** Qt (C++), JavaFX/Swing
  - **Ứng dụng lai (Hybrid):** Electron (Chromium + Node.js: VS Code, Slack, Teams)
- **Mức độ khả thi khi tự động hóa theo loại kiểm thử:**
  - *Rất phù hợp (Ưu tiên số 1):* Regression Testing, Smoke Testing, Data-Driven Testing.
  - *Phù hợp vừa phải:* UI Functional Testing, Performance Testing.
  - *Hạn chế / Không khả thi:* Usability Testing (cần trực giác người), Exploratory Testing.

**Ghi chú thuyết trình (Speaker Notes):**
> Vì sao desktop testing phức tạp? Vì cùng là desktop app nhưng app viết bằng WPF có cấu trúc XAML khác hoàn toàn app viết bằng Win32 cổ điển hay app viết bằng Electron. Công cụ kiểm thử phải có khả năng hiểu được lớp Accessibility API tương ứng của từng công nghệ.

---

## Slide 8: 5 Thách thức đặc thù trong Desktop Automation

- **1. Nhận diện đối tượng UI (Object Recognition):** Không có chuẩn DOM/CSS duy nhất như web; phụ thuộc vào UI Automation ID, Win32 Handle, hoặc tọa độ/hình ảnh.
- **2. Đồng bộ hóa thời gian thực (Synchronization):** Không có sự kiện "Page Load Complete"; dễ sinh lỗi Flaky Test do ứng dụng phản hồi trễ.
- **3. Hộp thoại hệ thống & Đa cửa sổ:** Cửa sổ Open/Save File Dialog, Print Dialog là tiến trình riêng của Windows, cần cơ chế chuyển đổi ngữ cảnh.
- **4. Yêu cầu môi trường hiển thị:** Thường yêu cầu phiên Desktop thật (GUI session hoạt động, không khóa màn hình), khó chạy headless hoàn toàn như web.
- **5. Gánh nặng bảo trì (Maintenance Overhead):** Giao diện thay đổi làm đứt gãy selector nếu không thiết kế theo Page Object Model (POM).

**Ghi chú thuyết trình (Speaker Notes):**
> Đây là 5 bài toán đau đầu nhất của kỹ sư automation desktop. Trong đó, Flaky test (lúc pass lúc fail) là kẻ thù số một, nguyên nhân chủ yếu do dùng thời gian chờ cố định Sleep thay vì cơ chế chờ có điều kiện Smart Wait.

---

## Slide 9: Kỹ thuật Record & Playback

- **Khái niệm:** Công cụ ghi lại hành vi bàn phím, chuột của tester trên ứng dụng và tự sinh mã kịch bản để phát lại.
- **Quy trình hoạt động:**
  1. *Record:* Bắt sự kiện người dùng + chụp thông tin đối tượng UI.
  2. *Generate:* Tự động sinh mã nguồn (C#, Python, Groovy...).
  3. *Refactor:* Tester chỉnh sửa selector, thêm Checkpoint và biến số.
  4. *Playback:* Công cụ phát lại và xuất báo cáo đạt/không đạt.
- **Đánh giá hai mặt:**
  - *Ưu điểm:* Dễ tiếp cận, tạo test cực nhanh, không cần biết lập trình ngay từ đầu.
  - *Nhược điểm:* Kịch bản dễ gãy khi UI thay đổi vị trí, khó xử lý dữ liệu động, kịch bản dài và khó tái sử dụng.

**Ghi chú thuyết trình (Speaker Notes):**
> Record & Playback là chiếc phao cứu sinh cho người mới bắt đầu. Tuy nhiên trong môi trường chuyên nghiệp, nó chỉ dùng để dò tìm đối tượng và khung sườn ban đầu, sau đó bắt buộc phải refactor mã nguồn thì mới duy trì lâu dài được.

---

## Slide 10: Kỹ thuật Data-Driven Testing (DDT)

- **Bản chất:** Tách rời hoàn toàn Logic kịch bản kiểm thử và Dữ liệu kiểm thử.
- **Mô hình kiến trúc:**

```
Kịch bản logic dùng chung ◄── [File Dữ liệu: Excel / CSV / JSON / DB]
        │
        ├── Thực thi Dòng 1 ──► Kết quả TC01
        ├── Thực thi Dòng 2 ──► Kết quả TC02
        └── Thực thi Dòng N ──► Kết quả TC0N
```

- **Ví dụ thực tế (Login Form):**
  - Cùng một hàm `test_login(username, password, expected_outcome)`.
  - Nạp 5 dòng dữ liệu: Đúng mật khẩu, sai mật khẩu, bỏ trống user, bỏ trống pass, tài khoản bị khóa.
  - Tự động chạy 5 lần và ghi nhận báo cáo độc lập cho từng trường hợp.

**Ghi chú thuyết trình (Speaker Notes):**
> Thay vì viết 5 hàm kiểm thử đăng nhập giống hệt nhau, DDT cho phép ta viết đúng 1 kịch bản và nạp bảng dữ liệu 5 dòng. Khi cần thêm test case biên, ta chỉ việc thêm dòng mới trong file Excel mà không cần sửa một dòng code nào.

---

## Slide 11: Checkpoints & Assertions

- **Định nghĩa:** Điểm kiểm tra logic trong script để xác nhận phần mềm hoạt động đúng kỳ vọng.
- **6 Loại Checkpoint phổ biến trên Desktop:**
  1. *Text / Value:* So khớp chuỗi hiển thị trên nhãn (Label, TextBox).
  2. *Property:* Kiểm tra trạng thái Enabled/Disabled, Visible, Checked.
  3. *Bitmap / Image:* So sánh hình ảnh pixel đồ thị, vùng vẽ.
  4. *DataGrid / Table:* Kiểm tra toàn bộ danh sách bản ghi hiển thị trên bảng.
  5. *File Output:* Kiểm tra nội dung tệp PDF, Excel xuất ra từ app.
  6. *Database:* Xác minh dữ liệu đã ghi xuống cơ sở dữ liệu ngầm.
- **Quy tắc vàng:** *"Không có Checkpoint thì không gọi là Kiểm thử!"*

**Ghi chú thuyết trình (Speaker Notes):**
> Nếu một kịch bản nhấn từ đầu đến cuối mà ứng dụng văng lỗi ngầm nhưng không có checkpoint bắt lại thì tool vẫn báo Pass. Đó là nguy cơ False Positive cực kỳ nguy hiểm. Checkpoint chính là thước đo quyết định chất lượng kịch bản.

---

## Slide 12: Fully Automated vs Semi-Automated

| Tiêu chí | Fully Automated | Semi-Automated |
|---|---|---|
| **Cơ chế hoạt động** | Tự động 100% từ chuẩn bị, thực thi đến báo cáo | Máy chạy phần lặp lại, người kiểm tra phần cảm quan |
| **Sự can thiệp của người** | Hoàn toàn không cần giám sát | Có sự phối hợp trực tiếp của tester |
| **Chi phí thiết lập** | Cao (cần framework hoàn chỉnh, xử lý ngoại lệ) | Trung bình (script hỗ trợ từng tác vụ riêng rẽ) |
| **Độ linh hoạt** | Kém linh hoạt khi giao diện đổi đột ngột | Rất linh hoạt vì con người chủ động phán đoán |
| **Ứng dụng tối ưu** | Regression Suite, Smoke Test, Nightly Run CI/CD | Usability Testing, Exploratory Testing, Phần cứng |

**Ghi chú thuyết trình (Speaker Notes):**
> Không phải lúc nào tự động hóa 100% cũng là phương án tối ưu. Với các bài test về cảm quan đồ họa hoặc liên quan đến máy in, thiết bị ngoại vi, phương pháp Bán tự động (Semi-Automated) vừa tiết kiệm chi phí vừa mang lại hiệu quả thực tế cao hơn.

---

## Slide 13: Khi nào nên & Không nên làm Automation?

- **NÊN ÁP DỤNG KHI:**
  - Kịch bản kiểm thử hồi quy cần chạy lặp lại nhiều lần qua mỗi bản phát hành.
  - Kịch bản cần kiểm tra với khối lượng dữ liệu khổng lồ (DDT).
  - Kịch bản cần kiểm tra tính năng cốt lõi (Core Business) đã ổn định.
  - Kịch bản cần phản hồi tức thời trong đường ống CI/CD.
- **KHÔNG NÊN ÁP DỤNG KHI:**
  - Ứng dụng hoặc tính năng đang thay đổi giao diện/nghiệp vụ liên tục.
  - Kịch bản chỉ chạy thử nghiệm 1 đến 2 lần rồi bỏ.
  - Các bài kiểm thử trải nghiệm người dùng đòi hỏi cảm nhận thị giác.
  - Thời gian viết script kiểm thử lớn hơn nhiều lần thời gian test bằng tay.
- **Nguyên tắc ngón tay cái:** Chạy lặp lại **từ 3 lần trở lên** thì hãy cân nhắc tự động hóa.

**Ghi chú thuyết trình (Speaker Notes):**
> Đây là chiếc la bàn giúp đội ngũ QA không bị sa đà vào việc "tự động hóa phong trào". Cần đánh giá kỹ chi phí bỏ ra viết và bảo trì so với lợi ích thời gian tiết kiệm được.

---

## Slide 14: Toàn cảnh thị trường công cụ Desktop Automation

- **Nhóm Mã nguồn mở / Lập trình (Code-based):**
  - *WinAppDriver:* Chuẩn Appium/WebDriver của Microsoft, miễn phí, mạnh mẽ cho Win10/11.
  - *PyAutoGUI / SikuliX:* Dựa trên tọa độ và thị giác máy tính OpenCV, dễ tiếp cận.
  - *Robot Framework:* Hướng từ khóa (Keyword-Driven), mở rộng qua FlaUI.
- **Nhóm Thương mại / Trọn gói (All-in-One Commercial):**
  - *TestComplete (SmartBear):* Hàng đầu cho doanh nghiệp, tích hợp AI, Object recognition vượt trội.
  - *Ranorex Studio:* RanoreXPath cực mạnh, giao diện chuyên nghiệp, ổn định cao.
  - *OpenText UFT One:* Giải pháp truyền thống cho các tập đoàn tài chính/ERP quy mô lớn.
  - *Katalon Studio:* Freemium, giao diện thân thiện, đóng gói sẵn nhiều tính năng.

**Ghi chú thuyết trình (Speaker Notes):**
> Thị trường chia thành hai trường phái rõ rệt: Một bên là các thư viện code mã nguồn mở linh hoạt và miễn phí, bên kia là các nền tảng thương mại trả phí có giao diện đồ họa đầy đủ tính năng.

---

## Slide 15: Khung 6 nhóm tiêu chí đánh giá công cụ (21 Tiêu chí)

- **1. Năng lực kỹ thuật (Technical - Trọng số cao nhất):**
  - Hỗ trợ công nghệ UI (Win32, WPF, Qt, Electron), Object Recognition (UIA), DDT, Checkpoints, CI/CD.
- **2. Khả năng sử dụng (Usability):**
  - Độ dốc học tập (Learning Curve), tài liệu hướng dẫn, cộng đồng người dùng, IDE tích hợp.
- **3. Hiệu năng & Độ ổn định (Performance & Reliability):**
  - Tốc độ thực thi, độ ổn định chống flaky test, cơ chế chờ thông minh (Waits).
- **4. Chi phí & Giá trị đầu tư (Cost & ROI):**
  - Bản quyền (Free vs Paid), chi phí setup môi trường, chi phí đào tạo nhân lực, thời gian hoàn vốn.
- **5. Khả năng bảo trì (Maintainability):**
  - Kháng biến động UI, hỗ trợ Page Object Model (POM), tái sử dụng code, quản lý Git.
- **6. Hệ sinh thái & Khả năng mở rộng (Ecosystem):**
  - Plugin, Framework mở rộng, hỗ trợ từ hãng/cộng đồng, tính năng AI thông minh.

**Ghi chú thuyết trình (Speaker Notes):**
> Để không bị cảm tính khi chọn tool, nhóm đã lượng hóa thành 6 nhóm với 21 tiêu chí cụ thể. Mỗi tiêu chí đều có thang điểm từ 1 đến 5 và gán trọng số tương ứng để quy về thang 100 điểm.

---

## Slide 16: Ma trận đối chiếu & Định hướng chọn Tool A / Tool B

- **Biểu mẫu Ma trận chấm điểm (Thang 100 điểm):**
  - Điểm quy đổi = Điểm đánh giá (1-5) × Trọng số tiêu chí.
  - Áp dụng độc lập cho cả hai công cụ.
- **Định hướng lựa chọn 2 công cụ đại diện:**
  - *Nguyên tắc 1 (Đối trọng giải pháp):* 1 công cụ Mã nguồn mở hướng lập trình đối đầu 1 công cụ Thương mại trọn gói có GUI.
  - *Nguyên tắc 2 (Common Case Study):* Bắt buộc cả 2 tool cùng thực thi trên một ứng dụng mẫu thống nhất để so sánh khách quan.
  - *Nguyên tắc 3 (Khả thi học thuật):* Có thể cài đặt và demo thực tế trong môi trường học tập.
- **Chuyển tiếp:** Xin mời bạn **Kan (trình bày Tool A)** và bạn **Tùng (trình bày Tool B)** tiếp nối phần demo thực nghiệm!

**Ghi chú thuyết trình (Speaker Notes):**
> Khung tiêu chí và ma trận chấm điểm này đã sẵn sàng. Ngay sau đây, Kan sẽ đại diện trình bày về Tool A và Tùng trình bày về Tool B, cùng áp dụng trên một bài toán thực tế để chúng ta thấy rõ ưu nhược điểm của từng trường phái. Xin cảm ơn thầy và các bạn đã lắng nghe!
