# -*- coding: utf-8 -*-
"""Apply the 8 Place-dj targeted production upgrades to the Blogger theme XML."""
import io, sys

PATH = 'DarnaDJ_Updated_Package/theme-Place-dj-com.xml'
data = io.open(PATH, 'r', encoding='utf-8').read()
orig_len = len(data)
changes = []

def u(s):
    """Escape non-ASCII to \\uXXXX (theme JS convention)."""
    return ''.join(('\\u%04x' % ord(c)) if ord(c) > 127 else c for c in s)

def apply(name, old, new, expect=1):
    global data
    n = data.count(old)
    if n != expect:
        print('!! FAIL [%s]: expected %d occurrence(s), found %d' % (name, expect, n))
        print('   old head:', repr(old[:120]))
        sys.exit(1)
    data = data.replace(old, new)
    changes.append(name)
    print('OK  [%s] (%d)' % (name, n))

# ============================================================
# UPGRADE 1 — Header height/shape (CSS) + hero filter robustness (JS)
# ============================================================
apply('U1 header-inner css',
"""  .header-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding: 12px 0;
    flex-wrap: wrap;
  }""",
"""  .header-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px 16px;
    padding: 12px 0;
    flex-wrap: wrap;
    min-height: 60px;
  }""")

apply('U1 search-bar shrink css',
"""  .search-bar { background: rgba(255,255,255,.1); border-radius: 8px; padding: 8px 16px; display: flex; align-items: center; gap: 8px; }""",
"""  .search-bar { background: rgba(255,255,255,.1); border-radius: 8px; padding: 8px 16px; display: flex; align-items: center; gap: 8px; min-width: 0; flex: 0 1 auto; }""")

# ============================================================
# UPGRADE 5 + 3 + 4 + 2 CSS  (inserted before the Responsive block)
# ============================================================
NEW_CSS = """  /* ===== \"Most liked\" rail (editorial selection) ===== */
  .top-picks-note { font-size: .85rem; color: $(muted.color); margin: -14px 0 16px; }
  .top-picks-rail { display: flex; gap: 14px; overflow-x: auto; overflow-y: hidden; scroll-snap-type: x proximity; -webkit-overflow-scrolling: touch; padding: 4px 2px 14px; scrollbar-width: thin; }
  .top-picks-rail::-webkit-scrollbar { height: 8px; }
  .top-picks-rail::-webkit-scrollbar-thumb { background: $(border.color); border-radius: 8px; }
  .top-pick-card { flex: 0 0 240px; scroll-snap-align: start; }
  .top-pick-link { display: block; background: $(card.bg); border: 1px solid $(border.color); border-radius: 14px; overflow: hidden; color: $(text.color); height: 100%; transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease; }
  .top-pick-link:hover { transform: translateY(-3px); box-shadow: 0 10px 24px rgba(0,0,0,.10); }
  .top-pick-link:focus-visible { outline: none; border-color: $(accent.color); box-shadow: 0 0 0 3px rgba(201,150,43,.35); }
  .top-pick-media { display: block; aspect-ratio: 4 / 3; background: $(bg.color); overflow: hidden; }
  .top-pick-media img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .top-pick-noimg { display: flex; align-items: center; justify-content: center; height: 100%; color: $(muted.color); font-size: .8rem; }
  .top-pick-body { display: block; padding: 12px 14px 14px; }
  .top-pick-title { display: block; font-weight: 700; font-size: .95rem; margin-bottom: 4px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .top-pick-meta { display: block; font-size: .8rem; color: $(muted.color); margin-bottom: 6px; }
  .top-pick-price { display: block; font-weight: 700; color: $(primary.color); }
  @media (max-width: 768px) { .top-pick-card { flex-basis: 74%; } }

  /* ===== Rating section ===== */
  .rating-section { margin-top: 36px; background: $(card.bg); border-radius: 12px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,.04); }
  .rating-summary { display: flex; align-items: center; gap: 10px; margin-bottom: 16px; flex-wrap: wrap; }
  .rating-avg { font-size: 1.6rem; font-weight: 700; color: $(primary.dark); }
  .rating-stars { color: $(accent.color); letter-spacing: 2px; }
  .rating-count { color: $(muted.color); font-size: .9rem; }
  .rating-fieldset { border: 0; padding: 0; margin: 0 0 12px; }
  .rating-fieldset legend { font-size: .85rem; font-weight: 600; color: $(muted.color); margin-bottom: 6px; padding: 0; }
  .rating-input { display: inline-flex; gap: 4px; direction: ltr; }
  .rating-star { background: none; border: 0; font-size: 1.9rem; line-height: 1; color: $(border.color); cursor: pointer; padding: 0 2px; transition: color .15s ease, transform .15s ease; }
  .rating-star:hover, .rating-star.is-on { color: $(accent.color); }
  .rating-star:focus-visible { outline: 2px solid $(accent.color); outline-offset: 2px; border-radius: 4px; }
  .rating-note { font-size: .78rem; color: $(muted.color); margin-top: 10px; }
  .rating-feedback { font-size: .85rem; color: $(primary.color); margin-top: 8px; min-height: 1em; }
  .rating-list-wrap { margin-top: 20px; }
  .rating-list-wrap h3 { font-size: 1rem; color: $(primary.dark); margin-bottom: 10px; }
  .rating-list { list-style: none; padding: 0; margin: 0; }
  .rating-item { padding: 10px 0; border-bottom: 1px solid $(border.color); display: grid; gap: 2px; }
  .rating-item:last-child { border-bottom: 0; }
  .rating-item-stars { color: $(accent.color); letter-spacing: 2px; }
  .rating-item-text { font-size: .9rem; }
  .rating-item-date { font-size: .75rem; color: $(muted.color); }

  /* ===== Sidebar filter card ===== */
  .darna-filters-card { padding: 18px; }
  .darna-filters-card .darna-filters { background: transparent; border: 0; box-shadow: none; padding: 0; margin: 0; border-radius: 0; }
  .darna-filters-card .filters-row { grid-template-columns: 1fr; }

  /* ===== Region descriptions ===== */
  .discovery-intro { color: $(muted.color); margin: -14px 0 20px; font-size: .95rem; }
  .discovery-card .discovery-desc { display: block; font-size: .78rem; color: $(muted.color); margin-top: 4px; font-weight: 400; }
  .discovery-card:hover .discovery-desc { color: $(primary.color); }

  /* ===== Responsive ===== */"""

apply('U2/3/4/5 new css',
"""  /* ===== Responsive ===== */""",
NEW_CSS)

# footer 2 columns on mobile
apply('U5 footer mobile 2col',
"""    .footer-grid { grid-template-columns: 1fr; }""",
"""    .footer-grid { grid-template-columns: 1fr 1fr; }
    .footer-grid > div:first-child,
    .footer-grid > div:last-child { grid-column: 1 / -1; }""")

print('--- CSS done, len now', len(data))
io.open(PATH, 'w', encoding='utf-8').write(data)
print('WROTE', PATH)
