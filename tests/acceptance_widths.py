import json, sys
from playwright.sync_api import sync_playwright

WIDTHS = [320, 360, 375, 390, 430, 768, 1024, 1280, 1440]
URL = "http://localhost:8099/preview.html"

def run():
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        for w in WIDTHS:
            ctx = browser.new_context(viewport={"width": w, "height": 800}, device_scale_factor=1)
            page = ctx.new_page()
            errors = []
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: errors.append("pageerror: " + str(e)))
            try:
                page.goto(URL, wait_until="load", timeout=30000)
                page.wait_for_timeout(400)
                data = page.evaluate("""() => {
                    const de = document.documentElement;
                    const wa = document.querySelector('.whatsapp-float');
                    const waR = wa ? wa.getBoundingClientRect() : null;
                    return {
                        scrollWidth: de.scrollWidth,
                        innerWidth: window.innerWidth,
                        bodyScrollWidth: document.body.scrollWidth,
                        filters: !!document.querySelector('.darna-filters'),
                        applyBtn: !!document.querySelector('.filter-apply'),
                        cards: document.querySelectorAll('.property-card').length,
                        waVisible: wa ? (waR.width > 0 && waR.height > 0) : false,
                        waRight: waR ? Math.round(waR.right) : null,
                        waLeft: waR ? Math.round(waR.left) : null,
                        waBottom: waR ? Math.round(waR.bottom) : null,
                        svgIcons: document.querySelectorAll('.feature-icon svg, .loc-icon svg').length,
                    };
                }""")
                overflow = data["scrollWidth"] - data["innerWidth"]
                results.append({
                    "width": w,
                    "horizontal_overflow_px": overflow,
                    "has_hscroll": overflow > 1,
                    "filters": data["filters"],
                    "applyBtn": data["applyBtn"],
                    "cards": data["cards"],
                    "waVisible": data["waVisible"],
                    "waRight": data["waRight"],
                    "waBottom": data["waBottom"],
                    "svgIcons": data["svgIcons"],
                    "consoleErrors": errors,
                })
            except Exception as e:
                results.append({"width": w, "error": str(e)})
            ctx.close()
        browser.close()
    return results

if __name__ == "__main__":
    res = run()
    print(json.dumps(res, ensure_ascii=False, indent=1))
    fails = [r for r in res if r.get("has_hscroll") or r.get("error") or r.get("consoleErrors")]
    print("\n=== SUMMARY ===")
    print("widths tested:", len(res))
    print("horizontal-scroll failures:", sum(1 for r in res if r.get("has_hscroll")))
    print("error/console failures:", sum(1 for r in res if r.get("error") or r.get("consoleErrors")))
