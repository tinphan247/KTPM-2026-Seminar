# 📜 NỘI QUY VÀ NGUYÊN TẮC LÀM VIỆC NHÓM
## Đề tài Seminar: Automation Testing for Desktop Applications
### Nhóm 02 – Lớp Kiểm thử phần mềm (Software Testing) – FIT@HCMUS
**Thời gian áp dụng:** Đợt làm việc nước rút Lần 2 (27/10/2026 – 31/10/2026)  
**Nhóm trưởng:** Phan Trung Tín (MSSV: 23120372)

---

## 🎯 1. TÔN CHỈ & MỤC TIÊU CHUNG

1. **Mục tiêu tối thượng:** Hoàn thành xuất sắc bài Seminar Lần 2, nộp đúng hạn trước **18:00 ngày 30/10/2026** (trước hạn chót 31/10 của Giảng viên), đạt điểm số cao nhất ở cả 3 phần: Báo cáo kỹ thuật, Demo thực nghiệm, và Slide thuyết trình.
2. **Nguyên tắc cốt lõi:**
   - **Minh bạch (Transparency):** Mọi đóng góp đều phải được ghi nhận rõ ràng qua commit trên Git, checklist và nhật ký công việc.
   - **Đúng hạn (Punctuality):** Tuyệt đối không trễ deadline các mốc từng ngày.
   - **Chủ động & Tương trợ (Proactivity & Support):** Gặp khó khăn kỹ thuật phải báo ngay để nhóm cùng giải quyết, không ôm việc hay giấu lỗi.
   - **Chất lượng học thuật (Academic Rigor):** Bài báo cáo và demo phải thể hiện sự đầu tư chuyên sâu, có số liệu thực nghiệm định lượng, không làm đối phó.

---

## 👥 2. PHÂN CÔNG VAI TRÒ & TRÁCH NHIỆM

| STT | Thành viên | MSSV | Vai trò chính | Trách nhiệm then chốt |
|:---:|---|:---:|---|---|
| **M1** | **Phan Trung Tín** | 23120372 | **Nhóm trưởng (Team Lead)** | • Điều phối tiến độ, tổ chức họp sync hằng ngày.<br>• Xây dựng ứng dụng mẫu `MiniSum.exe` (v1, v2, v3).<br>• Bổ sung cơ sở lý thuyết (POM, Flaky Test, Wait, Oracle).<br>• Review Pull Request, merge code, đóng gói ZIP và nộp bài.<br>• Có quyền quyết định cuối cùng khi nhóm có bất đồng kỹ thuật. |
| **M2** | **Nguyễn Lê Quang Kan** | 23120279 | **Chuyên trách Katalon Studio** | • Thiết lập môi trường và cấu hình Katalon Studio kết nối WinAppDriver.<br>• Thực nghiệm 3 nhóm demo (Record-Playback, Checkpoint, Data-Driven).<br>• Viết tài liệu phân tích nguyên lý hoạt động sâu sắc của Katalon.<br>• Quay video demo Katalon thuyết minh tiếng Việt rõ ràng. |
| **M3** | **Bùi Quang Tùng** | 20120397 | **Chuyên trách WinAppDriver** | • Thiết lập WinAppDriver và Accessibility Insights for Windows.<br>• Phát triển dự án test C# NUnit áp dụng Page Object Model (POM).<br>• Thực nghiệm 3 nhóm demo (Basic, Assert + Screenshot on Fail, DDT).<br>• Viết tài liệu nguyên lý WinAppDriver & quay video demo WinAppDriver. |
| **M4** | **Trần Vũ Quang** | 23120346 | **Chuyên trách AI & Comparison** | • Thiết kế Prompt sinh Test case BVA và Test script tự động.<br>• Thực nghiệm định lượng: đo thời gian viết test, LOC, tỷ lệ ảo giác của AI.<br>• Cập nhật bảng đối chiếu công cụ và vẽ biểu đồ so sánh thực nghiệm.<br>• Chuẩn hóa dữ liệu test và quay video demo thực tế quy trình AI. |
| **M5** | **Phạm Tấn Phát** | 20120636 | **Chuyên trách Slide Thuyết trình** | • Nghiên cứu toàn bộ báo cáo để cô đọng thành slide thuyết trình 8 phần.<br>• Thiết kế chuẩn thẩm mỹ: nền trắng, chữ đen, font chữ to rõ (≥18pt).<br>• Chèn hình ảnh thực nghiệm, biểu đồ số liệu trực quan, layout khoa học.<br>• Xuất bản file PowerPoint (`.pptx`) và export PDF chính thức (`.pdf`). |

---

## 🌿 3. QUY ĐỊNH LÀM VIỆC VỚI GIT & GITHUB

> ⚠️ **LƯU Ý ĐẶC BIỆT:** Giảng viên sẽ kiểm tra trực tiếp `git log` để đánh giá công sức thực tế của từng cá nhân. Do đó, việc tuân thủ quy tắc Git là **BẮT BUỘC**.

### 3.1. Quy tắc phân nhánh (Branching Strategy)
- Nhánh `main`: Chỉ chứa mã nguồn và tài liệu ổn định đã được kiểm duyệt. **Tuyệt đối không push trực tiếp lên main.**
- Mỗi thành viên làm việc **duy nhất** trên nhánh feature cá nhân:
  - `feature/tin-setup-report` (Tín)
  - `feature/kan-katalon` (Kan)
  - `feature/tung-winappdriver` (Tùng)
  - `feature/quang-ai-comparison` (Quang)
  - `feature/phat-slide` (Phát)

### 3.2. Quy ước Commit Message (Conventional Commits)
Mỗi commit phải ghi rõ loại hành động và tên người thực hiện:
```text
feat(kan):    Thêm test script Record-Playback cho màn hình Login
feat(tung):   Cài đặt Page Object Model cho CalculatorPage.cs
demo(quang):  Bổ sung prompt và output thực nghiệm sinh test case BVA
slide(phat):  Hoàn thành thiết kế slide Phần 4 - Katalon Studio
docs(tin):    Bổ sung lý thuyết Page Object Model vào 02-theory.md
fix(tung):    Sửa lỗi locator FindElementByAccessibilityId bị timeout
chore(tin):   Merge branch và cập nhật checklist nộp bài
```

### 3.3. Tần suất và kích thước commit
- **Chia nhỏ commit:** Mỗi tính năng / task nhỏ hoàn thành phải commit ngay. Tuyệt đối không để dồn 1 commit khổng lồ chứa hàng chục file vào cuối đợt.
- **Tần suất tối thiểu:** Mỗi thành viên phải có ít nhất **3 – 5 commit có ý nghĩa** mỗi ngày trong các ngày làm việc (27–30/10).
- **Trước khi bắt đầu làm việc mỗi ngày:** Chạy `git checkout main && git pull origin main` sau đó checkout về branch cá nhân và `git merge main` để cập nhật các thay đổi mới nhất từ đồng đội.

---

## 📁 4. QUY CHUẨN MÃ NGUỒN, TÀI LIỆU & FILE SIZE

1. **Cấu trúc thư mục:** Không tự ý tạo các thư mục nằm ngoài cấu trúc chuẩn của dự án:
   ```text
   KTPM-2026-Seminar/
   ├── docs/                   # Toàn bộ file báo cáo Markdown & screenshots
   ├── case-study-app/         # Mã nguồn & file thực thi MiniSum.exe
   ├── demo-scripts/           # Script kiểm thử Katalon & WinAppDriver
   ├── ai/                     # Prompts và outputs thực nghiệm AI
   └── slides/                 # Slide PowerPoint (.pptx) và PDF
   ```
2. **Giới hạn kích thước file (QUAN TRỌNG):**
   - Theo quy định môn học: **Mỗi file tải lên phải ≤ 20MB**.
   - Nếu file thực thi hoặc tài liệu vượt quá 20MB, phải dùng 7-Zip chia nhỏ thành nhiều phần (`.zip.001`, `.zip.002`...).
   - Video demo: **Không nộp file video mp4 nặng hàng trăm MB vào gói ZIP**, mà nộp qua danh sách liên kết YouTube (chế độ Unlisted) trong file `video-links.md`.
3. **Quy cách tài liệu Markdown & Slide:**
   - Sử dụng bảng mã **UTF-8**, cú pháp Markdown chuẩn.
   - Hình ảnh chụp màn hình phải crop gọn gàng vùng trọng tâm, độ phân giải sắc nét, lưu trong thư mục `docs/screenshots/<tool>/`.
   - Slide thuyết trình: **Nền trắng, chữ đen, font Arial/Calibri/Segoe UI kích thước ≥ 18pt**, tránh dàn trải chữ quá nhiều; tăng cường biểu đồ, sơ đồ luồng và ảnh minh họa.

---

## 🎥 5. TIÊU CHUẨN VIDEO DEMO THỰC NGHIỆM

Nhóm sẽ sản xuất **3 video demo riêng biệt** tương ứng với 3 nội dung:
1. `Demo Katalon Studio` (Phụ trách: Kan)
2. `Demo WinAppDriver C# NUnit` (Phụ trách: Tùng)
3. `Demo AI Test Automation` (Phụ trách: Quang)

**Yêu cầu kỹ thuật bắt buộc cho video:**
- **Độ phân giải:** Tối thiểu **1080p (Full HD)**, tốc độ khung hình mượt mà (30 hoặc 60 fps).
- **Âm thanh:** Thuyết minh bằng **tiếng Việt rõ ràng, dễ nghe**, không lẫn tạp âm ồn ào.
- **Thao tác:** Liền mạch, giải thích rõ: mục đích ca test -> thao tác chạy tool -> kết quả màn hình -> kết luận PASS/FAIL.
- **Thời lượng:** Mỗi video từ **5 đến 8 phút** (không quá ngắn gây sơ sài, không quá dài lan man).
- **Hạn nộp video:** Chậm nhất **12:00 trưa ngày 30/10/2026**, Kan, Tùng, Quang phải gửi file video cho Tín để upload lên YouTube và tổng hợp link.

---

## 🤖 6. NGUYÊN TẮC SỬ DỤNG TRÍ TUỆ NHÂN TẠO (AI)

1. **Tính minh bạch:** Được phép sử dụng các công cụ AI (ChatGPT, Gemini, Claude, GitHub Copilot) hỗ trợ công việc. Tuy nhiên, **toàn bộ việc sử dụng phải được kê khai trung thực** trong file `ai-usage-declaration.md`.
2. **Lưu trữ bằng chứng:**
   - Mọi prompt ra lệnh cho AI sinh test case hoặc script phải được lưu lại thành file `.md` trong `ai/prompts/`.
   - Kết quả do AI sinh ra phải lưu tại `ai/output/`.
3. **Trách nhiệm kiểm chứng (Human-in-the-loop):**
   - Tuyệt đối không sao chép mù quáng code do AI sinh ra nếu chưa chạy thử và hiểu rõ cơ chế.
   - Khi AI sinh sai locator hoặc script không chạy được, phải ghi nhận lại trường hợp lỗi đó (hallucination) để làm minh chứng so sánh thực nghiệm.

---

## 📊 7. CHÍNH SÁCH ĐÁNH GIÁ ĐÓNG GÓP (% CONTRIBUTION)

### 7.1. Mức cơ sở (Baseline)
- Khởi điểm ban đầu: **20.0% đều cho cả 5 thành viên** (dựa trên 24.0 giờ làm việc ước tính và số lượng task tương đương).

### 7.2. Quy tắc trừ điểm đóng góp:
- **Trễ hạn task:** Trễ hạn quá 6 giờ mà không báo trước hoặc không có lý do bất khả kháng: **-1% đến -2%** / lần.
- **Không tham gia sync tiến độ:** Vắng mặt buổi họp sync 21:00 hằng ngày mà không xin phép trước: **-1%** / buổi.
- **Chất lượng kém / Đùn đẩy việc:** Sản phẩm giao nộp qua loa, sai sót nghiêm trọng khiến thành viên khác phải làm lại hoàn toàn: **-3% đến -5%**.
- **Không có commit Git:** Không commit trên branch cá nhân đúng quy định: **-2%**.

### 7.3. Quy tắc cộng điểm đóng góp:
- **Cứu nguy blocker:** Chủ động hỗ trợ đồng đội giải quyết các lỗi kỹ thuật khó khăn: **+1% đến +2%**.
- **Vượt mức tiến độ & chất lượng xuất sắc:** Hoàn thành trước hạn với sản phẩm chỉn chu, chuyên nghiệp: **+1% đến +2%**.

### 7.4. Quy trình chốt %:
- Vào **15:00 ngày 30/10/2026**, cả nhóm sẽ họp nhanh qua Google Meet/Zalo để rà soát toàn bộ sản phẩm thực tế, đối chiếu commit log và biểu quyết chốt % cuối cùng trước khi Leader điền vào biểu mẫu Google Sheets chính thức.

---

## ⏰ 8. CHẾ ĐỘ LIÊN LẠC & BÁO CÁO HẰNG NGÀY

1. **Kênh trao đổi chính:** Nhóm **Zalo / Discord** của nhóm. Mọi thành viên phải bật thông báo cho nhóm.
2. **Daily Check-in (21:00 mỗi tối):**
   Mỗi tối vào lúc **21:00**, từng thành viên gửi tin nhắn báo cáo nhanh theo cú pháp:
   ```text
   [BÁO CÁO TIẾN ĐỘ - NGÀY ...]
   1. Đã hoàn thành hôm nay: (Mã task + tên task)
   2. Kế hoạch ngày mai: (Mã task dự kiến)
   3. Khó khăn / Cần hỗ trợ: (Nếu có thì mô tả rõ, nếu không thì ghi 'Không')
   ```
3. **Nguyên tắc "30 phút – 2 giờ":**
   - Khi gặp lỗi kỹ thuật (ví dụ không bắt được element, script crash, conflict git): Tự debug tối đa **30 - 45 phút**. Nếu không tìm ra nguyên nhân, **ngay lập tức gửi thông báo + ảnh chụp màn hình lên nhóm** để nhờ hỗ trợ, không được im lặng giấu lỗi quá 2 giờ.

---

> 🤝 **CAM KẾT CỦA TOÀN THỂ THÀNH VIÊN:**  
> Toàn bộ 5 thành viên đã đọc kỹ, thấu hiểu và nhất trí tuân thủ 100% các quy tắc trên vì sự thành công chung của nhóm 02!
