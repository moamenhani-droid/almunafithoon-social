#!/usr/bin/env python3
"""يملأ قالب HTML ببيانات JSON ويصدّره PNG بالأبعاد الدقيقة عبر Chrome بلا واجهة.

الاستخدام:
  render.py <template.html> <out.png> [--data data.json] [--size post|square|story]

  --data  ملف JSON بمفاتيح المتغيرات: {"TITLE": "...", "IMAGE": "/abs/path.jpg"}
          مسارات الصور تُحوَّل تلقائياً إلى file:// إن كانت مطلقة.
  --size  يُستنتج من اسم القالب إن لم يُعطَ (story-* ← story).

ينشئ نسخة مملوءة مؤقتة بجانب القالب حتى تعمل المسارات النسبية للخطوط والشعار، ثم يحذفها.
يتحقق في النهاية من أبعاد الصورة الناتجة.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile

SIZES = {"post": (1080, 1350), "square": (1080, 1080), "story": (1080, 1920)}
CHROME = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "", shutil.which("chromium") or "",
    shutil.which("chromium-browser") or "",
]


def find_chrome():
    for c in CHROME:
        if c and os.path.exists(c):
            return c
    sys.exit("لم يُعثر على Chrome أو Chromium.")


def fill(html, data):
    for k, v in data.items():
        v = str(v)
        if k in ("IMAGE", "BG") and v.startswith("/"):
            v = "file://" + v
        html = html.replace("{{%s}}" % k, v)
    left = sorted(set(re.findall(r"\{\{(\w+)\}\}", html)) - {"IMAGE", "BG"})
    if left:
        print("تنبيه — متغيرات لم تُملأ:", ", ".join(left), file=sys.stderr)
    return html


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("template"); ap.add_argument("out")
    ap.add_argument("--data"); ap.add_argument("--size", choices=SIZES)
    a = ap.parse_args()

    size = a.size or ("story" if "story" in os.path.basename(a.template) else "post")
    w, h = SIZES[size]
    tpl = os.path.abspath(a.template)
    html = open(tpl, encoding="utf-8").read()
    data = json.load(open(a.data, encoding="utf-8")) if a.data else {}
    html = fill(html, data)

    fd, tmp = tempfile.mkstemp(suffix=".html", prefix="_render_", dir=os.path.dirname(tpl))
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(html)
    out = os.path.abspath(a.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    try:
        subprocess.run([find_chrome(), "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=1", "--allow-file-access-from-files",
                        f"--window-size={w},{h}", "--virtual-time-budget=4000",
                        f"--screenshot={out}", "file://" + tmp],
                       check=True, capture_output=True)
    finally:
        os.remove(tmp)

    try:
        from PIL import Image
        got = Image.open(out).size
        status = "✓" if got == (w, h) else f"✗ متوقع {w}×{h}"
        print(f"{status} {out} — {got[0]}×{got[1]}")
    except ImportError:
        print(f"✓ {out}")


if __name__ == "__main__":
    main()
