# Changelog — DARNADJ

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
