/*
 * Place-dj (بلاَس) — authoritative theme test suite.
 * Targets DarnaDJ_Updated_Package/theme-Place-dj-com.xml (the shipped theme).
 *
 * Covers:
 *   1. XML structural integrity (sections, widgets, hero text, no placeholder form URL).
 *   2. Price logic (base x1.10 once, pricefinal as-is, missing -> null).
 *   3. Label parsing (beds/baths/sqm/type/area/status).
 *   4. Status classification (available / unavailable / unknown).
 *
 * Run: node tests/place_dj_theme.test.js
 */
const fs = require('fs');
const path = require('path');

const XML = path.join(__dirname, '..', 'DarnaDJ_Updated_Package', 'theme-Place-dj-com.xml');
const src = fs.readFileSync(XML, 'utf8');

let pass = 0, fail = 0;
function ok(name, cond, extra) {
  if (cond) { pass++; console.log('  PASS ' + name); }
  else { fail++; console.log('  FAIL ' + name + (extra ? '  -> ' + extra : '')); }
}
function eq(name, got, want) {
  const g = JSON.stringify(got), w = JSON.stringify(want);
  ok(name, g === w, 'got ' + g + ' want ' + w);
}

console.log('\n=== Place-dj theme tests ===\n');

/* ---------- 1. Structural ---------- */
console.log('[structural]');
ok('XML parses', (() => {
  try { require('child_process').execSync(`python3 -c "import xml.dom.minidom as m; m.parse('${XML}')"`, { stdio: 'ignore' }); return true; }
  catch (e) { return false; }
})());
for (const sec of ['header-widgets', 'home-before-posts', 'main-blog', 'home-after-posts', 'sidebar-widgets', 'footer-widgets']) {
  ok(`section present: ${sec}`, src.includes(`id='${sec}'`));
}
for (const wid of ['Blog1', 'Label1', 'HTML2', 'PopularPosts1']) {
  ok(`widget present: ${wid}`, src.includes(`id='${wid}'`));
}
ok('hero H1 exact (بلاَس — اعثر على سكنك في جيبوتي)', src.includes('<h1>بلاَس &#8212; اعثر على سكنك في جيبوتي</h1>'));
ok('hero description exact', src.includes('اكتشف الشقق والفلل والمنازل والاستوديوهات، واستكشف الخيارات المناسبة لك وتواصل معنا للتحقق من التوفر والحجز.'));
ok('browse-by-region has 6 regions', ['جيبوتي المدينة','علي صبيح','تاجورة','أوبوك','أرتا','دخيل'].every(r => src.includes(`search/label/${r}`)));
ok('no placeholder Google Forms URL', !src.includes('docs.google.com/forms'));
ok('add-property URL is a central config', src.includes('window.PLACEDJ_ADD_PROPERTY_URL'));
ok('popular widget titled يفضلها الزائرون', src.includes("title='يفضلها الزائرون'"));
ok('language selector present (ar/en/fr)', src.includes("value='ar'") && src.includes("value='en'") && src.includes("value='fr'"));
ok('RTL/LTR via languageDirection', src.includes("expr:dir='data:blog.languageDirection'"));
ok('search form posts to Blogger searchUrl', src.includes("expr:action='data:blog.searchUrl'"));
ok('comments includable preserved', src.includes("<b:include data='post' name='comments'/>"));

/* ---------- 2/3/4. Extract & evaluate the theme JS ---------- */
console.log('\n[logic]');
const m = src.match(/<script type='text\/javascript'>\s*\/\/<!\[CDATA\[([\s\S]*?)\/\/\]\]>\s*<\/script>/);
ok('theme JS block found', !!m);
if (m) {
  const js = m[1];
  // Minimal DOM/browser shims so the IIFE runs and exposes its internals.
  const noop = () => {};
  const emptyList = () => ({ forEach: noop, length: 0 });
  const documentShim = {
    readyState: 'complete',
    querySelectorAll: emptyList,
    querySelector: () => null,
    getElementById: () => null,
    createElement: () => ({ setAttribute: noop, appendChild: noop, addEventListener: noop, style: {}, classList: { add: noop, remove: noop, toggle: noop } }),
    addEventListener: noop,
    createTreeWalker: () => ({ nextNode: () => null }),
    createDocumentFragment: () => ({ appendChild: noop }),
    createTextNode: (t) => ({ nodeValue: t })
  };
  const windowShim = {};
  const sandbox = {
    window: windowShim,
    document: documentShim,
    localStorage: { getItem: () => null, setItem: noop },
    NodeFilter: { SHOW_TEXT: 4 },
    setTimeout: noop, clearTimeout: noop,
    fetch: () => Promise.reject(new Error('no-network')),
    encodeURIComponent, parseInt, parseFloat, isFinite, Math, String, Array, JSON, Object, RegExp, Error, Promise
  };
  let api = null, evalErr = null;
  try {
    const runner = new Function('window', 'document', 'localStorage', 'NodeFilter', 'setTimeout', 'clearTimeout', 'fetch', js + '\n;return window;');
    api = runner(sandbox.window, sandbox.document, sandbox.localStorage, sandbox.NodeFilter, sandbox.setTimeout, sandbox.clearTimeout, sandbox.fetch);
  } catch (e) { evalErr = e; }
  ok('theme JS executes without error', !evalErr, evalErr && evalErr.message);

  if (api) {
    // Price logic
    eq('price:100 cur:USD per:night -> 110 USD', api.darnaComputePrice(['price:100','cur:USD','per:night']), { amount: 110, currency: 'USD', per: 'night', source: 'base' });
    eq('pricefinal:110 -> 110 (no extra fee)', api.darnaComputePrice(['pricefinal:110','cur:USD']), { amount: 110, currency: 'USD', per: '', source: 'final' });
    eq('missing price -> null', api.darnaComputePrice(['cur:USD','type:شقة']), null);
    eq('price:2000 -> 2200', api.darnaComputePrice(['price:2000','cur:USD','per:month']).amount, 2200);
    eq('formatPrice USD/night', api.darnaFormatPrice({ amount: 110, currency: 'USD', per: 'night' }, 'ar'), '$110 / ليلة');
    eq('formatPrice thousands', api.darnaFormatPrice({ amount: 2200, currency: 'USD', per: 'month' }, 'ar'), '$2,200 / شهر');

    // Label parsing
    const f = api.darnaParseFields(['عقارات','للإيجار','جيبوتي المدينة','فيلا','price:100','cur:USD','per:night','type:فيلا','beds:4','baths:3','kitchens:2','sqm:320','status:متوفر']);
    eq('parse type', f.type, 'فيلا');
    eq('parse area', f.area, 'جيبوتي المدينة');
    eq('parse beds', f.beds, '4');
    eq('parse baths', f.baths, '3');
    eq('parse sqm', f.sqm, '320');
    eq('parse status', f.status, 'متوفر');

    // Status classification
    eq('status متوفر -> available', api.darnaStatusClass('متوفر').cls, 'is-available');
    eq('status غير متوفر -> unavailable', api.darnaStatusClass('غير متوفر').cls, 'is-unavailable');
    eq('status empty -> unknown', api.darnaStatusClass('').cls, '');

    // Non-property detection (complaint-style post has NO labels at all)
    const f2 = api.darnaParseFields([]);
    ok('complaint post has no type', !f2.type);
    ok('complaint post has no area', !f2.area);
    // "للإيجار" must never be parsed as a region
    const f3 = api.darnaParseFields(['عقارات','للإيجار','جيبوتي المدينة','فيلا','type:فيلا','beds:2']);
    eq('للإيجار not treated as area; real region wins', f3.area, 'جيبوتي المدينة');
  }
}

console.log(`\n=== RESULT: ${pass} passed, ${fail} failed ===\n`);
process.exit(fail ? 1 : 0);
