"""Tải font Google Fonts (giấy phép SIL OFL) về thư mục assets/fonts của từng app
để trang chạy offline. Chỉ giữ subset latin, latin-ext, vietnamese.

Chạy:  python tools/fetch_fonts.py
Kết quả: <app>/assets/fonts/*.woff2 và <app>/assets/fonts/fonts.css
"""
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")   # để Google trả về woff2
KEEP = {"latin", "latin-ext", "vietnamese"}

APPS = {
    "phan1-saigon-frames": [
        "Fraunces:ital,opsz,wght@0,9..144,400..800;1,9..144,400..800",
        "Be+Vietnam+Pro:wght@400;500;600;700",
        "IBM+Plex+Mono:wght@400;600",
    ],
    "phan2-studydesk": [
        "Patrick+Hand",
        "Nunito:wght@400..800",
        "JetBrains+Mono:wght@500;700",
    ],
}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main():
    for app, families in APPS.items():
        out = ROOT / app / "assets" / "fonts"
        out.mkdir(parents=True, exist_ok=True)
        css_out = ["/* Font tải từ Google Fonts (SIL Open Font License), lưu cục bộ để chạy offline.\n"
                   "   Sinh bởi tools/fetch_fonts.py – không sửa tay. */\n"]
        for fam in families:
            css = get(f"https://fonts.googleapis.com/css2?family={fam}&display=swap").decode()
            for subset, block in re.findall(r"/\* ([a-z-]+) \*/\s*(@font-face \{.*?\})", css, re.S):
                if subset not in KEEP:
                    continue
                name = re.search(r"font-family: '([^']+)'", block).group(1)
                style = re.search(r"font-style: (\w+)", block).group(1)
                weight = re.search(r"font-weight: ([\d ]+)", block).group(1).replace(" ", "-")
                url = re.search(r"url\((https://[^)]+)\)", block).group(1)
                fname = f"{name.lower().replace(' ', '-')}-{style}-{weight}-{subset}.woff2"
                (out / fname).write_bytes(get(url))
                css_out.append(f"/* {subset} */\n" + block.replace(url, fname) + "\n")
                print(app, fname)
        (out / "fonts.css").write_text("".join(css_out), encoding="utf-8")


if __name__ == "__main__":
    main()
