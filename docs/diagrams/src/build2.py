# -*- coding: utf-8 -*-
"""Diagrams 06-11 (v2)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit import *  # noqa

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)


# --------------------------------------------------------------------------- 06
def d06():
    f = Fig()
    parts = [
        ("Kịch bản Kiểm thử", "(Groovy / Java)", BLUE, BLUE_FILL, BLUE_DEEP),
        ("Katalon Test Engine", "(Appium Client)", BLUE, BLUE_FILL, BLUE_DEEP),
        ("Microsoft WinAppDriver", "(Port 4723)", BLUE, BLUE_FILL, BLUE_DEEP),
        ("Windows UI Automation", "(UIA)", BLUE, BLUE_FILL, BLUE_DEEP),
        ("Ứng dụng Desktop", "(WPF / MiniSum.exe)", GREEN, GREEN_FILL, GREEN),
    ]
    n = len(parts)
    pw = 344
    gap = (W - 2 * M - n * pw) / (n - 1)
    centers = [M + pw / 2 + i * (pw + gap) for i in range(n)]
    hy, hh = 24, 152

    def header():
        for i, (name, sub, col, fill, dark) in enumerate(parts):
            nl = wrap(name, 29, pw - 40, "semi")
            f.rect(centers[i] - pw / 2, hy, pw, hh, fill=fill, stroke=col, sw=3, rx=10)
            f.block(centers[i], hy + 22, nl, 29, "semi", dark, "middle", 38)
            f.text(centers[i], hy + hh - 26, sub, 24, "reg", BODY, "middle")

    header()

    msgs = [
        ("note", "1. Khởi tạo phiên kiểm thử (Session Initialization)"),
        (0, 1, "startApplicationWithTitle(appPath, title)", 0),
        (1, 2, "HTTP POST /session (DesiredCapabilities: app, platformName)", 0),
        (2, 4, "Kích hoạt tiến trình (Process Launch)", 0),
        (2, 3, "Quét tìm Top-Level Window có Name = title (HWND)", 0),
        (3, 2, "Trả về Window Handle (HWND)", 1),
        (2, 1, "HTTP 200 OK (Session ID: GUID)", 1),
        ("note", "2. Tương tác & định vị phần tử (Element Interaction)"),
        (0, 1, "sendKeys(findWindowsObject('txtUser'), 'admin')", 0),
        (1, 2, "HTTP POST /session/{id}/element (using: accessibility id, value: txtUser)", 0),
        (2, 3, 'FindFirst(TreeScope_Descendants, AutomationId == "txtUser")', 0),
        (3, 2, "UIA Element Reference", 1),
        (2, 1, "HTTP 200 OK (Element ID)", 1),
        (1, 2, "HTTP POST /session/{id}/element/{elId}/value (Keys: 'admin')", 0),
        (2, 3, "SetValue / SendInput (Gửi bàn phím ảo)", 0),
        (3, 4, "Cập nhật văn bản trong ô txtUser", 0),
        ("note", "3. Kiểm tra trạng thái & đóng phiên (Verification & Teardown)"),
        (0, 1, "getAttribute(findWindowsObject('lblMessage'), 'Name')", 0),
        (1, 2, "HTTP GET /session/{id}/element/{elId}/attribute/Name", 0),
        (2, 3, "GetCurrentPropertyValue(UIA_NamePropertyId)", 0),
        (3, 2, '"Đăng nhập thành công!"', 1),
        (2, 1, "HTTP 200 OK (Value)", 1),
        (0, 1, "closeApplication()", 0),
        (1, 2, "HTTP DELETE /session/{id}", 0),
        (2, 4, "Hủy tiến trình / Giải phóng Window Handle", 0),
        (2, 1, "HTTP 200 OK", 1),
    ]

    # --- pre-compute rows so the lifelines know where to stop
    rows = []
    y = hy + hh + 34
    top = y
    for m in msgs:
        if m[0] == "note":
            rows.append(("note", m[1], y))
            y += 56 + 26
        else:
            src, dst, label, dashed = m
            x1, x2 = centers[src], centers[dst]
            span = abs(x2 - x1)
            lw = min(760, max(524, span + 140))
            lines = wrap(label, 26, lw)
            rows.append(("msg", (src, dst, lines, dashed), y))
            y += 34 * len(lines) + 10 + 30
    bottom = y - 16

    # lifelines first
    for c in centers:
        f.line(c, hy + hh, c, bottom, stroke="#D5DAE2", sw=2, dash="6 8", marker=False)

    # messages
    for kind, payload, yy in rows:
        if kind == "note":
            f.rect(M, yy, W - 2 * M, 56, fill="#EDF1F6", stroke="#D8E0EA", sw=2, rx=8)
            f.text(M + 22, yy + 28, payload, 28, "semi", BLUE_DEEP, "start")
            continue
        src, dst, lines, dashed = payload
        x1, x2 = centers[src], centers[dst]
        wmax = max(tw(l, 26) for l in lines)
        cx = (x1 + x2) / 2
        f.rect(cx - wmax / 2 - 10, yy - 6, wmax + 20, 34 * len(lines) + 12,
               fill="#FFFFFF", stroke="none", rx=4)
        f.block(cx, yy, lines, 26, "reg", MUTED if dashed else BODY, "middle", 34)
        yline = yy + 34 * len(lines) + 10
        f.line(x1, yline, x2, yline, stroke=MUTED if dashed else BODY,
               sw=2.6 if dashed else 3, dash="9 7" if dashed else None)

    header()
    for i, (name, sub, col, fill, dark) in enumerate(parts):
        f.rect(centers[i] - 12, bottom - 8, 24, 10, fill=col, stroke="none", rx=2)
    return f.render(os.path.join(OUT, "06-sequence-kien-truc-thi-hanh.png"))


# --------------------------------------------------------------------------- 07
def d07():
    f = Fig()
    steps = [
        ("1", "Khởi động WinAppDriver", "Dịch vụ lắng nghe tại cổng 4723"),
        ("2", "Mở Windows Object Spy", "Trên thanh công cụ Katalon"),
        ("3", "Cấu hình AUT", "Chọn ứng dụng mục tiêu cần soi"),
        ("4", "Bắt phần tử (Capture)", "Nhấn Alt + ` để khóa đối tượng"),
        ("5", "Tinh chỉnh & Verify", "Chọn thuộc tính + Highlight"),
        ("6", "Lưu vào Object Repository", "Sinh file .wrs cho Test Case"),
    ]
    bw, gap, bh = 540, 88, 200
    x0 = (W - (3 * bw + 2 * gap)) / 2
    rows = [steps[0:3], steps[3:6]]
    ys = [26, 26 + bh + 84]
    for r, row in enumerate(rows):
        y = ys[r]
        for i, (num, title, sub) in enumerate(row):
            x = x0 + i * (bw + gap)
            f.rect(x, y, bw, bh, fill="#FFFFFF", stroke=BLUE, sw=2.6, rx=12)
            f.rect(x, y, 10, bh, fill=BLUE, stroke="none", rx=5)
            f.rect(x + 34, y + 30, 60, 60, fill=BLUE, stroke="none", rx=30)
            f.text(x + 64, y + 60, num, 32, "semi", "#FFFFFF", "middle")
            tl = wrap(title, 33, bw - 130, "semi")
            f.block(x + 112, y + 26, tl, 33, "semi", INK, "start", 40)
            sl = wrap(sub, 27, bw - 150)
            f.block(x + 112, y + 30 + 40 * len(tl) + 10, sl, 27, "reg", MUTED, "start", 36)
            if i < 2:
                f.line(x + bw + 6, y + bh / 2, x + bw + gap - 6, y + bh / 2, sw=3.4)
    x3 = x0 + 2 * (bw + gap) + bw / 2
    x4 = x0 + bw / 2
    ymid = ys[0] + bh + 40
    f.raw('<path d="M %.1f %.1f V %.1f H %.1f" fill="none" stroke="%s" stroke-width="3.4"/>'
          % (x3, ys[0] + bh, ymid, x4, BODY))
    f.line(x4, ymid, x4, ys[1] - 1, sw=3.4)
    return f.render(os.path.join(OUT, "07-quy-trinh-object-spy.png"))


# --------------------------------------------------------------------------- 08
def d08():
    f = Fig()
    f.rect(505, 24, 940, 100, fill=BLUE, stroke="none", rx=12)
    f.text(975, 58, "Test Suite Collection (TSC)", 34, "semi", "#FFFFFF", "middle")
    f.text(975, 96, "Điều phối đa môi trường · chạy song song hoặc tuần tự", 26, "reg", "#CFE3F6", "middle")

    f.rect(420, 200, 1140, 420, fill="#FCFAFF", stroke=PURPLE, sw=2.6, rx=14, dash="12 9")

    l1 = 250
    f.rect(500, l1, 520, 120, fill=BLUE_FILL, stroke=BLUE, sw=3, rx=10)
    f.text(760, l1 + 44, "Test Suite: Smoke / BVA", 31, "semi", BLUE_DEEP, "middle")
    f.text(760, l1 + 86, "(Data Binding, Iteration)", 26, "reg", BLUE, "middle")

    f.rect(1080, l1, 460, 120, fill=BLUE_FILL, stroke=BLUE, sw=3, rx=10)
    f.text(1310, l1 + 44, "Test Suite: Regression", 31, "semi", BLUE_DEEP, "middle")
    f.text(1310, l1 + 86, "(chạy lại toàn bộ)", 26, "reg", BLUE, "middle")

    l2 = 450
    for x, t, s in [(500, "Test Case 1", "Login Success"),
                    (855, "Test Case 2", "Login Failed"),
                    (1210, "Test Case 3", "BVA Calculation")]:
        f.rect(x, l2, 320, 116, fill="#FFFFFF", stroke=GRAY_STROKE, sw=2.6, rx=10)
        f.text(x + 160, l2 + 42, t, 30, "semi", INK, "middle")
        f.text(x + 160, l2 + 82, s, 25, "reg", MUTED, "middle")

    f.rect(36, l1, 280, 120, fill=AMBER_FILL, stroke=AMBER, sw=2.6, rx=10)
    f.text(176, l1 + 44, "Test Data", 30, "semi", AMBER, "middle")
    f.text(176, l1 + 84, "(Excel / CSV)", 25, "reg", AMBER, "middle")

    orx, ory = 855, 706
    f.rect(orx, ory, 320, 100, fill=GREEN_FILL, stroke=GREEN, sw=2.6, rx=10)
    f.text(orx + 160, ory + 40, "Object Repository", 29, "semi", GREEN, "middle")
    f.text(orx + 160, ory + 76, "(.wrs)", 25, "reg", GREEN, "middle")

    f.line(760, 124, 760, l1 - 1)
    f.line(1310, 124, 1310, l1 - 1)

    f.line(316, l1 + 60, 500, l1 + 60, dash="10 8", stroke=AMBER)
    f.label(408, l1 + 32, ["Data Binding"], 23, AMBER)

    bus = l2 - 20
    f.line(620, l1 + 120, 620, bus, marker=False)
    f.line(620, bus, 1330, bus, marker=False)
    for cx in (620, 1015, 1330):
        f.line(cx, bus, cx, l2 - 1)

    # Regression suite also runs Test Case 1: enter it from the left edge
    f.raw('<path d="M 1400 %.1f V %.1f H 470 V 508 H %.1f" fill="none" stroke="%s" '
          'stroke-width="3" marker-end="url(#ah)"/>' % (l1 + 120, bus - 44, 499, BODY))

    merge = ory - 40
    for cx in (620, 1015, 1330):
        f.line(cx, l2 + 116, cx, merge, marker=False, sw=3)
    f.line(620, merge, 1330, merge, marker=False)
    f.line(1015, merge, 1015, ory - 1, sw=3)

    f.text(W / 2, 856, "Vùng nét đứt: Test Listener (Hook AOP @Before / @After / Auto Screenshot) "
                       "— lắng nghe & can thiệp sự kiện của Suite và Test Case",
           24, "reg", PURPLE, "middle")
    return f.render(os.path.join(OUT, "08-cau-truc-du-an-katalon.png"))


# --------------------------------------------------------------------------- 09 / 11
def _demo_roadmap(fname, stages):
    f = Fig()
    bw, gap, bh = 540, 100, 216
    x0 = (W - (3 * bw + 2 * gap)) / 2
    y = 26
    for i, (head, lines) in enumerate(stages):
        x = x0 + i * (bw + gap)
        f.rect(x, y, bw, bh, fill="#FFFFFF", stroke=BLUE, sw=2.6, rx=12)
        f.rect(x, y, bw, 62, fill=BLUE, stroke="none", rx=12)
        f.rect(x, y + 46, bw, 16, fill=BLUE, stroke="none", rx=0)
        f.text(x + bw / 2, y + 31, head, 30, "semi", "#FFFFFF", "middle")
        yy = y + 92
        for ln in lines:
            f.rect(x + 36, yy + 10, 10, 10, fill=BLUE, stroke="none", rx=3)
            ll = wrap(ln, 28, bw - 110)
            f.block(x + 62, yy, ll, 28, "reg", BODY, "start", 38)
            yy += 40 * len(ll) + 22
        if i < 2:
            f.line(x + bw + 8, y + bh / 2, x + bw + gap - 8, y + bh / 2, sw=3.6)
    return f.render(os.path.join(OUT, fname))


def d09():
    return _demo_roadmap("09-demo-katalon-ba-buoc.png", [
        ("Demo 1 · Thiết lập", ["Cấu hình môi trường", "Nhận diện control"]),
        ("Demo 2 · Cơ bản", ["Record & Playback", "Gán Checkpoint"]),
        ("Demo 3 · Nâng cao", ["Data-Driven (BVA)", "Chuyển trạng thái"]),
    ])


def d11():
    return _demo_roadmap("11-demo-winappdriver-ba-buoc.png", [
        ("Demo 1 · Thiết lập", ["Khởi động driver", "Soi ID bằng UIA"]),
        ("Demo 2 · Cơ bản", ["Viết code Test Case", "Assertion + Chụp ảnh"]),
        ("Demo 3 · Nâng cao", ["Data-Driven BVA", "Đọc file Excel"]),
    ])


# --------------------------------------------------------------------------- 10
def d10():
    f = Fig()
    bw = 1160
    x = (W - bw) / 2
    y = 26
    layers = [
        ("Test Script (C# / NUnit hoặc Python / pytest)", "Dùng Appium / Selenium Client Library",
         GRAY_FILL, GRAY_STROKE, INK, BODY),
        ("Microsoft WinAppDriver.exe", "Lắng nghe tại 127.0.0.1:4723", BLUE_FILL, BLUE, BLUE_DEEP, BLUE),
        ("Windows UI Automation (UIA) Engine", None, TEAL_FILL, TEAL, TEAL, TEAL),
        ("Application Under Test (AUT)", "WPF, WinForms, UWP, Win32", GREEN_FILL, GREEN, GREEN, GREEN),
    ]
    labels = ["HTTP / JSON Wire / W3C WebDriver (Port 4723)",
              "Native API Calls (C++ / COM)",
              "Tương tác sự kiện hệ điều hành"]
    for i, (title, sub, fill, stroke, dark, subcol) in enumerate(layers):
        h = 128
        f.rect(x, y, bw, h, fill=fill, stroke=stroke, sw=3, rx=12)
        f.text(x + bw / 2, y + (52 if sub else h / 2), title, 34, "semi", dark, "middle")
        if sub:
            f.text(x + bw / 2, y + 96, sub, 27, "reg", subcol, "middle")
        y += h
        if i < len(layers) - 1:
            f.line(x + bw / 2, y, x + bw / 2, y + 96)
            lab = labels[i]
            lw = tw(lab, 25)
            lx = x + bw / 2 + 34
            f.rect(lx - 8, y + 32, lw + 16, 32, fill="#FFFFFF", stroke="none", rx=4)
            f.text(lx, y + 48, lab, 25, "reg", MUTED, "start")
            y += 96
    return f.render(os.path.join(OUT, "10-kien-truc-bon-tang-winappdriver.png"))


if __name__ == "__main__":
    for fn in (d06, d07, d08, d09, d11, d10):
        print(fn.__name__, fn())
