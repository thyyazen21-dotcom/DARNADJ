import json,unittest
from pathlib import Path
DATA=json.loads((Path(__file__).parent/"listings-ar.json").read_text(encoding="utf-8"))
class ListingDataTests(unittest.TestCase):
 def test_six_described_entries(self):
  x=DATA["listings"]; self.assertEqual(len(x),6); self.assertEqual(len({i["id"] for i in x}),6); self.assertTrue(all(i["title"] and i["marketing_description"] for i in x))
 def test_positive_usd_prices(self):
  self.assertEqual(DATA["currency"],"USD")
  for i in DATA["listings"]: self.assertTrue(all(isinstance(v,(int,float)) and v>0 for v in i["prices_usd"].values()))
 def test_eight_units_not_claimed_available(self):
  self.assertEqual(DATA["repeated_units"]["count"],8); self.assertIn("لم تُحدد حالة التوافر الحالية.",DATA["data_quality_notes"])
if __name__=="__main__": unittest.main()
