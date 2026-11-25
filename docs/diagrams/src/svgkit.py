# -*- coding: utf-8 -*-
"""Minimal SVG toolkit for redrawing the seminar diagrams.

Everything is laid out in absolute pixels on a 1950 px wide canvas, which is
exactly 6.5 in at 300 dpi -> the usable text width of the Word document
(A4, margins 0.98 + 0.79 in).
"""
import os
import subprocess
from xml.sax.saxutils import escape

from PIL import Image, ImageFont

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FONT_DIR = r"C:\Windows\Fonts"
FONTS = {
    "reg":   (os.path.join(FONT_DIR, "segoeui.ttf"),  "Segoe UI", 400),
    "semi":  (os.path.join(FONT_DIR, "segoeuib.ttf"), "Segoe UI", 600),
    "mono":  (os.path.join(FONT_DIR, "consola.ttf"),  "Consolas", 400),
    "monob": (os.path.join(FONT_DIR, "consolab.ttf"), "Consolas", 700),
}

W = 1950
M = 36

INK      = "#111827"
BODY     = "#374151"
MUTED    = "#6B7280"
RULE     = "#9AA3AF"

BLUE      = "#0B63B0"
BLUE_FILL = "#EAF2FB"
BLUE_DEEP = "#0A4C8F"

GRAY_FILL   = "#F6F7F9"
GRAY_STROKE = "#C9CFD8"

GREEN      = "#127A57"
GREEN_FILL = "#E9F6F0"
RED        = "#B42318"
RED_FILL   = "#FDEDEB"
AMBER      = "#A9600B"
AMBER_FILL = "#FEF4E6"
PURPLE      = "#5A3FA0"
PURPLE_FILL = "#F1EDFB"
TEAL        = "#0F6B6B"
TEAL_FILL   = "#E7F4F4"

_fcache = {}


def _font(key, size):
    k = (key, size)
    if k not in _fcache:
        _fcache[k] = ImageFont.truetype(FONTS[key][0], size)
    return _fcache[k]


def tw(text, size, key="reg"):
    """Measured width of a single line, with a little safety margin."""
    return _font(key, size).getlength(text) * 1.015


def wrap(text, size, maxw, key="reg"):
    """Greedy word wrap; breaks over-long tokens by character."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if tw(trial, size, key) <= maxw or not cur:
            if tw(trial, size, key) > maxw and not cur:
                # single token wider than the box -> hard break
                piece = ""
                for ch in word:
                    if tw(piece + ch, size, key) > maxw and piece:
                        lines.append(piece)
                        piece = ch
                    else:
                        piece += ch
                cur = piece
            else:
                cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


class Fig:
    def __init__(self, width=W):
        self.w = width
        self.parts = []
        self.bottom = 0.0

    # ---------- primitives ----------
    def raw(self, s):
        self.parts.append(s)

    def rect(self, x, y, w, h, fill="none", stroke="none", sw=3, rx=10, dash=None, opacity=None):
        d = ' stroke-dasharray="%s"' % dash if dash else ""
        o = ' opacity="%s"' % opacity if opacity else ""
        self.raw('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" '
                 'fill="%s" stroke="%s" stroke-width="%s"%s%s/>'
                 % (x, y, w, h, rx, fill, stroke, sw, d, o))
        self.bottom = max(self.bottom, y + h)

    def line(self, x1, y1, x2, y2, stroke=BODY, sw=3, dash=None, marker=True, opacity=None):
        d = ' stroke-dasharray="%s"' % dash if dash else ""
        m = ' marker-end="url(#ah)"' if marker else ""
        o = ' opacity="%s"' % opacity if opacity else ""
        self.raw('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width="%s" stroke-linecap="butt"%s%s%s/>'
                 % (x1, y1, x2, y2, stroke, sw, d, m, o))
        self.bottom = max(self.bottom, y1, y2)

    def path(self, d, stroke=BODY, sw=3, dash=None, marker=True, fill="none"):
        da = ' stroke-dasharray="%s"' % dash if dash else ""
        m = ' marker-end="url(#ah)"' if marker else ""
        self.raw('<path d="%s" fill="%s" stroke="%s" stroke-width="%s" '
                 'stroke-linejoin="miter"%s%s/>' % (d, fill, stroke, sw, da, m))

    def text(self, x, y, s, size=32, key="reg", color=INK, anchor="start", opacity=None):
        o = ' opacity="%s"' % opacity if opacity else ""
        self.raw('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" font-weight="%s" '
                 'fill="%s" text-anchor="%s" dominant-baseline="central" '
                 'xml:space="preserve"%s>%s</text>'
                 % (x, y, FONTS[key][1], size, FONTS[key][2], color, anchor, o, escape(s)))

    def block(self, x, ytop, lines, size=32, key="reg", color=INK, anchor="start", lh=None):
        """Multi-line text block; ytop is the top of the first line box."""
        lh = lh or round(size * 1.34)
        for i, ln in enumerate(lines):
            self.text(x, ytop + lh * (i + 0.5), ln, size, key, color, anchor)
        self.bottom = max(self.bottom, ytop + lh * len(lines))
        return ytop + lh * len(lines)

    # ---------- composite ----------
    def box(self, x, y, w, lines, size=32, key="reg", color=INK, fill="#FFFFFF",
            stroke=GRAY_STROKE, sw=3, rx=10, padx=22, pady=20, lh=None,
            align="middle", dash=None):
        lh = lh or round(size * 1.34)
        h = 2 * pady + lh * len(lines)
        self.rect(x, y, w, h, fill=fill, stroke=stroke, sw=sw, rx=rx, dash=dash)
        tx = x + w / 2 if align == "middle" else x + padx
        self.block(tx, y + pady, lines, size, key, color,
                   "middle" if align == "middle" else "start", lh)
        return h

    def badge(self, x, y, w, h, s, size=34, fill=BLUE, color="#FFFFFF", rx=8, key="semi"):
        self.rect(x, y, w, h, fill=fill, stroke="none", rx=rx)
        self.text(x + w / 2, y + h / 2, s, size, key, color, "middle")

    def label(self, cx, cy, lines, size=26, color=BODY, bg="#FFFFFF", pad=6, key="reg"):
        """Text with an opaque background, used on top of connectors."""
        widths = [tw(l, size, key) for l in lines]
        wmax = max(widths)
        lh = round(size * 1.3)
        h = lh * len(lines) + pad
        self.rect(cx - wmax / 2 - pad, cy - h / 2, wmax + 2 * pad, h, fill=bg, stroke="none", rx=4)
        self.block(cx - wmax / 2, cy - h / 2 + pad / 2, lines, size, key, color, "start", lh)

    def arrow_v(self, cx, y1, y2, label=None, dash=None, color=BODY, lsize=26, label_side="right"):
        self.line(cx, y1, cx, y2 - 1, stroke=color, dash=dash)
        if label:
            lines = wrap(label, lsize, 520)
            if label_side == "right":
                self.block(cx + 18, y1 + (y2 - y1) / 2 - len(lines) * lsize * 0.67,
                           lines, lsize, "reg", MUTED, "start")
            else:
                self.block(cx - 18, y1 + (y2 - y1) / 2 - len(lines) * lsize * 0.67,
                           lines, lsize, "reg", MUTED, "end")

    def arrow_h(self, y, x1, x2, label=None, dash=None, color=BODY, lsize=26):
        self.line(x1, y, x2 - 1, y, stroke=color, dash=dash)
        if label:
            self.label((x1 + x2) / 2, y - 26, wrap(label, lsize, abs(x2 - x1) - 20), lsize)

    # ---------- output ----------
    def render(self, path_png, height=None, dpi=300):
        h = int(round(height or (self.bottom + M)))
        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 %d %d">\n'
            '<defs>\n'
            '<marker id="ah" viewBox="0 0 10 10" refX="9.2" refY="5" markerWidth="19" '
            'markerHeight="19" orient="auto-start-reverse" markerUnits="userSpaceOnUse">'
            '<path d="M0,0.6 L10,5 L0,9.4 z" fill="#374151"/></marker>\n'
            '</defs>\n'
            '<rect width="%d" height="%d" fill="#FFFFFF"/>\n' % (self.w, h, self.w, h, self.w, h)
        ) + "\n".join(self.parts) + "\n</svg>\n"

        base = os.path.splitext(path_png)[0]
        svg_path = base + ".svg"
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg)
        subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
             "--force-device-scale-factor=1", "--default-background-color=FFFFFFFF",
             "--window-size=%d,%d" % (self.w, h),
             "--screenshot=" + path_png, "file:///" + svg_path.replace("\\", "/")],
            check=True, capture_output=True, timeout=120)
        im = Image.open(path_png).convert("RGB")
        im.save(path_png, dpi=(dpi, dpi))
        return path_png, im.size
