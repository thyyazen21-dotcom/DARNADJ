# VALIDATION_REPORT — DARNADJ

_Generated: 2026-10-13 12:21 UTC — local (sandbox) checks only._

## 1. XML well-formedness
| File | Result |
|------|--------|
| `theme/IMPORT_THIS_THEME.xml` (86,121 bytes) | ✅ well-formed (`xml.dom.minidom`) |

## 2. Automated tests
| Suite | Command | Result |
|-------|---------|--------|
| Price logic | `node tests/price_logic.test.js` | ✅ **15 passed, 0 failed** |
| Sample content | `node tests/sample_posts.test.js` | ✅ **111 passed, 0 failed** |

The price suite extracts the **shipped** JS functions from the XML (between
`var DARNA_SERVICE_FEE_RATE` and `// Expose for testing`) and asserts the 10% fee
is applied exactly once, inclusive prices are shown as-is, and missing prices → `null`.

## 3. Static / structural checks (theme)
| Check | Result |
|-------|--------|
| Forbidden messages in theme (`غير مكتملة`, `شامل رسوم خدمة المنصة`, `السعر النهائي شامل`) | ✅ 0 |
| `<b:section>` count | ✅ 6 |
| `<b:widget>` count | ✅ 5 (Blog1, HTML1, Label1, HTML2, PopularPosts1) |
| `PopularPosts1` setting | ✅ `numItemsToShow` present (Blog keeps `numPostsToShow`) |
| `b:if` / `</b:if>` balance | ✅ 19 / 19 |
| Duplicate HTML `id=` | ✅ only `gallery-main-img` (mutually exclusive `b:if`/`b:else` branches) and includable `id='main'` (Blogger convention) |
| Blogger v3 expressions | ✅ `data:view.isPost/isHomepage/isSearch/isPage`, `data:post.*`, `data:blog.*`, `data:view.title.jsonEscaped` |

## 4. Forbidden fee messages — sample content
| Location | Result |
|----------|--------|
| All of `06_Sample_Content/` (JSON, CSV, AR HTML, per-post HTML, README) | ✅ **0** occurrences of `شامل رسوم` / `السعر النهائي` / `رسوم خدمة المنصة` / `بيانات السعر غير مكتملة` / `أضف تسمية` |
| Post bodies | ✅ fee price line replaced by clean `السعر: $1,100 / شهر`; fee paragraph removed; WhatsApp CTA regenerated without fee language |

## 5. Browser-rendered checks (local static preview on `:8123`)
| Feature | Result |
|---------|--------|
| Homepage grid | ✅ 3 columns, 12 cards, deal chips (للإيجار/للبيع), availability badges (متوفر/غير متوفر) |
| Card specs | ✅ 🛏 beds · 🚿 baths · 🍳 kitchens · 📐 m² |
| Prices | ✅ USD with separator + unit (`$1,100 / شهر`, `$49.50 / ليلة`, `$4,400` sale) |
| Card carousel | ✅ prev/next, counter `1/3` |
| Filters | ✅ deal rent=11 / sale=1; area علي صبيح=2; type شقة=4; unavailable=2; min 1000=8; max 100=3; text فيلا=3; reset=12; sort asc/desc correct |
| Result count / empty state | ✅ "عدد النتائج: 12" |
| Detail page | ✅ title, status متوفر, deal للإيجار/للبيع, specs bar (6 items), description, amenities, contact, similar |
| Inquiry form | ✅ empty submit → Arabic errors; valid submit → `https://wa.me/25377313443?text=…` with property title + type + name + phone + post link; "الإرسال لا يؤكد الحجز" note |
| Fee text in rendered DOM | ✅ none |

## 6. Scope of validation (honest limits)
- These are **local** checks. They do **not** execute inside Blogger.
- Blogger-side rendering, the Layout editor, and widget saving are covered by
  structural/static assertions only; a manual Blogger upload test is recommended
  (see `NEXT_STEPS.md`).
- No backend is involved; the inquiry form opens WhatsApp and stores nothing.

## 7. Result
All local gates pass. The theme and sample content are ready to commit and push.
