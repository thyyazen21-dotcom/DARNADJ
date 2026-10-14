# -*- coding: utf-8 -*-
"""Stage 4 — Blogger Layout visibility (U8), section config, meta consistency (U6)."""
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

# ---------- U8: make header-widgets & footer-widgets sections visible in Layout ----------
old_layout = """  body#layout .site-header,
  body#layout .hero,
  body#layout .site-footer,
  body#layout .search-bar,
  body#layout .nav-toggle,
  body#layout .main-nav,
  body#layout .darna-filters,
  body#layout .skip-link { display: none !important; }"""
new_layout = """  body#layout .site-header,
  body#layout .site-footer { background: #eef1f4 !important; color: #1a1a1a !important; box-shadow: none !important; position: static !important; }
  body#layout .header-widgets .widget,
  body#layout .footer-widgets .widget { color: #1a1a1a !important; }
  body#layout .header-inner,
  body#layout .hero,
  body#layout .footer-grid,
  body#layout .footer-bottom,
  body#layout .search-bar,
  body#layout .nav-toggle,
  body#layout .main-nav,
  body#layout .darna-filters,
  body#layout .skip-link { display: none !important; }"""
apply('U8 layout visibility', old_layout, new_layout)

# ---------- U8: make the top-picks section addable in Layout ----------
apply('U8 top-picks addable',
"        <b:section class='home-top-picks' id='home-top-picks' maxwidgets='1' showaddelement='no'>",
"        <b:section class='home-top-picks' id='home-top-picks' maxwidgets='1' showaddelement='yes'>")

# ---------- U6: keep the fallback meta description consistent with the hero ----------
apply('U6 meta description',
"<meta content='بلاَس — اعثر على سكنك في جيبوتي: اكتشف الشقق والفلل والمنازل والاستوديوهات، واستكشف الخيارات المناسبة لك وتواصل معنا للتحقق من التوفر والحجز.' name='description'/>",
"<meta content='بلاَس — اعثر على سكنك في جيبوتي: اكتشف خيارات السكن، وقارن العقارات المتاحة، واختر ما يناسب احتياجاتك.' name='description'/>")

io.open(PATH, 'w', encoding='utf-8').write(data)
print('--- Stage 4 done. len =', len(data))
