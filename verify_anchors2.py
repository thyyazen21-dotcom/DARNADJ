# -*- coding: utf-8 -*-
"""Dry-run v2: verify Stage-2 anchors using LITERAL Arabic (markup encoding)."""
import io
PATH = 'DarnaDJ_Updated_Package/theme-Place-dj-com.xml'
data = io.open(PATH, 'r', encoding='utf-8').read()

anchors = {
 'U6 hero p': '<p>اكتشف الشقق والفلل والمنازل والاستوديوهات، واستكشف الخيارات المناسبة لك وتواصل معنا للتحقق من التوفر والحجز.</p>',
 'U6 footer brand p': "<p style='font-size:.9rem;opacity:.7;'>منصة تأجير العقارات في جيبوتي. أسعار واضحة بالدولار وتواصل مباشر.</p>",
 'U6 footer contact note': "<p style='margin-top:8px;'>الاستفسار لا يؤكد التوفر أو الحجز</p>",
 'U6 add-property note': "<p class='add-property-note' id='add-property-note'>إرسال النموذج لا يعني النشر التلقائي&#1563; تتم مراجعة العقار قبل النشر.</p>",
 'U2 filter open tag': "<div class='darna-filters' id='darna-filters'>",
 'U2 blog-posts tag': "<div class='blog-posts'>",
 'U7 region start': "<b:if cond='data:view.isHomepage'>\n        <section class='section discovery-section'>",
 'U7 region end': "<section class='section'>\n          <div class='add-property-card'>",
 'U3 before-posts anchor': "      <b:if cond='data:view.isHomepage'>\n        <b:section class='home-before-posts' id='home-before-posts' maxwidgets='2' showaddelement='yes'/>\n      </b:if>\n\n      <b:section class='main' id='main-blog' maxwidgets='1' showaddelement='no'>",
 'U2 PopularPosts1 anchor': "        <b:widget id='PopularPosts1' locked='false'",
 'U4 rating anchor': "                  </div>\n\n                  <section class='similar-section' hidden='hidden' id='similar-section'>",
}
for k, v in anchors.items():
    print('%-28s count=%d' % (k, data.count(v)))

print('\nadd-property entity &#1563; count:', data.count('&#1563;'))
print('add-property literal U+061B count:', data.count('\u061b'))
idx = data.find("id='add-property-note'")
print('add-property context:', repr(data[idx-40:idx+220]))

idx = data.find('اكتشف الشقق والفلل')
print('\nhero p context:', repr(data[idx-10:idx+230]))
