import os
import re
import subprocess
import markdown

base_dir = os.path.abspath('.')

def read_doc(filename):
    p = os.path.join(base_dir, 'docs', filename)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

def fix_images(md_text):
    def repl(match):
        alt = match.group(1)
        src = match.group(2).strip().strip('<>').replace('\\', '/')
        candidates = [
            os.path.normpath(os.path.join(base_dir, 'docs', src)),
            os.path.normpath(os.path.join(base_dir, src)),
            os.path.normpath(os.path.join(base_dir, 'docs', src.replace('../', ''))),
            os.path.normpath(os.path.join(base_dir, src.replace('../', '')))
        ]
        for c in candidates:
            if os.path.exists(c):
                uri = 'file:///' + c.replace('\\', '/')
                return f'![{alt}]({uri})'
        return f'![{alt}]({src})'
    return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', repl, md_text)

# Load individual chapters
p1 = read_doc('01-introduction.md')
p2 = read_doc('02-theory.md')
p3 = read_doc('03-toolsurvey.md')
p4 = read_doc('04-katalon-studio.md')
p5 = read_doc('05-winappdriver.md')
p6 = read_doc('06-comparison.md')
p7 = read_doc('07-ai-desktop-automation.md')
p8 = read_doc('08-exercises.md')

header_md = """# BÁO CÁO TOÀN VĂN CHUYÊN ĐỀ SEMINAR
# AUTOMATION TESTING FOR DESKTOP APPLICATIONS
## Tự Động Hóa Kiểm Thử Cho Ứng Dụng Desktop (Windows)

> **Môn học:** Software Testing (Kiểm thử phần mềm)  
> **Khoa:** Công nghệ Thông tin – Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM  
> **Nhóm thực hiện:** Nhóm 02 (ZipTool)  
> **Học kỳ:** HK1 – Năm học 2026-2027  
> **Thời gian nộp bài:** 30/10/2026 (Hạn chót giảng viên: 31/10/2026)

---

## 👥 THÀNH VIÊN VÀ ĐÁNH GIÁ ĐÓNG GÓP THỰC TẾ (LẦN 2)

| STT | Họ và Tên | MSSV | Vai trò chính Lần 2 | Đóng góp thực tế | % Chốt | Trạng thái |
|:---:|---|:---:|---|---|:---:|:---:|
| 1 | **Phan Trung Tín** | 23120372 | **Trưởng nhóm (Team Lead)**<br>Phát triển 3 bản `MiniSum.exe`, viết lý thuyết POM/Flaky/Wait/Oracle, thiết kế toàn bộ Slide (v1+v2), Handout bài tập, tích hợp báo cáo & đóng gói | 42.0h (22 tasks) | **35.0%** | Hoàn thành xuất sắc |
| 2 | **Nguyễn Lê Quang Kan** | 23120279 | **Chuyên trách Katalon Studio**<br>Thực nghiệm 3 demo Katalon, viết Custom Keyword `LoginKeyword.groovy`, Data-Driven BVA, 16 ảnh thực nghiệm, video YouTube | 30.0h (18 tasks) | **25.0%** | Hoàn thành xuất sắc |
| 3 | **Bùi Quang Tùng** | 20120397 | **Chuyên trách WinAppDriver**<br>Thực nghiệm WinAppDriver + C# NUnit, cài đặt Page Object Model (POM), DDT 12 ca BVA, chụp ảnh kiểm thử | 24.0h (21 tasks) | **20.0%** | Hoàn thành tốt |
| 4 | **Trần Vũ Quang** | 23120346 | **Chuyên trách AI & Comparison**<br>Prompt Engineering, sinh 19 ca BVA, test suite C# `ai-winappdriver`, số liệu đo đạc so sánh định lượng | 24.0h (17 tasks) | **20.0%** | Hoàn thành tốt |
| **Tổng** | | | | **120.0h (78 tasks)** | **100.0%** | |

---

## 📋 MỤC LỤC TỔNG QUAN

1. [Phần 1: Giới Thiệu & Bối Cảnh (Introduction)](#phan-1)
2. [Phần 2: Cơ Sở Lý Thuyết Kiểm Thử Tự Động Desktop (Theory)](#phan-2)
3. [Phần 3: Khảo Sát Thị Trường & Bộ Tiêu Chí Đánh Giá (Tool Survey)](#phan-3)
4. [Phần 4: Nghiên Cứu Công Cụ Đại Diện A – Katalon Studio](#phan-4)
5. [Phần 5: Nghiên Cứu Công Cụ Đại Diện B – Microsoft WinAppDriver](#phan-5)
6. [Phần 6: So Sánh Đối Chiếu Toàn Diện (Comparison)](#phan-6)
7. [Phần 7: Ứng Dụng Trí Tuệ Nhân Tạo (AI) Trong Desktop Automation](#phan-7)
8. [Phần 8: Hệ Thống Bài Tập Thực Hành 30 Phút Tại Lớp (Exercise)](#phan-8)
9. [Phần 9: Minh Chứng Thực Nghiệm, Kê Khai AI & Kết Luận](#phan-9)

---
"""

p9 = """
# Phần 9: Minh Chứng Thực Nghiệm, Kê Khai AI & Kết Luận <a id="phan-9"></a>

## 9.1 Minh chứng Video Demo YouTube (Chế độ Unlisted)
- **Demo 1 – Katalon Studio (Nguyễn Lê Quang Kan):**
  - **Liên kết YouTube:** [https://www.youtube.com/watch?v=w7c_X5f5SFo](https://www.youtube.com/watch?v=w7c_X5f5SFo)
  - **Chất lượng:** 1080p Full HD, thuyết minh tiếng Việt rõ ràng.
  - **Nội dung:** Cài đặt WinAppDriver, Record & Playback đăng nhập hợp lệ, tạo Checkpoint xác minh nhãn thông báo, Data-Driven Testing với 12 test case BVA đọc từ Excel, thực thi suite và xuất báo cáo HTML.

## 9.2 Nhật ký đóng góp trên Git Commit Log
- Hệ thống kho lưu trữ GitHub: `https://github.com/tinphan247/KTPM-2026-Seminar.git`
- Toàn bộ quá trình làm việc, giải quyết lỗi, phát triển ứng dụng mẫu và tài liệu đều được commit liên tục, minh bạch:
  - **Phan Trung Tín:** 27 commits chính thức trên Git log.
  - **Trần Vũ Quang:** 17 commits chính thức trên Git log (PR #3).
  - **Nguyễn Lê Quang Kan:** 14 commits chính thức trên Git log (PR #1).
  - **Bùi Quang Tùng:** 4 commits chính thức trên Git log.
  - Toàn bộ lịch sử commit chi tiết xem tại file `git-commit-log.md`.

## 9.3 Kê khai sử dụng Trí tuệ Nhân tạo (AI Usage Declaration)
Theo quy định môn học, nhóm thực hiện kê khai minh bạch:
- Các mô hình AI sử dụng: ChatGPT-4, Gemini Advanced, Claude 3.5, GitHub Copilot.
- Mục đích: Hỗ trợ tìm kiếm tài liệu tham khảo, thiết kế mẫu Prompt kỹ thuật Few-shot, gợi ý cấu trúc khung mã nguồn boilerplate C# POM và bảng phân tích giá trị biên BVA.
- Kiểm chứng: 100% dữ liệu, test script và ứng dụng thực thi đều được lập trình viên build, chạy thử trên Windows 11 và kiểm tra kỹ lưỡng trước khi đưa vào báo cáo. Chi tiết xem tại `ai-usage-declaration.md`.

## 9.4 Kết luận và Đánh giá chung
Seminar đã hoàn thành xuất sắc các mục tiêu đề ra:
1. Xây dựng bộ khung lý thuyết vững chắc về kiểm thử tự động Desktop (UI Automation, POM, Wait, Flaky Test, Test Oracle, Recovery Testing).
2. Xây dựng ứng dụng mẫu thực tế `MiniSum.exe` (v1, v2, v3) theo phong cách hiện đại Fluent Light để làm AUT cho toàn bộ demo.
3. Thực nghiệm sâu sắc hai đại diện tiêu biểu: **Katalon Studio** (Low-Code GUI) và **WinAppDriver** (Code-First), với các số liệu so sánh định lượng rõ ràng.
4. Triển khai thành công thực nghiệm AI Test Automation giúp rút ngắn 77.7% thời gian thiết kế kịch bản kiểm thử.
5. Thiết kế bài tập thực hành 30 phút tại lớp dễ tiếp cận, trực quan và đánh giá chính xác kỹ năng của sinh viên.
"""

# Combine
full_master_md = f"""{header_md}

# Phần 1: Giới Thiệu & Bối Cảnh (Introduction) <a id="phan-1"></a>

{p1}

# Phần 2: Cơ Sở Lý Thuyết Kiểm Thử Tự Động Desktop (Theory) <a id="phan-2"></a>

{p2}

# Phần 3: Khảo Sát Thị Trường & Bộ Tiêu Chí Đánh Giá (Tool Survey) <a id="phan-3"></a>

{p3}

# Phần 4: Nghiên Cứu Công Cụ Đại Diện A – Katalon Studio <a id="phan-4"></a>

{p4}

# Phần 5: Nghiên Cứu Công Cụ Đại Diện B – Microsoft WinAppDriver <a id="phan-5"></a>

{p5}

# Phần 6: So Sánh Đối Chiếu Toàn Diện (Comparison) <a id="phan-6"></a>

{p6}

# Phần 7: Ứng Dụng Trí Tuệ Nhân Tạo (AI) Trong Desktop Automation <a id="phan-7"></a>

{p7}

# Phần 8: Hệ Thống Bài Tập Thực Hành Đề Xuất (Exercise) <a id="phan-8"></a>

{p8}

{p9}
"""

# Fix image links
full_master_md_fixed = fix_images(full_master_md)

# Save markdown files
with open('docs/report_v2.md', 'w', encoding='utf-8') as f:
    f.write(full_master_md)

with open('docs/report.md', 'w', encoding='utf-8') as f:
    f.write(full_master_md)

print("Saved docs/report_v2.md and docs/report.md successfully!")

# Convert Markdown to HTML
html_body = markdown.markdown(
    full_master_md_fixed,
    extensions=['tables', 'fenced_code', 'toc']
)

# HTML Document with elegant print-ready CSS
html_full = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Báo Cáo Seminar – Automation Testing for Desktop Applications</title>
<style>
@page {{
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-center {{
        content: counter(page);
    }}
}}
body {{
    font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #1e293b;
    background: #ffffff;
    margin: 0;
    padding: 0;
}}
.cover-page {{
    text-align: center;
    padding: 100px 20px 60px 20px;
    page-break-after: always;
}}
.cover-univ {{
    font-size: 13pt;
    font-weight: bold;
    color: #334155;
    margin-bottom: 5px;
    text-transform: uppercase;
}}
.cover-subuniv {{
    font-size: 11pt;
    color: #64748b;
    margin-bottom: 40px;
}}
.cover-title {{
    font-size: 24pt;
    font-weight: 800;
    color: #1d4ed8;
    margin-bottom: 15px;
    line-height: 1.3;
}}
.cover-subtitle {{
    font-size: 15pt;
    font-weight: 600;
    color: #0f172a;
    margin-bottom: 50px;
}}
.cover-meta {{
    margin-top: 60px;
    font-size: 11.5pt;
    color: #334155;
    line-height: 1.8;
}}
.cover-table {{
    margin: 0 auto;
    border-collapse: collapse;
    width: 85%;
    text-align: left;
    margin-top: 20px;
}}
.cover-table td {{
    padding: 6px 12px;
}}
h1 {{
    font-size: 18pt;
    color: #1d4ed8;
    border-bottom: 2px solid #2563eb;
    padding-bottom: 6px;
    margin-top: 35px;
    margin-bottom: 16px;
    page-break-before: always;
}}
.cover-page h1 {{
    page-break-before: avoid;
}}
h2 {{
    font-size: 14pt;
    color: #0f172a;
    margin-top: 24px;
    margin-bottom: 12px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
}}
h3 {{
    font-size: 12pt;
    color: #1e293b;
    margin-top: 18px;
    margin-bottom: 8px;
}}
p, li {{
    text-align: justify;
    margin-bottom: 8px;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}}
th, td {{
    border: 1px solid #cbd5e1;
    padding: 7px 10px;
    text-align: left;
    vertical-align: top;
}}
th {{
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 600;
}}
tr:nth-child(even) {{
    background-color: #f8fafc;
}}
pre, code {{
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 9pt;
}}
pre {{
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 12px;
    overflow-x: auto;
    page-break-inside: avoid;
    line-height: 1.45;
}}
code {{
    background-color: #f1f5f9;
    padding: 2px 5px;
    border-radius: 3px;
    color: #0f172a;
}}
pre code {{
    background-color: transparent;
    padding: 0;
}}
img {{
    max-width: 95%;
    height: auto;
    display: block;
    margin: 14px auto;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    page-break-inside: avoid;
}}
blockquote {{
    border-left: 4px solid #2563eb;
    margin: 14px 0;
    padding: 8px 16px;
    background-color: #eff6ff;
    color: #1e3a8a;
    font-size: 10.5pt;
    border-radius: 0 4px 4px 0;
}}
hr {{
    border: 0;
    border-top: 1px solid #e2e8f0;
    margin: 25px 0;
}}
</style>
</head>
<body>

<div class="cover-page">
    <div class="cover-univ">Đại Học Quốc Gia TP. Hồ Chí Minh</div>
    <div class="cover-univ">Trường Đại Học Khoa Học Tự Nhiên – Khoa Công Nghệ Thông Tin</div>
    <div class="cover-subuniv">Bộ môn Kỹ thuật Phần mềm</div>
    
    <div style="margin: 60px 0 40px 0;">
        <div class="cover-title">BÁO CÁO CHUYÊN ĐỀ SEMINAR</div>
        <div class="cover-subtitle">AUTOMATION TESTING FOR DESKTOP APPLICATIONS<br><span style="font-size: 13pt; color: #475569; font-weight: normal;">Tự động hóa kiểm thử cho ứng dụng Desktop (Windows)</span></div>
    </div>
    
    <div class="cover-meta">
        <p><strong>Môn học:</strong> Kiểm thử Phần mềm (Software Testing)</p>
        <p><strong>Nhóm thực hiện:</strong> Nhóm 02 (ZipTool) — Lớp: 23_1</p>
        <p><strong>Giảng viên phụ trách:</strong> ThS. Huỳnh Phước Hải</p>
        
        <table class="cover-table">
            <thead>
                <tr>
                    <th>STT</th>
                    <th>Họ và Tên</th>
                    <th>MSSV</th>
                    <th>Vai trò chính (Lần 2)</th>
                    <th>% Chốt</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td><strong>Phan Trung Tín</strong> (Nhóm trưởng)</td>
                    <td>23120372</td>
                    <td>Lead, AUT MiniSum, Theory, Slide v1+v2, Handout, Báo cáo</td>
                    <td><strong>35.0%</strong></td>
                </tr>
                <tr>
                    <td>2</td>
                    <td><strong>Nguyễn Lê Quang Kan</strong></td>
                    <td>23120279</td>
                    <td>Katalon Studio trọn gói, Keyword, DDT BVA, Video YouTube</td>
                    <td><strong>25.0%</strong></td>
                </tr>
                <tr>
                    <td>3</td>
                    <td><strong>Bùi Quang Tùng</strong></td>
                    <td>20120397</td>
                    <td>WinAppDriver + C# NUnit, Page Object Model, DDT NPOI</td>
                    <td><strong>20.0%</strong></td>
                </tr>
                <tr>
                    <td>4</td>
                    <td><strong>Trần Vũ Quang</strong></td>
                    <td>23120346</td>
                    <td>AI Test Automation, Test Suite C# AI-WAD, Comparison</td>
                    <td><strong>20.0%</strong></td>
                </tr>
            </tbody>
        </table>
        
        <p style="margin-top: 50px; font-style: italic;">Thành phố Hồ Chí Minh, ngày 30 tháng 10 năm 2026</p>
    </div>
</div>

{html_body}

</body>
</html>
"""

html_path = os.path.abspath('report_master.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_full)

print(f"Generated HTML report at {html_path}!")

edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

target_pdfs = [
    os.path.abspath('seminar-final.pdf'),
    os.path.abspath('docs/report_v2.pdf')
]

for target_pdf in target_pdfs:
    cmd = [
        edge_exe,
        '--headless',
        '--disable-gpu',
        '--run-all-compositor-stages-before-draw',
        f'--print-to-pdf={target_pdf}',
        f'file:///{html_path}'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(target_pdf):
        print(f"Successfully exported {target_pdf}! Size: {os.path.getsize(target_pdf):,} bytes")
    else:
        print(f"Failed to export {target_pdf}: {res.stderr}")
