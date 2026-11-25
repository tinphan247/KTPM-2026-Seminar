# -*- coding: utf-8 -*-
"""Diagrams 12-15."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit import *  # noqa

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)


# --------------------------------------------------------------------------- 12
def d12():
    f = Fig()
    f.text(W / 2, 44, "So sánh thời gian hoàn thành bộ test suite", 40, "semi", INK, "middle")
    f.text(W / 2, 88, "Đơn vị: phút · cùng một phạm vi 12 ca kiểm thử BVA trên MiniSum",
           27, "reg", MUTED, "middle")

    name_w = 470
    tx0, tx1 = 560, 1880
    total = 120
    scale = (tx1 - tx0) / total
    axis_y = 150

    sections = [
        ("WinAppDriver thuần", "120 phút", AMBER, AMBER_FILL, [
            ("Phân tích BVA", 0, 25), ("Xây dựng POM C#", 25, 60),
            ("Viết kịch bản DDT", 60, 100), ("Debug & Run Pass", 100, 120)]),
        ("Katalon Studio", "90 phút", BLUE, BLUE_FILL, [
            ("Phân tích BVA", 0, 25), ("Spy & Object Repository", 25, 45),
            ("Record & Data Binding", 45, 75), ("Debug & Run Pass", 75, 90)]),
        ("WinAppDriver + AI", "29 phút", PURPLE, PURPLE_FILL, [
            ("Prompt sinh BVA", 0, 3), ("AI sinh POM", 3, 9),
            ("AI sinh Script DDT", 9, 17), ("Human Review & Debug", 17, 29)]),
    ]

    y = 190
    row_h = 46
    sec_h = 44 + 4 * row_h + 26
    axis_top, axis_bot = 130, y + 3 * sec_h - 26

    # gridlines first so the bars sit on top of them
    for m in range(0, total + 1, 10):
        gx = tx0 + m * scale
        f.raw('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#E4E7EC" '
              'stroke-width="1.6" stroke-dasharray="4 6"/>' % (gx, axis_top, gx, axis_bot))
        f.text(gx, axis_y, str(m), 23, "reg", MUTED, "middle")

    for sname, stotal, col, fill, tasks in sections:
        # section header
        f.rect(M, y, W - 2 * M, 44, fill=fill, stroke="none", rx=8)
        f.rect(M, y, 8, 44, fill=col, stroke="none", rx=4)
        f.text(M + 26, y + 22, sname, 28, "semi", col, "start")
        f.text(tx1, y + 22, "Tổng: " + stotal, 25, "semi", col, "end")
        y += 44

        for tname, a, b in tasks:
            cy = y + row_h / 2
            f.text(M + 26, cy, tname, 26, "reg", BODY, "start")
            bx = tx0 + a * scale
            bwid = max((b - a) * scale, 6)
            f.rect(bx, cy - 14, bwid, 28, fill=col, stroke="none", rx=5, opacity="0.85")
            dur = "%d′" % (b - a)
            if bwid > 90:
                f.text(bx + bwid / 2, cy, dur, 23, "semi", "#FFFFFF", "middle")
            else:
                f.text(bx + bwid + 12, cy, dur, 23, "reg", col, "start")
            y += row_h
        y += 26

    # axis line
    f.raw('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>'
          % (tx0, axis_bot + 6, tx1, axis_bot + 6, RULE))
    return f.render(os.path.join(OUT, "12-gantt-so-sanh-thoi-gian.png"))


# --------------------------------------------------------------------------- 13
def d13():
    f = Fig()
    bw, gap = 600, 30
    x0 = (W - (3 * bw + 2 * gap)) / 2

    f.rect((W - 760) / 2, 26, 760, 92, fill=BLUE, stroke="none", rx=12)
    f.text(W / 2, 72, "BÀN CÂN LỰA CHỌN GIẢI PHÁP", 34, "semi", "#FFFFFF", "middle")

    cards = [
        ("CHỌN KATALON STUDIO", BLUE, BLUE_FILL, [
            "Đội ngũ kiểm thử manual",
            "Cần chạy ngay, ít code",
            "Chấp nhận bản Free hạn chế",
            "Ưu tiên báo cáo có sẵn"]),
        ("CHỌN WINAPPDRIVER THUẦN", GRAY_STROKE.replace("#C9CFD8", "#5B6472"), GRAY_FILL, [
            "Đội ngũ SDET chuyên sâu",
            "Không được dùng AI đám mây (bảo mật tuyệt đối)",
            "Dự án nguồn mở 100%"]),
        ("WINAPPDRIVER + AI (TỐI ƯU)", PURPLE, PURPLE_FILL, [
            "Đội ngũ SDET muốn tối đa hóa năng suất",
            "Dự án lớn, cần mã sạch theo chuẩn POM",
            "Tiết kiệm 75% thời gian viết script",
            "Dự án CI/CD yêu cầu tốc độ thực thi cao"]),
    ]

    split = 26 + 92 + 66
    lc = x0 + bw / 2
    mc = x0 + bw + gap + bw / 2
    rc = x0 + 2 * (bw + gap) + bw / 2
    f.line(W / 2, 118, W / 2, split, marker=False)
    f.line(lc, split, rc, split, marker=False)
    for cx in (lc, mc, rc):
        f.line(cx, split, cx, split + 46)

    top = split + 48
    prepared = []
    for (title, col, fill, bullets), cx in zip(cards, (lc, mc, rc)):
        bl = [wrap(b, 27, bw - 90) for b in bullets]
        h = 26 + 46 + 20 + sum(40 * len(l) + 8 for l in bl) + 16
        prepared.append((cx, title, col, fill, bl, h))
    hmax = max(p[5] for p in prepared)
    for cx, title, col, fill, bl, h in prepared:
        x = cx - bw / 2
        f.rect(x, top, bw, hmax, fill="#FFFFFF", stroke=col, sw=2.6, rx=12)
        f.rect(x, top, bw, 62, fill=fill, stroke="none", rx=12)
        f.rect(x, top + 46, bw, 16, fill=fill, stroke="none")
        f.raw('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2.6"/>'
              % (x, top + 62, x + bw, top + 62, col))
        tl = wrap(title, 27, bw - 40, "semi")
        f.block(x + bw / 2, top + 12, tl, 27, "semi", col, "middle", 36)
        by = top + 82
        for l in bl:
            f.rect(x + 32, by + 11, 9, 9, fill=col, stroke="none", rx=3)
            f.block(x + 54, by, l, 27, "reg", BODY, "start", 38)
            by += 40 * len(l) + 8
    return f.render(os.path.join(OUT, "13-so-do-chon-giai-phap.png"))


# --------------------------------------------------------------------------- 14
def d14():
    f = Fig()
    f.rect(M, 26, W - 2 * M, 108, fill=BLUE, stroke="none", rx=12)
    f.text(W / 2, 58, "5 HƯỚNG ỨNG DỤNG AI TRONG DESKTOP AUTOMATION", 38, "semi", "#FFFFFF", "middle")
    f.text(W / 2, 104, "Trọng tâm thực nghiệm của Nhóm 02", 26, "reg", "#CFE3F6", "middle")

    items = [
        ("1", "AI Tự phục hồi Selector", "Self-Healing Locators", BLUE, BLUE_FILL),
        ("2", "Kiểm thử trực quan (Visual AI)", "Computer Vision / OpenCV", TEAL, TEAL_FILL),
        ("3", "AI Sinh kịch bản kiểm thử", "Test Script Generation", AMBER, AMBER_FILL),
        ("4", "AI Sinh dữ liệu kiểm thử", "Synthetic Test Data", PURPLE, PURPLE_FILL),
    ]
    cw = (W - 2 * M - 28) / 2
    ch = 150
    y0 = 26 + 108 + 34
    for i, (num, name, sub, col, fill) in enumerate(items):
        x = M + (i % 2) * (cw + 28)
        y = y0 + (i // 2) * (ch + 24)
        f.rect(x, y, cw, ch, fill="#FFFFFF", stroke=col, sw=2.6, rx=12)
        f.rect(x, y, 8, ch, fill=col, stroke="none", rx=4)
        f.rect(x + 34, y + 38, 74, 74, fill=fill, stroke=col, sw=2.4, rx=14)
        f.text(x + 71, y + 75, num, 38, "semi", col, "middle")
        f.block(x + 132, y + 40, wrap(name, 32, cw - 170, "semi"), 32, "semi", INK, "start", 40)
        f.text(x + 132, y + 108, sub, 26, "reg", col, "start")

    y5 = y0 + 2 * (ch + 24)
    f.rect(M, y5, W - 2 * M, 132, fill=GREEN_FILL, stroke=GREEN, sw=2.6, rx=12)
    f.rect(M, y5, 8, 132, fill=GREEN, stroke="none", rx=4)
    f.rect(M + 34, y5 + 30, 74, 74, fill="#FFFFFF", stroke=GREEN, sw=2.4, rx=14)
    f.text(M + 71, y5 + 67, "5", 38, "semi", GREEN, "middle")
    f.text(M + 132, y5 + 52, "Phân tích nguyên nhân lỗi tự động", 32, "semi", INK, "start")
    f.text(M + 132, y5 + 94, "Root Cause Analysis — đọc log, ảnh chụp và báo cáo để chỉ ra nguyên nhân gốc",
           26, "reg", GREEN, "start")
    return f.render(os.path.join(OUT, "14-nam-huong-ung-dung-ai.png"))


# --------------------------------------------------------------------------- 15
def d15():
    f = Fig()
    f.rect(M, 24, W - 2 * M, 96, fill="#F3F5F9", stroke=GRAY_STROKE, sw=2.6, rx=12)
    f.text(W / 2, 56, "CHUỖI THỰC NGHIỆM AI AUTOMATION CỦA NHÓM 02", 34, "semi", INK, "middle")
    f.text(W / 2, 94, "Trên ứng dụng mẫu MiniSum · hai demo nối tiếp nhau", 25, "reg", MUTED, "middle")

    bands = [
        ("AI DEMO 1", "Sinh test case & dữ liệu BVA", BLUE, BLUE_FILL, [
            ("Tài liệu đặc tả", "minisum-spec.md"),
            ("Prompt Few-Shot", "testcase-bva-prompt.md"),
            ("12 Test Cases BVA", "bva-testcases.xlsx")]),
        ("AI DEMO 2", "Sinh mã nguồn C# NUnit & xác minh trên WinAppDriver", PURPLE, PURPLE_FILL, [
            ("Prompt kiến trúc POM", "script-gen-prompt.md"),
            ("Script C# do GenAI sinh", "chatgpt-script-output.cs"),
            ("Xác minh chạy PASS", "verified-script.cs")]),
    ]

    nw, ngap = 470, 74
    x0 = (W - (3 * nw + 2 * ngap)) / 2
    y = 152
    for tag, sub, col, fill, nodes in bands:
        bh = 226
        f.rect(M, y, W - 2 * M, bh, fill="#FFFFFF", stroke=GRAY_STROKE, sw=2.2, rx=12)
        f.rect(M, y, 10, bh, fill=col, stroke="none", rx=5)
        f.text(M + 34, y + 34, tag, 27, "semi", col, "start")
        f.text(M + 34 + tw(tag, 27, "semi") + 14, y + 34, sub, 26, "reg", BODY, "start")
        for i, (name, fn) in enumerate(nodes):
            x = x0 + i * (nw + ngap)
            ny = y + 72
            f.rect(x, ny, nw, 120, fill=fill, stroke=col, sw=2.4, rx=10)
            f.block(x + nw / 2, ny + 22, wrap(name, 27, nw - 44, "semi"), 27, "semi", INK, "middle", 36)
            f.text(x + nw / 2, ny + 92, fn, 23, "mono", col, "middle")
            if i < 2:
                f.line(x + nw + 10, ny + 60, x + nw + ngap - 10, ny + 60, sw=3.2, stroke=col)
        y += bh + 24
    return f.render(os.path.join(OUT, "15-chuoi-thuc-nghiem-ai.png"))


if __name__ == "__main__":
    for fn in (d12, d13, d14, d15):
        print(fn.__name__, fn())
