import json
from playwright.sync_api import sync_playwright

PAGES = {
    "home": "https://shershar.blogspot.com/",
    "post": "https://shershar.blogspot.com/2026/10/Beach-villa-rent-djibouti-DJ-VIL-0012.html",
    "label_villa": "https://shershar.blogspot.com/search/label/%D9%81%D9%8A%D9%84%D8%A7",
    "contact": "https://shershar.blogspot.com/p/contact.html",
}
WIDTHS = [375, 1280]

def run():
    out = []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--no-sandbox"])
        for name, url in PAGES.items():
            for w in WIDTHS:
                ctx = b.new_context(viewport={"width": w, "height": 800})
                pg = ctx.new_page()
                errs = []
                pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
                pg.on("pageerror", lambda e: errs.append("pageerror:" + str(e)))
                rec = {"page": name, "width": w}
                try:
                    pg.goto(url, wait_until="load", timeout=45000)
                    pg.wait_for_timeout(800)
                    d = pg.evaluate("""() => ({
                        sw: document.documentElement.scrollWidth,
                        iw: window.innerWidth,
                        title: document.title,
                        cards: document.querySelectorAll('.property-card').length,
                        wa: !!document.querySelector('.whatsapp-float'),
                    })""")
                    rec.update({
                        "overflow_px": d["sw"] - d["iw"],
                        "has_hscroll": (d["sw"] - d["iw"]) > 1,
                        "title": d["title"],
                        "cards": d["cards"],
                        "has_whatsapp_float": d["wa"],
                        "consoleErrors": errs[:5],
                    })
                except Exception as e:
                    rec["error"] = str(e)
                out.append(rec)
                ctx.close()
        b.close()
    return out

if __name__ == "__main__":
    r = run()
    print(json.dumps(r, ensure_ascii=False, indent=1))
