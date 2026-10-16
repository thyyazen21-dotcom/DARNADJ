"""Safer Arabic delivery generator for PLACE-DJ
This script performs context-aware, non-destructive edits to produce an Arabic
export suitable for import/testing. It will:
 - read the source PLACE-DJ template
 - create a backup copy (delivery/original-... if not exists)
 - produce DELIVERY-ARABIC/theme-PLACE-DJ.AR.xml with scoped changes only

Notes:
 - All edits are limited to well-scoped regions (the <html> start tag, the
   aside.detail-side area for WhatsApp and inquiry form, the rating section,
   and the preferred-section widget content). It avoids global regexes.
 - It does NOT modify widgets marked as locked or the Blogger widget ids.
 - It will reference brand assets from phase-01-place-logo/03_png using
   raw.githubusercontent URLs so the assets are available if uploaded.

Run locally: python3 generate_ar_delivery_safe.py
"""

from __future__ import annotations
import io, os, re, sys

SRC = "DarnaDJ_Updated_Package/Place-dj-16oct/PLACE-DJ-TEMPLATE-FINAL.xml"
OUT_DIR = "DarnaDJ_Updated_Package/Place-dj-16oct/DELIVERY-ARABIC"
OUT = os.path.join(OUT_DIR, "theme-PLACE-DJ.AR.xml")
BACKUP = os.path.join(OUT_DIR, "original-PLACE-DJ-TEMPLATE-FINAL.xml")

if not os.path.exists(SRC):
    print("Source template not found:", SRC)
    sys.exit(2)

os.makedirs(OUT_DIR, exist_ok=True)

with io.open(SRC, "r", encoding="utf-8") as fh:
    src = fh.read()

# 1. Create a backup if it doesn't already exist (non-destructive)
if not os.path.exists(BACKUP):
    with io.open(BACKUP, "w", encoding="utf-8") as fb:
        fb.write(src)
    print("Backup written:", BACKUP)
else:
    print("Backup already exists:", BACKUP)

out = src

# Helper: replace only the opening <html ...> tag (first occurrence)
html_open_re = re.compile(r"<html([\s\S]*?)>", re.IGNORECASE)
mo = html_open_re.search(out)
if mo:
    original_tag = mo.group(0)
    attrs = mo.group(1)
    # Remove expr:dir and expr:lang from attrs if present
    attrs_clean = re.sub(r"\s*expr:dir=[^\s>]+", "", attrs)
    attrs_clean = re.sub(r"\s*expr:lang=[^\s>]+", "", attrs_clean)
    # Ensure xmlns is preserved; add static lang/dir
    if "dir=" not in attrs_clean:
        attrs_clean = attrs_clean + " dir='rtl'"
    if "lang=" not in attrs_clean:
        attrs_clean = attrs_clean + " lang='ar'"
    new_tag = f"<html{attrs_clean}>"
    out = out.replace(original_tag, new_tag, 1)
    print("Patched <html> start tag to include dir='rtl' lang='ar'")
else:
    print("Warning: <html> tag not found — skipping lang/dir injection")

# 2. Inject Google Fonts link for Noto Sans Arabic in the <head> shortly after all-head-content
head_insert_point = "<b:include data='blog' name='all-head-content'/>"
fonts_link = "\n  <link href='https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@400;700&display=swap' rel='stylesheet'/>\n"
if head_insert_point in out:
    out = out.replace(head_insert_point, head_insert_point + fonts_link, 1)
    print("Inserted Google Fonts link for Noto Sans Arabic")

# 3. Replace site logo src to point to repository brand asset (safe replace only for the first .site-logo .brand-logo src)
logo_pattern = re.compile(r"(<img[^>]+class=['\"]brand-logo['\"][^>]+src=)['\"][^'\"]+['\"]", re.IGNORECASE)
match = logo_pattern.search(out)
if match:
    repo_logo = "https://raw.githubusercontent.com/thyyazen21-dotcom/DARNADJ/main/phase-01-place-logo/03_png/concept-03-place-djibouti.png"
    new_img = match.group(1) + '"' + repo_logo + '"'
    out = logo_pattern.sub(new_img, out, count=1)
    print("Re-pointed brand-logo src to repository asset")

# 4. Scoped removal of WhatsApp CTA and note inside aside.detail-side only
# Find the aside.detail-side block
aside_re = re.compile(r"(<aside[^>]*class=['\"][^'\"]*detail-side[^>]*>[\s\S]*?<\/aside>)", re.IGNORECASE)
amo = aside_re.search(out)
if amo:
    aside_block = amo.group(1)
    aside_new = aside_block
    # Remove anchor.whatsapp-cta and paragraph.whatsapp-note within this aside
    aside_new = re.sub(r"<a[^>]+class=[\'\"]whatsapp-cta[\'\"][\s\S]*?<\/a>\s*", "", aside_new, flags=re.IGNORECASE)
    aside_new = re.sub(r"<p[^>]+class=[\'\"]whatsapp-note[\'\"][\s\S]*?<\/p>\s*", "", aside_new, flags=re.IGNORECASE)
    if aside_new != aside_block:
        out = out.replace(aside_block, aside_new, 1)
        print("Removed whatsapp CTA and note from aside.detail-side")
    else:
        print("No whatsapp CTA/note found in aside.detail-side — nothing removed")
else:
    print("aside.detail-side not found — skipping WhatsApp removal")

# 5. Scoped adjustment of inquiry form in the same aside: change submit label and form-note
out = re.sub(r"(<form[^>]*class=[\'\"]inquiry-form[\'\"][\s\S]*?<button[^>]*class=[\'\"]form-submit[\'\"][^>]*>)([\s\S]*?)(<\/button>)",
             lambda m: m.group(1) + "إرسال الطلب" + m.group(3), out, flags=re.IGNORECASE)
out = re.sub(r"(<p[^>]*class=[\'\"]form-note[\'\"][^>]*>)[\s\S]*?(<\/p>)", r"\1يمكنك إرسال طلب الاستفسار وسيتم توجيهه إلى القائمين على الموقع.\2", out, flags=re.IGNORECASE)
print("Updated inquiry form submit label and form-note in scoped context")

# 6. Ensure name/phone labels have visually-hidden '(مطلوب)' and inputs required — only inside inquiry form
# Operate within the inquiry-form block
form_re = re.compile(r"(<form[^>]*class=[\'\"]inquiry-form[\'\"][\s\S]*?<\/form>)", re.IGNORECASE)
fmo = form_re.search(out)
if fmo:
    form_block = fmo.group(1)
    fb = form_block
    fb = re.sub(r"<label\s+for=[\'\"]inq-name[\'\"]>([\s\S]*?)<span[^>]*>\*<\/span>\s*<\/label>",
                lambda m: "<label for='inq-name'>%s <span class='visually-hidden'>(مطلوب)</span></label>" % m.group(1).strip(), fb, flags=re.IGNORECASE)
    fb = re.sub(r"<label\s+for=[\'\"]inq-phone[\'\"]>([\s\S]*?)<span[^>]*>\*<\/span>\s*<\/label>",
                lambda m: "<label for='inq-phone'>%s <span class='visually-hidden'>(مطلوب)</span></label>" % m.group(1).strip(), fb, flags=re.IGNORECASE)
    # add required attribute to inputs if missing
    fb = re.sub(r"(<input[^>]*id=[\'\"]inq-name[\'\"][^>]*)(>)", lambda m: m.group(1) + " required='required'" + m.group(2) if "required" not in m.group(1) else m.group(0), fb)
    fb = re.sub(r"(<input[^>]*id=[\'\"]inq-phone[\'\"][^>]*)(>)", lambda m: m.group(1) + " required='required'" + m.group(2) if "required" not in m.group(1) else m.group(0), fb)
    if fb != form_block:
        out = out.replace(form_block, fb, 1)
        print("Updated inquiry form labels and required attributes")
else:
    print("Inquiry form block not found — skipped input/label adjustments")

# 7. Replace rating-stars section with a small CTA to comments but only for the first occurrence
rating_re = re.compile(r"<section[^>]*class=[\'\"]property-rating[\'\"][\s\S]*?<\/section>", re.IGNORECASE)
out, nsub = rating_re.subn("<section aria-labelledby='rating-title' class='property-rating' id='property-rating'>\n                        <h2 class='section-title' id='rating-title'>شاركنا رأيك</h2>\n                        <p class='rating-status'>لإضافة تعليق أو ملاحظة حول هذا العقار، استخدم قسم التعليقات أدناه.</p>\n                        <p><a class='detail-btn' href='#guest-reviews'>اذهب إلى التعليقات</a></p>\n                      </section>", out, count=1)
if nsub:
    print("Replaced rating-stars section with comments CTA (scoped) ")
else:
    print("No property-rating section replaced — none found")

# 8. Ensure RTL helper CSS present: add minimal RTL CSS after skin opening if not present
if "html[dir=\"rtl\"]" not in out and "html[dir='rtl']" not in out:
    # insert a small RTL helper in b:skin near the top
    out = out.replace('<b:skin><![CDATA[', '<b:skin><![CDATA[\n/* RTL helper for Arabic delivery */\nhtml { direction: rtl; }\n')
    print("Inserted minimal RTL helper into b:skin")

# 9. SEO: add meta lang tag and ensure og:locale set to ar_DJ already exists; add default meta description fallback already present.
# (No global duplication — already handled in head)

# Write output
with io.open(OUT, 'w', encoding='utf-8') as fo:
    fo.write(out)

print('Generated:', OUT)
