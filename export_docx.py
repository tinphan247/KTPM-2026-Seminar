import os
import re
import glob
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from PIL import Image

base_dir = os.path.abspath('.')

def find_image(src):
    src_clean = src.strip().strip('<>').replace('\\', '/')
    candidates = [
        os.path.normpath(os.path.join(base_dir, 'docs', src_clean)),
        os.path.normpath(os.path.join(base_dir, src_clean)),
        os.path.normpath(os.path.join(base_dir, 'docs', src_clean.replace('../', ''))),
        os.path.normpath(os.path.join(base_dir, src_clean.replace('../', ''))),
    ]
    for c in candidates:
        if os.path.exists(c) and os.path.isfile(c):
            return c
    
    bname = os.path.basename(src_clean)
    matches = glob.glob(os.path.join(base_dir, '**', bname), recursive=True)
    if matches:
        return matches[0]
    return None

def parse_inline(text):
    text = re.sub(r'<\/?b>', '**', text)
    text = re.sub(r'<\/?strong>', '**', text)
    text = re.sub(r'<\/?i>', '*', text)
    text = re.sub(r'<\/?em>', '*', text)
    text = re.sub(r'<br\s*\/?>', '\n', text)
    text = re.sub(r'<a\s+[^>]*id="[^"]*"[^>]*><\/a>', '', text)
    
    pattern = re.compile(
        r'(\*\*\*(.+?)\*\*\*)'
        r'|(\*\*(.+?)\*\*)'
        r'|(\*([^\*]+?)\*)'
        r'|(`([^`]+?)`)'
        r'|(\[([^\]]+)\]\(([^)]+)\))'
    )
    
    runs = []
    pos = 0
    for m in pattern.finditer(text):
        start, end = m.span()
        if start > pos:
            runs.append({'text': text[pos:start], 'bold': False, 'italic': False, 'code': False})
        
        if m.group(1):
            runs.append({'text': m.group(2), 'bold': True, 'italic': True, 'code': False})
        elif m.group(3):
            runs.append({'text': m.group(4), 'bold': True, 'italic': False, 'code': False})
        elif m.group(5):
            runs.append({'text': m.group(6), 'bold': False, 'italic': True, 'code': False})
        elif m.group(7):
            runs.append({'text': m.group(8), 'bold': False, 'italic': False, 'code': True})
        elif m.group(9):
            runs.append({'text': m.group(10), 'bold': False, 'italic': False, 'code': False, 'link': m.group(11)})
        pos = end
    
    if pos < len(text):
        runs.append({'text': text[pos:], 'bold': False, 'italic': False, 'code': False})
    
    return runs

def add_inline_runs(paragraph, text, base_font='Times New Roman', base_size=Pt(11.5), base_color=RGBColor(0, 0, 0)):
    items = parse_inline(text)
    for it in items:
        run = paragraph.add_run(it['text'])
        if it['code']:
            run.font.name = 'Consolas'
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(180, 20, 60)
        else:
            run.font.name = base_font
            run.font.size = base_size
            if it.get('link'):
                run.font.color.rgb = RGBColor(0, 45, 156)
                run.font.underline = True
            else:
                run.font.color.rgb = base_color
        
        if it['bold']:
            run.bold = True
        if it['italic']:
            run.italic = True

def set_cell_shading(cell, color_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_table_borders(table, color="000000", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>\n'
        f'  <w:top w:w="{top}" w:type="dxa"/>\n'
        f'  <w:bottom w:w="{bottom}" w:type="dxa"/>\n'
        f'  <w:left w:w="{left}" w:type="dxa"/>\n'
        f'  <w:right w:w="{right}" w:type="dxa"/>\n'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_shading(cell, "F8F9FA")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>\n'
        f'  <w:left w:val="single" w:sz="6" w:space="0" w:color="002D9C"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(code_text.rstrip())
    run.font.name = 'Consolas'
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(30, 41, 59)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

def add_blockquote(doc, bq_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_shading(cell, "F8FAFC")
    set_cell_margins(cell, top=100, bottom=100, left=160, right=160)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="none"/>\n'
        f'  <w:left w:val="single" w:sz="18" w:space="0" w:color="2563EB"/>\n'
        f'  <w:bottom w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.25
    add_inline_runs(p, bq_text.strip(), base_font='Times New Roman', base_size=Pt(10.5), base_color=RGBColor(30, 41, 59))
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

def add_caption_paragraph(doc, caption_text, caption_type="bảng"):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.line_spacing = 1.15
    
    clean = re.sub(r'<\/?p[^>]*>', '', caption_text)
    clean = re.sub(r'<\/?b>', '**', clean)
    clean = re.sub(r'<\/?i>', '*', clean)
    clean = re.sub(r'<[^>]+>', '', clean).strip()
    
    add_inline_runs(p, clean, base_font='Times New Roman', base_size=Pt(10), base_color=RGBColor(30, 41, 59))

def build_docx_report():
    doc = Document()
    
    # Section 0: Cover Page
    sec_cover = doc.sections[0]
    sec_cover.page_width = Inches(8.27)
    sec_cover.page_height = Inches(11.69)
    sec_cover.top_margin = Inches(0.8)
    sec_cover.bottom_margin = Inches(0.6)
    sec_cover.left_margin = Inches(0.98)
    sec_cover.right_margin = Inches(0.79)
    sec_cover.different_first_page_header_footer = True
    
    # ================= COVER PAGE =================
    p_univ1 = doc.add_paragraph()
    p_univ1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_univ1.paragraph_format.space_before = Pt(5)
    p_univ1.paragraph_format.space_after = Pt(2)
    r = p_univ1.add_run('ĐẠI HỌC QUỐC GIA TPHCM')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
    
    p_univ2 = doc.add_paragraph()
    p_univ2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_univ2.paragraph_format.space_before = Pt(0)
    p_univ2.paragraph_format.space_after = Pt(3)
    r = p_univ2.add_run('TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.bold = True
    
    p_univ3 = doc.add_paragraph()
    p_univ3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_univ3.paragraph_format.space_before = Pt(3)
    p_univ3.paragraph_format.space_after = Pt(2)
    r = p_univ3.add_run('KHOA CÔNG NGHỆ THÔNG TIN')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11.5)
    r.bold = True
    
    p_univ4 = doc.add_paragraph()
    p_univ4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_univ4.paragraph_format.space_before = Pt(0)
    p_univ4.paragraph_format.space_after = Pt(18)
    r = p_univ4.add_run('BỘ MÔN KIỂM THỬ PHẦN MỀM')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    
    # Divider Rule
    p_rule1 = doc.add_paragraph()
    p_rule1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_rule1.paragraph_format.space_before = Pt(0)
    p_rule1.paragraph_format.space_after = Pt(20)
    r = p_rule1.add_run('―' * 42)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.bold = True
    
    # Report Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(8)
    r = p_title.add_run('Báo cáo Seminar')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(24)
    r.bold = True
    r.font.color.rgb = RGBColor(0, 45, 156)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(20)
    r = p_sub.add_run('Đề tài: Automation Testing cho Desktop Applications')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.bold = True
    
    # Divider Rule
    p_rule2 = doc.add_paragraph()
    p_rule2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_rule2.paragraph_format.space_before = Pt(0)
    p_rule2.paragraph_format.space_after = Pt(18)
    r = p_rule2.add_run('―' * 42)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.bold = True
    
    # Course
    p_course = doc.add_paragraph()
    p_course.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_course.paragraph_format.space_before = Pt(0)
    p_course.paragraph_format.space_after = Pt(20)
    r = p_course.add_run('Môn học: Kiểm thử phần mềm')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.bold = True
    
    # Info Table (2 Columns: Students and Supervisor)
    tbl_info = doc.add_table(rows=1, cols=2)
    tbl_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_l, cell_r = tbl_info.cell(0, 0), tbl_info.cell(0, 1)
    cell_l.width = Inches(3.6)
    cell_r.width = Inches(2.8)
    
    p_sl = cell_l.paragraphs[0]
    p_sl.paragraph_format.line_spacing = 1.3
    p_sl.paragraph_format.space_after = Pt(2)
    r = p_sl.add_run('Sinh viên thực hiện:\n')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    r.bold = True
    r.italic = True
    
    students = [
        'Phan Trung Tín (23120372)',
        'Nguyễn Lê Quang Kan (23120279)',
        'Bùi Quang Tùng (20120397)',
        'Trần Vũ Quang (23120346)'
    ]
    for s in students:
        r = p_sl.add_run(f'• {s}\n')
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
    
    p_sr = cell_r.paragraphs[0]
    p_sr.paragraph_format.line_spacing = 1.3
    p_sr.paragraph_format.space_after = Pt(2)
    r = p_sr.add_run('Giáo viên hướng dẫn:\n')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    r.bold = True
    r.italic = True
    r = p_sr.add_run('ThS. Huỳnh Phước Hải\n')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    
    # Date
    p_date = doc.add_paragraph()
    p_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_date.paragraph_format.space_before = Pt(20)
    p_date.paragraph_format.space_after = Pt(10)
    r = p_date.add_run('Thành phố Hồ Chí Minh, ngày 30 tháng 10 năm 2026')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    
    # Logo
    logo_file = os.path.join(base_dir, 'docs', 'images', 'hcmus_logo.png')
    if os.path.exists(logo_file):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(6)
        p_logo.paragraph_format.space_after = Pt(0)
        p_logo.add_run().add_picture(logo_file, width=Inches(1.4))
    
    # ================= SECTION 1: BODY =================
    doc.add_section()
    sec_body = doc.sections[1]
    sec_body.page_width = Inches(8.27)
    sec_body.page_height = Inches(11.69)
    sec_body.top_margin = Inches(1.0)
    sec_body.bottom_margin = Inches(0.9)
    sec_body.left_margin = Inches(0.98)
    sec_body.right_margin = Inches(0.79)
    sec_body.different_first_page_header_footer = False
    sec_body.header.is_linked_to_previous = False
    sec_body.footer.is_linked_to_previous = False
    
    # Setup Running Header
    hdr = sec_body.header
    p_hdr = hdr.paragraphs[0]
    p_hdr.text = ''
    tbl_hdr = hdr.add_table(rows=1, cols=2, width=Inches(6.5))
    tbl_hdr.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_hl, c_hr = tbl_hdr.cell(0, 0), tbl_hdr.cell(0, 1)
    c_hl.width = Inches(3.25)
    c_hr.width = Inches(3.25)
    
    p_hl = c_hl.paragraphs[0]
    p_hl.paragraph_format.space_before = Pt(0)
    p_hl.paragraph_format.space_after = Pt(2)
    r = p_hl.add_run('Báo cáo Seminar')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(9.5)
    r.italic = True
    
    p_hr = c_hr.paragraphs[0]
    p_hr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_hr.paragraph_format.space_before = Pt(0)
    p_hr.paragraph_format.space_after = Pt(2)
    r = p_hr.add_run('Trường Đại học Khoa học Tự nhiên - ĐHQG HCM\nMôn: Kiểm thử phần mềm')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(9)
    
    for c in [c_hl, c_hr]:
        tcPr = c._tc.get_or_add_tcPr()
        tcBorders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>\n'
            f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
            f'</w:tcBorders>'
        )
        tcPr.append(tcBorders)
    
    # Setup Running Footer
    ftr = sec_body.footer
    p_ftr = ftr.paragraphs[0]
    p_ftr.text = ''
    tbl_ftr = ftr.add_table(rows=1, cols=2, width=Inches(6.5))
    tbl_ftr.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_fl, c_fr = tbl_ftr.cell(0, 0), tbl_ftr.cell(0, 1)
    c_fl.width = Inches(3.25)
    c_fr.width = Inches(3.25)
    
    p_fl = c_fl.paragraphs[0]
    p_fl.paragraph_format.space_before = Pt(3)
    p_fl.paragraph_format.space_after = Pt(0)
    r = p_fl.add_run('LaTeX by Nhóm 02')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(9.5)
    
    p_fr = c_fr.paragraphs[0]
    p_fr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_fr.paragraph_format.space_before = Pt(3)
    p_fr.paragraph_format.space_after = Pt(0)
    r = p_fr.add_run('Trang ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(9.5)
    fld = parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="PAGE"/>')
    p_fr._p.append(fld)
    
    for c in [c_fl, c_fr]:
        tcPr = c._tc.get_or_add_tcPr()
        tcBorders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>\n'
            f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
            f'</w:tcBorders>'
        )
        tcPr.append(tcBorders)
    
    # ================= FRONT MATTER: TOC, LOT, LOF =================
    # 1. Mục lục
    p_toc_title = doc.add_paragraph()
    p_toc_title.paragraph_format.space_before = Pt(10)
    p_toc_title.paragraph_format.space_after = Pt(14)
    r = p_toc_title.add_run('Mục lục')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(18)
    r.bold = True
    
    toc_data = [
        (1, "1", "Giới Thiệu & Bối Cảnh (Introduction)", "1"),
        (2, "1.1", "Bối cảnh và động lực của kiểm thử tự động Desktop", "1"),
        (2, "1.2", "Đặc thù kỹ thuật của ứng dụng Desktop trên Windows", "2"),
        (2, "1.3", "Lý do chọn đề tài, mục tiêu và phạm vi nghiên cứu", "3"),
        (1, "2", "Cơ Sở Lý Thuyết Kiểm Thử Tự Động Desktop (Theory)", "4"),
        (2, "2.1", "Kiến trúc UI Automation & Cơ chế điều khiển Windows", "4"),
        (2, "2.2", "Kỹ thuật Record & Playback và cơ chế ánh xạ phần tử", "6"),
        (2, "2.3", "Mô hình thiết kế Page Object Model (POM) cho Desktop", "8"),
        (2, "2.4", "Kiểm thử điều khiển bằng dữ liệu (Data-Driven Testing - DDT)", "11"),
        (2, "2.5", "Các kỹ thuật xác minh (Verification & Checkpoints)", "12"),
        (2, "2.6", "Kiểm soát và xử lý hiện tượng Flaky Test trong Desktop UI", "13"),
        (2, "2.7", "Cơ chế đồng bộ hóa giao diện và chiến lược chờ (Waits & Synchronization)", "14"),
        (2, "2.8", "Các dạng Test Oracle và nguồn dữ liệu đối chiếu kết quả mong đợi", "15"),
        (2, "2.9", "Kiểm thử phục hồi lỗi (Recovery Testing & Exception Handling)", "15"),
        (2, "2.10", "Hiện thực ứng dụng thực nghiệm: MiniSum (v1, v2, v3)", "16"),
        (1, "3", "Khảo Sát Thị Trường & Bộ Tiêu Chí Đánh Giá (Tool Survey)", "17"),
        (2, "3.1", "Bối cảnh thị trường công cụ kiểm thử tự động Desktop năm 2026", "17"),
        (2, "3.2", "Khảo sát chi tiết 6 công cụ kiểm thử Desktop phổ biến", "18"),
        (2, "3.3", "Thiết lập bộ tiêu chí đánh giá và ma trận so sánh tổng quan", "19"),
        (2, "3.4", "Lý do lựa chọn Katalon Studio và WinAppDriver làm đại diện nghiên cứu sâu", "20"),
        (1, "4", "Nghiên Cứu Công Cụ Đại Diện A – Katalon Studio", "21"),
        (2, "4.1", "Tổng quan công cụ, kiến trúc và mô hình bản quyền", "21"),
        (2, "4.2", "Thiết lập môi trường thực nghiệm với Katalon Studio và WinAppDriver", "22"),
        (2, "4.3", "Thực nghiệm 1: Record & Playback kịch bản Đăng nhập MiniSum", "23"),
        (2, "4.4", "Thực nghiệm 2: Thiết lập Checkpoint xác minh giao diện và thông báo lỗi", "24"),
        (2, "4.5", "Thực nghiệm 3: Data-Driven Testing với 12 test case phân tích giá trị biên (BVA)", "25"),
        (2, "4.6", "Phân tích báo cáo kiểm thử và cơ chế tự động ghi nhận bằng chứng", "26"),
        (2, "4.7", "Mở rộng kịch bản với Groovy Scripting và Custom Keywords", "27"),
        (2, "4.8", "Đánh giá ưu điểm, hạn chế và phạm vi áp dụng tối ưu của Katalon Studio", "28"),
        (1, "5", "Nghiên Cứu Công Cụ Đại Diện B – Microsoft WinAppDriver", "29"),
        (2, "5.1", "Tổng quan dự án, giao thức WebDriver và kiến trúc giao tiếp", "29"),
        (2, "5.2", "Thiết lập môi trường và cấu hình Visual Studio với NUnit", "30"),
        (2, "5.3", "Nhận diện và dò tìm phần tử giao diện với Accessibility Insights", "31"),
        (2, "5.4", "Hiện thực kiểm thử Đăng nhập theo mô hình Page Object Model (POM)", "32"),
        (2, "5.5", "Kiểm thử chức năng Tính tổng MiniSum v2 và bắt lỗi giao diện", "33"),
        (2, "5.6", "Data-Driven Testing với NUnit TestCaseSource và thư viện NPOI", "34"),
        (2, "5.7", "Xử lý ngoại lệ, chụp màn hình tự động và xuất báo cáo kiểm thử", "35"),
        (2, "5.8", "Đánh giá ưu điểm, hạn chế và tính khả thi trong dự án dài hạn", "36"),
        (1, "6", "So Sánh Đối Chiếu Toàn Diện (Comparison)", "37"),
        (2, "6.1", "Ma trận so sánh định tính theo 10 tiêu chí kỹ thuật", "37"),
        (2, "6.2", "So sánh định lượng qua kết quả thực nghiệm thực tế trên MiniSum", "38"),
        (2, "6.3", "Phân tích chi phí sở hữu tổng thể (TCO) và bài toán kinh tế", "39"),
        (2, "6.4", "Mô hình cây quyết định (Decision Tree) lựa chọn công cụ phù hợp", "40"),
        (1, "7", "Ứng Dụng Trí Tuệ Nhân Tạo (AI) Trong Desktop Automation", "41"),
        (2, "7.1", "Xu hướng và các cấp độ ứng dụng AI trong kiểm thử tự động Desktop", "41"),
        (2, "7.2", "Kỹ thuật Prompt Engineering sinh mã kiểm thử tự động từ đặc tả UI", "42"),
        (2, "7.3", "Thực nghiệm sinh kịch bản WinAppDriver POM bằng quy trình Prompting 2 pha", "43"),
        (2, "7.4", "Đo lường hiệu quả định lượng: Tốc độ, độ chính xác và tỷ lệ thành công", "44"),
        (2, "7.5", "Thách thức, cạm bẫy và nguyên tắc kiểm soát chất lượng mã nguồn do AI sinh ra", "45"),
        (1, "8", "Hệ Thống Bài Tập Thực Hành Cá Nhân 30 Phút Tại Lớp (Exercise)", "46"),
        (2, "8.1", "Mục tiêu và yêu cầu bài tập thực hành cá nhân", "46"),
        (2, "8.2", "Đề bài chi tiết: Tự động hóa kiểm thử chức năng Đăng nhập MiniSum", "46"),
        (2, "8.3", "Hướng dẫn từng bước với Katalon Studio (Tùy chọn A)", "47"),
        (2, "8.4", "Hướng dẫn từng bước với WinAppDriver và C# NUnit (Tùy chọn B)", "48"),
        (2, "8.5", "Barem chấm điểm chi tiết và tiêu chí đánh giá (Thang điểm 10)", "49"),
        (1, "9", "Minh Chứng Thực Nghiệm, Kê Khai AI & Kết Luận", "50"),
        (2, "9.1", "Minh chứng Video Demo YouTube (Chế độ Unlisted)", "50"),
        (2, "9.2", "Nhật ký đóng góp trên Git Commit Log", "50"),
        (2, "9.3", "Kê khai sử dụng Trí tuệ Nhân tạo (AI Usage Declaration)", "51"),
        (2, "9.4", "Kết luận và Đánh giá chung", "51")
    ]
    
    tbl_toc = doc.add_table(rows=len(toc_data), cols=3)
    tbl_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, (level, num, title, page) in enumerate(toc_data):
        row = tbl_toc.rows[idx]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width = Inches(0.55 if level == 1 else 0.75)
        c1.width = Inches(5.35 if level == 1 else 5.15)
        c2.width = Inches(0.6)
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(3 if level == 1 else 1)
        p0.paragraph_format.space_after = Pt(1)
        r0 = p0.add_run(num)
        r0.font.name = 'Times New Roman'
        r0.font.size = Pt(10.5 if level == 1 else 10)
        r0.bold = (level == 1)
        r0.font.color.rgb = RGBColor(0, 45, 156) if level == 1 else RGBColor(0, 0, 0)
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(3 if level == 1 else 1)
        p1.paragraph_format.space_after = Pt(1)
        r1 = p1.add_run(('  ' if level == 2 else '') + title)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(10.5 if level == 1 else 10)
        r1.bold = (level == 1)
        
        p2 = c2.paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p2.paragraph_format.space_before = Pt(3 if level == 1 else 1)
        p2.paragraph_format.space_after = Pt(1)
        r2 = p2.add_run(page)
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(10.5 if level == 1 else 10)
        r2.bold = (level == 1)
    
    doc.add_page_break()
    
    # 2. Danh sách bảng
    p_lot_title = doc.add_paragraph()
    p_lot_title.paragraph_format.space_before = Pt(10)
    p_lot_title.paragraph_format.space_after = Pt(14)
    r = p_lot_title.add_run('Danh sách bảng')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(18)
    r.bold = True
    
    lot_data = [
        ("0.1", "Phân công vai trò và tỷ lệ đóng góp thực tế của các thành viên Nhóm 02", "v"),
        ("1.1", "Lý do lựa chọn và tính cấp thiết của đề tài kiểm thử tự động ứng dụng Desktop", "3"),
        ("2.1", "Phân loại các cấp độ kiểm thử phần mềm và mức độ khả thi tự động hóa", "5"),
        ("2.2", "Đánh giá ưu điểm và hạn chế của phương pháp Record & Playback", "7"),
        ("2.3", "Thiết kế tập dữ liệu kiểm thử điều khiển bằng dữ liệu (DDT) cho chức năng Đăng nhập", "11"),
        ("2.4", "Phân loại các hình thức Checkpoint xác minh trong kiểm thử Desktop", "12"),
        ("2.5", "Cơ chế hiện thực mô hình Page Object Model trên các công cụ kiểm thử", "9"),
        ("2.6", "Phân tích ưu điểm và nhược điểm khi áp dụng mô hình Page Object Model", "10"),
        ("2.7", "Các biểu hiện thực tế đặc trưng của hiện tượng Flaky Test", "13"),
        ("2.8", "Phân tích các nhóm nguyên nhân gốc rễ dẫn đến Flaky Test trên Desktop", "13"),
        ("2.9", "Các biện pháp kỹ thuật nhằm phát hiện, cô lập và giảm thiểu Flaky Test", "14"),
        ("2.10", "Bộ tiêu chí đối chiếu phân biệt giữa Flaky Test và Lỗi thực sự của ứng dụng", "14"),
        ("2.11", "So sánh chi tiết các cơ chế chờ và đồng bộ hóa giao diện (Synchronization & Waits)", "14"),
        ("2.12", "Phân loại các dạng Test Oracle và nguồn dữ liệu đối chiếu kết quả mong đợi", "15"),
        ("2.13", "Các kịch bản và cơ chế xử lý ngoại lệ trong kiểm thử phục hồi lỗi Desktop", "16"),
        ("3.1", "Ma trận so sánh 6 công cụ kiểm thử tự động Desktop phổ biến năm 2026", "19"),
        ("4.1", "Bảng phân tích giá trị biên (BVA) cho hai trường nhập số A và số B", "25"),
        ("4.2", "Thiết kế 12 ca kiểm thử phân tích giá trị biên (BVA) cho chức năng Tính tổng", "25"),
        ("5.1", "Danh sách định danh UI Automation (Accessibility ID) của các phần tử trên MiniSum", "31"),
        ("6.1", "Ma trận so sánh định tính toàn diện giữa Katalon Studio và WinAppDriver (10 tiêu chí)", "37"),
        ("6.2", "Bảng so sánh định lượng hiệu năng thực thi kiểm thử trên ứng dụng MiniSum", "38"),
        ("6.3", "Bảng phân tích chi phí sở hữu tổng thể (TCO) ước tính cho nhóm dự án 5 người trong 3 năm", "39"),
        ("7.1", "Kết quả đo lường định lượng hiệu quả sinh mã kiểm thử của các mô hình AI", "44"),
        ("8.1", "Bảng phân bổ thời gian thực hành cá nhân 30 phút tại lớp", "47"),
        ("8.2", "Bảng barem chấm điểm chi tiết bài tập thực hành cá nhân (Thang điểm 10)", "49")
    ]
    
    tbl_lot = doc.add_table(rows=len(lot_data), cols=3)
    tbl_lot.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, (num, title, page) in enumerate(lot_data):
        row = tbl_lot.rows[idx]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width = Inches(0.8)
        c1.width = Inches(5.1)
        c2.width = Inches(0.6)
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(2)
        p0.paragraph_format.space_after = Pt(1)
        r0 = p0.add_run(f'Bảng {num}')
        r0.font.name = 'Times New Roman'
        r0.font.size = Pt(10)
        r0.bold = True
        r0.font.color.rgb = RGBColor(0, 45, 156)
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(2)
        p1.paragraph_format.space_after = Pt(1)
        r1 = p1.add_run(title)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(10)
        
        p2 = c2.paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p2.paragraph_format.space_before = Pt(2)
        p2.paragraph_format.space_after = Pt(1)
        r2 = p2.add_run(page)
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(10)
    
    doc.add_page_break()
    
    # 3. Danh sách hình vẽ
    p_lof_title = doc.add_paragraph()
    p_lof_title.paragraph_format.space_before = Pt(10)
    p_lof_title.paragraph_format.space_after = Pt(14)
    r = p_lof_title.add_run('Danh sách hình vẽ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(18)
    r.bold = True
    
    lof_data = [
        ("1", "Sơ đồ kiến trúc kiểm thử tự động ứng dụng Desktop", "4"),
        ("2", "Quy trình Record & Playback và cơ chế ánh xạ phần tử Windows UIA", "6"),
        ("3", "Mô hình thiết kế kiểm thử Page Object Model (POM) cho ứng dụng Desktop", "8"),
        ("4", "Giao diện ứng dụng mẫu MiniSum (Màn hình Đăng nhập và Màn hình Tính tổng)", "10"),
        ("5", "Không gian làm việc và Object Repository trong Katalon Studio", "21"),
        ("6", "Thực thi kịch bản Record & Playback và xác minh Checkpoint trên Katalon Studio", "23"),
        ("7", "Báo cáo HTML Report kết quả thực thi kiểm thử trên Katalon Studio", "26"),
        ("8", "Kiến trúc điều khiển của WinAppDriver và Windows Application Driver", "29"),
        ("9", "Mã nguồn kịch bản C# NUnit POM và cây thực thi Test Explorer", "32"),
        ("10", "Quy trình Prompt Engineering 2 pha ứng dụng AI trong Desktop Automation", "43"),
        ("11", "Biểu đồ so sánh thời gian phát triển kịch bản kiểm thử giữa 3 phương pháp", "44")
    ]
    
    tbl_lof = doc.add_table(rows=len(lof_data), cols=3)
    tbl_lof.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, (num, title, page) in enumerate(lof_data):
        row = tbl_lof.rows[idx]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width = Inches(0.8)
        c1.width = Inches(5.1)
        c2.width = Inches(0.6)
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(2)
        p0.paragraph_format.space_after = Pt(1)
        r0 = p0.add_run(f'Hình {num}')
        r0.font.name = 'Times New Roman'
        r0.font.size = Pt(10)
        r0.bold = True
        r0.font.color.rgb = RGBColor(0, 45, 156)
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(2)
        p1.paragraph_format.space_after = Pt(1)
        r1 = p1.add_run(title)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(10)
        
        p2 = c2.paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p2.paragraph_format.space_before = Pt(2)
        p2.paragraph_format.space_after = Pt(1)
        r2 = p2.add_run(page)
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(10)
    
    doc.add_page_break()
    
    # ================= OVERVIEW & TABLE 0.1 =================
    p_ov1 = doc.add_paragraph()
    p_ov1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ov1.paragraph_format.space_before = Pt(10)
    p_ov1.paragraph_format.space_after = Pt(4)
    r = p_ov1.add_run('BÁO CÁO TOÀN VĂN CHUYÊN ĐỀ SEMINAR\nAUTOMATION TESTING FOR DESKTOP APPLICATIONS')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.bold = True
    r.font.color.rgb = RGBColor(0, 45, 156)
    
    p_ov2 = doc.add_paragraph()
    p_ov2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ov2.paragraph_format.space_before = Pt(0)
    p_ov2.paragraph_format.space_after = Pt(14)
    r = p_ov2.add_run('Tự Động Hóa Kiểm Thử Cho Ứng Dụng Desktop (Windows)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.italic = True
    
    meta_box = """• Môn học: Software Testing (Kiểm thử phần mềm)
• Bộ môn: Kiểm thử phần mềm
• Khoa: Công nghệ Thông tin – Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
• Nhóm thực hiện: Nhóm 02
• Học kỳ: HK1 – Năm học 2026-2027
• Thời gian nộp bài: 30/10/2026 (Hạn chót giảng viên: 31/10/2026)"""
    add_blockquote(doc, meta_box)
    
    p_contrib_h = doc.add_paragraph()
    p_contrib_h.paragraph_format.space_before = Pt(14)
    p_contrib_h.paragraph_format.space_after = Pt(8)
    r = p_contrib_h.add_run('THÀNH VIÊN VÀ ĐÁNH GIÁ ĐÓNG GÓP THỰC TẾ (LẦN 2)')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.bold = True
    
    # Table 0.1
    tbl01_data = [
        ["STT", "Họ và Tên", "MSSV", "Vai trò chính Lần 2", "Đóng góp thực tế", "% Chốt", "Trạng thái"],
        ["1", "Phan Trung Tín", "23120372", "Trưởng nhóm (Team Lead)\nPhát triển 3 bản MiniSum.exe, viết lý thuyết POM/Flaky/Wait/Oracle, thiết kế toàn bộ Slide (v1+v2), Handout bài tập, tích hợp báo cáo & đóng gói", "42.0h (22 tasks)", "25.0%", "Hoàn thành xuất sắc"],
        ["2", "Nguyễn Lê Quang Kan", "23120279", "Chuyên trách Katalon Studio\nThực nghiệm 3 demo Katalon, viết Custom Keyword LoginKeyword.groovy, Data-Driven BVA, 16 ảnh thực nghiệm, video YouTube", "30.0h (18 tasks)", "25.0%", "Hoàn thành xuất sắc"],
        ["3", "Bùi Quang Tùng", "20120397", "Chuyên trách WinAppDriver\nThực nghiệm WinAppDriver + C# NUnit, cài đặt Page Object Model (POM), DDT 12 ca BVA, chụp ảnh kiểm thử, video YouTube", "24.0h (21 tasks)", "25.0%", "Hoàn thành tốt"],
        ["4", "Trần Vũ Quang", "23120346", "Chuyên trách AI & Comparison\nPrompt Engineering, sinh 19 ca BVA, test suite C# ai-winappdriver, số liệu đo đạc so sánh định lượng, video YouTube", "24.0h (17 tasks)", "25.0%", "Hoàn thành tốt"],
        ["Tổng", "", "", "", "120.0h (78 tasks)", "100.0%", ""]
    ]
    
    tbl01 = doc.add_table(rows=len(tbl01_data), cols=7)
    tbl01.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl01, color="000000", sz="4")
    
    col_w = [Inches(0.4), Inches(1.3), Inches(0.8), Inches(2.2), Inches(0.9), Inches(0.55), Inches(0.9)]
    for r_idx, row in enumerate(tbl01.rows):
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        if r_idx == 0:
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_w[c_idx]
            val = tbl01_data[r_idx][c_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            
            if r_idx == 0:
                set_cell_shading(cell, "F0F4F8")
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(val)
                r.font.name = 'Times New Roman'
                r.font.size = Pt(9.5)
                r.bold = True
            elif r_idx == len(tbl01_data) - 1:
                set_cell_shading(cell, "F7F7F7")
                r = p.add_run(val)
                r.font.name = 'Times New Roman'
                r.font.size = Pt(9.5)
                r.bold = True
                if c_idx in [0, 4, 5]:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                if c_idx in [0, 2, 5]:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(val)
                r.font.name = 'Times New Roman'
                r.font.size = Pt(9)
                if c_idx == 1:
                    r.bold = True
    
    add_caption_paragraph(doc, "Bảng 0.1: Phân công vai trò và tỷ lệ đóng góp thực tế của các thành viên Nhóm 02", "bảng")
    
    doc.add_page_break()
    
    # ================= PROCESS CHAPTERS 1 TO 9 =================
    with open('docs/report_v2.md', 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    intro_end = md_text.find('# 1. Giới Thiệu & Bối Cảnh (Introduction)')
    if intro_end != -1:
        content_md = md_text[intro_end:]
    else:
        content_md = md_text
    
    lines = content_md.split('\n')
    i = 0
    in_code = False
    code_lines = []
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check code fence
        if stripped.startswith('```'):
            if in_code:
                code_text = '\n'.join(code_lines)
                add_code_block(doc, code_text)
                in_code = False
                code_lines = []
            else:
                in_code = True
                code_lines = []
            i += 1
            continue
        
        if in_code:
            code_lines.append(line)
            i += 1
            continue
        
        # Blank line
        if not stripped:
            i += 1
            continue
        
        # HTML comment or tag to ignore
        if stripped.startswith('<!--') or stripped == '</div>':
            i += 1
            continue
        
        # Captions
        if stripped.startswith('<p class="table-caption">') or stripped.startswith('<p class="figure-caption">'):
            add_caption_paragraph(doc, stripped)
            i += 1
            continue
        
        # Headings
        if stripped.startswith('#'):
            h_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
            if h_match:
                level = len(h_match.group(1))
                h_text = h_match.group(2).strip()
                h_text = re.sub(r'<a\s+[^>]*id="[^"]*"[^>]*><\/a>', '', h_text).strip()
                
                h_para = doc.add_heading('', level=min(level, 4))
                if level == 1:
                    h_para.paragraph_format.space_before = Pt(24)
                    h_para.paragraph_format.space_after = Pt(12)
                    h_para.paragraph_format.page_break_before = True
                    r = h_para.add_run(h_text)
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(16)
                    r.bold = True
                    r.font.color.rgb = RGBColor(0, 45, 156)
                elif level == 2:
                    h_para.paragraph_format.space_before = Pt(16)
                    h_para.paragraph_format.space_after = Pt(6)
                    r = h_para.add_run(h_text)
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(13)
                    r.bold = True
                    r.font.color.rgb = RGBColor(0, 0, 0)
                elif level == 3:
                    h_para.paragraph_format.space_before = Pt(12)
                    h_para.paragraph_format.space_after = Pt(4)
                    r = h_para.add_run(h_text)
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(11.5)
                    r.bold = True
                    r.font.color.rgb = RGBColor(0, 0, 0)
                else:
                    h_para.paragraph_format.space_before = Pt(8)
                    h_para.paragraph_format.space_after = Pt(2)
                    r = h_para.add_run(h_text)
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(11)
                    r.bold = True
                    r.italic = True
                
                i += 1
                continue
        
        # Markdown Image: ![Alt](Src)
        img_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)$', stripped)
        if img_match:
            alt = img_match.group(1)
            src = img_match.group(2).strip()
            img_path = find_image(src)
            if img_path and os.path.exists(img_path):
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(10)
                p.paragraph_format.space_after = Pt(4)
                try:
                    with Image.open(img_path) as im:
                        w, h = im.size
                    target_w = min(Inches(5.8), Inches(w / 120.0))
                    if target_w < Inches(3.0):
                        target_w = Inches(3.5)
                    p.add_run().add_picture(img_path, width=target_w)
                except Exception as e:
                    print(f"Error adding picture {img_path}: {e}")
            else:
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(f'[{alt}]')
                r.italic = True
            i += 1
            continue
        
        # Markdown Table: begins with |
        if stripped.startswith('|') and stripped.endswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|') and lines[i].strip().endswith('|'):
                table_lines.append(lines[i].strip())
                i += 1
            
            if len(table_lines) >= 2:
                rows_data = []
                for t_line in table_lines:
                    if re.match(r'^\|(?:\s*:?-+:?\s*\|)+$', t_line):
                        continue
                    cols = [c.strip() for c in t_line.strip('|').split('|')]
                    rows_data.append(cols)
                
                if rows_data:
                    num_cols = max(len(r) for r in rows_data)
                    tbl = doc.add_table(rows=len(rows_data), cols=num_cols)
                    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
                    set_table_borders(tbl, color="000000", sz="4")
                    
                    for r_idx, r_data in enumerate(rows_data):
                        row = tbl.rows[r_idx]
                        trPr = row._tr.get_or_add_trPr()
                        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
                        if r_idx == 0:
                            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
                        
                        for c_idx in range(num_cols):
                            cell = row.cells[c_idx]
                            cell_val = r_data[c_idx] if c_idx < len(r_data) else ""
                            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
                            
                            p = cell.paragraphs[0]
                            p.paragraph_format.space_before = Pt(2)
                            p.paragraph_format.space_after = Pt(2)
                            p.paragraph_format.line_spacing = 1.15
                            
                            if r_idx == 0:
                                set_cell_shading(cell, "F0F4F8")
                                add_inline_runs(p, cell_val, base_font='Times New Roman', base_size=Pt(9.5))
                                for r in p.runs:
                                    r.bold = True
                            else:
                                if r_idx % 2 == 1:
                                    set_cell_shading(cell, "FFFFFF")
                                else:
                                    set_cell_shading(cell, "FAFAFA")
                                add_inline_runs(p, cell_val, base_font='Times New Roman', base_size=Pt(9))
            continue
        
        # Blockquote: begins with >
        if stripped.startswith('>'):
            bq_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                bq_lines.append(re.sub(r'^>\s?', '', lines[i].strip()))
                i += 1
            add_blockquote(doc, '\n'.join(bq_lines))
            continue
        
        # Horizontal rule: ---
        if stripped in ['---', '***', '___']:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            r = p.add_run('―' * 50)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(8)
            r.font.color.rgb = RGBColor(203, 213, 225)
            i += 1
            continue
        
        # Bullet list: starts with - or *
        list_match = re.match(r'^(\s*)([-*]|\d+\.)\s+(.+)$', line)
        if list_match:
            indent_str = list_match.group(1)
            marker = list_match.group(2)
            item_text = list_match.group(3)
            
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.3
            
            indent_level = len(indent_str) // 2
            p.paragraph_format.left_indent = Inches(0.25 * (indent_level + 1))
            
            if marker in ['-', '*']:
                bullet_char = '• ' if indent_level == 0 else '◦ '
                r_mark = p.add_run(bullet_char)
                r_mark.font.name = 'Times New Roman'
                r_mark.font.size = Pt(11)
            else:
                r_mark = p.add_run(f'{marker} ')
                r_mark.font.name = 'Times New Roman'
                r_mark.font.size = Pt(11)
                r_mark.bold = True
            
            add_inline_runs(p, item_text, base_font='Times New Roman', base_size=Pt(11.5))
            i += 1
            continue
        
        # Regular paragraph
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.35
        add_inline_runs(p, stripped, base_font='Times New Roman', base_size=Pt(11.5))
        i += 1
    
    # Save documents
    target_docs = [
        os.path.abspath('seminar-final.docx'),
        os.path.abspath('docs/report_v2.docx')
    ]
    for path in target_docs:
        doc.save(path)
        print(f"Successfully generated {path}! File size: {os.path.getsize(path):,} bytes")

if __name__ == '__main__':
    print("Exporting Word Document (.docx)...")
    build_docx_report()
