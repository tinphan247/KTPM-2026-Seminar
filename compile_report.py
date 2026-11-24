import os
import re
import subprocess
import base64
import markdown
import pypdf

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

def clean_chapter_text(md_text):
    lines = md_text.split('\n')
    start = 0
    in_local_toc = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('## Mục lục'):
            in_local_toc = True
            continue
        if in_local_toc:
            if stripped == '---':
                start = i + 1
                in_local_toc = False
            continue
        if stripped.startswith('#') or stripped.startswith('>') or stripped.startswith('- **') or stripped == '---' or not stripped:
            start = i + 1
            continue
        else:
            start = i
            break
    return '\n'.join(lines[start:])

# Load individual chapters
p1 = clean_chapter_text(read_doc('01-introduction.md'))
p2 = clean_chapter_text(read_doc('02-theory.md'))
p3 = clean_chapter_text(read_doc('03-toolsurvey.md'))
p4 = clean_chapter_text(read_doc('04-katalon-studio.md'))
p5 = clean_chapter_text(read_doc('05-winappdriver.md'))
p6 = clean_chapter_text(read_doc('06-comparison.md'))
p7 = clean_chapter_text(read_doc('07-ai-desktop-automation.md'))
p8 = clean_chapter_text(read_doc('08-exercises.md'))

# Load HCMUS Logo base64
logo_path = os.path.join(base_dir, 'docs', 'images', 'hcmus_logo.png')
logo_b64 = ''
if os.path.exists(logo_path):
    with open(logo_path, 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode('utf-8')

header_md = """<div class="report-intro-box">
<h1 style="page-break-before: avoid; margin-top: 0; text-align: center; font-size: 18pt;">BÁO CÁO TOÀN VĂN CHUYÊN ĐỀ SEMINAR<br><span style="font-size: 14pt; color: #000000;">AUTOMATION TESTING FOR DESKTOP APPLICATIONS</span></h1>
<p style="text-align: center; font-style: italic; margin-top: 4px; margin-bottom: 18pt;">Tự Động Hóa Kiểm Thử Cho Ứng Dụng Desktop (Windows)</p>

> **Môn học:** Software Testing (Kiểm thử phần mềm)  
> **Bộ môn:** Kiểm thử phần mềm  
> **Khoa:** Công nghệ Thông tin – Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM  
> **Nhóm thực hiện:** Nhóm 02  
> **Học kỳ:** HK1 – Năm học 2026-2027  
> **Thời gian nộp bài:** 30/10/2026 (Hạn chót giảng viên: 31/10/2026)

---

## THÀNH VIÊN VÀ ĐÁNH GIÁ ĐÓNG GÓP THỰC TẾ (LẦN 2)

| STT | Họ và Tên | MSSV | Vai trò chính Lần 2 | Đóng góp thực tế | % Chốt | Trạng thái |
|:---:|---|:---:|---|---|:---:|:---:|
| 1 | **Phan Trung Tín** | 23120372 | **Trưởng nhóm (Team Lead)**<br>Phát triển 3 bản `MiniSum.exe`, viết lý thuyết POM/Flaky/Wait/Oracle, thiết kế toàn bộ Slide (v1+v2), Handout bài tập, tích hợp báo cáo & đóng gói | 42.0h (22 tasks) | **25.0%** | Hoàn thành xuất sắc |
| 2 | **Nguyễn Lê Quang Kan** | 23120279 | **Chuyên trách Katalon Studio**<br>Thực nghiệm 3 demo Katalon, viết Custom Keyword `LoginKeyword.groovy`, Data-Driven BVA, 16 ảnh thực nghiệm, video YouTube | 30.0h (18 tasks) | **25.0%** | Hoàn thành xuất sắc |
| 3 | **Bùi Quang Tùng** | 20120397 | **Chuyên trách WinAppDriver**<br>Thực nghiệm WinAppDriver + C# NUnit, cài đặt Page Object Model (POM), DDT 12 ca BVA, chụp ảnh kiểm thử, video YouTube | 24.0h (21 tasks) | **25.0%** | Hoàn thành tốt |
| 4 | **Trần Vũ Quang** | 23120346 | **Chuyên trách AI & Comparison**<br>Prompt Engineering, sinh 19 ca BVA, test suite C# `ai-winappdriver`, số liệu đo đạc so sánh định lượng, video YouTube | 24.0h (17 tasks) | **25.0%** | Hoàn thành tốt |
| **Tổng** | | | | **120.0h (78 tasks)** | **100.0%** | |

<p class="table-caption"><b>Bảng 0.1:</b> <i>Phân công vai trò và tỷ lệ đóng góp thực tế của các thành viên Nhóm 02</i></p>

</div>
"""

p9 = """
# Phần 9: Minh Chứng Thực Nghiệm, Kê Khai AI & Kết Luận <a id="phan-9"></a>

## 9.1 Minh chứng Video Demo YouTube (Chế độ Unlisted)
- **Demo 1 – Katalon Studio (Nguyễn Lê Quang Kan):**
  - **Liên kết YouTube:** [https://www.youtube.com/watch?v=w7c_X5f5SFo](https://www.youtube.com/watch?v=w7c_X5f5SFo)
  - **Chất lượng:** 1080p Full HD, thuyết minh tiếng Việt rõ ràng.
  - **Nội dung:** Cài đặt WinAppDriver, Record & Playback đăng nhập hợp lệ, tạo Checkpoint xác minh nhãn thông báo, Data-Driven Testing với 12 test case BVA đọc từ Excel, thực thi suite và xuất báo cáo HTML.
- **Demo 2 – WinAppDriver & C# NUnit (Bùi Quang Tùng):**
  - **Liên kết YouTube:** [https://youtu.be/OujklJs2DhA](https://youtu.be/OujklJs2DhA)
  - **Chất lượng:** 1080p Full HD, thuyết minh trực quan trên môi trường Visual Studio.
  - **Nội dung:** Khởi tạo WinAppDriver & WindowsDriver mở MiniSum.exe, kiểm thử Đăng nhập theo mô hình Page Object Model (POM), cơ chế chụp màn hình tự động và Data-Driven Testing với NUnit + NPOI.
- **Demo 3 – AI in Desktop Test Automation (Trần Vũ Quang):**
  - **Liên kết YouTube:** [https://www.youtube.com/watch?v=144GVavGjWA](https://www.youtube.com/watch?v=144GVavGjWA)
  - **Chất lượng:** 1080p Full HD, thuyết minh quy trình Prompt Engineering và thực thi script.
  - **Nội dung:** Thử nghiệm kỹ thuật Prompting 2 pha với ChatGPT-4, Gemini Advanced và Claude 3.5; sinh mã nguồn C# WinAppDriver Page Object Model hoàn chỉnh và thực thi suite kiểm thử tự động 19 ca BVA trên ứng dụng MiniSum PASS 100%.

## 9.2 Nhật ký đóng góp trên Git Commit Log
- Hệ thống kho lưu trữ GitHub: `https://github.com/tinphan247/KTPM-2026-Seminar.git`
- Toàn bộ quá trình làm việc, giải quyết lỗi, phát triển ứng dụng mẫu và tài liệu đều được commit liên tục, minh bạch. Chi tiết xem tại `git-commit-log.md`.

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

# Combine Master Markdown
full_master_md = f"""{header_md}

# 1. Giới Thiệu & Bối Cảnh (Introduction) <a id="phan-1"></a>

{p1}

# 2. Cơ Sở Lý Thuyết Kiểm Thử Tự Động Desktop (Theory) <a id="phan-2"></a>

{p2}

# 3. Khảo Sát Thị Trường & Bộ Tiêu Chí Đánh Giá (Tool Survey) <a id="phan-3"></a>

{p3}

# 4. Nghiên Cứu Công Cụ Đại Diện A – Katalon Studio <a id="phan-4"></a>

{p4}

# 5. Nghiên Cứu Công Cụ Đại Diện B – Microsoft WinAppDriver <a id="phan-5"></a>

{p5}

# 6. So Sánh Đối Chiếu Toàn Diện (Comparison) <a id="phan-6"></a>

{p6}

# 7. Ứng Dụng Trí Tuệ Nhân Tạo (AI) Trong Desktop Automation <a id="phan-7"></a>

{p7}

# 8. Hệ Thống Bài Tập Thực Hành Cá Nhân 30 Phút Tại Lớp (Exercise) <a id="phan-8"></a>

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

# Build Complete HTML matching HCMUS LaTeX Template with MONOCHROME (B&W) STYLING
html_full = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Báo cáo Seminar: Automation Testing for Desktop Applications</title>
<style>
@page {{
    size: A4;
    margin: 30mm 20mm 25mm 20mm;
    @top-left {{
        content: "Báo cáo Seminar";
        font-family: 'Times New Roman', Times, serif;
        font-size: 10pt;
        color: #000000;
        border-bottom: 0.5pt solid #000000;
        vertical-align: bottom;
        padding-bottom: 2mm;
    }}
    @top-right {{
        content: "Trường Đại học Khoa học Tự nhiên - ĐHQG HCM\\A Môn: Kiểm thử phần mềm";
        white-space: pre-line;
        font-family: 'Times New Roman', Times, serif;
        font-size: 10pt;
        color: #000000;
        text-align: right;
        border-bottom: 0.5pt solid #000000;
        vertical-align: bottom;
        padding-bottom: 2mm;
    }}
    @bottom-left {{
        content: "Nhóm 02 · Automation Testing for Desktop Applications";
        font-family: 'Times New Roman', Times, serif;
        font-size: 10pt;
        color: #000000;
        vertical-align: top;
        padding-top: 2.5mm;
    }}
    @bottom-right {{
        content: "Trang " counter(page);
        font-family: 'Times New Roman', Times, serif;
        font-size: 10pt;
        color: #000000;
        vertical-align: top;
        padding-top: 2.5mm;
    }}
}}

@page :first {{
    margin: 22mm 20mm 20mm 20mm;
    @top-left {{ content: none; }}
    @top-right {{ content: none; }}
    @bottom-left {{ content: none; }}
    @bottom-right {{ content: none; }}
}}

body {{
    font-family: 'Times New Roman', Times, serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #000000;
    margin: 0;
    padding: 0;
}}

/* ========================================================
   COVER PAGE (TRANG BÌA THEO TEMPLATE KHTN)
   ======================================================== */
.cover-page {{
    page-break-after: always;
    min-height: 250mm;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;
}}

.institution-header {{
    text-align: center;
    line-height: 1.45;
}}
.univ-line1 {{
    font-size: 12.5pt;
    font-weight: normal;
    letter-spacing: 0.5px;
    margin: 0;
    color: #000000;
}}
.univ-line2 {{
    font-size: 13pt;
    font-weight: bold;
    letter-spacing: 0.5px;
    margin: 4px 0 0 0;
    color: #000000;
}}
.univ-line3 {{
    font-size: 11.5pt;
    font-weight: bold;
    letter-spacing: 0.5px;
    margin: 10px 0 0 0;
    color: #000000;
}}
.univ-line4 {{
    font-size: 10.5pt;
    font-weight: normal;
    letter-spacing: 0.5px;
    margin: 4px 0 0 0;
    color: #000000;
}}

.cover-rule {{
    border: none;
    border-top: 2.5px solid #000000;
    width: 100%;
    margin: 35px 0 25px 0;
}}

.cover-title-box {{
    margin: 20px 0 25px 0;
}}
.cover-title-main {{
    font-size: 24pt;
    font-weight: bold;
    margin-bottom: 12px;
    color: #000000;
}}
.cover-title-sub {{
    font-size: 16pt;
    font-weight: bold;
    line-height: 1.35;
    color: #000000;
}}

.cover-course {{
    font-size: 13pt;
    font-weight: bold;
    margin: 15px 0 35px 0;
    color: #000000;
}}

.cover-info-container {{
    display: flex;
    justify-content: space-between;
    width: 88%;
    margin: 0 auto 35px auto;
    font-size: 11.5pt;
    line-height: 1.8;
    color: #000000;
}}
.info-col-left {{
    text-align: left;
}}
.info-col-right {{
    text-align: left;
    padding-left: 20px;
}}
.info-label {{
    font-style: italic;
    font-weight: bold;
    margin-bottom: 6px;
}}

.cover-date {{
    font-size: 11pt;
    margin: 15px 0 25px 0;
    color: #000000;
}}

.cover-logo-box {{
    margin-top: 10px;
    margin-bottom: 5px;
}}
.hcmus-logo-img {{
    width: 120px;
    height: auto;
    display: inline-block;
    background: transparent !important;
}}

/* ========================================================
   FRONT MATTER: MỤC LỤC, DANH SÁCH BẢNG & HÌNH
   ======================================================== */
.latex-frontmatter {{
    page-break-after: always;
}}
.latex-toc-title {{
    font-size: 18pt;
    font-weight: bold;
    margin: 0 0 14px 0;
    text-align: left;
    color: #000000;
}}
.toc-entry {{
    display: flex;
    align-items: baseline;
    margin-bottom: 3.5px;
    font-size: 10.5pt;
    line-height: 1.32;
    color: #000000;
}}
.toc-sec {{
    font-weight: bold;
    margin-top: 6px;
}}
.toc-subsec {{
    padding-left: 18px;
    font-size: 10pt;
}}
.toc-num {{
    color: #000000;
    min-width: 30px;
    font-weight: bold;
}}
.toc-subsec .toc-num {{
    min-width: 32px;
    font-weight: normal;
}}
.toc-text {{
    flex-shrink: 0;
    color: #000000;
}}
.toc-dots {{
    flex-grow: 1;
    border-bottom: 1.2pt dotted #444444;
    margin: 0 6px 3px 6px;
    height: 1em;
}}
.toc-page {{
    min-width: 20px;
    text-align: right;
    color: #000000;
}}
.toc-sec .toc-page {{
    font-weight: bold;
}}

.report-intro-box {{
    page-break-after: always;
}}
.report-intro-box h1 {{
    page-break-before: avoid !important;
}}

/* ========================================================
   BODY CONTENT (LATEX MONOCHROME REPORT STYLING)
   ======================================================== */
h1 {{
    font-size: 17pt;
    font-weight: bold;
    color: #000000;
    margin-top: 26pt;
    margin-bottom: 12pt;
    border: none;
    padding: 0;
    page-break-before: always;
}}
.cover-page h1, .latex-frontmatter h1 {{
    page-break-before: avoid;
}}

h2 {{
    font-size: 13.5pt;
    font-weight: bold;
    color: #000000;
    margin-top: 18pt;
    margin-bottom: 8pt;
    border: none;
    padding: 0;
}}

h3 {{
    font-size: 11.5pt;
    font-weight: bold;
    color: #000000;
    margin-top: 14pt;
    margin-bottom: 6pt;
    border: none;
    padding: 0;
}}

p, li {{
    text-align: justify;
    text-justify: inter-word;
    margin-bottom: 8pt;
    line-height: 1.5;
    color: #000000;
}}

a {{
    color: #000000;
    text-decoration: none;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14pt auto 4pt auto;
    font-size: 9.5pt;
    border: 1px solid #000000;
    page-break-inside: avoid;
}}
th, td {{
    border: 0.5pt solid #000000;
    padding: 6px 8px;
    text-align: left;
    vertical-align: top;
    color: #000000;
}}
th {{
    background-color: #f2f2f2;
    font-weight: bold;
    color: #000000;
}}
tr:nth-child(even) {{
    background-color: #fafafa;
}}

pre, code {{
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8.5pt;
    color: #000000;
}}
pre {{
    background-color: #f9f9f9;
    border: 0.5pt solid #cccccc;
    border-radius: 2px;
    padding: 10px 12px;
    overflow-x: auto;
    page-break-inside: avoid;
    line-height: 1.45;
    margin: 12pt 0;
}}
code {{
    background-color: #f2f2f2;
    padding: 1px 4px;
    border-radius: 2px;
}}
pre code {{
    background-color: transparent;
    padding: 0;
}}

img {{
    max-width: 90%;
    height: auto;
    display: block;
    margin: 12pt auto 4pt auto;
    border: 0.5pt solid #aaaaaa;
    page-break-inside: avoid;
    background: transparent;
}}

.table-caption, .figure-caption {{
    text-align: center;
    font-size: 10pt;
    font-style: italic;
    margin-top: 4pt;
    margin-bottom: 14pt;
    page-break-before: avoid;
    color: #000000;
}}
.table-caption b, .figure-caption b {{
    font-style: normal;
    font-weight: bold;
    color: #000000;
}}

blockquote {{
    border-left: 2.5pt solid #000000;
    margin: 12pt 0;
    padding: 6pt 12pt;
    background-color: #f7f7f7;
    color: #000000;
    font-size: 10pt;
}}

hr {{
    border: 0;
    border-top: 0.5pt solid #888888;
    margin: 20pt 0;
}}
</style>
</head>
<body>

<!-- ========================================================
     PAGE 1: TRANG BÌA CHUẨN TEMPLATE KHTN - ĐHQG HCM
     ======================================================== -->
<div class="cover-page">
    <div class="institution-header">
        <p class="univ-line1">ĐẠI HỌC QUỐC GIA TPHCM</p>
        <p class="univ-line2">TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN</p>
        <p class="univ-line3">KHOA CÔNG NGHỆ THÔNG TIN</p>
        <p class="univ-line4">BỘ MÔN KIỂM THỬ PHẦN MỀM</p>
    </div>

    <div class="cover-rule"></div>

    <div class="cover-title-box">
        <div class="cover-title-main">Báo cáo Seminar</div>
        <div class="cover-title-sub">Đề tài: Automation Testing cho Desktop Applications</div>
    </div>

    <div class="cover-rule" style="margin-top: 25px; margin-bottom: 35px;"></div>

    <div class="cover-course">Môn học: Kiểm thử phần mềm</div>

    <div class="cover-info-container">
        <div class="info-col-left">
            <div class="info-label">Sinh viên thực hiện:</div>
            <div>Phan Trung Tín (23120372)</div>
            <div>Nguyễn Lê Quang Kan (23120279)</div>
            <div>Bùi Quang Tùng (20120397)</div>
            <div>Trần Vũ Quang (23120346)</div>
        </div>
        <div class="info-col-right">
            <div class="info-label">Giáo viên hướng dẫn:</div>
            <div>ThS. Huỳnh Phước Hải</div>
        </div>
    </div>

    <div class="cover-date">Thành phố Hồ Chí Minh, ngày 30 tháng 10 năm 2026</div>

    <div class="cover-logo-box">
        <img src="data:image/png;base64,{logo_b64}" class="hcmus-logo-img" alt="HCMUS Logo">
    </div>
</div>

<!-- ========================================================
     PAGE 2: MỤC LỤC (TABLE OF CONTENTS)
     ======================================================== -->
<div class="latex-frontmatter">
    <h1 class="latex-toc-title">Mục lục</h1>

    <div class="toc-entry toc-sec">
        <span class="toc-num">1</span>
        <span class="toc-text">Giới Thiệu & Bối Cảnh (Introduction)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">1</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">1.1</span>
        <span class="toc-text">Bối cảnh và động lực của kiểm thử tự động Desktop</span>
        <span class="toc-dots"></span>
        <span class="toc-page">1</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">1.2</span>
        <span class="toc-text">Đặc thù kỹ thuật của ứng dụng Desktop trên Windows</span>
        <span class="toc-dots"></span>
        <span class="toc-page">2</span>
    </div>

    <div class="toc-entry toc-sec">
        <span class="toc-num">2</span>
        <span class="toc-text">Cơ Sở Lý Thuyết Kiểm Thử Tự Động Desktop (Theory)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">4</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">2.1</span>
        <span class="toc-text">Kiến trúc UI Automation & Cơ chế điều khiển Windows</span>
        <span class="toc-dots"></span>
        <span class="toc-page">4</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">2.2</span>
        <span class="toc-text">Kỹ thuật Record & Playback và cơ chế ánh xạ phần tử</span>
        <span class="toc-dots"></span>
        <span class="toc-page">6</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">2.3</span>
        <span class="toc-text">Mô hình thiết kế Page Object Model (POM) cho Desktop</span>
        <span class="toc-dots"></span>
        <span class="toc-page">8</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">2.4</span>
        <span class="toc-text">Hiện tượng Flaky Test, cơ chế Explicit Wait và Test Oracle</span>
        <span class="toc-dots"></span>
        <span class="toc-page">10</span>
    </div>

    <div class="toc-entry toc-sec">
        <span class="toc-num">3</span>
        <span class="toc-text">Khảo Sát Thị Trường & Bộ Tiêu Chí Đánh Giá (Tool Survey)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">13</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">3.1</span>
        <span class="toc-text">Bức tranh công cụ kiểm thử tự động Desktop hiện nay</span>
        <span class="toc-dots"></span>
        <span class="toc-page">13</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">3.2</span>
        <span class="toc-text">Bộ tiêu chí đánh giá toàn diện gồm 10 khía cạnh</span>
        <span class="toc-dots"></span>
        <span class="toc-page">14</span>
    </div>

    <div class="toc-entry toc-sec">
        <span class="toc-num">4</span>
        <span class="toc-text">Nghiên Cứu Công Cụ Đại Diện A: Katalon Studio</span>
        <span class="toc-dots"></span>
        <span class="toc-page">17</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">4.1</span>
        <span class="toc-text">Tổng quan và cơ chế FlaUI tích hợp trong Katalon</span>
        <span class="toc-dots"></span>
        <span class="toc-page">17</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">4.2</span>
        <span class="toc-text">Thực nghiệm 3 Demo: Cài đặt, Record/Playback, BVA Data-Driven</span>
        <span class="toc-dots"></span>
        <span class="toc-page">19</span>
    </div>

    <div class="toc-entry toc-sec">
        <span class="toc-num">5</span>
        <span class="toc-text">Nghiên Cứu Công Cụ Đại Diện B: Microsoft WinAppDriver</span>
        <span class="toc-dots"></span>
        <span class="toc-page">24</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">5.1</span>
        <span class="toc-text">Kiến trúc Windows Application Driver và chuẩn WebDriver</span>
        <span class="toc-dots"></span>
        <span class="toc-page">24</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">5.2</span>
        <span class="toc-text">Cài đặt Framework C# NUnit POM và thực nghiệm 3 Demo</span>
        <span class="toc-dots"></span>
        <span class="toc-page">26</span>
    </div>

    <div class="toc-entry toc-sec">
        <span class="toc-num">6</span>
        <span class="toc-text">So Sánh Đối Chiếu Toàn Diện (Comparison)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">30</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">6.1</span>
        <span class="toc-text">Đối chiếu tính năng kỹ thuật và trải nghiệm lập trình</span>
        <span class="toc-dots"></span>
        <span class="toc-page">30</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">6.2</span>
        <span class="toc-text">Số liệu thực nghiệm định lượng: Thời gian, LOC, Tài nguyên</span>
        <span class="toc-dots"></span>
        <span class="toc-page">33</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">6.3</span>
        <span class="toc-text">Ma trận chấm điểm và hướng dẫn lựa chọn công cụ</span>
        <span class="toc-dots"></span>
        <span class="toc-page">35</span>
    </div>

    <div class="toc-entry toc-sec">
        <span class="toc-num">7</span>
        <span class="toc-text">Ứng Dụng AI Trong Desktop Automation Testing</span>
        <span class="toc-dots"></span>
        <span class="toc-page">37</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">7.1</span>
        <span class="toc-text">Quy trình Prompt Engineering 2 pha (Phân tích BVA và Sinh code)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">37</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">7.2</span>
        <span class="toc-text">Thực nghiệm đối chiếu: ChatGPT-4, Gemini Advanced, Claude 3.5</span>
        <span class="toc-dots"></span>
        <span class="toc-page">39</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">7.3</span>
        <span class="toc-text">Thực thi Test Suite C# AI-WinAppDriver 19 ca BVA đạt 100% PASS</span>
        <span class="toc-dots"></span>
        <span class="toc-page">42</span>
    </div>

    <div class="toc-entry toc-sec">
        <span class="toc-num">8</span>
        <span class="toc-text">Bài Tập Thực Hành Cá Nhân 30 Phút Tại Lớp (Exercise)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">44</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">8.1</span>
        <span class="toc-text">Mục tiêu, chuẩn bị tài nguyên từ GitHub và Starter Kit</span>
        <span class="toc-dots"></span>
        <span class="toc-page">44</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">8.2</span>
        <span class="toc-text">Nội dung Bài 1 (Đăng nhập), Bài 2 (Tính tổng BVA) & Barem điểm</span>
        <span class="toc-dots"></span>
        <span class="toc-page">45</span>
    </div>

    <div class="toc-entry toc-sec">
        <span class="toc-num">9</span>
        <span class="toc-text">Minh Chứng Thực Nghiệm, Kê Khai AI & Kết Luận</span>
        <span class="toc-dots"></span>
        <span class="toc-page">48</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">9.1</span>
        <span class="toc-text">Danh sách 3 Video Demo YouTube chính thức</span>
        <span class="toc-dots"></span>
        <span class="toc-page">48</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">9.2</span>
        <span class="toc-text">Nhật ký Git Commit Log và Kê khai trung thực sử dụng AI</span>
        <span class="toc-dots"></span>
        <span class="toc-page">49</span>
    </div>
    <div class="toc-entry toc-subsec">
        <span class="toc-num">9.3</span>
        <span class="toc-text">Kết luận tổng kết và hướng phát triển</span>
        <span class="toc-dots"></span>
        <span class="toc-page">50</span>
    </div>
</div>

<!-- ========================================================
     PAGE 3: DANH SÁCH BẢNG (LIST OF TABLES)
     ======================================================== -->
<div class="latex-frontmatter">
    <h1 class="latex-toc-title">Danh sách bảng</h1>

    <div class="toc-entry">
        <span class="toc-num">1</span>
        <span class="toc-text">Bảng khảo sát và thang điểm bộ tiêu chí đánh giá công cụ kiểm thử Desktop</span>
        <span class="toc-dots"></span>
        <span class="toc-page">14</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">2</span>
        <span class="toc-text">Bảng đối chiếu kỹ thuật chi tiết giữa Katalon Studio và Microsoft WinAppDriver</span>
        <span class="toc-dots"></span>
        <span class="toc-page">31</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">3</span>
        <span class="toc-text">Bảng đo đạc định lượng thực nghiệm thời gian, số dòng mã (LOC) và tài nguyên</span>
        <span class="toc-dots"></span>
        <span class="toc-page">33</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">4</span>
        <span class="toc-text">Bảng ma trận phân tích so sánh toàn diện 10 tiêu chí</span>
        <span class="toc-dots"></span>
        <span class="toc-page">35</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">5</span>
        <span class="toc-text">Bảng 12 ca kiểm thử giá trị biên (BVA) chuẩn hóa do AI sinh</span>
        <span class="toc-dots"></span>
        <span class="toc-page">38</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">6</span>
        <span class="toc-text">Bảng đo đạc thời gian sinh kịch bản và tỷ lệ ảo giác giữa các mô hình AI</span>
        <span class="toc-dots"></span>
        <span class="toc-page">41</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">7</span>
        <span class="toc-text">Bảng phân bổ thời gian thực hành cá nhân 30 phút tại lớp</span>
        <span class="toc-dots"></span>
        <span class="toc-page">45</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">8</span>
        <span class="toc-text">Bảng barem chấm điểm chi tiết bài tập thực hành cá nhân (Thang điểm 10)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">47</span>
    </div>
</div>

<!-- ========================================================
     PAGE 4: DANH SÁCH HÌNH VẼ (LIST OF FIGURES)
     ======================================================== -->
<div class="latex-frontmatter">
    <h1 class="latex-toc-title">Danh sách hình vẽ</h1>

    <div class="toc-entry">
        <span class="toc-num">1</span>
        <span class="toc-text">Sơ đồ kiến trúc kiểm thử tự động ứng dụng Desktop (Mermaid Flowchart)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">4</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">2</span>
        <span class="toc-text">Giao diện màn hình Đăng nhập của ứng dụng mẫu thực nghiệm MiniSum</span>
        <span class="toc-dots"></span>
        <span class="toc-page">8</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">3</span>
        <span class="toc-text">Giao diện chức năng Tính tổng và lưu vết lịch sử trên ứng dụng MiniSum v2</span>
        <span class="toc-dots"></span>
        <span class="toc-page">8</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">4</span>
        <span class="toc-text">Quy trình ghi nhận và phát lại hành vi tương tác giao diện Record & Playback (Mermaid Flowchart)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">9</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">5</span>
        <span class="toc-text">Mô hình thiết kế kiểm thử Page Object Model (POM) cho ứng dụng Desktop (Mermaid Flowchart)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">11</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">6</span>
        <span class="toc-text">Giao diện làm việc và cấu trúc thư mục dự án kiểm thử trong Katalon Studio</span>
        <span class="toc-dots"></span>
        <span class="toc-page">17</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">7</span>
        <span class="toc-text">Kho đối tượng Object Repository lưu trữ định vị phần tử ứng dụng MiniSum</span>
        <span class="toc-dots"></span>
        <span class="toc-page">18</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">8</span>
        <span class="toc-text">Khởi chạy ứng dụng MiniSum thông qua trình điều khiển Windows Driver trên Katalon Studio</span>
        <span class="toc-dots"></span>
        <span class="toc-page">20</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">9</span>
        <span class="toc-text">Thực thi kịch bản kiểm thử đăng nhập và xác minh Checkpoint nhãn thông báo thành công</span>
        <span class="toc-dots"></span>
        <span class="toc-page">20</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">10</span>
        <span class="toc-text">Thiết lập liên kết dữ liệu kiểm thử giá trị biên (BVA) từ file Excel vào Test Suite</span>
        <span class="toc-dots"></span>
        <span class="toc-page">21</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">11</span>
        <span class="toc-text">Báo cáo HTML Report trực quan kết quả thực thi kiểm thử tự động trên Katalon Studio</span>
        <span class="toc-dots"></span>
        <span class="toc-page">21</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">12</span>
        <span class="toc-text">Cửa sổ Console khởi chạy dịch vụ Microsoft WinAppDriver tại cổng 4723</span>
        <span class="toc-dots"></span>
        <span class="toc-page">25</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">13</span>
        <span class="toc-text">Dò tìm thuộc tính AutomationId các phần tử trên màn hình Đăng nhập bằng Accessibility Insights</span>
        <span class="toc-dots"></span>
        <span class="toc-page">26</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">14</span>
        <span class="toc-text">Dò tìm thuộc tính và AutomationId của nút Đăng xuất (btnLogout)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">26</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">15</span>
        <span class="toc-text">Dò tìm thuộc tính AutomationId ô hiển thị kết quả tính toán (lblResult)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">26</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">16</span>
        <span class="toc-text">Dò tìm thuộc tính AutomationId trường nhập mật khẩu (txtPassword)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">27</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">17</span>
        <span class="toc-text">Dò tìm thuộc tính nhãn cảnh báo đăng nhập thất bại (lblMessage)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">27</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">18</span>
        <span class="toc-text">Dò tìm thuộc tính AutomationId ô nhập số thứ nhất (txtNumA)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">27</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">19</span>
        <span class="toc-text">Dò tìm thuộc tính AutomationId ô nhập số thứ hai (txtNumB)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">27</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">20</span>
        <span class="toc-text">Dò tìm thuộc tính AutomationId trường nhập tài khoản (txtUsername)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">28</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">21</span>
        <span class="toc-text">Dò tìm thuộc tính AutomationId nút thực thi Tính tổng (btnCalculate)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">28</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">22</span>
        <span class="toc-text">Kết quả thực thi toàn bộ kịch bản kiểm thử WinAppDriver thành công (100% Passed) trên Terminal</span>
        <span class="toc-dots"></span>
        <span class="toc-page">29</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">23</span>
        <span class="toc-text">Minh chứng cơ chế bắt ngoại lệ và chụp ảnh màn hình tự động lưu trữ khi phát hiện ca kiểm thử thất bại</span>
        <span class="toc-dots"></span>
        <span class="toc-page">29</span>
    </div>
    <div class="toc-entry">
        <span class="toc-num">24</span>
        <span class="toc-text">Sơ đồ quy trình Prompt Engineering 2 pha ứng dụng AI trong kiểm thử thực tế (Mermaid Flowchart)</span>
        <span class="toc-dots"></span>
        <span class="toc-page">38</span>
    </div>
</div>

<!-- ========================================================
     CONTENT: TOÀN BỘ 9 PHẦN NỘI DUNG CHÍNH
     ======================================================== -->
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
        '--no-pdf-header-footer',
        f'--print-to-pdf={target_pdf}',
        f'file:///{html_path}'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(target_pdf):
        print(f"Successfully exported {target_pdf}! Size: {os.path.getsize(target_pdf):,} bytes")
    else:
        print(f"Failed to export {target_pdf}: {res.stderr}")
