import json, re, unittest
from pathlib import Path
import xml.etree.ElementTree as ET

HERE = Path(__file__).parent
DATA = json.loads((HERE / "listings-ar.json").read_text(encoding="utf-8"))
THEME = (HERE / "theme-PLACE-DJ.AR.xml").read_text(encoding="utf-8")

class ListingDataTests(unittest.TestCase):
    def test_six_described_entries(self):
        items = DATA["listings"]
        self.assertEqual(len(items), 6)
        self.assertEqual(len({item["id"] for item in items}), 6)
        self.assertTrue(all(item["title"] and item["marketing_description"] for item in items))

    def test_positive_usd_prices(self):
        self.assertEqual(DATA["currency"], "USD")
        for item in DATA["listings"]:
            self.assertTrue(all(isinstance(v, (int, float)) and v > 0 for v in item["prices_usd"].values()))

    def test_eight_units_not_claimed_available(self):
        self.assertEqual(DATA["repeated_units"]["count"], 8)
        self.assertIn("لم تُحدد حالة التوافر الحالية.", DATA["data_quality_notes"])

class BloggerThemeTests(unittest.TestCase):
    def test_theme_is_well_formed_xml(self):
        ET.fromstring(THEME)

    def test_rtl_and_main_landmark(self):
        self.assertIn("dir='rtl' lang='ar'", THEME)
        self.assertIn("role='main' aria-label='المحتوى الرئيسي'", THEME)

    def test_protected_components_remain(self):
        for anchor in ("id='preferred-section'", "class='search-bar'", "class='inquiry-form'",
                       "id='property-grid'", "id='guest-reviews'"):
            self.assertIn(anchor, THEME)

    def test_accessibility_and_image_regressions(self):
        self.assertIn("expr:aria-label='&quot;عرض تفاصيل العقار: &quot; + data:post.title'", THEME)
        self.assertIn("background: $(primary.dark); border: none; color: #fff; min-height: 34px;", THEME)
        self.assertIn("width='720' height='540' loading='lazy' decoding='async'", THEME)
        self.assertNotIn("class='rating-stars'", THEME)
        self.assertNotIn("class='whatsapp-cta'", THEME)

    def test_widget_ids_are_unique(self):
        ids = re.findall(r"<b:widget\b[^>]*\bid=['\"]([^'\"]+)['\"]", THEME)
        self.assertEqual(len(ids), len(set(ids)), "Duplicate Blogger widget IDs")

if __name__ == "__main__":
    unittest.main()
