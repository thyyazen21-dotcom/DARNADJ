#!/usr/bin/env python3
"""Structural validator for the Place-dj Blogger theme.
Checks: XML well-formedness, b:section/b:widget integrity, duplicate id attributes,
required sections/widgets, and JS syntax (via node --check).
"""
import re, sys, subprocess, tempfile, os
import xml.dom.minidom as minidom

THEME = "DarnaDJ_Updated_Package/theme-Place-dj-com.xml"
fails = []
passes = []

def check(name, cond, detail=""):
    (passes if cond else fails).append((name, detail))
    print(("  PASS " if cond else "  FAIL ") + name + ((" -> " + detail) if detail else ""))

raw = open(THEME, encoding="utf-8").read()

# 1. XML well-formedness
try:
    minidom.parseString(raw)
    check("XML well-formed", True)
except Exception as e:
    check("XML well-formed", False, str(e))

# 2. Required sections
required_sections = ["header-widgets","home-before-posts","home-top-picks","main-blog","home-after-posts","sidebar-widgets","footer-widgets"]
found_sections = re.findall(r"<b:section[^>]*\bid='([^']+)'", raw)
for s in required_sections:
    check(f"section present: {s}", s in found_sections)

# 3. Required widgets
required_widgets = {"Blog1":"Blog","Label1":"Label","HTML2":"HTML","HTMLFilter1":"HTML","HTMLTopPicks1":"HTML","PopularPosts1":"PopularPosts"}
found_widgets = dict(re.findall(r"<b:widget[^>]*\bid='([^']+)'[^>]*\btype='([^']+)'", raw))
for wid, wtype in required_widgets.items():
    check(f"widget present: {wid} ({wtype})", found_widgets.get(wid) == wtype, found_widgets.get(wid,"missing"))

# 4. Duplicate id attributes on rendered HTML elements.
# Exclusions (documented, all legitimate):
#  - b:includable / b:section / b:widget ids: scoped to their widget, not global HTML ids.
#  - dynamic ids (contain 'data:'): resolved per-render by Blogger.
#  - Blogger-standard comment markup ids (emitted by the default comment includables).
#  - ids used in mutually exclusive <b:if>/<b:else> branches (only one renders).
BLOGGER_STD_IDS = {"comment-actions","comment-editor","comment-popup",
                   "comment-post-message","comments","comment-holder",
                   "comment-form","comments-block","comment-editor-src"}
MUTUALLY_EXCLUSIVE_IDS = {"gallery-main-img"}  # <b:if>/<b:else> branches
INCLUDABLE_IDS = set(re.findall(r"<b:includable[^>]*\bid='([^']+)'", raw))
html_ids = [i for i in re.findall(r"\bid='([^']+)'", raw)
            if not i.startswith("data:")
            and i not in INCLUDABLE_IDS
            and i not in BLOGGER_STD_IDS
            and i not in MUTUALLY_EXCLUSIVE_IDS]
dupes = sorted({i for i in html_ids if html_ids.count(i) > 1})
check("no duplicate rendered id attributes", len(dupes) == 0, ", ".join(dupes))

# 5. b:section/b:widget open/close balance (use [\s>] so b:widget-settings is NOT counted)
for tag in ["b:section","b:widget","b:includable"]:
    opens = len(re.findall(rf"<{tag}[\s>]", raw))
    selfclose = len(re.findall(rf"<{tag}[\s][^>]*/>", raw))
    closes = len(re.findall(rf"</{tag}>", raw))
    check(f"{tag} balanced ({opens} open / {selfclose} self / {closes} close)", opens == selfclose + closes, f"{opens} vs {selfclose}+{closes}")

# 6. Required feature markers
features = {
    "search form (data:blog.searchUrl)": "data:blog.searchUrl",
    "filter panel (darna-filters)": 'id="darna-filters"',
    "sidebar filter widget": "id='HTMLFilter1'",
    "top picks section": "id='home-top-picks'",
    "top picks rail": 'id="top-picks-rail"',
    "rating section": "id='rating-section'",
    "rating stars input": "id='rating-input'",
    "region browse intro": "اختر الحي الأقرب إلى أسلوب حياتك",
    "region links (place-dj.com)": "https://www.place-dj.com/search/label/",
    "footer 2-col mobile rule": ".footer-grid { grid-template-columns: 1fr 1fr; }",
    "top picks JS wired": "darnaInitTopPicks();",
    "rating JS wired": "darnaInitRating();",
    "property grid": "id='property-grid'",
    "language selector": "id='lang-select'",
    "RTL/LTR dir binding": "expr:dir='data:blog.languageDirection'",
    "hero exact title": "بلاَس &#8212; اعثر على سكنك في جيبوتي",
    "add-property button": "id='add-property-btn'",
    "favorites panel": "id='favorites-panel'",
    "compare bar": "id='compare-bar'",
    "comments include": "name='comments'",
    "footer nav": "class='footer-grid'",
    "schema.org JSON-LD": "application/ld+json",
    "og:site_name": "property='og:site_name'",
    "region browse section": "حسب المنطقة في جيبوتي",
}
for label, needle in features.items():
    check(f"feature: {label}", needle in raw)

# 7. JS syntax check (extract the CDATA script block)
m = re.search(r"<script type='text/javascript'>\s*//<!\[CDATA\[(.*?)//\]\]>\s*</script>", raw, re.S)
if m:
    js = m.group(1)
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(js); tmp = f.name
    r = subprocess.run(["node","--check",tmp], capture_output=True, text=True)
    check("theme JS syntax (node --check)", r.returncode == 0, r.stderr.strip()[:200])
    os.unlink(tmp)
else:
    check("theme JS block extracted", False, "CDATA script not found")

# 8. No dead Google Forms placeholder
check("no dead forms placeholder", "docs.google.com/forms/' " not in raw and "https://docs.google.com/forms/\"" not in raw)

print(f"\n=== STRUCTURE: {len(passes)} passed, {len(fails)} failed ===")
sys.exit(1 if fails else 0)
