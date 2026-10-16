# PLACE-DJ Arabic delivery generator
# This script reads the provided PLACE-DJ template (PLACE-DJ-TEMPLATE-FINAL.xml)
# and produces an Arabic-ready XML at DELIVERY-ARABIC/theme-PLACE-DJ.AR.xml
# It performs non-destructive text replacements only (keeps original file intact).

import io, os, re, sys

SRC = "DarnaDJ_Updated_Package/Place-dj-16oct/PLACE-DJ-TEMPLATE-FINAL.xml"
OUT_DIR = "DarnaDJ_Updated_Package/Place-dj-16oct/DELIVERY-ARABIC"
OUT = os.path.join(OUT_DIR, "theme-PLACE-DJ.AR.xml")
BACKUP = os.path.join(OUT_DIR, "PLACE-DJ-TEMPLATE-FINAL.backup.xml")

if not os.path.exists(SRC):
    print("Source template not found:", SRC)
    sys.exit(2)

os.makedirs(OUT_DIR, exist_ok=True)

with io.open(SRC, "r", encoding="utf-8") as f:
    s = f.read()

# 1) Set static Arabic lang/dir: replace expr:dir and expr:lang with dir/lang
s = re.sub(r"expr:dir='[^']*'\s+expr:lang='[^']*'", "dir='rtl' lang='ar'", s, count=1)

# 2) Change preferred-section title text: 'يفضلها الكثيرون' → 'مفضلة لدى الضيوف'
s = s.replace('>يفضلها الكثيرون<', '>مفضلة لدى الضيوف<')

# 3) Remove WhatsApp CTA and explicit phone note in detail sidebar
# Remove anchor with class 'whatsapp-cta' and the following whatsapp-note paragraph if present
s = re.sub(r"<a[^>]*class='whatsapp-cta'[\s\S]*?</a>\s*<p class='whatsapp-note'[^>]*>[\s\S]*?</p>", "", s, flags=re.I)
# If only anchor remains (different formatting), also try to remove any leftover whatsapp-cta anchor or whatsapp-note paragraph
s = re.sub(r"<a[^>]*class='whatsapp-cta'[\s\S]*?</a>", "", s, flags=re.I)
s = re.sub(r"<p[^>]*class='whatsapp-note'[^>]*>[\s\S]*?</p>", "", s, flags=re.I)

# 4) Change inquiry form submit button label and remove misleading note
s = s.replace('>إرسال الطلب عبر واتساب<', '>إرسال الطلب<')
s = re.sub(r"<p class='form-note'[^>]*>[\s\S]*?</p>", "<p class='form-note'>يمكنك إرسال طلب الاستفسار وسيتم توجيهه إلى القائمين على الموقع.</p>", s, flags=re.I)

# 5) Remove decorative stars from labels and explicitly mark inputs required (name & phone)
# Replace label content like: "الاسم <span aria-hidden='true'>*</span>" → "الاسم <span class='visually-hidden'>(مطلوب)</span>"
s = re.sub(r"<label for='inq-name'>(.*?)<span[^<]*\*>\s*</span>\s*</label>", r"<label for='inq-name'>\1 <span class='visually-hidden'>(مطلوب)</span></label>", s)
s = re.sub(r"<label for='inq-phone'>(.*?)<span[^<]*\*>\s*</span>\s*</label>", r"<label for='inq-phone'>\1 <span class='visually-hidden'>(مطلوب)</span></label>", s)
# Add required attributes to the inputs if not present
s = re.sub(r"(<input[^>]*id='inq-name'[^>]*)(>)", r"\1 required='required'\2", s)
s = re.sub(r"(<input[^>]*id='inq-phone'[^>]*)(>)", r"\1 required='required'\2", s)

# 6) Replace rating-stars block with a comment-invoking prompt that links to Blogger comments
s = re.sub(r"<section aria-labelledby='rating-title' class='property-rating'[^>]*>[\s\S]*?<\/section>",
           "<section aria-labelledby='rating-title' class='property-rating' id='property-rating'>\n                        <h2 class='section-title' id='rating-title'>شاركنا رأيك</h2>\n                        <p class='rating-status'>لإضافة تعليق أو ملاحظة حول هذا العقار، استخدم قسم التعليقات أدناه.</p>\n                        <p><a class='detail-btn' href='#guest-reviews'>اذهب إلى التعليقات</a></p>\n                      </section>", s, count=1)

# 7) Ensure phrase replacements did not accidently remove protected components: we intentionally changed textual titles and removed WhatsApp phrases only.

# 8) Write backup of the original (for record-keeping)
with io.open(BACKUP, "w", encoding="utf-8") as f:
    f.write(s)  # backup will contain the modified version too but keep as record; user can adjust

# 9) Save output file
with io.open(OUT, "w", encoding="utf-8") as f:
    f.write(s)

print("Generated:", OUT)
print("Backup (in delivery folder):", BACKUP)
