# -*- coding: utf-8 -*-
"""Diagrams 01-05."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit import *  # noqa

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)


def d01():
    f = Fig()
    root_w, root_h = 700, 104
    f.rect((W - root_w) / 2, 24, root_w, root_h, fill=BLUE, stroke="none", rx=14)
    f.text(W / 2, 24 + root_h / 2, "Desktop Applications", 44, "semi", "#FFFFFF", "middle")

    cols, gap = 3, 32
    cw = (W - 2 * M - (cols - 1) * gap) / cols
    centers = [M + cw / 2 + i * (cw + gap) for i in range(cols)]

    bus_y = 172
    f.line(W / 2, 24 + root_h, W / 2, bus_y, marker=False)
    f.line(centers[0], bus_y, centers[2], bus_y, marker=False)

    tree = [
        ("Ứng dụng bản địa thuần túy", "(Windows Native Apps)", BLUE_FILL, BLUE, BLUE_DEEP,
         ["Win32 / MFC (C++, giao diện Windows truyền thống)",
          "WinForms (.NET Framework, mô hình hướng sự kiện)",
          "WPF (Windows Presentation Foundation – kiến trúc XAML, DirectX)",
          "UWP (Universal Windows Platform – ứng dụng hiện đại từ Windows Store)"]),
        ("Ứng dụng đa nền tảng", "(Cross-Platform Native Apps)", TEAL_FILL, TEAL, TEAL,
         ["Qt (C++/QML, phổ biến trong hệ thống nhúng và công nghiệp)",
          "JavaFX / Swing (Java Virtual Machine)"]),
        ("Ứng dụng lai", "(Hybrid / Embedded Web Apps)", AMBER_FILL, AMBER, AMBER,
         ["Electron (Đóng gói Chromium + Node.js: VS Code, Slack, Teams)",
          ".NET MAUI / Blazor Hybrid (Kết hợp WebView2 và .NET)"]),
    ]

    top = 202
    for i, (name, sub, fill, stroke, dark, kids) in enumerate(tree):
        x = M + i * (cw + gap)
        f.line(centers[i], bus_y, centers[i], top - 1)
        nl = wrap(name, 34, cw - 44, "semi")
        f.rect(x, top, cw, 132, fill=fill, stroke=stroke, sw=3, rx=10)
        y = top + 20
        f.block(x + cw / 2, y, nl, 34, "semi", dark, "middle", 44)
        f.text(x + cw / 2, top + 132 - 34, sub, 27, "reg", stroke, "middle")

        cy = top + 132 + 64
        bx = x + 58
        bw = cw - 58
        spine = x + 28
        last_mid = cy
        mids = []
        for kid in kids:
            kl = wrap(kid, 30, bw - 44)
            h = 36 + 40 * len(kl)
            f.rect(bx, cy, bw, h, fill="#FFFFFF", stroke=GRAY_STROKE, sw=2.5, rx=8)
            f.block(bx + 22, cy + 18, kl, 30, "reg", BODY, "start", 40)
            mids.append(cy + h / 2)
            cy += h + 22
        last_mid = mids[-1]
        f.line(spine, top + 132, spine, last_mid, marker=False, sw=2.5, stroke=stroke)
        for m in mids:
            f.line(spine, m, bx - 1, m, sw=2.5, stroke=stroke)
    return f.render(os.path.join(OUT, "01-phan-loai-desktop-application.png"))


def d02():
    f = Fig()
    cx = W / 2
    bw = 1060
    y = 30
    steps = [
        ("Thực hiện hành động thao tác trên AUT", None),
        ("Trích xuất giá trị thực tế từ phần tử UI", "(Actual Value)"),
        ("So sánh đối chiếu với giá trị kỳ vọng", "(Expected Value)"),
    ]
    for title, sub in steps:
        tl = wrap(title, 38, bw - 60, "semi")
        h = 44 + 50 * len(tl) + (40 if sub else 0)
        f.rect(cx - bw / 2, y, bw, h, fill="#FFFFFF", stroke=GRAY_STROKE, sw=3, rx=10)
        f.block(cx, y + 22, tl, 38, "semi", INK, "middle", 50)
        if sub:
            f.text(cx, y + h - 26, sub, 28, "reg", MUTED, "middle")
        y += h
        if title != steps[-1][0]:
            f.line(cx, y, cx, y + 66)
            y += 66

    split_y = y + 44
    f.line(cx, y, cx, split_y, marker=False)
    lc, rc = 470, W - 470
    f.line(lc, split_y, rc, split_y, marker=False)
    f.line(lc, split_y, lc, split_y + 44)
    f.line(rc, split_y, rc, split_y + 44)

    bw2 = 700
    ytop = split_y + 46
    for cxx, title, sub, fill, stroke, dark in (
            (lc, "Khớp giá trị", "(Test Case PASS)", GREEN_FILL, GREEN, GREEN),
            (rc, "Không khớp giá trị", "(Test Case FAIL)", RED_FILL, RED, RED)):
        f.rect(cxx - bw2 / 2, ytop, bw2, 158, fill=fill, stroke=stroke, sw=3, rx=10)
        f.text(cxx, ytop + 58, title, 38, "semi", dark, "middle")
        f.text(cxx, ytop + 112, sub, 28, "reg", stroke, "middle")

    ay = ytop + 158 + 70
    f.line(rc, ytop + 158, rc, ay)
    items = ["Chụp ảnh màn hình tại thời điểm lỗi",
             "Ghi log chi tiết thông số và stacktrace",
             "Đánh dấu trạng thái lỗi vào báo cáo"]
    bw3 = 780
    f.rect(rc - bw3 / 2, ay, bw3, 40 + 46 * 3, fill=GRAY_FILL, stroke=GRAY_STROKE, sw=3, rx=10)
    for i, it in enumerate(items):
        f.text(rc - bw3 / 2 + 30, ay + 20 + 46 * i + 23, "•", 30, "reg", RED, "start")
        f.text(rc - bw3 / 2 + 56, ay + 20 + 46 * i + 23, it, 30, "reg", BODY, "start")
    return f.render(os.path.join(OUT, "02-luong-checkpoint.png"))


def d03():
    f = Fig()
    pw = 900
    panels = [
        (M, "Không dùng POM", RED, RED_FILL, "#FFFFFF",
         [("code", ["TC01_Login",
                    '  find("txtUser").sendKeys(u)',
                    '  find("txtPass").sendKeys(p)',
                    '  find("btnLogin").click()',
                    '  find("lblMessage").getText()'])],
         ["Locator rải khắp test case", "→ đổi UI phải sửa nhiều nơi"]),
        (W - M - pw, "Dùng POM", BLUE, BLUE_FILL, BLUE_FILL,
         [("code", ["TC01_Login", "  loginPage.Login(u, p)", "  Assert(lblMessage)"]),
          ("arrow", "gọi"),
          ("code", ["LoginPage", "  locator + Login()"])],
         ["Locator tập trung một nơi"]),
    ]

    # pre-compute heights
    def panel_height(items, caption):
        h = 34 + 54 + 26
        for kind, val in items:
            if kind == "code":
                h += 40 + 44 * len(val) + 22
            else:
                h += 66
        h += 26 + 44 * len(caption) + 30
        return h

    ph = max(panel_height(p[5], p[6]) for p in panels)
    for x, title, stroke, fill, codefill, items, caption in panels:
        f.rect(x, 26, pw, ph, fill=fill, stroke=stroke, sw=3, rx=14, dash=None)
        f.text(x + pw / 2, 26 + 58, title, 40, "semi", stroke, "middle")
        y = 26 + 34 + 54 + 20
        for kind, val in items:
            if kind == "code":
                h = 40 + 44 * len(val)
                f.rect(x + 44, y, pw - 88, h, fill="#FFFFFF", stroke=GRAY_STROKE, sw=2.5, rx=8)
                f.block(x + 68, y + 20, val, 29, "mono", BODY, "start", 44)
                y += h + 22
            else:
                f.line(x + pw / 2, y, x + pw / 2, y + 64)
                f.label(x + pw / 2 + 46, y + 32, [val], 26)
                y += 66
        f.block(x + pw / 2, y + 4, caption, 30, "reg", stroke, "middle", 44)
    return f.render(os.path.join(OUT, "03-so-sanh-pom.png"))


def d04():
    f = Fig()
    cx = W / 2
    y = 30
    bw = 1080
    f.rect(cx - bw / 2, y, bw, 100, fill="#FFFFFF", stroke=GRAY_STROKE, sw=3, rx=10)
    f.text(cx, y + 50, "Test Case: nhập A = 5, B = 7, nhấn TÍNH TỔNG", 38, "semi", INK, "middle")
    y += 100 + 70
    f.line(cx, y - 70, cx, y)

    f.rect(cx - bw / 2, y, bw, 148, fill=BLUE_FILL, stroke=BLUE, sw=3, rx=10)
    f.text(cx, y + 44, "Giá trị thực tế (Actual Value)", 30, "semi", BLUE_DEEP, "middle")
    f.text(cx, y + 100, 'lblResult = "Ket qua: 5 + 7 = 12"', 32, "mono", INK, "middle")
    y += 148

    split_y = y + 60
    f.line(cx, y, cx, split_y, marker=False)
    lc, rc = 500, W - 500
    f.line(lc, split_y, rc, split_y, marker=False)
    f.line(lc, split_y, lc, split_y + 52)
    f.line(rc, split_y, rc, split_y + 52)

    ytop = split_y + 54
    lw = 800
    f.rect(lc - lw / 2, ytop, lw, 190, fill=PURPLE_FILL, stroke=PURPLE, sw=3, rx=10)
    f.text(lc, ytop + 40, "Oracle: đặc tả quy tắc", 32, "semi", PURPLE, "middle")
    f.text(lc, ytop + 96, 'lblResult = "Ket qua: A + B = A+B"', 29, "mono", INK, "middle")
    f.text(lc, ytop + 148, "(derived oracle)", 27, "reg", PURPLE, "middle")

    f.rect(rc - lw / 2, ytop, lw, 190, fill=GRAY_FILL, stroke=GRAY_STROKE, sw=3, rx=10)
    f.text(rc, ytop + 40, "So sánh", 32, "semi", INK, "middle")
    f.text(rc, ytop + 96, "Expected  ⇄  Actual", 30, "reg", BODY, "middle")
    f.text(rc, ytop + 148, "(assert)", 27, "reg", MUTED, "middle")

    vy = ytop + 190 + 70
    f.line(lc, ytop + 190, lc, vy, marker=False)
    f.line(rc, ytop + 190, rc, vy, marker=False)
    f.line(lc, vy, rc, vy, marker=False)
    f.line(W / 2, vy, W / 2, vy + 40)

    vh, half = 112, 720
    vx = W / 2 - half
    vtop = vy + 42
    f.raw('<clipPath id="verdict"><rect x="%.1f" y="%.1f" width="%d" height="%d" rx="12"/>'
          '</clipPath>' % (vx, vtop, 2 * half, vh))
    f.rect(vx, vtop, 2 * half, vh, fill=GREEN_FILL, stroke="none", rx=12)
    f.raw('<rect x="%.1f" y="%.1f" width="%d" height="%d" fill="%s" clip-path="url(#verdict)"/>'
          % (W / 2, vtop, half, vh, RED_FILL))
    f.rect(vx, vtop, 2 * half, vh, fill="none", stroke=RULE, sw=3, rx=12)
    f.line(W / 2, vtop + 2, W / 2, vtop + vh - 2, stroke=RULE, sw=2, marker=False)
    f.text(vx + half / 2, vtop + vh / 2, "Khớp  →  PASS", 36, "semi", GREEN, "middle")
    f.text(vx + half + half / 2, vtop + vh / 2, "Không khớp  →  FAIL", 36, "semi", RED, "middle")
    return f.render(os.path.join(OUT, "04-luong-test-oracle.png"))


def d05():
    f = Fig()
    f.rect(M, 26, W - 2 * M, 92, fill=BLUE, stroke="none", rx=12)
    f.text(W / 2, 72, "BỘ TIÊU CHÍ ĐÁNH GIÁ CÔNG CỤ AUTOMATION TESTING CHO DESKTOP",
           38, "semi", "#FFFFFF", "middle")

    groups = [
        ("1", "NĂNG LỰC KỸ THUẬT", BLUE, BLUE_FILL, [
            "Hỗ trợ các công nghệ UI desktop",
            "Năng lực nhận diện đối tượng (UIA)",
            "Tính năng Record & Playback",
            "Khả năng Data-Driven Testing",
            "Hệ thống Checkpoint & Báo cáo"]),
        ("2", "KHẢ NĂNG SỬ DỤNG", TEAL, TEAL_FILL, [
            "Độ dốc học tập (Learning Curve)",
            "Chất lượng tài liệu và hướng dẫn",
            "Độ lớn cộng đồng hỗ trợ",
            "Khả năng tích hợp IDE (VS Code, VS)",
            "Độ tiện dụng của giao diện công cụ"]),
        ("3", "HIỆU NĂNG & TÍNH ỔN ĐỊNH", AMBER, AMBER_FILL, [
            "Tốc độ thực thi kịch bản",
            "Độ ổn định (chống flaky test)",
            "Cơ chế đồng bộ hóa (Wait handling)",
            "Mức tiêu hao tài nguyên hệ thống"]),
        ("4", "CHI PHÍ & GIÁ TRỊ ĐẦU TƯ", PURPLE, PURPLE_FILL, [
            "Bản quyền (Free / Commercial)",
            "Chi phí thiết lập môi trường ban đầu",
            "Chi phí đào tạo nhân sự",
            "Khả năng thu hồi vốn đầu tư (ROI)"]),
        ("5", "BẢO TRÌ & TÍNH LINH HOẠT", GREEN, GREEN_FILL, [
            "Khả năng chịu biến động UI",
            "Hỗ trợ mô hình thiết kế (POM)",
            "Tái sử dụng thành phần kịch bản",
            "Tương thích quản lý mã nguồn (Git)"]),
        ("6", "HỆ SINH THÁI & MỞ RỘNG", RED, RED_FILL, [
            "Khả năng mở rộng qua Plugin",
            "Tích hợp thư viện kiểm thử phổ biến",
            "Khả năng tích hợp CI/CD Pipelines",
            "Tính năng ứng dụng AI / Smart Testing"]),
    ]

    cols, gap = 3, 30
    cw = (W - 2 * M - (cols - 1) * gap) / cols
    rows_y = [26 + 92 + 34, None]

    cards = []
    for num, name, stroke, fill, bullets in groups:
        nl = wrap(name, 33, cw - 128, "semi")
        bl = []
        for b in bullets:
            bl.append(wrap(b, 28, cw - 108))
        h = 26 + max(62, 40 * len(nl)) + 20 + sum(40 * len(x) + 6 for x in bl) + 18
        cards.append((num, name, stroke, fill, nl, bl, h))

    for r in range(2):
        row = cards[r * 3:(r + 1) * 3]
        hmax = max(c[6] for c in row)
        for i, (num, name, stroke, fill, nl, bl, h) in enumerate(row):
            x = M + i * (cw + gap)
            y = rows_y[r]
            oy = (hmax - h) / 2
            f.rect(x, y, cw, hmax, fill="#FFFFFF", stroke=stroke, sw=2.5, rx=12)
            f.rect(x, y, cw, 8, fill=stroke, stroke="none", rx=4)
            f.rect(x + 26, y + oy + 30, 58, 58, fill=fill, stroke=stroke, sw=2.5, rx=10)
            f.text(x + 26 + 29, y + oy + 30 + 29, num, 32, "semi", stroke, "middle")
            f.block(x + 100, y + oy + 28, nl, 33, "semi", INK, "start", 40)
            by = y + oy + 28 + max(62, 40 * len(nl)) + 14
            for b in bl:
                f.text(x + 30, by + 20, "•", 28, "reg", stroke, "start")
                f.block(x + 52, by, b, 28, "reg", BODY, "start", 38)
                by += 40 * len(b) + 6
        if r == 0:
            rows_y[1] = rows_y[0] + hmax + 28
    return f.render(os.path.join(OUT, "05-bo-tieu-chi-6-nhom.png"))


if __name__ == "__main__":
    for fn in (d01, d02, d03, d04, d05):
        print(fn.__name__, fn())
