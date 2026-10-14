# -*- coding: utf-8 -*-
import re
p = 'DarnaDJ_Updated_Package/theme-Place-dj-com.xml'
data = open(p, 'r', encoding='utf-8').read()

def show(name, s):
    print('==== %s ====' % name)
    print(repr(s))
    print('count=%d' % data.count(s))
    print()

# 1 hero p
m = re.search(r'<p>\u0627\u0643\u062a\u0634\u0641.*?</p>', data, re.S)
show('hero_p', m.group(0))

# 2 footer brand p
m = re.search(r"<p style='font-size:\.9rem;opacity:\.7;'>.*?</p>", data, re.S)
show('footer_brand_p', m.group(0))

# 3 footer contact note p
m = re.search(r"<p style='margin-top:8px;'>.*?</p>", data, re.S)
show('footer_contact_note', m.group(0))

# 6 add-property note
m = re.search(r"<p class='add-property-note' id='add-property-note'>.*?</p>", data, re.S)
show('addprop_note', m.group(0))

# 7 JS google forms note line
m = re.search(r"if \(note\) note\.textContent = '.*?';", data, re.S)
show('js_google_forms_note', m.group(0))

# 4 filter panel block
start = data.find("<div class='darna-filters' id='darna-filters'>")
end = data.find("<div class='blog-posts'>")
show('filter_panel_block', data[start:end])

# 5 region section block
start = data.find("<b:if cond='data:view.isHomepage'>\n        <section class='section discovery-section'>")
end = data.find("<section class='section'>\n          <div class='add-property-card'>")
show('region_block', data[start:end])

# 8 detail-grid end + similar start
start = data.find("</aside>\n                  </div>\n\n                  <section class='similar-section'")
show('detail_insert_anchor', data[start:start+220])
