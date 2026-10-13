# Changelog — DARNADJ

## 2026-10-13 — Production recovery: layout, cards, gallery, detail, filters, form, SEO

### Theme — `project-bolt-sb1-qvsojasd/project/DarnaDJ_Delivery_Package/theme/IMPORT_THIS_THEME.xml`
- **Layout editor fixed:** added an isolated `body#layout` CSS block so the Blogger
  Layout editor no longer inherits visitor layout (flex/overflow/sticky). Admin-only
  rules are scoped to `body#layout`; visitor rules are untouched.
- **Sections:** 6 `b:section` regions — `header-widgets`, `home-before-posts`,
  `main-blog` (Blog1), `home-after-posts`, `sidebar-widgets`, `footer-widgets` —
  with `showaddelement`/`maxwidgets` so widgets can be arranged without breaking.
- **Cards:** responsive CSS Grid (3 cols ≥1100px, 2 default, 1 ≤768px); horizontal
  4:3 images with `object-fit: cover`; no fixed heights clipping titles/prices;
  RTL preserved; no horizontal overflow.
- **Price:** clean USD display `$1,100` / `$1,100 / شهر` (thousands separator +
  unit). The two forbidden visitor-facing messages are **removed** (0 occurrences):
  the admin "price incomplete" notice and the "final price includes platform
  service fee (10%)" notice. 10% fee applied exactly once.
- **Status vs deal:** availability badge (متوفر / غير متوفر) separated from the
  deal ribbon (للإيجار / للبيع) via `darnaStatusClass` + new `darnaDealClass`.
- **Per-card gallery:** prev/next, `n / m` counter, touch/swipe, mouse, keyboard;
  buttons never navigate to the post; each card isolated; lazy loading; handles
  1 image / missing images.
- **Detail page:** title, price + status + deal, main gallery, specs bar with icons
  (beds/baths/kitchens/area/type/area-name), description, amenities, location,
  terms, contact + inquiry form, similar properties.
- **Inquiry form:** name, phone, request type (rent/buy/inquiry), check-in/out
  dates, guests, message, auto-filled property name; Arabic validation errors;
  double-submit guard; generates an organised WhatsApp message with property name
  + post link to the official `+25377313443`; clarifies WhatsApp ≠ booking.
- **Filters:** text (Arabic-normalised), type, area, sale/rent, available/unavailable,
  min/max price, beds, baths, sort asc/desc, reset, result count, empty state.
- **SEO/a11y/perf:** Open Graph + Twitter card + theme-color + valid JSON-LD
  (BlogPosting on posts, WebSite on home); no misleading schema fields.

### Sample content — `DarnaDJ_Updated_Package/06_Sample_Content/`
- All 12 posts re-enriched with structured labels
  (`type:` `beds:` `baths:` `kitchens:` `sqm:` `status:`); sale/unavailable set.
- **Forbidden fee messages removed from every post body**; the fee price line is
  replaced by a clean USD line (`السعر: $1,100 / شهر`) and the WhatsApp CTA text
  is regenerated without fee language.
- Regenerated `DarnaDJ_12_Posts_Content.json` / `.csv` / `_AR.html` and the 12
  per-post `sample_posts_html/*.html` copy-paste files.

### Tests
- `tests/price_logic.test.js`: 15/15 pass.
- `tests/sample_posts.test.js`: 111/111 pass (adds a per-post assertion that the
  body contains **no** forbidden fee message and shows the clean USD price).

## 2026-10-12 — Sample content pack (12 posts)

### New — `DarnaDJ_Updated_Package/06_Sample_Content/`
- `DarnaDJ_12_Posts_Content_AR.html`: formatted (RTL) pack for 12 property posts —
  title, Blogger labels, 3 images each, and a full copy-paste HTML body per post.
- `DarnaDJ_12_Posts_Content.csv` / `.json`: the same 12 posts in structured form
  (property id, area, type, price label, base/final price, currency, unit, labels,
  image URLs, body HTML).
- `images/`: 36 placeholder JPEGs (3 per property), verified real-estate photos.
- `README.md`: usage + price-rule notes.
- Prices follow the unified convention: `price:` (base → ×1.10 once) or
  `pricefinal:` (already inclusive → as-is); `cur:` + `per:` for currency/unit.
- Verified: `tests/sample_posts.test.js` runs every post's labels through the
  theme's real price functions — 99/99 checks pass.

## 2026-10-12 — Final delivery execution (fee-inclusive pricing)

### Theme — `project-bolt-sb1-qvsojasd/project/DarnaDJ_Delivery_Package/theme/IMPORT_THIS_THEME.xml`
- **PopularPosts1 widget fix:** `numPostsToShow` → `numItemsToShow` (value `5`).
  `Blog` widgets keep their valid `numPostsToShow` settings.
- **Unified, fee-inclusive price logic** added (`darnaComputePrice` /
  `darnaFormatPrice` / `darnaRenderPrices`), reading structured labels
  `price:` / `pricefinal:` / `cur:` / `per:`. The 10% tenant service fee is
  applied **exactly once**; an already-inclusive price is shown as-is.
- **Cards (homepage + search):** show the numeric final price + currency +
  pricing unit; price-related labels are hidden from the meta chips; added a
  “fees included” badge. Removed the earlier note that implied the fee is
  not already part of the displayed price.
- **Detail page:** shows the **same** final price as the card (no difference,
  no double charge). Fee disclosure rewritten to state the price is final and
  inclusive. Gallery kept intact.
- **Card image:** changed from square `1:1` to horizontal `4:3`
  (`resizeImage(..., 600, "4:3")` + `aspect-ratio: 4 / 3`).
- **Missing data:** clear admin state instead of a fabricated/zero price or
  a generic placeholder.

### Policy pages — `content_templates/static_pages/`
- `fees.html`: tenant service fee is now described as **included in the
  displayed price**; example updated (base 100 → displayed 110; inclusive 110
  shown as-is). Owner commission unchanged. Added the label convention.
- `terms.html`: prices section updated to final, fee-inclusive pricing.

### Language templates — `DarnaDJ_Updated_Package/05_Content_Templates/`
- AR / EN / FR property-post templates now show the **final, fee-inclusive**
  price and document the label convention.

### Docs & tests
- `theme/PRICE_LABELS.md`: documents the label convention and rules.
- `tests/price_logic.test.js`: extracts the shipped price functions from the XML
  and asserts 14 cases (100 → 110, inclusive → as-is, missing → null, etc.).
