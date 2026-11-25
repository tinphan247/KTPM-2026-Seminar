# -*- coding: utf-8 -*-
"""Diagrams 16-18: CI/CD pipeline, semi-automated flow, decision table."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit import *  # noqa

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)


# --------------------------------------------------------------------------- 16
def d16():
    f = Fig()
    f.rect(M, 24, W - 2 * M, 92, fill="#F3F5F9", stroke=GRAY_STROKE, sw=2.4, rx=12)
    f.text(W / 2, 56, "ĐƯỜNG ỐNG HOÀN TOÀN TỰ ĐỘNG", 34, "semi", INK, "middle")
    f.text(W / 2, 92, "Fully Automated Pipeline — từ commit tới thông báo kết quả", 25, "reg", MUTED, "middle")

    steps = ["Kích hoạt CI/CD", "Biên dịch mã", "Triển khai build",
             "Chạy Test Suite", "Xuất báo cáo", "Gửi thông báo"]
    n = len(steps)
    gap = 34
    bw = (W - 2 * M - (n - 1) * gap) / n
    y = 152
    bh = 176
    for i, s in enumerate(steps):
        x = M + i * (bw + gap)
        f.rect(x, y, bw, bh, fill=BLUE_FILL, stroke=BLUE, sw=2.6, rx=12)
        f.rect(x + bw / 2 - 26, y + 18, 52, 34, fill=BLUE, stroke="none", rx=17)
        f.text(x + bw / 2, y + 35, str(i + 1), 22, "semi", "#FFFFFF", "middle")
        lines = wrap(s, 29, bw - 30, "semi")
        f.block(x + bw / 2, y + 64, lines, 29, "semi", BLUE_DEEP, "middle", 40)
        if i < n - 1:
            f.line(x + bw + 6, y + bh / 2, x + bw + gap - 5, y + bh / 2, sw=3.2)
    yb = y + bh + 34
    f.rect((W - 1240) / 2, yb, 1240, 64, fill="#FFFFFF", stroke=BLUE, sw=2.2, rx=10, dash="10 8")
    f.text(W / 2, yb + 32, "Cả 6 khâu chạy tự động 100% — không có điểm dừng thủ công",
           26, "reg", BLUE, "middle")
    return f.render(os.path.join(OUT, "16-pipeline-tu-dong-hoan-toan.png"))


# --------------------------------------------------------------------------- 17
def d17():
    f = Fig()
    f.rect(M, 24, W - 2 * M, 92, fill="#F3F5F9", stroke=GRAY_STROKE, sw=2.4, rx=12)
    f.text(W / 2, 56, "QUY TRÌNH BÁN TỰ ĐỘNG", 34, "semi", INK, "middle")
    f.text(W / 2, 92, "Semi-Automated Flow — máy làm phần lặp lại, người giữ phần cảm quan", 25, "reg",
           MUTED, "middle")

    stages = [
        ("TỰ ĐỘNG", BLUE, BLUE_FILL,
         ["Tạo 50 bản ghi dữ liệu mẫu",
          "Mở sẵn form chỉnh sửa chi tiết"]),
        ("THỦ CÔNG", AMBER, AMBER_FILL,
         ["Tester kiểm tra độ mượt đồ họa, cảm quan giao diện",
          "và khả năng tương tác của form"]),
        ("TỰ ĐỘNG", BLUE, BLUE_FILL,
         ["Lưu log, chụp ảnh màn hình",
          "Cập nhật kết quả vào hệ thống quản lý test"]),
    ]
    cw = 1420
    x = (W - cw) / 2
    y = 152
    ch = 172
    for i, (tag, col, fill, lines) in enumerate(stages):
        f.rect(x, y, cw, ch, fill="#FFFFFF", stroke=col, sw=2.6, rx=12)
        f.rect(x, y, 10, ch, fill=col, stroke="none", rx=5)
        tagw = tw(tag, 22, "semi") + 40
        f.rect(x + 36, y + 24, tagw, 38, fill=col, stroke="none", rx=19)
        f.text(x + 36 + tagw / 2, y + 43, tag, 22, "semi", "#FFFFFF", "middle")
        f.block(x + 36, y + 78, lines, 28, "reg", BODY, "start", 40)
        y += ch
        if i < len(stages) - 1:
            f.line(x + cw / 2, y + 6, x + cw / 2, y + 60, sw=3.4)
            y += 66
    return f.render(os.path.join(OUT, "17-quy-trinh-ban-tu-dong.png"))


# --------------------------------------------------------------------------- 18
def d18():
    f = Fig()
    f.rect(M, 24, W - 2 * M, 92, fill=BLUE, stroke="none", rx=12)
    f.text(W / 2, 58, "BẢNG QUYẾT ĐỊNH ÁP DỤNG KIỂM THỬ TỰ ĐỘNG", 34, "semi", "#FFFFFF", "middle")
    f.text(W / 2, 96, "Khi nào nên — khi nào không nên chuyển sang automation", 25, "reg",
           "#CFE3F6", "middle")

    cols = [
        ("NÊN ÁP DỤNG AUTOMATION", GREEN, GREEN_FILL, [
            "Kịch bản lặp đi lặp lại nhiều lần",
            "Bộ kịch bản hồi quy quy mô lớn",
            "Kiểm thử cần số lượng dữ liệu lớn (DDT)",
            "Kịch bản chạy trên nhiều cấu hình OS",
            "Cần kết quả nhanh trong CI/CD",
            "Tính năng nghiệp vụ cốt lõi đã ổn định"]),
        ("KHÔNG NÊN ÁP DỤNG AUTOMATION", RED, RED_FILL, [
            "Kịch bản chỉ chạy 1 đến 2 lần rồi bỏ",
            "Giao diện thay đổi liên tục",
            "Cần cảm nhận và phán đoán chủ quan",
            "Chi phí viết kịch bản lớn hơn thời gian tiết kiệm",
            "Dự án ngắn hạn, gấp rút bàn giao",
            "Tính năng đang trong giai đoạn thử nghiệm"]),
    ]
    gap = 40
    pw = (W - 2 * M - gap) / 2
    y = 152
    prepared = []
    for title, col, fill, items in cols:
        bl = [wrap(i, 27, pw - 96) for i in items]
        h = 74 + 18 + sum(40 * len(l) + 16 for l in bl) + 14
        prepared.append((title, col, fill, bl, h))
    ph = max(p[4] for p in prepared)
    for k, (title, col, fill, bl, h) in enumerate(prepared):
        x = M + k * (pw + gap)
        f.rect(x, y, pw, ph, fill="#FFFFFF", stroke=col, sw=2.6, rx=12)
        f.rect(x, y, pw, 74, fill=col, stroke="none", rx=12)
        f.rect(x, y + 56, pw, 18, fill=col, stroke="none")
        f.text(x + pw / 2, y + 37, title, 30, "semi", "#FFFFFF", "middle")
        by = y + 74 + 18
        for l in bl:
            f.rect(x + 34, by + 13, 10, 10, fill=col, stroke="none", rx=3)
            f.block(x + 58, by, l, 27, "reg", BODY, "start", 40)
            by += 40 * len(l) + 16
    yq = y + ph + 34
    f.rect(M, yq, W - 2 * M, 108, fill=AMBER_FILL, stroke=AMBER, sw=2.4, rx=12)
    f.rect(M, yq, 10, 108, fill=AMBER, stroke="none", rx=5)
    f.block(M + 36, yq + 24,
            ["Quy tắc thực dụng (Rule of Thumb): một kịch bản dự kiến phải chạy lặp lại từ 3 lần trở lên",
             "trong vòng đời sản phẩm là ứng viên sáng giá để chuyển sang tự động hoá."],
            27, "reg", AMBER, "start", 34)
    return f.render(os.path.join(OUT, "18-bang-quyet-dinh-automation.png"))


if __name__ == "__main__":
    for fn in (d16, d17, d18):
        print(fn.__name__, fn())
