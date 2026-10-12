# Darna DJ — Unified Price Labels (Single Source of Truth)

The Blogger theme (`IMPORT_THIS_THEME.xml`) renders **one numeric final price** on
every property card and on the property detail page. The price is read from
structured **post labels**, so the same value is always used everywhere and the
tenant service fee is applied **exactly once**.

## Label convention

Add these labels to a property post (Blogger → post → Labels). The separator may
be `:`, `-` or `_` (e.g. `price:100`, `price-100`, `price_100`).

| Label | Meaning |
|-------|---------|
| `price:100` | **Base price BEFORE** the 10% tenant service fee. Displayed = `base × 1.10`. |
| `pricefinal:110` | **Final price ALREADY including** the 10% fee. Displayed as-is (no extra). |
| `cur:USD` | Currency code (default `USD`). |
| `per:night` | Pricing unit: `night`, `day`, `week`, `month`, `stay`. |

Optional basic-facts labels (rendered as chips on the card/detail meta):
`beds:2`, `baths:1`, `cap:4`.

## Rules enforced

1. **One source of truth.** Cards, detail page and all three languages use the
   same computation (`darnaComputePrice`).
2. **Fee applied once.** If only `price:` is present → `final = base × 1.10`.
   If `pricefinal:` is present → displayed as-is. If both are present,
   `pricefinal:` wins, so the 10% is never applied twice.
3. **No fabricated price.** If neither label is present, or the value is not a
   number, the theme shows a clear **admin data-missing** state
   (`⚠ بيانات السعر غير مكتملة …`) instead of `0` or a guessed value.
4. **Always show the numeric price.** The numeric price is always shown from
   the property data; it is never replaced by a generic request.
5. **Fee disclosure** stays on the policy page (`fees.html`). Cards/detail only
   carry a positive “fees included” badge — never a note implying the fee is
   not already included.

## Worked examples

- `price:100` + `cur:USD` + `per:night` → **110 USD / night** (100 × 1.10).
- `pricefinal:110` + `cur:USD` + `per:night` → **110 USD / night** (unchanged).
- `price:100` + `pricefinal:110` → **110 USD** (no double fee).
- no price label → admin data-missing state (not published as complete).

## Tests

`tests/price_logic.test.js` extracts the shipped functions from the XML and
asserts the rules above:

```
node tests/price_logic.test.js
```
