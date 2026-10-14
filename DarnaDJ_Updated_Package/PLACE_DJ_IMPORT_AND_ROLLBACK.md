# PLACE_DJ_IMPORT_AND_ROLLBACK.md

> **تعليمات الاستيراد والتراجع** — منصة **بلاَس / Place-dj** (Blogger).

---

## 1. محتويات الحزمة

| الملف | الوصف |
|---|---|
| `theme-Place-dj-com.xml` | **القالب النهائي المُصلَّح** (استورده في Blogger) |
| `_archive/theme-Place-dj-com.original.xml` | **النسخة الأصلية غير المعدّلة** (للتراجع) |
| `PLACE_DJ_EXECUTION_STATE.md` | ملف الحالة الوحيد للاسترداد |
| `PLACE_DJ_TEST_REPORT.md` | تقرير الاختبار (72 ناجح / 0 فاشل) |
| `PLACE_DJ_LIMITATIONS.md` | قائمة القيود والمحدوديات |
| `PLACE_DJ_GOOGLE_FORMS_SPEC.md` | مواصفة Google Forms (محجوب) |
| `PLACE_DJ_IMPORT_AND_ROLLBACK.md` | هذا الملف |

---

## 2. خطوات الاستيراد (Import)

1. **احفظ نسخة احتياطية أولًا:** Blogger → المظهر (Theme) → السهم ▾ → **النسخ الاحتياطي (Backup)** → نزّل النسخة الحالية.
2. Blogger → **المظهر (Theme)** → السهم ▾ بجانب «تخصيص» → **استعادة (Restore)** → ارفع `theme-Place-dj-com.xml`.
3. **الإعدادات:** Settings → Posts → عدد المنشورات في الصفحة الرئيسية (يُفضّل 12+).
4. **العنوان (اختياري للتناسق):** اضبط عنوان المدوّنة إلى «بلاَس».
5. **الصفحات الثابتة المطلوبة** (روابط التذييل/القائمة):
   - `p/contact.html` — تواصل معنا
   - `p/terms.html` — الشروط والأحكام
   - `p/privacy.html` — الخصوصية
   - `p/cancellation.html` — الإلغاء والاسترداد
   - `p/complaints.html` — تقديم شكوى
   - `p/advertise.html` — الإعلان
6. **تسميات المنشورات (Labels):** التزم باصطلاح التسميات الموثّق في ملف الحالة (القسم 3) لعمل الفلاتر:
   `price:` / `pricefinal:` / `cur:USD` / `per:night|month` / `type` / `beds:` / `baths:` / `kitchens:` / `sqm:` / `status:متوفر|غير متوفر` / المنطقة (تسمية عربية عادية).
7. **Google Forms (اختياري لاحقًا):** بعد إنشاء النموذج من حساب المالك، ضع رابطه في `window.PLACEDJ_ADD_PROPERTY_URL` داخل القالب. حتى ذلك الحين يعمل زر «أضف عقارك» عبر واتساب.

---

## 3. خطوات التراجع (Rollback)

**الطريقة 1 — النسخة الأصلية من الحزمة:**
1. Blogger → المظهر → السهم ▾ → **استعادة (Restore)** → ارفع `_archive/theme-Place-dj-com.original.xml`.

**الطريقة 2 — النسخة الاحتياطية من Blogger:**
1. Blogger → المظهر → **النسخ الاحتياطي/الاستعادة** → اختر النسخة الاحتياطية السابقة التي نزّلتها في الخطوة 1 من الاستيراد.

**الطريقة 3 — Git:**
```bash
cd DARNADJ
git checkout b71279d27bb5daa2f263f32919514c70916a74c0 -- DarnaDJ_Updated_Package/theme-Place-dj-com.xml
```

---

## 4. التحقق بعد الاستيراد

1. افتح الصفحة الرئيسية: تأكد من ظهور الـHero بالنص الصحيح، شبكة العقارات، الفلاتر، قسم «تصفّح حسب المنطقة».
2. جرّب البحث الشامل (صندوق البحث في الأعلى) → يجب أن ينقلك إلى `/search?q=...`.
3. جرّب الفلاتر (النوع/المنطقة/الحالة/السعر) → يجب أن يتغيّر عدد النتائج.
4. افتح صفحة عقار مفردة → تأكد من التفاصيل، زر واتساب، التعليقات.
5. جرّب تبديل اللغة (AR/EN/FR) → يجب أن تُحدَّث لغة واجهة Blogger.

---

## 5. أوامر إعادة الاختبار (محليًا)

```bash
node tests/place_dj_theme.test.js       # 41/41
python3 tests/validate_structure.py     # 31/31
cd preview && python3 -m http.server 8124   # ثم افتح /test_theme.html
```
