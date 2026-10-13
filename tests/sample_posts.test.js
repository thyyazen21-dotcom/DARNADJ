/*
 * DARNADJ — sample content validation.
 * Runs every generated post's Blogger labels through the REAL price functions
 * shipped in the theme XML, and checks the body matches the computed price.
 * Run: node tests/sample_posts.test.js
 */
const fs = require('fs');
const path = require('path');

const XML = path.join(__dirname, '..', 'project-bolt-sb1-qvsojasd', 'project',
  'DarnaDJ_Delivery_Package', 'theme', 'IMPORT_THIS_THEME.xml');
const JSONF = path.join(__dirname, '..', 'DarnaDJ_Updated_Package', '06_Sample_Content',
  'DarnaDJ_12_Posts_Content.json');

const src = fs.readFileSync(XML, 'utf8');
const start = src.indexOf('var DARNA_SERVICE_FEE_RATE');
const end = src.indexOf('// Expose for testing');
const block = src.slice(start, end);
const api = new Function('window', block +
  '\nreturn { darnaComputePrice: darnaComputePrice, darnaFormatPrice: darnaFormatPrice };')({});

const data = JSON.parse(fs.readFileSync(JSONF, 'utf8'));
let pass = 0, fail = 0;
function ok(name, cond, extra) {
  if (cond) { pass++; console.log('  PASS ' + name); }
  else { fail++; console.log('  FAIL ' + name + (extra ? '  -> ' + extra : '')); }
}
function fmt(x) { return Number.isInteger(x) ? String(x) : x.toFixed(2); }
function fmtMoney(x) {
  return '$' + (Number.isInteger(x)
    ? x.toLocaleString('en-US')
    : x.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
}

console.log('DARNADJ sample content validation\n');
ok('12 posts generated', data.posts.length === 12, 'got ' + data.posts.length);

for (const p of data.posts) {
  const info = api.darnaComputePrice(p.labels);
  const label = p.pid;
  ok(label + ' price computes', !!info, 'null');
  if (!info) continue;
  ok(label + ' final matches (' + fmt(p.final) + ')', info.amount === p.final,
     'theme=' + info.amount + ' file=' + p.final);
  ok(label + ' currency USD', info.currency === 'USD', info.currency);
  ok(label + ' unit ' + p.per, info.per === p.per, info.per);
  // body shows the same numeric final price (clean USD format, e.g. $1,100 / شهر)
  ok(label + ' body shows final price', p.body.indexOf(fmtMoney(p.final)) >= 0, fmtMoney(p.final));
  // body must NOT contain the two forbidden visitor-facing fee messages (brief Section 3)
  ok(label + ' no forbidden fee message',
     !/شامل رسوم|السعر النهائي|رسوم خدمة المنصة|بيانات السعر غير مكتملة|أضف تسمية/.test(p.body));
  // 3 images, first is the cover/featured
  ok(label + ' has 3 images', p.images.length === 3, p.images.length);
  ok(label + ' body embeds all images',
     p.images.every(u => p.body.indexOf(u) >= 0));
  // no forbidden contact-for-price phrase
  ok(label + ' no contact-for-price', !/تواصل معنا لمعرفة السعر|contact us for price/i.test(p.body));
}

// explicit fee-once checks
const base = data.posts.find(p => p.price_label.startsWith('price:'));
const fin = data.posts.find(p => p.price_label.startsWith('pricefinal:'));
ok('base post applies x1.10 once', base && base.final === Math.round(base.base * 1.1 * 100) / 100);
ok('inclusive post is shown as-is', fin && fin.final === Number(fin.price_label.split(':')[1]));

console.log('\n' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
