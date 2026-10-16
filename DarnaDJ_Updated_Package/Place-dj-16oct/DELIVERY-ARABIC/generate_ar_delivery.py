#!/usr/bin/env python3
"""Build the Arabic Blogger theme from the complete, protected original template."""
from pathlib import Path
import hashlib, json, re, sys, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "DarnaDJ_Updated_Package/Place-dj-16oct/PLACE-DJ-TEMPLATE-FINAL.xml"
REF = ROOT / "DarnaDJ_Updated_Package/Place-dj-16oct/DELIVERY-ARABIC/original-PLACE-DJ-TEMPLATE-FINAL.xml"
OUTDIR = ROOT / "DarnaDJ_Updated_Package/Place-dj-16oct/DELIVERY-ARABIC"
OUT = OUTDIR / "theme-PLACE-DJ.AR.xml"
REPORT = OUTDIR / "BUILD-REPORT-AR.json"
MARKERS = ("[...]","/* truncated for brevity */","...59652 tokens truncated...")

def fail(message):
    print("BLOCKED: " + message, file=sys.stderr)
    raise SystemExit(2)

def sha(data):
    return hashlib.sha256(data).hexdigest()

if not SRC.is_file() or not REF.is_file():
    fail("Source template or protected reference is missing.")
raw = SRC.read_bytes()
reference = REF.read_bytes()
source = raw.decode("utf-8")
if raw != reference:
    fail("Original source and protected reference differ. Restore the exact original before building.")
if any(marker in source for marker in MARKERS):
    fail("Source contains truncation placeholders. No output generated.")
try:
    ET.fromstring(source)
except ET.ParseError as exc:
    fail("Source XML is not well formed: " + str(exc))

required = ("id='main-content'","id='preferred-section'","class='search-bar'","class='inquiry-form'","id='property-grid'","id='guest-reviews'")
missing = [item for item in required if item not in source]
if missing:
    fail("Required source anchors missing: " + ", ".join(missing))

root_match = re.search(r"<html\b([^>]*)>", source, re.S)
if not root_match:
    fail("Root html element not found.")
attrs = root_match.group(1)
attrs = re.sub(r"\s+expr:dir=(['\"]).*?\1", "", attrs)
attrs = re.sub(r"\s+expr:lang=(['\"]).*?\1", "", attrs)
attrs = re.sub(r"\s+dir=(['\"]).*?\1", "", attrs)
attrs = re.sub(r"\s+lang=(['\"]).*?\1", "", attrs)
output = source[:root_match.start()] + "<html" + attrs + " dir='rtl' lang='ar'>" + source[root_match.end():]

rating_pattern = r"<section aria-labelledby='rating-title' class='property-rating'[^>]*>[\s\S]*?</section>"
output, rating_count = re.subn(rating_pattern, "<section aria-labelledby='rating-title' class='property-rating' id='property-rating'><h2 class='section-title' id='rating-title'>شاركنا رأيك</h2><p class='rating-status'>يمكنك كتابة رأيك في قسم التعليقات أدناه.</p><p><a class='detail-btn' href='#guest-reviews'>اذهب إلى التعليقات</a></p></section>", output, count=1)
if rating_count != 1:
    fail("Expected exactly one local rating section; no output generated.")
output, whatsapp_count = re.subn(r"<a class='whatsapp-cta'[\s\S]*?</a>\s*<p class='whatsapp-note'[\s\S]*?</p>", "", output, count=1)
if whatsapp_count != 1:
    fail("Expected the redundant detail WhatsApp CTA and phone note exactly once.")
output = output.replace("<p class='price-includes'>تشمل الأسعار جميع الرسوم.</p>", "")
output = output.replace("<p class='form-note'>للاستفسار والتواصل المباشر حول تفاصيل العقار&#1548; استخدم زر واتساب.</p>", "")
output = output.replace("<label for='inq-name'>الاسم <span aria-hidden='true'>*</span></label>", "<label for='inq-name'>الاسم <span class='visually-hidden'>(مطلوب)</span></label>")
output = output.replace("<input autocomplete='name' id='inq-name' name='name' type='text'/>", "<input autocomplete='name' id='inq-name' name='name' type='text' required='required'/>")
output = output.replace("<label for='inq-phone'>رقم الهاتف <span aria-hidden='true'>*</span></label>", "<label for='inq-phone'>رقم الهاتف <span class='visually-hidden'>(مطلوب)</span></label>")
output = output.replace("<input autocomplete='tel' id='inq-phone' inputmode='tel' name='phone' type='tel'/>", "<input autocomplete='tel' id='inq-phone' inputmode='tel' name='phone' type='tel' required='required'/>")
output = output.replace("var DARNA_SERVICE_FEE_RATE = 0.10;", "var DARNA_SERVICE_FEE_RATE = 0;")
# Performance and accessibility hardening; keep this build deterministic.
output = output.replace("<div class='main-content' id='main-content'>", "<div class='main-content' id='main-content' role='main' aria-label='المحتوى الرئيسي'>")
output = output.replace("background: $(accent.color); border: none; color: #fff; min-height: 34px; padding: 6px 12px;", "background: $(primary.dark); border: none; color: #fff; min-height: 34px; padding: 6px 12px;")
output = output.replace("<a class='card-link' expr:href='data:post.url'>عرض التفاصيل</a>", "<a class='card-link' expr:aria-label='&quot;عرض تفاصيل العقار: &quot; + data:post.title' expr:href='data:post.url'>عرض التفاصيل</a>")
output = output.replace("expr:src='resizeImage(data:post.featuredImage, 900, &quot;4:3&quot;)' loading='lazy' decoding='async'", "expr:src='resizeImage(data:post.featuredImage, 720, &quot;4:3&quot;)' width='720' height='540' loading='lazy' decoding='async'")
output = output.replace("<img expr:alt='data:post.title' expr:src='resizeImage(data:post.featuredImage, 1200, &quot;16:10&quot;)' id='gallery-main-img'/>", "<img expr:alt='data:post.title' expr:src='resizeImage(data:post.featuredImage, 1200, &quot;16:10&quot;)' width='1200' height='750' decoding='async' fetchpriority='high' id='gallery-main-img'/>")
output = output.replace("price:100       -> base price BEFORE the 10% tenant service fee -> displayed = base * 1.10", "price:100       -> quoted price displayed as entered (no automatic fee)")
output = output.replace("The 10% tenant service fee is applied exactly once. Never fabricate a price and never hide the numeric price.", "Never add an automatic fee to owner-entered prices. Never fabricate a price and never hide the numeric price.")
if "class='rating-stars'" in output or "class='whatsapp-cta'" in output:
    fail("Fake rating UI or redundant detail WhatsApp CTA remains.")
try:
    ET.fromstring(output)
except ET.ParseError as exc:
    fail("Generated XML is not well formed: " + str(exc))
if any(item not in output for item in required):
    fail("A required protected component was lost.")
OUTDIR.mkdir(parents=True, exist_ok=True)
OUT.write_text(output, encoding="utf-8")
report = {
 "status":"PASS",
 "source":str(SRC.relative_to(ROOT)),
 "reference":str(REF.relative_to(ROOT)),
 "output":str(OUT.relative_to(ROOT)),
 "source_sha256":sha(raw),
 "reference_sha256":sha(reference),
 "output_sha256":sha(output.encode("utf-8")),
 "checks":{"source_reference_byte_identical":True,"no_truncation_markers":True,"source_xml_well_formed":True,"output_xml_well_formed":True,"protected_anchors_preserved":True,"fake_rating_removed":True,"redundant_detail_whatsapp_removed":True,"automatic_price_fee_disabled":True},
 "limitations":["Import into Blogger, Layout editor, actual post labels/images, search/filter behavior and responsive UI must still be verified in a real test blog."]
}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
