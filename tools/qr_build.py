"""Make everything for the QR codes from qr/register.md (the one register):
  1. the short forwarding pages: mkdocs.yml gets  q/ID.md -> target page  (plugin mkdocs-redirects);
  2. the QR pictures: qr/png/ID.png, 26 mm wide at 600 dpi: the code (17 mm, black on white) and the two-line label.
The book's Word builder places qr/png/ID.png wherever a chapter paragraph starts with {qr:ID}.
Run from the repository root:  python tools/qr_build.py"""
import re
from pathlib import Path
import segno
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://ag999git.github.io/002-cbse-cs-class-11'
DPI = 600
MM = DPI / 25.4
OR, INK = (197, 90, 17), (38, 38, 38)


def register():
    rows = []
    for line in (ROOT / 'qr' / 'register.md').read_text(encoding='utf-8').split('\n'):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) == 6 and re.fullmatch(r'\d{4}', cells[0]):
            rows.append(dict(id=cells[0], kind=cells[1], name=cells[2], section=cells[3], anchor=cells[4], target=cells[5]))
    return rows


def redirects(rows):
    for r in rows:
        assert (ROOT / 'book' / r['target']).exists(), f"{r['id']}: target page missing: {r['target']}"
    block = '  - redirects:\n      redirect_maps:\n' + ''.join(f"        'q/{r['id']}.md': '{r['target']}'\n" for r in rows)
    y = (ROOT / 'mkdocs.yml').read_text(encoding='utf-8')
    y = re.sub(r'\nplugins:\n(?:  .*\n)+', '\n', y)          # replace the whole plugins block each time
    y = y.rstrip('\n') + '\nplugins:\n  - search\n' + block
    (ROOT / 'mkdocs.yml').write_text(y, encoding='utf-8')


def picture(r):
    url = f"{SITE}/q/{r['id']}/"
    qr = segno.make(url, error='m')
    n = qr.symbol_size(border=4)[0]                 # modules including the standard 4-module quiet zone
    scale = max(1, int(19 * MM) // n)               # whole pixels per module: every square the same size
    tmp = ROOT / 'qr' / 'png' / f"_{r['id']}.png"
    qr.save(tmp, scale=scale, border=4, dark='black', light='white')
    code = Image.open(tmp).convert('RGB')
    side = code.size[0]
    tmp.unlink()
    W = max(int(26 * MM), side)
    f_kind = ImageFont.truetype('calibrib.ttf', int(8 / 72 * DPI))
    f_name = ImageFont.truetype('calibri.ttf', int(8 / 72 * DPI))
    H = side + int(8.5 * MM)
    im = Image.new('RGB', (W, H), 'white')
    im.paste(code, ((W - side) // 2, 0))  # the quiet zone is part of the code picture
    d = ImageDraw.Draw(im)
    for text, font, col, y in ((r['kind'], f_kind, OR, side + int(0.6 * MM)), (r['name'], f_name, INK, side + int(4.2 * MM))):
        tw = d.textlength(text, font=font)
        assert tw <= W, f"{r['id']}: label too long: {text}"
        d.text(((W - tw) / 2, y), text, fill=col, font=font)
    im.save(ROOT / 'qr' / 'png' / f"{r['id']}.png", dpi=(DPI, DPI))
    return url, qr.version


if __name__ == '__main__':
    rows = register()
    (ROOT / 'qr' / 'png').mkdir(parents=True, exist_ok=True)
    redirects(rows)
    for r in rows:
        url, ver = picture(r)
        print(f"{r['id']}  version {ver}  {url}  ->  {r['target']}")
    print(len(rows), 'codes made; mkdocs.yml forwarding list updated')
