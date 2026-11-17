# -*- coding: utf-8 -*-
"""Vẽ 12 ảnh minh họa SVG (800x600) cho Saigon Frames.
Ảnh là hình phẳng tự vẽ bằng code, mô phỏng các công trình/khung cảnh Sài Gòn, không lấy từ nguồn ngoài.
Chạy: python tools/gen_photos.py  -> ghi vào phan1-saigon-frames/assets/photos/"""
import os, random

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "phan1-saigon-frames", "assets", "photos")
os.makedirs(OUT, exist_ok=True)

SKY = {
    "sang": ("#f7d9a6", "#fdf1dc"), "trua": ("#86c3e3", "#e1f0f6"), "chieu": ("#ec8a5c", "#f9cf8e"),
    "dem": ("#141d36", "#33426a"), "xanh": ("#2d3a66", "#8494bf"),
}


def svg(label, sky, body, sun=None):
    a, b = SKY[sky]
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" role="img" aria-label="{label}">'
         f'<title>{label}</title><defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
         f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient></defs>'
         f'<rect width="800" height="600" fill="url(#sky)"/>')
    if sun:
        x, y, r, c, o = sun
        s += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity="{o}"/>'
    if sky == "dem":
        rnd = random.Random(label)
        s += "".join(f'<circle cx="{rnd.randint(0, 800)}" cy="{rnd.randint(0, 260)}" r="{rnd.choice([1, 1, 1.6])}" fill="#fff" opacity=".7"/>'
                     for _ in range(40))
    return s + body + "</svg>"


def rect(x, y, w, h, c, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" {extra}/>'


def windows(x, y, cols, rows, w, h, gx, gy, c, lit=None, seed=0):
    rnd = random.Random(seed)
    out = ""
    for i in range(cols):
        for j in range(rows):
            col = c if not lit or rnd.random() > lit[1] else lit[0]
            out += rect(x + i * (w + gx), y + j * (h + gy), w, h, col)
    return out


def arches(x, y, n, w, h, gap, c):
    out = ""
    for i in range(n):
        cx = x + i * (w + gap)
        r = w / 2
        out += f'<path d="M{cx} {y + h}V{y + r}A{r} {r} 0 0 1 {cx + w} {y + r}V{y + h}Z" fill="{c}"/>'
    return out


def tree(x, base, s, c="#4f7a4a", trunk="#5b4636"):
    return (rect(x - 4 * s, base - 40 * s, 8 * s, 40 * s, trunk)
            + f'<circle cx="{x}" cy="{base - 55 * s}" r="{30 * s}" fill="{c}"/>'
            + f'<circle cx="{x - 22 * s}" cy="{base - 40 * s}" r="{20 * s}" fill="{c}"/>'
            + f'<circle cx="{x + 22 * s}" cy="{base - 42 * s}" r="{22 * s}" fill="{c}"/>')


def street(c="#6f6a66", line="#e9e2d0", y=520):
    return rect(0, y, 800, 600 - y, c) + "".join(rect(40 + i * 120, y + 38, 60, 6, line) for i in range(7))


def bike(x, y, c="#c0392b"):
    return (f'<circle cx="{x}" cy="{y}" r="11" fill="#222"/><circle cx="{x + 46}" cy="{y}" r="11" fill="#222"/>'
            f'<path d="M{x} {y}L{x + 16} {y - 20}H{x + 36}L{x + 46} {y}" stroke="{c}" stroke-width="7" fill="none"/>'
            f'<circle cx="{x + 24}" cy="{y - 38}" r="8" fill="#f2c6a0"/>{rect(x + 18, y - 32, 13, 20, "#2e4a7d")}')


def post_office():
    yellow = "#f2c46d"
    b = rect(90, 230, 620, 290, yellow) + rect(90, 220, 620, 18, "#e2ae52")
    b += f'<path d="M300 230 400 150 500 230Z" fill="#e2ae52"/>' + rect(330, 170, 140, 70, yellow)
    b += '<circle cx="400" cy="200" r="24" fill="#fdf6e3" stroke="#7a5a2b" stroke-width="4"/>'
    b += '<path d="M400 200V184M400 200l11 7" stroke="#7a5a2b" stroke-width="4" stroke-linecap="round"/>'
    b += arches(120, 300, 9, 46, 110, 18, "#7c5a3a") + arches(120, 430, 9, 46, 80, 18, "#5e4430")
    b += rect(90, 410, 620, 10, "#e2ae52") + rect(0, 520, 800, 80, "#c9b79c")
    b += tree(55, 525, 1.3) + tree(750, 525, 1.4)
    return svg("Bưu điện giữa trưa", "trua", b, (660, 90, 40, "#fff7d6", .9))


def cathedral():
    brick = "#b5533c"; dark = "#8e3b2a"
    b = rect(220, 300, 360, 220, brick)
    for x in (180, 520):
        b += rect(x, 170, 100, 350, brick) + f'<path d="M{x} 170 {x + 50} 60 {x + 100} 170Z" fill="#6d7a83"/>'
        b += f'<path d="M{x + 50} 60V30M{x + 40} 42H{x + 60}" stroke="#4b555c" stroke-width="5"/>'
        b += arches(x + 30, 210, 1, 40, 70, 0, dark) + arches(x + 30, 320, 1, 40, 90, 0, dark)
    b += '<circle cx="400" cy="360" r="40" fill="#f3dccc" stroke="' + dark + '" stroke-width="8"/>'
    b += arches(370, 430, 1, 60, 90, 0, dark) + f'<path d="M220 300 400 240 580 300Z" fill="{dark}"/>'
    b += rect(0, 520, 800, 80, "#d9cbb8") + tree(80, 525, 1.6, "#5d8a52") + tree(720, 525, 1.5, "#5d8a52")
    b += '<ellipse cx="400" cy="560" rx="70" ry="14" fill="#e8e0d0"/>'
    return svg("Hai tháp chuông", "sang", b, (130, 110, 46, "#fff3d0", .85))


def opera():
    cream = "#efe2c8"; shade = "#d6c3a0"
    b = rect(110, 250, 580, 270, cream) + f'<path d="M110 250Q400 120 690 250Z" fill="{shade}"/>'
    b += arches(330, 260, 1, 140, 190, 0, "#8c6b4a") + arches(350, 290, 1, 100, 160, 0, "#f6c977")
    b += rect(150, 300, 130, 12, shade) + rect(520, 300, 130, 12, shade)
    b += windows(160, 330, 3, 2, 26, 50, 22, 40, "#8c6b4a") + windows(530, 330, 3, 2, 26, 50, 22, 40, "#8c6b4a")
    for x in (240, 560):
        b += f'<path d="M{x} 160c20 10 20 40 0 50c-20-10-20-40 0-50Z" fill="#c8a35d"/>' + rect(x - 3, 205, 6, 45, "#c8a35d")
    b += rect(0, 520, 800, 80, "#8a7f73") + "".join(rect(250 + i * 30, 470 + i * 10, 300 - i * 60, 10, "#dacdb0") for i in range(5))
    return svg("Nhà hát lúc chiều", "chieu", b, (640, 140, 70, "#ffe2a8", .8))


def market():
    wall = "#f0d9a8"; red = "#b54a32"
    b = rect(120, 290, 560, 230, wall) + rect(120, 280, 560, 20, red)
    b += rect(340, 150, 120, 140, wall) + f'<path d="M330 150 400 105 470 150Z" fill="{red}"/>'
    b += '<circle cx="400" cy="200" r="34" fill="#fffaf0" stroke="#5a3d25" stroke-width="5"/>'
    b += '<path d="M400 200V176M400 200l16 10" stroke="#5a3d25" stroke-width="5" stroke-linecap="round"/>'
    b += arches(340, 360, 1, 120, 160, 0, "#6e4b2d") + arches(160, 380, 3, 40, 80, 22, "#6e4b2d") + arches(540, 380, 3, 40, 80, 22, "#6e4b2d")
    b += rect(345, 300, 110, 30, "#2f5d50") + '<text x="400" y="322" font-family="Georgia,serif" font-size="18" fill="#f8efd8" text-anchor="middle">CHỢ</text>'
    b += street() + bike(140, 560) + bike(560, 575, "#2a6f97") + bike(380, 588, "#d4a017")
    return svg("Cổng chợ phía Nam", "sang", b, (680, 100, 42, "#fff1c9", .9))


def apartment(label, sky, base, balcony, plant, seed, signs=False):
    b = rect(140, 110, 520, 410, base)
    rnd = random.Random(seed)
    for j in range(7):
        y = 130 + j * 55
        for i in range(6):
            x = 160 + i * 82
            win = "#ffd889" if sky == "dem" and rnd.random() > .45 else "#3d4a52"
            b += rect(x, y, 62, 34, win) + rect(x - 4, y + 34, 70, 8, balcony)
            if rnd.random() > .5:
                b += f'<circle cx="{x + 12}" cy="{y + 30}" r="9" fill="{plant}"/><circle cx="{x + 50}" cy="{y + 30}" r="7" fill="{plant}"/>'
            if signs and rnd.random() > .78:
                b += rect(x + 4, y + 6, 54, 20, rnd.choice(["#e76f51", "#2a9d8f", "#f4a261", "#e9c46a"]))
    b += rect(0, 520, 800, 80, "#6f6a66") + tree(80, 525, 1.4) + tree(730, 525, 1.2)
    return svg(label, sky, b, (700, 80, 34, "#fff4cf", .8) if sky != "dem" else (680, 90, 26, "#f4f1de", .9))


def stair_block():
    wall = "#d8d0c4"
    b = rect(0, 0, 800, 600, "#cfc6b8") + rect(250, 0, 300, 600, "#efe9df")
    for j in range(9):
        y = 20 + j * 66
        b += f'<path d="M260 {y + 50}Q400 {y - 10} 540 {y + 50}" stroke="#7b6f62" stroke-width="10" fill="none"/>'
        b += rect(262, y + 50, 276, 8, "#9e9184")
    b += rect(0, 0, 250, 600, wall) + rect(550, 0, 250, 600, wall)
    b += windows(40, 40, 2, 6, 70, 50, 50, 45, "#5f6d78") + windows(590, 40, 2, 6, 70, 50, 50, 45, "#5f6d78")
    b += '<circle cx="400" cy="300" r="70" fill="none" stroke="#b9ab99" stroke-width="3" opacity=".7"/>'
    return svg("Cầu thang xoắn", "sang", b)


def tower_river():
    b = rect(0, 430, 800, 170, "#2b4466") + "".join(rect(60 + i * 110, 470 + (i % 3) * 30, 70, 4, "#6f8db8") for i in range(7))
    b += f'<path d="M360 430V140L390 40 420 140V430Z" fill="#5a6f8f"/>' + windows(372, 160, 2, 14, 14, 10, 8, 8, "#a9c2e3", ("#ffe08a", .4), 3)
    b += rect(80, 300, 120, 130, "#3e5170") + rect(210, 260, 90, 170, "#4a5f80") + rect(480, 280, 110, 150, "#45597a") + rect(610, 320, 130, 110, "#3e5170")
    b += windows(95, 315, 5, 5, 12, 10, 10, 12, "#6c84a8", ("#ffd27a", .35), 5) + windows(495, 295, 5, 6, 12, 10, 8, 12, "#6c84a8", ("#ffd27a", .35), 6)
    b += f'<path d="M0 430H800" stroke="#9fb6d4" stroke-width="2"/><path d="M390 440V590" stroke="#ffd27a" stroke-width="6" opacity=".35"/>'
    return svg("Tòa tháp bên sông", "xanh", b, (150, 120, 30, "#f2e9d0", .8))


def lotus_tower():
    b = rect(0, 470, 800, 130, "#3c3f4a")
    b += f'<path d="M370 470V170Q400 110 430 170V470Z" fill="#6f7f95"/>'
    b += '<ellipse cx="455" cy="230" rx="55" ry="14" fill="#9aa9bc"/><path d="M410 230h90v10h-90z" fill="#596a80"/>'
    b += windows(380, 190, 3, 18, 10, 8, 6, 6, "#c7d3e1", ("#fff2b3", .2), 9)
    b += rect(60, 330, 110, 140, "#59657a") + rect(190, 280, 110, 190, "#677489") + rect(540, 300, 100, 170, "#5e6a7f") + rect(660, 350, 110, 120, "#525d70")
    b += windows(75, 345, 4, 5, 14, 12, 12, 12, "#8796ab") + windows(555, 315, 3, 6, 16, 12, 14, 12, "#8796ab")
    return svg("Tháp búp sen", "trua", b, (130, 90, 40, "#fffbe6", .9))


def bridge():
    b = rect(0, 420, 800, 180, "#16223d") + "".join(rect(30 + i * 95, 450 + (i % 4) * 32, 55, 3, "#ffcf7a") for i in range(8))
    b += f'<path d="M400 420V130" stroke="#d9dde6" stroke-width="16"/>'
    for i in range(9):
        b += f'<path d="M400 {150 + i * 18}L{60 + i * 32} 400M400 {150 + i * 18}L{740 - i * 32} 400" stroke="#cfd6e4" stroke-width="2" opacity=".85"/>'
    b += rect(0, 395, 800, 14, "#e7eaf1") + rect(0, 409, 800, 6, "#ff9f5a")
    b += "".join(f'<circle cx="{40 + i * 64}" cy="392" r="4" fill="#ffd27a"/>' for i in range(13))
    b += f'<path d="M0 418H800" stroke="#ffd27a" stroke-width="2" opacity=".5"/>'
    return svg("Cầu dây văng về đêm", "dem", b, (650, 90, 26, "#f4f1de", .95))


def alley():
    b = rect(0, 0, 800, 600, "#e9c891")
    b += f'<path d="M0 0H300L360 600H0Z" fill="#d79b63"/><path d="M800 0H500L440 600H800Z" fill="#c7865a"/>'
    b += f'<path d="M300 0H500L440 600H360Z" fill="#f6dfb3"/>'
    b += windows(40, 60, 2, 3, 70, 80, 40, 60, "#6e4a33") + windows(600, 60, 2, 3, 70, 80, 40, 60, "#6e4a33")
    for y in (90, 140, 190):
        b += f'<path d="M300 {y}Q400 {y + 40} 500 {y}" stroke="#3b3b3b" stroke-width="2" fill="none"/>'
    b += "".join(f'<circle cx="{330 + i * 35}" cy="{110 + (i % 2) * 10}" r="9" fill="#e63946" opacity=".9"/>' for i in range(5))
    b += bike(370, 520, "#2a6f97") + rect(80, 420, 120, 18, "#2f5d50") + rect(90, 438, 10, 70, "#2f5d50") + rect(180, 438, 10, 70, "#2f5d50")
    b += '<circle cx="120" cy="405" r="14" fill="#f2c6a0"/><circle cx="165" cy="405" r="14" fill="#f2c6a0"/>'
    b += tree(700, 560, 1.1, "#678d58")
    return svg("Hẻm chiều", "chieu", b)


def walking_street():
    b = rect(0, 460, 800, 140, "#43403e") + f'<path d="M260 600 380 460H420L540 600Z" fill="#d8cbb4" opacity=".55"/>'
    for x, w, h, c in ((20, 160, 300, "#2e3a55"), (190, 120, 240, "#3a4766"), (480, 140, 280, "#33405e"), (630, 160, 330, "#2a3550")):
        b += rect(x, 460 - h, w, h, c) + windows(x + 14, 480 - h, int((w - 20) / 26), int(h / 34) - 1, 14, 18, 12, 16, "#55638a", ("#ffd27a", .55), x)
    b += rect(330, 230, 140, 230, "#f1e2c2") + arches(350, 300, 3, 26, 60, 14, "#a2805a") + f'<path d="M330 230 400 190 470 230Z" fill="#c9a86b"/>'
    b += "".join(f'<circle cx="{60 + i * 52}" cy="470" r="3" fill="#fff2b0"/>' for i in range(14))
    b += "".join(f'<path d="M{150 + i * 90} 590v-34" stroke="#222" stroke-width="10" stroke-linecap="round"/><circle cx="{150 + i * 90}" cy="545" r="8" fill="#f2c6a0"/>' for i in range(6))
    return svg("Phố đi bộ đêm", "dem", b, (720, 70, 22, "#f4f1de", .9))


SCENES = {
    "buu-dien": post_office, "hai-thap-chuong": cathedral, "nha-hat": opera, "cong-cho": market,
    "chung-cu-ca-phe": lambda: apartment("Chung cư cà phê", "sang", "#e8d7bd", "#a68a64", "#5f8f4e", 11, True),
    "ban-cong-xanh": lambda: apartment("Ban công xanh", "trua", "#c9d8cf", "#7d9488", "#3f7a45", 22),
    "cau-thang-xoan": stair_block, "thap-ben-song": tower_river, "thap-bup-sen": lotus_tower,
    "cau-day-vang": bridge, "hem-chieu": alley, "pho-di-bo": walking_street,
}

for name, fn in SCENES.items():
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf8") as f:
        f.write(fn())
print("wrote", len(SCENES), "svg to", OUT)
