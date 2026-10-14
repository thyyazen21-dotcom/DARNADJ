# -*- coding: utf-8 -*-
"""Stage 3 — JS upgrades: darnaInitTopPicks, darnaInitRating, wiring, note replacement.
NOTE: this theme stores JS string Arabic as LITERAL UTF-8 (regexes use \\uXXXX)."""
import io, sys
PATH = 'DarnaDJ_Updated_Package/theme-Place-dj-com.xml'
data = io.open(PATH, 'r', encoding='utf-8').read()

def apply(name, old, new, expect=1):
    global data
    n = data.count(old)
    if n != expect:
        print('!! FAIL [%s]: expected %d, found %d' % (name, expect, n))
        print('   old head:', repr(old[:160]))
        sys.exit(1)
    data = data.replace(old, new)
    print('OK  [%s]' % name)

# ---------------- 1) Replace the Google Forms JS note with marketing copy ----------------
old_note = 'نموذج Google Forms قيد التجهيز من حساب المالك. حاليًا يُرسل طلبك عبر واتساب، وتُراجع الإدارة العقار قبل النشر.'
new_note = 'أضف عقارك ليصل إلى الباحثين عن سكن في جيبوتي — تُراجع الإدارة العقار قبل النشر.'
apply('U6 JS add-property note', old_note, new_note)

# ---------------- 2) Insert new JS functions before the Init block ----------------
INIT_MARK = '  /* ================= Init ================= */\n  function darnaInit() {'
assert data.count(INIT_MARK) == 1, 'init marker count=%d' % data.count(INIT_MARK)

NEW_JS = r"""
  /* ================= Top picks rail (editorial, manually configurable) ================= */
  // CURATION: set window.PLACEDJ_TOP_PICKS to an array of post URLs (or unique parts of
  // them). Only REAL posts already present on this page are shown. If left empty, the rail
  // shows the first available real properties (an editorial default). This section NEVER
  // fabricates view counts and does NOT claim to be sorted by views.
  window.PLACEDJ_TOP_PICKS = window.PLACEDJ_TOP_PICKS || [];
  function darnaInitTopPicks() {
    var rail = document.getElementById('top-picks-rail');
    var section = document.getElementById('top-picks-section');
    if (!rail || !section) return;
    var grid = document.getElementById('property-grid');
    var pool = grid ? Array.prototype.slice.call(grid.querySelectorAll('.property-card')) : [];
    if (!pool.length) return; // nothing real to show -> keep the section hidden
    var configured = Array.isArray(window.PLACEDJ_TOP_PICKS) ? window.PLACEDJ_TOP_PICKS : [];
    var chosen = [];
    configured.forEach(function (u) {
      if (!u) return;
      var m = pool.filter(function (c) {
        var cu = c.getAttribute('data-url') || '';
        return cu === u || cu.indexOf(u) !== -1;
      })[0];
      if (m && chosen.indexOf(m) === -1) chosen.push(m);
    });
    if (!chosen.length) chosen = pool.slice(0, 6);
    function txt(cls, s) { var e = document.createElement('span'); e.className = cls; e.textContent = s; return e; }
    chosen.forEach(function (card) {
      var rec = darnaRecordFrom(card);
      var art = document.createElement('article');
      art.className = 'top-pick-card';
      art.setAttribute('role', 'listitem');
      var a = document.createElement('a');
      a.className = 'top-pick-link';
      a.setAttribute('href', rec.url || '#');
      var media = document.createElement('span');
      media.className = 'top-pick-media';
      if (rec.image) {
        var img = document.createElement('img');
        img.setAttribute('src', rec.image);
        img.setAttribute('alt', rec.title || '');
        img.setAttribute('loading', 'lazy');
        media.appendChild(img);
      } else {
        media.appendChild(txt('top-pick-noimg', 'لا توجد صورة'));
      }
      a.appendChild(media);
      var body = document.createElement('span');
      body.className = 'top-pick-body';
      body.appendChild(txt('top-pick-title', rec.title || ''));
      var meta = [rec.type, rec.area].filter(function (x) { return x; }).join(' · ');
      body.appendChild(txt('top-pick-meta', meta));
      var price = rec.price ? (rec.price + (rec.unit ? ' / ' + rec.unit : '')) : '';
      body.appendChild(txt('top-pick-price', price));
      a.appendChild(body);
      art.appendChild(a);
      rail.appendChild(art);
    });
    section.hidden = false;
  }

  /* ================= Ratings (per-device; integratable with an external service) ================= */
  // STORAGE: ratings are saved in THIS browser's localStorage only (per device, per post).
  // They are NOT shared between visitors. To collect shared ratings, connect an external
  // service by setting window.PLACEDJ_RATINGS_ENDPOINT to a URL that accepts
  // POST {postId, value, comment}. No secrets are placed in this public script.
  window.PLACEDJ_RATINGS_ENDPOINT = window.PLACEDJ_RATINGS_ENDPOINT || '';
  var RATING_STORE = 'placedj_ratings_v1';
  function darnaRatingPostId() {
    var art = document.querySelector('.property-detail');
    var id = art && art.getAttribute('data-post-id');
    return id || (window.location.pathname || 'post');
  }
  function darnaRatingKey() { return RATING_STORE + '::' + darnaRatingPostId(); }
  function darnaReadRatings() {
    try { var raw = localStorage.getItem(darnaRatingKey()); var arr = raw ? JSON.parse(raw) : []; return Array.isArray(arr) ? arr : []; }
    catch (e) { return []; }
  }
  function darnaWriteRatings(list) {
    try { localStorage.setItem(darnaRatingKey(), JSON.stringify(list)); return true; } catch (e) { return false; }
  }
  function darnaInitRating() {
    var form = document.getElementById('rating-form');
    var input = document.getElementById('rating-input');
    if (!form || !input) return;
    var stars = Array.prototype.slice.call(input.querySelectorAll('.rating-star'));
    var current = 0;
    function paint(v) {
      stars.forEach(function (s) {
        var sv = parseInt(s.getAttribute('data-value'), 10);
        s.classList.toggle('is-on', sv <= v);
        s.setAttribute('aria-checked', sv === current ? 'true' : 'false');
      });
    }
    function setCurrent(v) { current = v; paint(v); }
    stars.forEach(function (s, i) {
      s.addEventListener('click', function () { setCurrent(parseInt(s.getAttribute('data-value'), 10)); });
      s.addEventListener('mouseenter', function () { paint(parseInt(s.getAttribute('data-value'), 10)); });
      s.addEventListener('focus', function () { paint(parseInt(s.getAttribute('data-value'), 10)); });
      s.addEventListener('keydown', function (e) {
        var k = e.key;
        if (k === 'ArrowRight' || k === 'ArrowUp') { e.preventDefault(); if (stars[i + 1]) stars[i + 1].focus(); }
        else if (k === 'ArrowLeft' || k === 'ArrowDown') { e.preventDefault(); if (stars[i - 1]) stars[i - 1].focus(); }
        else if (k === 'Enter' || k === ' ') { e.preventDefault(); setCurrent(parseInt(s.getAttribute('data-value'), 10)); }
      });
    });
    input.addEventListener('mouseleave', function () { paint(current); });
    var avgEl = document.getElementById('rating-avg');
    var countEl = document.getElementById('rating-count');
    var summary = document.getElementById('rating-summary');
    var disp = document.getElementById('rating-stars-display');
    var listWrap = document.getElementById('rating-list-wrap');
    var listEl = document.getElementById('rating-list');
    var feedback = document.getElementById('rating-feedback');
    function starString(n) { var s = ''; for (var i = 0; i < 5; i++) s += (i < n ? '\u2605' : '\u2606'); return s; }
    function render() {
      var list = darnaReadRatings();
      if (list.length) {
        var sum = list.reduce(function (a, r) { return a + (parseInt(r.v, 10) || 0); }, 0);
        var avg = sum / list.length;
        if (avgEl) avgEl.textContent = avg.toFixed(1);
        if (disp) disp.textContent = starString(Math.round(avg));
        if (countEl) countEl.textContent = '(' + list.length + ')';
        if (summary) summary.hidden = false;
        if (listWrap) listWrap.hidden = false;
        if (listEl) {
          listEl.innerHTML = '';
          list.slice().reverse().forEach(function (r) {
            var li = document.createElement('li');
            li.className = 'rating-item';
            var st = document.createElement('span');
            st.className = 'rating-item-stars';
            st.textContent = starString(parseInt(r.v, 10) || 0);
            li.appendChild(st);
            if (r.c) { var c = document.createElement('span'); c.className = 'rating-item-text'; c.textContent = r.c; li.appendChild(c); }
            listEl.appendChild(li);
          });
        }
      } else {
        if (summary) summary.hidden = true;
        if (listWrap) listWrap.hidden = true;
      }
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!current) { if (feedback) feedback.textContent = 'اختر عدد النجوم أولاً.'; return; }
      var commentEl = document.getElementById('rating-comment');
      var comment = commentEl ? String(commentEl.value || '').trim().slice(0, 500) : '';
      var list = darnaReadRatings();
      var entry = { v: current, c: comment, t: Date.now(), self: true };
      var mineIdx = -1;
      for (var i = 0; i < list.length; i++) { if (list[i] && list[i].self) { mineIdx = i; break; } }
      if (mineIdx >= 0) list[mineIdx] = entry; else list.push(entry); // anti-abuse: one entry per device
      var saved = darnaWriteRatings(list);
      if (window.PLACEDJ_RATINGS_ENDPOINT) {
        try {
          fetch(window.PLACEDJ_RATINGS_ENDPOINT, {
            method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ postId: darnaRatingPostId(), value: current, comment: comment })
          }).catch(function () { });
        } catch (e) { }
      }
      render();
      if (feedback) feedback.textContent = saved ? 'شكرًا لك! تم حفظ تقييمك على هذا الجهاز.' : 'تعذّر حفظ التقييم على هذا الجهاز.';
      if (commentEl) commentEl.value = '';
      setCurrent(0);
    });
    render();
  }

"""

data = data.replace(INIT_MARK, NEW_JS + INIT_MARK)
print('OK  [U3+U4 insert JS functions]')

# ---------------- 3) Wire the new functions into darnaInit ----------------
apply('U3/U4 wire into darnaInit',
'    darnaInitFilters();\n    darnaInitFavorites();',
'    darnaInitFilters();\n    darnaInitTopPicks();\n    darnaInitRating();\n    darnaInitFavorites();')

# ---------------- 4) Rating summary label (honest, per-device wording) ----------------
apply('U4 summary label',
"                    <div class='rating-summary' hidden='hidden' id='rating-summary'>\n                      <span class='rating-avg' id='rating-avg'>\u2014</span>",
"                    <div class='rating-summary' hidden='hidden' id='rating-summary'>\n                      <span class='rating-avg-label'>متوسط تقييماتك على هذا الجهاز:</span>\n                      <span class='rating-avg' id='rating-avg'>\u2014</span>")

# ---------------- 5) CSS for the new label ----------------
apply('U4 label CSS',
'  .rating-count { color: $(muted.color); font-size: .9rem; }',
'  .rating-count { color: $(muted.color); font-size: .9rem; }\n  .rating-avg-label { font-size: .85rem; color: $(muted.color); }')

io.open(PATH, 'w', encoding='utf-8').write(data)
print('--- Stage 3 done. len =', len(data))
