# Kế hoạch Seminar: Automation Testing for Desktop Apps

Môn Software Testing – FIT@HCMUS · Nhóm 4 thành viên · Thời lượng đề xuất: 8 tuần (W1–W8)

## 1. Cấu trúc nhóm

| Member | Vai trò | Trách nhiệm chính | Review chéo |
| --- | --- | --- | --- |
| M1 | Theory & Testing Foundation | Lý thuyết, kiến trúc, tiêu chí đánh giá tool, mapping lý thuyết→tool | Review Tool A |
| M2 | Tool A (đề xuất: **WinAppDriver/Appium + Python** hoặc **pywinauto**) | Nghiên cứu + thực nghiệm đầy đủ Tool A | Review Tool B |
| M3 | Tool B (đề xuất: **FlaUI (C#)** hoặc **AutoIt/Sikuli**) | Nghiên cứu + thực nghiệm Tool B, cùng case study | Review Theory |
| M4 | AI + Integration + Comparison (PM/Integrator) | AI demo, so sánh tool, case study chung, bài tập, tích hợp | Review Integration (do M1 làm chéo bổ sung, xem mục 9) |

Lưu ý: chọn tool cuối cùng ở task T-110 dựa trên tiêu chí của M1. Case study đề xuất: **Windows Calculator / Notepad++ / ứng dụng WinForms tự viết (Student Manager)** – nên dùng app WinForms/WPF tự viết nhỏ để kiểm soát được bug và có PASS/FAIL chủ động.

## 2–3. Work Breakdown Structure

Priority: H/M/L. Status khởi tạo: Todo.

### PHASE 1 – Research (W1–W2)

| ID | Member | Task | Description | Input | Output | Evidence | Dependency | Priority | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-101 | M1 | Lý thuyết Automation & Desktop Testing | Định nghĩa, phân loại, khái niệm, ưu/nhược, khi nào dùng/không | Sách ISTQB, tài liệu tool vendor | `theory.md` | Link nguồn, notes, commit | – | H | Todo |
| T-102 | M1 | Thuật ngữ | Bảng thuật ngữ EN–VI (locator, UIA, Win32, MSAA, flaky, wait…) | T-101 | `terminology.md` | Commit, nguồn | T-101 | M | Todo |
| T-103 | M1 | Khái niệm R&P, Data-driven, Checkpoint, Semi/Full | Mô tả + ví dụ minh hoạ mỗi khái niệm | T-101 | `theory-core-concepts.md` | Notes, link | T-101 | H | Todo |
| T-104 | M1 | Kiến trúc & workflow automation | Vẽ architecture + workflow | T-101 | `architecture.drawio`, `workflow.drawio` + PNG | File drawio, PNG | T-101 | H | Todo |
| T-105 | M1 | Tiêu chí đánh giá tool | Bộ tiêu chí có trọng số | T-101, yêu cầu GV | `tool-evaluation-criteria.md` | Commit, meeting note | T-101 | H | Todo |
| T-106 | M2 | Khảo sát tool nhóm UIA/Appium | Liệt kê ≥3 ứng viên, chấm theo tiêu chí | T-105 | `tool-survey-a.md` | Link docs, screenshot trang docs | T-105 | H | Todo |
| T-107 | M3 | Khảo sát tool nhóm FlaUI/AutoIt/Sikuli | Liệt kê ≥3 ứng viên, chấm theo tiêu chí | T-105 | `tool-survey-b.md` | Link docs, screenshot | T-105 | H | Todo |
| T-108 | M4 | Khảo sát AI trong testing | Tổng quan AI testing, AI desktop (LLM, vision, self-healing) | Papers, blog, docs | `ai-survey.md` | Link, notes | – | M | Todo |
| T-109 | M4 | Định nghĩa Case Study chung | Chọn app, 3 scenario (Install/Basic/Complex), test data schema | T-105 | `case-study.md`, `test-scenarios.xlsx` | Meeting note, decision log | T-105 | H | Todo |
| T-110 | M1 | Chốt Tool A/B | Họp quyết định dựa trên điểm số | T-106, T-107, T-109 | `decision-log.md` (mục tool selection) | Meeting note, bảng điểm | T-106,T-107,T-109 | H | Todo |
| T-111 | M1 | Theory → Tool mapping | Mỗi khái niệm lý thuyết map sang tính năng cụ thể mỗi tool | T-103, T-110 | `theory-tool-mapping.md` | Commit | T-110 | M | Todo |

### PHASE 2 – Experiment (W3–W5)

| ID | Member | Task | Description | Input | Output | Evidence | Dependency | Priority | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-201 | M2 | Tool A overview + architecture | Chức năng, nguyên lý, workflow tool A | T-110 | `tool-a/research.md` | Link docs, diagram PNG | T-110 | H | Todo |
| T-202 | M2 | Tool A – Demo 1 Installation | Cài, cấu hình, tạo project, chạy script đầu tiên | T-201 | `tool-a/installation.md`, `tool-a/test-project/` | `screenshot-a-01..n.png`, log chạy | T-201 | H | Todo |
| T-203 | M2 | Tool A – Demo 2 Basic | UI interaction, R&P, checkpoint | T-202, T-109 | `tool-a/demo-scenarios.md` (Demo 2), `tests/basic/` | Screenshot, execution log | T-202 | H | Todo |
| T-204 | M2 | Tool A – Data-driven | Chạy test từ CSV/Excel | T-203 | `tool-a/test-data/test-data.xlsx`, `tests/data_driven/` | Report chạy ≥5 dòng data | T-203 | H | Todo |
| T-205 | M2 | Tool A – Demo 3 Complex | Workflow nhiều bước, test data, verification, PASS/FAIL (có ≥1 case FAIL cố ý) | T-204 | `tests/complex/`, `tool-a/demo-scenarios.md` (Demo 3) | Report HTML/xml, screenshot PASS/FAIL | T-204 | H | Todo |
| T-206 | M2 | Tool A – Error handling, reporting, maintenance | Wait, retry, screenshot on fail, report, đổi UI để thử maintain | T-205 | `tool-a/error-reporting-maintenance.md` | Log, before/after code diff | T-205 | M | Todo |
| T-207 | M2 | Tool A – Limitations + video | Case tool không xử lý tốt; quay video | T-205 | `tool-a/limitations.md`, `demo-tool-a.mp4` | Video file, link YouTube unlisted | T-206 | H | Todo |
| T-211 | M3 | Tool B overview + architecture | Như T-201 | T-110 | `tool-b/research.md` | Link docs, diagram PNG | T-110 | H | Todo |
| T-212 | M3 | Tool B – Demo 1 Installation | Như T-202 | T-211 | `tool-b/installation.md`, `tool-b/test-project/` | `screenshot-b-01..n.png`, log | T-211 | H | Todo |
| T-213 | M3 | Tool B – Demo 2 Basic | Cùng scenario Basic với Tool A | T-212, T-109 | `tool-b/demo-scenarios.md` (Demo 2) | Screenshot, log | T-212 | H | Todo |
| T-214 | M3 | Tool B – Data-driven | Cùng bộ `test-data.xlsx` với Tool A | T-213, T-204 | `tool-b/tests/data_driven/` | Report ≥5 dòng data | T-213 | H | Todo |
| T-215 | M3 | Tool B – Demo 3 Complex | Cùng workflow Complex với Tool A | T-214, T-205 (scenario) | `tool-b/tests/complex/` | Report, screenshot PASS/FAIL | T-214 | H | Todo |
| T-216 | M3 | Tool B – Error handling, reporting, maintenance | Như T-206 | T-215 | `tool-b/error-reporting-maintenance.md` | Log, diff | T-215 | M | Todo |
| T-217 | M3 | Tool B – Limitations + video | Như T-207 | T-215 | `tool-b/limitations.md`, `demo-tool-b.mp4` | Video, link YouTube | T-216 | H | Todo |
| T-218 | M4 | Chuẩn bị app case study | Build/host app WinForms/WPF có bug cài sẵn + bản fixed | T-109 | `case-study-app/` (source + release) | Build log, screenshot app | T-109 | H | Todo |

### PHASE 3 – AI (W4–W6)

| ID | Member | Task | Description | Input | Output | Evidence | Dependency | Priority | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-301 | M4 | AI generate Test Case | Prompt template sinh test case từ spec/UI | T-109 | `ai/prompts/testcase-gen.md`, `ai/output/testcases-ai.xlsx` | Prompt + output gốc, screenshot hội thoại | T-109 | H | Todo |
| T-302 | M4 | AI generate Test Data | Sinh data hợp lệ/biên/sai, đưa vào data-driven | T-301 | `ai/output/test-data-ai.csv` | Prompt, file, kết quả chạy | T-301 | H | Todo |
| T-303 | M4 | AI sinh automation script | Sinh script cho Tool A và B từ test case; sửa lỗi AI | T-203, T-213, T-301 | `ai/output/script-ai-tool-a.py`, `script-ai-tool-b.*` | Diff trước/sau sửa, log chạy | T-203,T-213 | H | Todo |
| T-304 | M4 | AI phân tích lỗi | Đưa log/screenshot fail cho AI phân tích root cause | T-205, T-215 | `ai/failure-analysis.md` | Log gốc, phản hồi AI, đánh giá đúng/sai | T-205,T-215 | M | Todo |
| T-305 | M4 | AI hỗ trợ maintenance | Đổi UI app → AI cập nhật locator | T-206, T-216 | `ai/maintenance-demo.md` | Diff locator, kết quả chạy | T-206,T-216 | M | Todo |
| T-306 | M4 | Tổng quát hoá AI workflow | Prompt library tái sử dụng + quy trình + đánh giá độ chính xác | T-301..T-305 | `ai/reusable-workflow.md`, `ai/evaluation.xlsx` | Bảng đo | T-305 | H | Todo |
| T-307 | M4 | Video AI demo | Quay ≥2 AI demo | T-303,T-304 | `demo-ai.mp4` | Video, link YouTube | T-306 | H | Todo |

### PHASE 4 – Integration (W6–W7)

| ID | Member | Task | Description | Input | Output | Evidence | Dependency | Priority | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-401 | M4 | So sánh Tool A vs B | Bảng 16 tiêu chí, số liệu thực nghiệm (thời gian chạy, số dòng code, flaky rate) | T-207, T-217 | `comparison.md`, `comparison-metrics.xlsx` | Log đo, screenshot | T-207,T-217 | H | Todo |
| T-402 | M1 | Bổ sung lý thuyết từ kết quả thực nghiệm | Cập nhật theory khi thực nghiệm khác lý thuyết | T-401 | `theory.md` v2, `theory-vs-practice.md` | Diff commit | T-401 | M | Todo |
| T-403 | M4 | Bài tập cho lớp | 3 bài (cài, record+checkpoint, data-driven) + đáp án + rubric | T-401 | `exercises/exercise-01..03.md`, `exercises/solutions/`, `rubric.md` | Chạy thử đáp án (screenshot) | T-401 | H | Todo |
| T-404 | M4 | Báo cáo tích hợp | Ghép report đầy đủ, mục lục, trích dẫn | Mọi `.md` | `report.docx`, `report.pdf` | Commit, version | T-401,T-402 | H | Todo |
| T-405 | M4 | Kiểm tra nhất quán | Report vs slide vs demo, thuật ngữ, số liệu | T-404 | `consistency-check.md` | Checklist đã tick | T-404 | H | Todo |
| T-406 | M1 | Review Tool A | Dùng checklist R-A | T-207 | `reviews/review-tool-a.md` | PR comment | T-207 | H | Todo |
| T-407 | M2 | Review Tool B | Dùng checklist R-B, chạy lại source của Tool B trên máy mình | T-217 | `reviews/review-tool-b.md` | PR comment, log chạy lại | T-217 | H | Todo |
| T-408 | M3 | Review Theory | Dùng checklist R-T | T-402 | `reviews/review-theory.md` | PR comment | T-402 | H | Todo |
| T-409 | M2 | Review Integration | Dùng checklist R-I | T-405 | `reviews/review-integration.md` | PR comment | T-405 | H | Todo |

### PHASE 5 – Presentation (W7–W8)

| ID | Member | Task | Description | Input | Output | Evidence | Dependency | Priority | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-501 | M1 | Slide phần lý thuyết | Slide + speaker notes | T-402 | `slides/part1-theory.pptx` | Commit | T-402 | H | Todo |
| T-502 | M2 | Slide + demo script Tool A | Slide, kịch bản demo trực tiếp | T-207 | `slides/part2-tool-a.pptx`, `demo-script-a.md` | Commit | T-207 | H | Todo |
| T-503 | M3 | Slide + demo script Tool B | Như T-502 | T-217 | `slides/part3-tool-b.pptx`, `demo-script-b.md` | Commit | T-217 | H | Todo |
| T-504 | M4 | Slide AI + so sánh + tổng hợp | Ghép slide hoàn chỉnh | T-307, T-401, T-501..T-503 | `slides/seminar-final.pptx` | Commit | T-501..T-503 | H | Todo |
| T-505 | All | Rehearsal ×2 | Diễn tập có bấm giờ, ghi feedback | T-504 | `rehearsal-notes.md` | Ảnh/ghi hình rehearsal, meeting note | T-504 | H | Todo |
| T-506 | M4 | Upload YouTube | Upload 3 video, điền link vào report | T-207,T-217,T-307 | `video-links.md` | Screenshot trang YouTube | T-307 | H | Todo |
| T-507 | All | Review với giảng viên | Gửi bản nháp, ghi nhận feedback | T-504 | `teacher-feedback.md` | Email/ảnh trao đổi | T-504 | M | Todo |

### PHASE 6 – Finalization (W8)

| ID | Member | Task | Description | Input | Output | Evidence | Dependency | Priority | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T-601 | All | Sửa theo feedback | Mỗi người sửa phần của mình | T-507 | Issue đóng + PR | Link PR | T-507 | H | Todo |
| T-602 | M4 | Final report + slide | Xuất bản cuối | T-601 | `report-final.pdf`, `seminar-final.pptx` | Git tag | T-601 | H | Todo |
| T-603 | M2, M3 | Dọn source & test data | README chạy lại được, requirements | T-601 | `tool-a/`, `tool-b/` final | Chạy lại sạch trên máy sạch (log) | T-601 | H | Todo |
| T-604 | M4 | Final evidence pack | Tổng hợp minh chứng, work allocation | Toàn bộ | `evidence/INDEX.md`, `work-allocation.md` | Link commit/PR/meeting | T-602,T-603 | H | Todo |
| T-605 | M4 | Final checklist + tag v1.0 | Tick checklist, tạo release | T-604 | `FINAL-CHECKLIST.md`, tag `v1.0` | Release link | T-604 | H | Todo |

## 4. Deliverables từng member

- **M1:** `theory.md`, `terminology.md`, `architecture.drawio`, `workflow.drawio`, `tool-evaluation-criteria.md`, `theory-tool-mapping.md`, `part1-theory.pptx`, 3 review.
- **M2:** `tool-a/` (research, installation, demo-scenarios, test-project, test-data, screenshots, results, limitations), `demo-tool-a.mp4`, slide Tool A.
- **M3:** `tool-b/` (cùng cấu trúc), `demo-tool-b.mp4`, slide Tool B.
- **M4:** `ai/`, `comparison.md`, `case-study.md`, `case-study-app/`, `exercises/`, `report.pdf`, `seminar-final.pptx`, `FINAL-CHECKLIST.md`, `demo-ai.mp4`.

Cân bằng: M2/M3 thiên về thực nghiệm (nhiều demo), M1 thiên về lý thuyết + diagram + review, M4 thiên về AI + tích hợp. Để M1 không nhẹ hơn, M1 còn **hỗ trợ quay/dựng video** và **chuẩn bị Q&A** (T-505).

## 5. Evidence – quy ước chung

| Loại task | Evidence bắt buộc lưu vào `evidence/` |
| --- | --- |
| Research | Link docs, ghi chú, screenshot trang nguồn, commit |
| Experiment | Source code, screenshot, execution log/report, commit |
| Demo | Script, video, screenshot |
| Meeting | Meeting note, decision log, task cập nhật |
| AI | Prompt gốc, output gốc AI, bản đã sửa, diff, kết quả chạy |
| Review | PR comment + checklist đã tick |

## 6. Dependency chính

`T-105 → T-106/T-107/T-109 → T-110 → Phase 2 (M2 ∥ M3 ∥ T-218)` · `T-203/T-213 → T-303` · `T-207 + T-217 → T-401 → T-403/T-404 → T-405` · `T-504 → T-505 → T-507 → Phase 6`. Điểm đồng bộ bắt buộc: **T-109** (case study) và **T-205 ↔ T-215** (cùng scenario/test data).

## 7. Timeline

| Tuần | Mục tiêu | Mốc |
| --- | --- | --- |
| W1 | T-101..T-105, T-108 | Criteria xong |
| W2 | T-106, T-107, T-109, T-110, T-111 | **Chốt tool + case study** |
| W3 | T-201..T-203, T-211..T-213, T-218 | Demo 1 + 2 chạy |
| W4 | T-204, T-205, T-214, T-215, T-301, T-302 | Complex PASS/FAIL |
| W5 | T-206, T-207, T-216, T-217, T-303 | Video tool xong |
| W6 | T-304..T-307, T-401, T-402 | Comparison + AI xong |
| W7 | T-403..T-409, T-501..T-504 | Draft report + slide, review chéo |
| W8 | T-505..T-507, T-601..T-605 | **Nộp v1.0** |

Buffer: nếu giảng viên ấn định thời hạn ngắn hơn, nén W1–W2 thành 1 tuần và chạy song song T-201/T-211 ngay khi chốt tool.

## 8. RACI

| Task | M1 | M2 | M3 | M4 |
| --- | --- | --- | --- | --- |
| Theory, terminology, diagrams | A/R | I | C | C |
| Tool evaluation criteria | A/R | C | C | C |
| Chọn tool + case study | R | C | C | A/R |
| Tool A research & demo | C | A/R | I | C |
| Tool B research & demo | C | I | A/R | C |
| Case study app | I | C | C | A/R |
| AI experiments | I | C | C | A/R |
| Tool comparison | C | C | C | A/R |
| Exercises | C | C | C | A/R |
| Report tích hợp | C | C | C | A/R |
| Slide từng phần | R (P1) | R (P2) | R (P3) | R (P4) + A |
| Review chéo | R (A) | R (B) | R (Theory) | C |
| Video upload | I | R | R | A/R |
| Final checklist & tag | C | C | C | A/R |

Ghi chú: để tránh Accountable trùng người thực hiện ở phần Integration, M2 là reviewer (T-409) và Accountable cho quyết định merge cuối là **cả nhóm qua PR approval**.

## 9. Review process

Quy tắc: tác giả **không được tự approve**; PR cần ≥1 approval của reviewer chỉ định. Reviewer phải **chạy lại** source (với tool) hoặc **đọc đối chiếu nguồn** (với theory).

| Reviewer → Đối tượng | Checklist chính |
| --- | --- |
| M1 → Tool A (R-A) | \[ \] Cài lại được theo `installation.md` \[ \] Script chạy lại ra cùng kết quả \[ \] 3 demo đủ 8 mục (Objective→Conclusion) \[ \] R&P, Data-driven, Checkpoint có bằng chứng \[ \] Có ca FAIL hợp lý \[ \] Limitations trung thực \[ \] Khớp `theory-tool-mapping.md` |
| M2 → Tool B (R-B) | Như R-A, thêm: \[ \] Dùng đúng case study + test data chung |
| M3 → Theory (R-T) | \[ \] Đủ 11 mục GV yêu cầu \[ \] Nguồn trích dẫn rõ \[ \] Thuật ngữ nhất quán \[ \] Không mâu thuẫn kết quả thực nghiệm \[ \] Diagram đúng |
| M2 → Integration (R-I) | \[ \] Số liệu comparison khớp log gốc \[ \] Report/slide/video khớp nhau \[ \] Bài tập chạy được bằng đáp án \[ \] Đủ checklist nộp bài \[ \] Link video mở được |

Chặn merge nếu còn mục chưa tick. M4 (người tích hợp) review chéo bổ sung phần AI bởi M3 (T-306 phải có ít nhất 1 review từ M3).

## 10. Git workflow

- **Branch:** `main` (protected, chỉ nhận qua PR), `develop`, nhánh tính năng `feature/m2-tool-a-demo2`, `docs/m1-theory`, `fix/m3-datadriven`.
- **Commit** (Conventional Commits): `feat(tool-a): add data-driven test with xlsx`, `docs(theory): add checkpoint section`, `test(tool-b): add complex workflow`, `chore(evidence): add screenshots demo1`. Commit nhỏ, mỗi commit gắn ID task: `[T-204]`.
- **PR:** template gồm Task ID, mô tả, evidence đính kèm, checklist review. Một PR = một task hoặc nhóm task nhỏ.
- **Review:** reviewer theo mục 9, comment trực tiếp; tác giả sửa rồi re-request.
- **Merge:** squash merge vào `develop`; cuối tuần W8 merge `develop` → `main`, tag `v0.x` mỗi mốc, `v1.0` khi nộp.
- Không commit file >50MB: video đưa lên YouTube và ghi link vào `video-links.md`.

## 11. Folder structure

```
seminar-desktop-automation/
├── README.md
├── docs/
│   ├── theory.md  terminology.md  tool-evaluation-criteria.md
│   ├── theory-tool-mapping.md  case-study.md  comparison.md
│   ├── architecture.drawio  workflow.drawio
│   └── report/ (report.docx, report-final.pdf)
├── case-study-app/            # app WinForms/WPF + bug list
├── tool-a/
│   ├── research.md  installation.md  demo-scenarios.md  limitations.md
│   ├── test-project/  test-data/  results/  screenshots/
├── tool-b/                    # cấu trúc giống tool-a
├── ai/
│   ├── prompts/  output/  failure-analysis.md  reusable-workflow.md
├── exercises/ (exercise-01..03.md, solutions/, rubric.md)
├── slides/
├── videos/video-links.md
├── reviews/
├── evidence/ (meeting-notes/, weekly/, INDEX.md, work-allocation.md)
└── FINAL-CHECKLIST.md
```

## 12. Definition of Done

**M1 (Theory) DONE khi:** \[ \] `theory.md` đủ 11 mục \[ \] `terminology.md` ≥30 thuật ngữ \[ \] 2 diagram có file nguồn + PNG \[ \] Tiêu chí đánh giá có trọng số \[ \] Mapping lý thuyết→tool \[ \] Có nguồn tham khảo \[ \] Đã cập nhật theo thực nghiệm \[ \] M3 review \[ \] Slide phần 1.

**M2 (Tool A) / M3 (Tool B) DONE khi:** \[ \] Cài thành công + screenshot \[ \] Basic automation \[ \] Record & Playback \[ \] Data-driven (≥5 dòng) \[ \] Checkpoint \[ \] Complex workflow \[ \] Có PASS và FAIL \[ \] Source code chạy lại được \[ \] Test data \[ \] Video \[ \] Limitations \[ \] Documentation theo 8 mục \[ \] Thành viên khác đã review. (Tool B thêm: \[ \] cùng case study/test data với Tool A.)

**M4 DONE khi:** \[ \] ≥2 AI demo có prompt + output + kết quả chạy \[ \] Workflow AI tái sử dụng \[ \] `comparison.md` đủ 16 tiêu chí, dựa trên số liệu thực nghiệm \[ \] Case study chung \[ \] ≥3 bài tập + đáp án + rubric \[ \] Report/slide/video nhất quán \[ \] Final checklist \[ \] M2 review.

## 13. Risk management

| Risk | Impact | Mitigation | Owner |
| --- | --- | --- | --- |
| Tool không cài được | Trễ Phase 2 | Thử trên VM/máy khác; dự phòng 1 tool thay thế đã khảo sát; quyết định trong 3 ngày | M2/M3 |
| Tool không hỗ trợ app (UI custom, không có UIA) | Không locate được control | Dùng app WinForms/WPF tự viết; fallback image/coordinate-based | M4 |
| Record không hoạt động | Thiếu demo R&P | Dùng recorder khác (vd Inspect.exe + script mẫu), ghi rõ làm hạn chế | M2/M3 |
| Data-driven khó triển khai | Thiếu yêu cầu bắt buộc | Bắt đầu với CSV, sau đó Excel; thử sớm ở W3–W4 | M2/M3 |
| Checkpoint không ổn định (flaky) | Kết quả sai | Explicit wait, retry, assertion theo property thay vì pixel | M2/M3 |
| Complex demo thất bại | Mất điểm demo | Quay video trước; chuẩn bị bản fallback đơn giản hoá | M2/M3 |
| AI sinh code sai | Demo sai | Luôn chạy và sửa, ghi lại diff; đây cũng là nội dung đánh giá | M4 |
| Không đủ evidence | Mất điểm quá trình | Evidence là DoD của mỗi task; weekly check | M4 |
| Video lỗi/quá nặng | Không nộp được | Quay thử sớm, giữ bản gốc, upload unlisted YouTube sớm W7 | M4 |
| Không đủ thời gian | Trễ nộp | Buffer W8; cắt Low priority trước; họp 15 phút 2 lần/tuần | M4 |

## Weekly Progress Template

```
### Tuần __ – Member __ – Ngày __/__
- Done: (ID – kết quả)
- Doing: (ID – % hoàn thành)
- Blocked: (vấn đề – cần ai hỗ trợ)
- Evidence: (link commit/PR/screenshot/video)
- Next task: (ID – deadline)
```

Lưu tại `evidence/weekly/week-XX-memberY.md`, cập nhật trước 20:00 Chủ nhật.

## 14. Final Deliverable Checklist

\[ \] Report (`report-final.pdf`/docx) · \[ \] Slides · \[ \] Tool A · \[ \] Tool B · \[ \] Source code · \[ \] Test data · \[ \] Demo videos (A, B, AI) + link YouTube · \[ \] AI demo · \[ \] Tool comparison · \[ \] Exercises + solutions · \[ \] References · \[ \] Work allocation · \[ \] Evidence (meeting notes, weekly, PR/commit links, reviews)