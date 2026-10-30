# BÁO CÁO TOÀN VĂN CHUYÊN ĐỀ SEMINAR – ROUND 2
# AUTOMATION TESTING FOR DESKTOP APPLICATIONS

- **Học phần:** Kiểm thử Phần mềm
- **Đơn vị:** Khoa Công nghệ Thông tin – Bộ môn Kỹ thuật Phần mềm
- **Nhóm thực hiện:** Nhóm 02 (ZipTool)
- **Giai đoạn:** Lần 2 – Seminar Automation Testing for Desktop Applications (27/10 – 30/10/2026)
- **Hạn nộp:** 31/10/2026

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

## BẢNG PHÂN CÔNG & TRẠCH NHIỆM (CẬP NHẬT LẦN 2)

| Thành viên | Vai trò / Phân công | Nội dung chi tiết phụ trách | Sản phẩm bàn giao | Trạng thái |
|---|---|---|---|:---:|
| **Tín** | **Team Lead + Theory & Integration** | - Bối cảnh, lý do chọn đề tài, mục tiêu/phạm vi.<br>- Cơ sở lý thuyết Automation Desktop.<br>- Tích hợp nội dung mới từ các nhóm còn lại.<br>- Đóng gói ZIP & nộp bài. | `01-introduction.md`<br>`02-theory.md`<br>`03-toolsurvey.md`<br>`report_v2.md` | **Hoàn thành** |
| **Kan** | **Tool A – Katalon Studio (M2)** | - Nghiên cứu nguyên lý Katalon Studio.<br>- Thiết lập kịch bản demo 3 nhóm (Setup, Record & Playback, DDT/BVA).<br>- Quay video demo. | `04-katalon-studio.md`<br>`demo-scripts/katalon/`<br>`docs/screenshots/katalon/` | **Hoàn thành** |
| **Tùng** | **Tool B – WinAppDriver (M3)** | - Nghiên cứu WinAppDriver + C# NUnit.<br>- Thiết lập demo (Basic, Assert + Screenshot on Fail, DDT).<br>- Quay video demo. | `05-winappdriver.md`<br>`demo-scripts/winappdriver/` | **Hoàn thành** |
| **Quang** | **AI + Comparison + Exercise (M4)** | - Prompt Engineering, thực nghiệm AI.<br>- So sánh Katalon vs WinAppDriver.<br>- Thiết kế bài tập. | `06-comparison.md`<br>`07-ai-desktop-automation.md`<br>`ai/` | **Hoàn thành** |
| **Phát** | **Slide PowerPoint (M5)** | - Thiết kế slide báo cáo. | `slides/seminar-group02.pptx` | **Chưa bắt đầu** |

---

# Phần 1: Giới Thiệu & Bối Cảnh (Introduction)

## 1. Bối cảnh

Phần mềm desktop vẫn giữ vai trò đặc biệt quan trọng trong doanh nghiệp (tài chính, ngân hàng, y tế, sản xuất, POS…). Khác với web,
desktop app tương tác sâu với hệ điều hành, driver phần cứng và file system, nên kiểm thử thủ công rút ngắn không đáp ứng được nhu cầu
phản hồi nhanh trong chu kỳ phát hành ngắn.

Vì vậy seminar **Automation Testing for Desktop Applications** nhóm 02 (ZipTool) đã chọn ứng dụng mẫu **MiniSum** (WinForms C#/.NET) làm
case study, và tổng hợp bài học từ 2 công cụ tự động hóa chính (Katalon Studio – WinAppDriver) cùng hướng nghiệm AI.

## 2. Lý do chọn đề tài

| Vấn đề thực tiễn | Lý do quan tâm nghiên cứu |
|---|---|
| Desktop app trong doanh nghiệp | Nhiều hệ thống cốt lõi vẫn chạy trên desktop, nhu cầu kiểm thử không suy giảm. |
| Kiểm thử thủ công hồi quy | Tốn thời gian/công sức, dễ trôi bug, không đủ tốc độ CI/CD. |
| Độ phức tạp đặc thù của desktop | Khác web về DOM/HTML, đòi hỏi locator/automation framework chuyên biệt. |
| Thách thức lựa chọn công cụ | Hệ sinh thái automation desktop rộng, cần tiêu chí đánh giá rõ ràng. |
| Xu hướng AI | GenAI hỗ trợ sinh test case/script/self-healing locator. |

## 3. Mục tiêu seminar

1. Làm chủ lý thuyết nền tảng về Automation Testing cho Desktop.
2. Khảo sát thị trường, xây dựng bộ tiêu chí đánh giá 2 công cụ đại diện.
3. Xây dựng & chạy kịch bản thực nghiệm: Setup / Record & Playback / DDT-BVA.
4. Nghiên cứu AI trong kiểm thử desktop.
5. Thiết kế bài tập thực hành.

## 4. Phạm vi seminar

- Hệ điều hành: Windows 10/11.
- Ứng dụng: MiniSum (WinForms C# – .NET 8).
- Kỹ thuật: Record & Playback, Checkpoints & Assertions, DDT, Waits, POM, Test Oracle, Recovery Testing.

---

# Phần 2: Cơ Sở Lý Thuyết Kiểm Thử Tự Động Desktop (Theory)

- Automation Testing là gì; Desktop Application Testing; đặc điểm & khó khăn đặc thù.
- Record & Playback; Data-Driven Testing; Checkpoints & Assertions.
- **Page Object Model (POM)** – định nghĩa, code C#, ưu điểm (T08).
- **Flaky Test** – nguyên nhân gốc rễ và cách xử lý (T09).
- **Wait Strategy** – Implicit / Explicit / Fluent Wait (T10).
- **Test Oracle** – cơ chế kiểm chứng trong kiểm thử giao diện desktop (T11).
- **Recovery Testing** – cơ chế phục hồi khi AUT treo/crash (T12).

→ Toàn bộ nội dung chi tiết tại: [`docs/02-theory.md`](02-theory.md)

---

# Phần 3: Khảo Sát Thị Trường & Bộ Tiêu Chí Đánh Giá (Tool Survey)

- Khảo sát 9 công cụ automation desktop (Katalon, WinAppDriver, Appium, Robot Framework, Cypress…).
- Bộ tiêu chí 6 nhóm: Technical Capabilities, Usability & Learning Curve, Performance & Reliability, Cost & ROI, Maintainability, Ecosystem.
- Xây dựng ma trận so sánh giữa Tool A và Tool B.

→ Toàn bộ nội dung: [`docs/03-toolsurvey.md`](03-toolsurvey.md)

---

# Phần 4: Nghiên Cứu Công Cụ Đại Diện A – Katalon Studio

- Kiến trúc thực thi (Windows Desktop Testing Engine, session, launcher).
- Object Repository & Object Spy (Windows Object Spy).
- Test Suite / Test Case / Test Listener.
- Demo 1: Setup; Demo 2: Record & Playback + Checkpoint; Demo 3: DDT BVA với Excel.
- Custom Keyword (LoginKeyword) hỗ trợ Keyword-Driven Testing.

→ Toàn bộ: [`docs/04-katalon-studio.md`](04-katalon-studio.md) | Scripts: [`demo-scripts/katalon/`](demo-scripts/katalon/)

---

# Phần 5: Nghiên Cứu Công Cụ Đại Diện B – Microsoft WinAppDriver

- WinAppDriver + C# NUnit; AppiumOptions; vòng đời session.
- Locators: AccessibilityId, Name, XPath.
- Screenshot on Fail; ExcelHelper (NPOI); DDT với `[TestCaseSource]`.
- POM: `LoginPage`, `CalculatorPage`; refactor code test dùng POM.

→ Toàn bộ: [`docs/05-winappdriver.md`](05-winappdriver.md) | Scripts: [`demo-scripts/winappdriver/`](demo-scripts/winappdriver/)

---

# Phần 6: So Sánh Đối Chiếu Hai Công Cụ (Comparison)

- Bảng tổng hợp so sánh 2 công cụ theo các nhóm tiêu chí.
- So sánh chi tiết theo 3 nhánh: Record & Playback; Checkpoints & Assertions; Data-Driven Testing.
- **So sánh định lượng:** thời gian viết test thủ công vs AI hỗ trợ (3 lượt), số dòng mã (LOC), độ phức tạp và tỷ lệ sửa lại — theo số liệu thực nghiệm từ nhóm (Quang – M4).

→ Toàn bộ: [`docs/06-comparison.md`](06-comparison.md)

---

# Phần 7: Ứng Dụng Trí Tuệ Nhân Tạo (AI) Trong Desktop Automation

- Vì sao AI là bước tiến cho desktop automation (self-healing locator, visual AI, script generation, synthetic data, root cause).
- Hiện trạng AI trên 2 công cụ đã nghiên cứu.
- Demo AI: Prompt → Sinh test case → Sinh script → Run test.
- Bài học thực tế & best practices.

→ Toàn bộ: [`docs/07-ai-desktop-automation.md`](07-ai-desktop-automation.md) | Prompts/outputs: [`ai/prompts/`](ai/prompts/), [`ai/output/`](ai/output/)

---

# Phần 8: Hệ Thống Bài Tập Thực Hành Đề Xuất (Exercise)

- Bài tập 1: Triển khai kịch bản kiểm thử cơ bản (mở app, thao tác, checkpoint).
- Bài tập 2: Kiểm thử khi có dữ liệu (Data-Driven/BVA).
- Bài tập 3: Nâng cao – xử lý biên & tối ưu (POM, self-healing, recovery).

→ Toàn bộ: [`docs/08-exercises.md`](08-exercises.md)

---

# Phần 9: Kết Luận & Hướng Phát Triển (Conclusion)

- Tổng kết kết quả seminar: xây dựng được pipeline automation cho desktop app MiniSum (Login → Calculator → History → Validation).
- Bài học rút ra: kiểm thử tự động desktop cần đủ 3 yếu tố (công cụ + locator + kiểm chứng), AI hỗ trợ nhưng cần verify.
- Hướng phát triển: CI/CD cho desktop, self-healing, mở rộng case study.

---

## Phụ lục

- Mã nguồn: [`case-study-app/`](case-study-app/)
- Script kiểm thử: [`demo-scripts/`](demo-scripts/)
- Ảnh chụp: [`docs/screenshots/`](docs/screenshots/)
- Video demo: [`video-links.md`](video-links.md)
- Kê khai AI: [`ai-usage-declaration.md`](ai-usage-declaration.md)
- Nhật ký commit: [`git-commit-log.md`](git-commit-log.md)

---

**BÁO CÁO TỔNG VĂN – ROUND 2** đã được tổng hợp tại `docs/report_v2.md` (Task T13).
