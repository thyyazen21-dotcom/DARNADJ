/*
 * Darna DJ — price logic test.
 * Extracts the real price functions from the shipped Blogger theme XML and
 * asserts the unified, fee-inclusive price rules:
 *   - base price (price:)   -> final = base * 1.10  (10% tenant fee applied ONCE)
 *   - inclusive (pricefinal:)-> displayed as-is      (no second increase)
 *   - missing price          -> null                 (admin data-missing state, no fabrication)
 * Run: node tests/price_logic.test.js
 */
const fs = require('fs');
const path = require('path');

const XML = path.join(__dirname, '..', 'project-bolt-sb1-qvsojasd', 'project',
  'DarnaDJ_Delivery_Package', 'theme', 'IMPORT_THIS_THEME.xml');
const src = fs.readFileSync(XML, 'utf8');

const start = src.indexOf('var DARNA_SERVICE_FEE_RATE');
const end = src.indexOf('// Expose for testing');
if (start < 0 || end < 0) { console.error('FAIL: could not locate price logic in XML'); process.exit(1); }
const block = src.slice(start, end);

// Evaluate the extracted block in an isolated scope.
const sandbox = {};
const fn = new Function('window', block + '\nreturn { darnaComputePrice: darnaComputePrice, darnaFormatPrice: darnaFormatPrice, darnaParsePriceLabels: darnaParsePriceLabels };');
const api = fn(sandbox);

let pass = 0, fail = 0;
function eq(name, got, want) {
  const g = JSON.stringify(got), w = JSON.stringify(want);
  if (g === w) { pass++; console.log('  PASS ' + name); }
  else { fail++; console.log('  FAIL ' + name + '\n       got  ' + g + '\n       want ' + w); }
}

console.log('Darna DJ price logic tests\n');

// 1) base price -> 100 becomes 110 (fee once)
eq('price:100 cur:USD per:night -> 110 USD',
  api.darnaComputePrice(['price:100', 'cur:USD', 'per:night']),
  { amount: 110, currency: 'USD', per: 'night', source: 'base' });

// 2) inclusive price -> unchanged
eq('pricefinal:110 -> 110 (no increase)',
  api.darnaComputePrice(['pricefinal:110', 'cur:USD', 'per:night']),
  { amount: 110, currency: 'USD', per: 'night', source: 'final' });

// 3) inclusive wins over base if both present (never double charge)
eq('pricefinal wins over price',
  api.darnaComputePrice(['price:100', 'pricefinal:110']),
  { amount: 110, currency: 'USD', per: '', source: 'final' });

// 4) default currency USD
eq('default currency is USD',
  api.darnaComputePrice(['price:50']),
  { amount: 55, currency: 'USD', per: '', source: 'base' });

// 5) missing price -> null (no fabrication, no zero)
eq('no price label -> null',
  api.darnaComputePrice(['شقة', 'جيبوتي المدينة']),
  null);

// 6) empty -> null
eq('empty labels -> null', api.darnaComputePrice([]), null);

// 7) alternate separators accepted
eq('price-100 / cur-USD / per-night',
  api.darnaComputePrice(['price-100', 'cur-USD', 'per-night']),
  { amount: 110, currency: 'USD', per: 'night', source: 'base' });
eq('price_100 / per_month',
  api.darnaComputePrice(['price_100', 'per_month']),
  { amount: 110, currency: 'USD', per: 'month', source: 'base' });

// 8) decimals
eq('price:99.5 -> 109.45',
  api.darnaComputePrice(['price:99.5']),
  { amount: 109.45, currency: 'USD', per: '', source: 'base' });

// 9) formatting
eq('format AR', api.darnaFormatPrice({ amount: 110, currency: 'USD', per: 'night' }, 'ar'), '$110 / ليلة');
eq('format AR month + thousands separator', api.darnaFormatPrice({ amount: 1100, currency: 'USD', per: 'month' }, 'ar'), '$1,100 / شهر');
eq('format EN', api.darnaFormatPrice({ amount: 110, currency: 'USD', per: 'night' }, 'en'), '$110 / night');
eq('format FR', api.darnaFormatPrice({ amount: 110, currency: 'USD', per: 'night' }, 'fr'), '$110 / nuit');
eq('format no unit', api.darnaFormatPrice({ amount: 55, currency: 'EUR', per: '' }, 'en'), '€55');

// 10) non-numeric price -> null (no fabrication)
eq('price:abc -> null', api.darnaComputePrice(['price:abc']), null);

console.log('\n' + pass + ' passed, ' + fail + ' failed');
process.exit(fail === 0 ? 0 : 1);
