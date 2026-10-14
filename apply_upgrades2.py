# -*- coding: utf-8 -*-
"""Stage 2 — markup upgrades (6, 7, 2, 3, 4)."""
import io, sys
PATH = 'DarnaDJ_Updated_Package/theme-Place-dj-com.xml'
data = io.open(PATH, 'r', encoding='utf-8').read()

def apply(name, old, new, expect=1):
    global data
    n = data.count(old)
    if n != expect:
        print('!! FAIL [%s]: expected %d, found %d' % (name, expect, n))
        print('   old head:', repr(old[:140]))
        sys.exit(1)
    data = data.replace(old, new)
    print('OK  [%s]' % name)

# ---------- UPGRADE 6: marketing copy ----------
apply('U6 hero p',
'<p>\u0627\u0643\u062a\u0634\u0641 \u0627\u0644\u0634\u0642\u0642 \u0648\u0627\u0644\u0641\u0644\u0644 \u0648\u0627\u0644\u0645\u0646\u0627\u0632\u0644 \u0648\u0627\u0644\u0627\u0633\u062a\u0648\u062f\u064a\u0648\u0647\u0627\u062a\u060c \u0648\u0627\u0633\u062a\u0643\u0634\u0641 \u0627\u0644\u062e\u064a\u0627\u0631\u0627\u062a \u0627\u0644\u0645\u0646\u0627\u0633\u0628\u0629 \u0644\u0643 \u0648\u062a\u0648\u0627\u0635\u0644 \u0645\u0639\u0646\u0627 \u0644\u0644\u062a\u062d\u0642\u0642 \u0645\u0646 \u0627\u0644\u062a\u0648\u0641\u0631 \u0648\u0627\u0644\u062d\u062c\u0632.</p>',
'<p>\u0627\u0643\u062a\u0634\u0641 \u062e\u064a\u0627\u0631\u0627\u062a \u0627\u0644\u0633\u0643\u0646 \u0641\u064a \u062c\u064a\u0628\u0648\u062a\u064a\u060c \u0648\u0642\u0627\u0631\u0646 \u0627\u0644\u0639\u0642\u0627\u0631\u0627\u062a \u0627\u0644\u0645\u062a\u0627\u062d\u0629\u060c \u0648\u0627\u062e\u062a\u0631 \u0645\u0627 \u064a\u0646\u0627\u0633\u0628 \u0627\u062d\u062a\u064a\u0627\u062c\u0627\u062a\u0643.</p>')

apply('U6 footer brand p',
"<p style='font-size:.9rem;opacity:.7;'>\u0645\u0646\u0635\u0629 \u062a\u0623\u062c\u064a\u0631 \u0627\u0644\u0639\u0642\u0627\u0631\u0627\u062a \u0641\u064a \u062c\u064a\u0628\u0648\u062a\u064a. \u0623\u0633\u0639\u0627\u0631 \u0648\u0627\u0636\u062d\u0629 \u0628\u0627\u0644\u062f\u0648\u0644\u0627\u0631 \u0648\u062a\u0648\u0627\u0635\u0644 \u0645\u0628\u0627\u0634\u0631.</p>",
"<p style='font-size:.9rem;opacity:.7;'>\u0645\u0633\u0627\u062d\u062a\u0643 \u0627\u0644\u0642\u0627\u062f\u0645\u0629 \u062a\u0628\u062f\u0623 \u0645\u0646 \u0647\u0646\u0627.</p>")

apply('U6 footer contact note',
"<p style='margin-top:8px;'>\u0627\u0644\u0627\u0633\u062a\u0641\u0633\u0627\u0631 \u0644\u0627 \u064a\u0624\u0643\u062f \u0627\u0644\u062a\u0648\u0641\u0631 \u0623\u0648 \u0627\u0644\u062d\u062c\u0632</p>",
"<p style='margin-top:8px;'>\u0627\u0643\u062a\u0634\u0641 \u0627\u0644\u0645\u0643\u0627\u0646 \u0627\u0644\u0630\u064a \u064a\u0646\u0627\u0633\u0628\u0643\u060c \u0648\u062a\u0648\u0627\u0635\u0644 \u0645\u0639\u0646\u0627 \u0644\u0644\u0627\u0633\u062a\u0641\u0633\u0627\u0631 \u0639\u0646 \u0627\u0644\u062a\u0648\u0641\u0631.</p>")

apply('U6 add-property note (static)',
"<p class='add-property-note' id='add-property-note'>\u0625\u0631\u0633\u0627\u0644 \u0627\u0644\u0646\u0645\u0648\u0630\u062c \u0644\u0627 \u064a\u0639\u0646\u064a \u0627\u0644\u0646\u0634\u0631 \u0627\u0644\u062a\u0644\u0642\u0627\u0626\u064a&#1563; \u062a\u062a\u0645 \u0645\u0631\u0627\u062c\u0639\u0629 \u0627\u0644\u0639\u0642\u0627\u0631 \u0642\u0628\u0644 \u0627\u0644\u0646\u0634\u0631.</p>",
"<p class='add-property-note' id='add-property-note'>\u0623\u0636\u0641 \u0639\u0642\u0627\u0631\u0643 \u0644\u064a\u0635\u0644 \u0625\u0644\u0649 \u0627\u0644\u0628\u0627\u062d\u062b\u064a\u0646 \u0639\u0646 \u0633\u0643\u0646 \u0641\u064a \u062c\u064a\u0628\u0648\u062a\u064a \u2014 \u062a\u064f\u0631\u0627\u062c\u0639 \u0627\u0644\u0625\u062f\u0627\u0631\u0629 \u0627\u0644\u0639\u0642\u0627\u0631 \u0642\u0628\u0644 \u0627\u0644\u0646\u0634\u0631.</p>")

# ---------- UPGRADE 7: region section (9 cards + intro) ----------
start = data.find("<b:if cond='data:view.isHomepage'>\n        <section class='section discovery-section'>")
end = data.find("<section class='section'>\n          <div class='add-property-card'>")
assert start > 0 and end > start, 'region anchors'
old_region = data[start:end]
NEW_REGION = """<b:if cond='data:view.isHomepage'>
        <section class='section discovery-section'>
          <h2 class='section-title'>\u062a\u0635\u0641\u0651\u062d \u062d\u0633\u0628 \u0627\u0644\u0645\u0646\u0637\u0642\u0629 \u0641\u064a \u062c\u064a\u0628\u0648\u062a\u064a</h2>
          <p class='discovery-intro'>\u0627\u062e\u062a\u0631 \u0627\u0644\u062d\u064a \u0627\u0644\u0623\u0642\u0631\u0628 \u0625\u0644\u0649 \u0623\u0633\u0644\u0648\u0628 \u062d\u064a\u0627\u062a\u0643\u060c \u0648\u0627\u0628\u062f\u0623 \u0628\u062c\u0648\u0644\u0629 \u0633\u0631\u064a\u0639\u0629 \u0628\u064a\u0646 \u0639\u0642\u0627\u0631\u0627\u062a \u062c\u064a\u0628\u0648\u062a\u064a \u0627\u0644\u0645\u062f\u064a\u0646\u0629 \u0648\u0627\u0644\u0645\u0646\u0627\u0637\u0642 \u0627\u0644\u0645\u062d\u064a\u0637\u0629.</p>
          <div class='discovery-grid'>
            <a class='discovery-card' href='https://www.place-dj.com/search/label/%D8%AC%D9%8A%D8%A8%D9%88%D8%AA%D9%8A%20%D8%A7%D9%84%D9%85%D8%AF%D9%8A%D9%86%D8%A9'><span aria-hidden='true' class='discovery-icon'>\U0001F3D9\uFE0F</span><span class='discovery-name'>\u0642\u0644\u0628 \u062c\u064a\u0628\u0648\u062a\u064a \u0627\u0644\u0645\u062f\u064a\u0646\u0629</span><span class='discovery-desc'>\u062d\u064a\u0627\u0629 \u0627\u0644\u0645\u062f\u064a\u0646\u0629 \u0648\u0627\u0644\u062e\u062f\u0645\u0627\u062a \u0642\u0631\u064a\u0628\u0629 \u0645\u0646\u0643</span></a>
            <a class='discovery-card' href='https://www.place-dj.com/search/label/%D9%87%D9%8A%D8%B1%D9%88%D9%86'><span aria-hidden='true' class='discovery-icon'>\U0001F30A</span><span class='discovery-name'>\u062d\u064a \u0647\u064a\u0631\u0648\u0646</span><span class='discovery-desc'>\u0625\u0637\u0644\u0627\u0644\u0629 \u0628\u062d\u0631\u064a\u0629 \u0648\u0623\u062c\u0648\u0627\u0621 \u0647\u0627\u062f\u0626\u0629</span></a>
            <a class='discovery-card' href='https://www.place-dj.com/search/label/%D9%87%D8%B1%D8%A7%D9%85%D9%88%D8%B3'><span aria-hidden='true' class='discovery-icon'>\U0001F3DB\uFE0F</span><span class='discovery-name'>\u0647\u0631\u0627\u0645\u0648\u0633</span><span class='discovery-desc'>\u0645\u0633\u0627\u062d\u0627\u062a \u0631\u0627\u0642\u064a\u0629 \u0644\u0644\u0639\u064a\u0634 \u0648\u0627\u0644\u0627\u0633\u062a\u0642\u0631\u0627\u0631</span></a>
            <a class='discovery-card' href='https://www.place-dj.com/search/label/%D8%BA%D8%A8%D9%88%D8%AF%D8%A9'><span aria-hidden='true' class='discovery-icon'>\U0001F3D8\uFE0F</span><span class='discovery-name'>\u063a\u0628\u0648\u062f\u0629</span><span class='discovery-desc'>\u0627\u062e\u062a\u064a\u0627\u0631\u0627\u062a \u0639\u0645\u0644\u064a\u0629 \u0644\u0644\u0639\u0627\u0626\u0644\u0627\u062a</span></a>
            <a class='discovery-card' href='https://www.place-dj.com/search/label/%D8%A3%D9%85%D8%A8%D9%88%D9%84%D9%8A'><span aria-hidden='true' class='discovery-icon'>\u2708\uFE0F</span><span class='discovery-name'>\u0623\u0645\u0628\u0648\u0644\u064a</span><span class='discovery-desc'>\u0642\u0631\u0628 \u0627\u0644\u0645\u0637\u0627\u0631 \u0648\u0627\u0644\u0648\u062c\u0647\u0627\u062a \u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629</span></a>
            <a class='discovery-card' href='https://www.place-dj.com/search/label/%D8%A7%D9%84%D8%A8%D9%84%D8%A7%D8%AA%D9%88'><span aria-hidden='true' class='discovery-icon'>\U0001F4CD</span><span class='discovery-name'>\u0627\u0644\u0628\u0644\u0627\u062a\u0648</span><span class='discovery-desc'>\u0645\u0648\u0642\u0639 \u0645\u0645\u064a\u0632 \u0648\u0633\u0637 \u0627\u0644\u0645\u062f\u064a\u0646\u0629</span></a>
            <a class='discovery-card' href='https://www.place-dj.com/search/label/%D8%A8%D9%8F%D9%84%D9%88%D8%B5'><span aria-hidden='true' class='discovery-icon'>\U0001F3E1</span><span class='discovery-name'>\u0628\u064f\u0644\u0648\u0635</span><span class='discovery-desc'>\u062a\u0646\u0648\u0639 \u0645\u0646\u0627\u0632\u0644 \u0648\u0634\u0642\u0642 \u0633\u0643\u0646\u064a\u0629</span></a>
            <a class='discovery-card' href='https://www.place-dj.com/search/label/%D8%A3%D8%B1%D8%A8%D9%87%D8%A7'><span aria-hidden='true' class='discovery-icon'>\U0001F3D9\uFE0F</span><span class='discovery-name'>\u0623\u0631\u0628\u0647\u0627</span><span class='discovery-desc'>\u062d\u064a \u0642\u0631\u064a\u0628 \u0645\u0646 \u0646\u0628\u0636 \u0627\u0644\u0645\u062f\u064a\u0646\u0629</span></a>
            <a class='discovery-card' href='https://www.place-dj.com/search/label/%D8%A8%D9%84%D8%A8%D9%84%D8%A7'><span aria-hidden='true' class='discovery-icon'>\U0001F305</span><span class='discovery-name'>\u0628\u0644\u0628\u0644\u0627 \u0648\u0645\u0627 \u062d\u0648\u0644\u0647\u0627</span><span class='discovery-desc'>\u062e\u064a\u0627\u0631\u0627\u062a \u0625\u0636\u0627\u0641\u064a\u0629 \u062d\u0648\u0644 \u0627\u0644\u0639\u0627\u0635\u0645\u0629</span></a>
          </div>
          <h2 class='section-title'>\u062a\u0635\u0641\u0651\u062d \u062d\u0633\u0628 \u0627\u0644\u0646\u0648\u0639</h2>
          <div class='filter-bar'>
            <a class='filter-chip' expr:href='data:blog.homepageUrl + &quot;search/label/\u0634\u0642\u0629&quot;'>\u0634\u0642\u0642</a>
            <a class='filter-chip' expr:href='data:blog.homepageUrl + &quot;search/label/\u0641\u064a\u0644\u0627&quot;'>\u0641\u0644\u0644</a>
            <a class='filter-chip' expr:href='data:blog.homepageUrl + &quot;search/label/\u0645\u0646\u0632\u0644&quot;'>\u0645\u0646\u0627\u0632\u0644</a>
            <a class='filter-chip' expr:href='data:blog.homepageUrl + &quot;search/label/\u0627\u0633\u062a\u0648\u062f\u064a\u0648&quot;'>\u0627\u0633\u062a\u0648\u062f\u064a\u0648\u0647\u0627\u062a</a>
            <a class='filter-chip' expr:href='data:blog.homepageUrl + &quot;search/label/\u063a\u0631\u0641\u0629&quot;'>\u063a\u0631\u0641</a>
          </div>
        </section>

        """
apply('U7 region section', old_region, NEW_REGION)

# ---------- UPGRADE 2: move filter panel to sidebar ----------
fstart = data.find("<div class='darna-filters' id='darna-filters'>")
fend = data.find("<div class='blog-posts'>")
assert fstart > 0 and fend > fstart, 'filter anchors'
old_filter = data[fstart:fend]
apply('U2 remove filter from content-area', old_filter, '')

FILTER_WIDGET = """        <b:widget id='HTMLFilter1' locked='false' title='\u062a\u0635\u0641\u064a\u0629 \u0646\u0635\u064a\u0629 (\u062f\u0627\u062e\u0644 \u0647\u0630\u0647 \u0627\u0644\u0635\u0641\u062d\u0629)' type='HTML' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='content'><![CDATA[<div class="darna-filters" id="darna-filters">
  <p class="filters-scope">\u062a\u064f\u0637\u0628\u064e\u0651\u0642 \u0647\u0630\u0647 \u0627\u0644\u0641\u0644\u0627\u062a\u0631 \u0639\u0644\u0649 \u0627\u0644\u0639\u0642\u0627\u0631\u0627\u062a \u0627\u0644\u0645\u0639\u0631\u0648\u0636\u0629 \u0641\u064a \u0647\u0630\u0647 \u0627\u0644\u0635\u0641\u062d\u0629 \u0641\u0642\u0637. \u0644\u0644\u0628\u062d\u062b \u0641\u064a \u0643\u0644 \u0627\u0644\u0645\u0646\u0634\u0648\u0631\u0627\u062a \u0627\u0633\u062a\u062e\u062f\u0645 \u0635\u0646\u062f\u0648\u0642 \u0627\u0644\u0628\u062d\u062b \u0641\u064a \u0627\u0644\u0623\u0639\u0644\u0649.</p>
  <details class="filters-disclosure" id="filters-disclosure" open="open">
    <summary class="filters-summary">\u0643\u0644 \u0627\u0644\u0641\u0644\u0627\u062a\u0631</summary>
    <div class="filters-row">
      <div class="filter-field" style="grid-column:1/-1;">
        <label for="f-q">\u0628\u062d\u062b \u0628\u0627\u0644\u0627\u0633\u0645 \u0623\u0648 \u0627\u0644\u0648\u0635\u0641</label>
        <input id="f-q" placeholder="\u0627\u0628\u062d\u062b \u0628\u0627\u0644\u0627\u0633\u0645 \u0623\u0648 \u0627\u0644\u0648\u0635\u0641 \u0623\u0648 \u0627\u0644\u0645\u0646\u0637\u0642\u0629..." type="search"/>
      </div>
      <div class="filter-field">
        <label for="f-type">\u0627\u0644\u0646\u0648\u0639</label>
        <select id="f-type">
          <option value="">\u0643\u0644 \u0627\u0644\u0623\u0646\u0648\u0627\u0639</option>
          <option value="\u0641\u064a\u0644\u0627">\u0641\u064a\u0644\u0627</option>
          <option value="\u0634\u0642\u0629">\u0634\u0642\u0629</option>
          <option value="\u0645\u0646\u0632\u0644">\u0645\u0646\u0632\u0644</option>
          <option value="\u0627\u0633\u062a\u0648\u062f\u064a\u0648">\u0627\u0633\u062a\u0648\u062f\u064a\u0648</option>
          <option value="\u063a\u0631\u0641\u0629">\u063a\u0631\u0641\u0629</option>
        </select>
      </div>
      <div class="filter-field">
        <label for="f-area">\u0627\u0644\u0645\u0646\u0637\u0642\u0629</label>
        <select id="f-area">
          <option value="">\u0643\u0644 \u0627\u0644\u0645\u0646\u0627\u0637\u0642</option>
          <option value="\u0623\u0648\u0628\u0648\u0643">\u0623\u0648\u0628\u0648\u0643</option>
          <option value="\u0639\u0644\u064a \u0635\u0628\u064a\u062d">\u0639\u0644\u064a \u0635\u0628\u064a\u062d</option>
          <option value="\u062a\u0627\u062c\u0648\u0631\u0629">\u062a\u0627\u062c\u0648\u0631\u0629</option>
          <option value="\u062c\u064a\u0628\u0648\u062a\u064a \u0627\u0644\u0645\u062f\u064a\u0646\u0629">\u062c\u064a\u0628\u0648\u062a\u064a \u0627\u0644\u0645\u062f\u064a\u0646\u0629</option>
          <option value="\u062f\u062e\u064a\u0644">\u062f\u062e\u064a\u0644</option>
          <option value="\u0623\u0631\u062a\u0651\u0627">\u0623\u0631\u062a\u0651\u0627</option>
        </select>
      </div>
      <div class="filter-field">
        <label for="f-status">\u0627\u0644\u062a\u0648\u0641\u0631</label>
        <select id="f-status">
          <option value="">\u0627\u0644\u0643\u0644</option>
          <option value="available">\u0645\u062a\u0648\u0641\u0631</option>
          <option value="unavailable">\u063a\u064a\u0631 \u0645\u062a\u0648\u0641\u0631</option>
        </select>
      </div>
      <div class="filter-field">
        <label for="f-min">\u0623\u062f\u0646\u0649 \u0633\u0639\u0631 ($)</label>
        <input id="f-min" inputmode="numeric" min="0" type="number"/>
      </div>
      <div class="filter-field">
        <label for="f-max">\u0623\u0642\u0635\u0649 \u0633\u0639\u0631 ($)</label>
        <input id="f-max" inputmode="numeric" min="0" type="number"/>
      </div>
      <div class="filter-field">
        <label for="f-unit">\u0648\u062d\u062f\u0629 \u0627\u0644\u0633\u0639\u0631</label>
        <select id="f-unit">
          <option value="">\u0643\u0644 \u0627\u0644\u0648\u062d\u062f\u0627\u062a</option>
          <option value="night">night</option>
          <option value="month">month</option>
        </select>
      </div>
      <div class="filter-field">
        <label for="f-beds">\u063a\u0631\u0641 \u0627\u0644\u0646\u0648\u0645</label>
        <select id="f-beds">
          <option value="">\u0627\u0644\u0643\u0644</option>
          <option value="1">1+</option>
          <option value="2">2+</option>
          <option value="3">3+</option>
          <option value="4">4+</option>
          <option value="5">5+</option>
        </select>
      </div>
      <div class="filter-field">
        <label for="f-baths">\u0627\u0644\u062d\u0645\u0627\u0645\u0627\u062a</label>
        <select id="f-baths">
          <option value="">\u0627\u0644\u0643\u0644</option>
          <option value="1">1+</option>
          <option value="2">2+</option>
          <option value="3">3+</option>
        </select>
      </div>
      <div class="filter-field">
        <label for="f-sqm">\u0623\u062f\u0646\u0649 \u0645\u0633\u0627\u062d\u0629 (\u0645\u00b2)</label>
        <input id="f-sqm" inputmode="numeric" min="0" type="number"/>
      </div>
      <div class="filter-field">
        <label for="f-sort">\u0627\u0644\u062a\u0631\u062a\u064a\u0628</label>
        <select id="f-sort">
          <option value="default">\u0627\u0644\u0627\u0641\u062a\u0631\u0627\u0636\u064a</option>
          <option value="price-asc">\u0627\u0644\u0633\u0639\u0631: \u0645\u0646 \u0627\u0644\u0623\u0642\u0644 \u0644\u0644\u0623\u0639\u0644\u0649</option>
          <option value="price-desc">\u0627\u0644\u0633\u0639\u0631: \u0645\u0646 \u0627\u0644\u0623\u0639\u0644\u0649 \u0644\u0644\u0623\u0642\u0644</option>
          <option value="beds-desc">\u063a\u0631\u0641 \u0627\u0644\u0646\u0648\u0645: \u0627\u0644\u0623\u0643\u062b\u0631 \u0623\u0648\u0644\u0627\u064b</option>
          <option value="sqm-desc">\u0627\u0644\u0645\u0633\u0627\u062d\u0629: \u0627\u0644\u0623\u0643\u0628\u0631 \u0623\u0648\u0644\u0627\u064b</option>
        </select>
      </div>
      <div class="filter-actions">
        <button class="filter-apply" id="f-apply" type="button">\u062a\u0637\u0628\u064a\u0642</button>
        <button class="filter-reset" id="f-reset" type="button">\u0625\u0639\u0627\u062f\u0629 \u062a\u0639\u064a\u064a\u0646</button>
      </div>
    </div>
  </details>
  <div aria-live="polite" class="filters-status" id="f-count"></div>
</div>]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
            <div class='widget-card darna-filters-card' id='darna-filters-section'>
              <h3><data:title/></h3>
              <div class='widget-content'><data:content/></div>
            </div>
          </b:includable>
        </b:widget>
"""
apply('U2 insert filter widget in sidebar',
"""        <b:widget id='PopularPosts1' locked='false'""",
FILTER_WIDGET + """        <b:widget id='PopularPosts1' locked='false'""")

# ---------- UPGRADE 3: top-picks section before main-blog ----------
TOP_PICKS = """      <b:if cond='data:view.isHomepage'>
        <b:section class='home-top-picks' id='home-top-picks' maxwidgets='1' showaddelement='no'>
          <b:widget id='HTMLTopPicks1' locked='false' title='\u064a\u0641\u0636\u0644\u0647\u0627 \u0627\u0644\u0643\u062b\u064a\u0631\u0648\u0646' type='HTML' version='2' visible='true'>
            <b:widget-settings>
              <b:widget-setting name='content'><![CDATA[<section class="top-picks-section" data-source="editorial" hidden="hidden" id="top-picks-section">
  <h2 class="section-title">\u064a\u0641\u0636\u0644\u0647\u0627 \u0627\u0644\u0643\u062b\u064a\u0631\u0648\u0646</h2>
  <p class="top-picks-note">\u0627\u062e\u062a\u064a\u0627\u0631\u0627\u062a \u0645\u0642\u062a\u0631\u062d\u0629 \u0645\u0646 \u0639\u0642\u0627\u0631\u0627\u062a \u0645\u062a\u0627\u062d\u0629 \u0639\u0644\u0649 \u0628\u0644\u0627\u064e\u0633.</p>
  <div aria-label="\u064a\u0641\u0636\u0644\u0647\u0627 \u0627\u0644\u0643\u062b\u064a\u0631\u0648\u0646" class="top-picks-rail" id="top-picks-rail" role="list"></div>
</section>]]></b:widget-setting>
            </b:widget-settings>
            <b:includable id='main'>
              <div class='widget-content'><data:content/></div>
            </b:includable>
          </b:widget>
        </b:section>
      </b:if>

"""
apply('U3 insert top-picks section',
"""      <b:if cond='data:view.isHomepage'>
        <b:section class='home-before-posts' id='home-before-posts' maxwidgets='2' showaddelement='yes'/>
      </b:if>

      <b:section class='main' id='main-blog' maxwidgets='1' showaddelement='no'>""",
"""      <b:if cond='data:view.isHomepage'>
        <b:section class='home-before-posts' id='home-before-posts' maxwidgets='2' showaddelement='yes'/>
      </b:if>

""" + TOP_PICKS + """      <b:section class='main' id='main-blog' maxwidgets='1' showaddelement='no'>""")

# ---------- UPGRADE 4: rating section in detail page ----------
RATING = """                  <section class='rating-section' id='rating-section'>
                    <h2 class='section-title'>\u0642\u064a\u0651\u0645 \u0647\u0630\u0627 \u0627\u0644\u0639\u0642\u0627\u0631</h2>
                    <div class='rating-summary' hidden='hidden' id='rating-summary'>
                      <span class='rating-avg' id='rating-avg'>\u2014</span>
                      <span aria-hidden='true' class='rating-stars' id='rating-stars-display'></span>
                      <span class='rating-count' id='rating-count'></span>
                    </div>
                    <form class='rating-form' id='rating-form' novalidate='novalidate'>
                      <fieldset class='rating-fieldset'>
                        <legend>\u0627\u062e\u062a\u0631 \u062a\u0642\u064a\u064a\u0645\u0643 \u0645\u0646 1 \u0625\u0644\u0649 5 \u0646\u062c\u0648\u0645</legend>
                        <div aria-label='\u0627\u0644\u062a\u0642\u064a\u064a\u0645 \u0628\u0627\u0644\u0646\u062c\u0648\u0645' class='rating-input' id='rating-input' role='radiogroup'>
                          <button aria-checked='false' aria-label='1 \u0646\u062c\u0645\u0629' class='rating-star' data-value='1' role='radio' tabindex='0' type='button'>\u2605</button>
                          <button aria-checked='false' aria-label='2 \u0646\u062c\u0648\u0645' class='rating-star' data-value='2' role='radio' tabindex='-1' type='button'>\u2605</button>
                          <button aria-checked='false' aria-label='3 \u0646\u062c\u0648\u0645' class='rating-star' data-value='3' role='radio' tabindex='-1' type='button'>\u2605</button>
                          <button aria-checked='false' aria-label='4 \u0646\u062c\u0648\u0645' class='rating-star' data-value='4' role='radio' tabindex='-1' type='button'>\u2605</button>
                          <button aria-checked='false' aria-label='5 \u0646\u062c\u0648\u0645' class='rating-star' data-value='5' role='radio' tabindex='-1' type='button'>\u2605</button>
                        </div>
                      </fieldset>
                      <div class='field'>
                        <label for='rating-comment'>\u062a\u0639\u0644\u064a\u0642 (\u0627\u062e\u062a\u064a\u0627\u0631\u064a)</label>
                        <textarea id='rating-comment' maxlength='500' rows='3'></textarea>
                      </div>
                      <button class='form-submit rating-submit' id='rating-submit' type='submit'>\u0625\u0631\u0633\u0627\u0644 \u0627\u0644\u062a\u0642\u064a\u064a\u0645</button>
                      <p class='rating-note' id='rating-note'>\u062a\u064f\u062d\u0641\u0637 \u062a\u0642\u064a\u064a\u0645\u0627\u062a\u0643 \u0639\u0644\u0649 \u0647\u0630\u0627 \u0627\u0644\u062c\u0647\u0627\u0632 \u0641\u0642\u0637. \u0644\u0639\u0631\u0636 \u062a\u0642\u064a\u064a\u0645\u0627\u062a \u0645\u0634\u062a\u0631\u0643\u0629 \u0628\u064a\u0646 \u0643\u0644 \u0627\u0644\u0632\u0648\u0627\u0631 \u064a\u0644\u0632\u0645 \u0631\u0628\u0637 \u062e\u062f\u0645\u0629 \u062a\u062e\u0632\u064a\u0646 \u062e\u0627\u0631\u062c\u064a\u0629.</p>
                      <div aria-live='polite' class='rating-feedback' id='rating-feedback' role='status'></div>
                    </form>
                    <div class='rating-list-wrap' hidden='hidden' id='rating-list-wrap'>
                      <h3>\u0627\u0644\u062a\u0642\u064a\u064a\u0645\u0627\u062a \u0627\u0644\u0633\u0627\u0628\u0642\u0629</h3>
                      <ul class='rating-list' id='rating-list'></ul>
                    </div>
                  </section>

"""
apply('U4 insert rating section',
"""                  </div>

                  <section class='similar-section' hidden='hidden' id='similar-section'>""",
"""                  </div>

""" + RATING + """                  <section class='similar-section' hidden='hidden' id='similar-section'>""")

io.open(PATH, 'w', encoding='utf-8').write(data)
print('--- Stage 2 done. len =', len(data))
