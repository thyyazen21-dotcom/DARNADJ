#!/usr/bin/env python3
"""Fail-closed PLACE-DJ Arabic delivery builder. Run from repository root."""
from pathlib import Path
import hashlib,json,re,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[3]
SRC=ROOT/"DarnaDJ_Updated_Package/Place-dj-16oct/PLACE-DJ-TEMPLATE-FINAL.xml"
REF=ROOT/"DarnaDJ_Updated_Package/Place-dj-16oct/DELIVERY-ARABIC/original-PLACE-DJ-TEMPLATE-FINAL.xml"
OUTDIR=ROOT/"DarnaDJ_Updated_Package/Place-dj-16oct/DELIVERY-ARABIC"
OUT=OUTDIR/"theme-PLACE-DJ.AR.xml"; REPORT=OUTDIR/"BUILD-REPORT-AR.json"
MARKERS=("[...]","/* truncated for brevity */","...59652 tokens truncated...")
def stop(msg):
 print("BLOCKED: "+msg,file=sys.stderr); sys.exit(2)
def digest(b): return hashlib.sha256(b).hexdigest()
if not SRC.is_file() or not REF.is_file(): stop("Source template or protected reference is missing.")
raw=SRC.read_bytes(); ref=REF.read_bytes(); src=raw.decode("utf-8")
if raw!=ref: stop("Source and protected reference are not byte-identical; resolve provenance first.")
if any(m in src for m in MARKERS): stop("Template contains truncation placeholders. Restore the complete original XML; no output generated.")
try: ET.fromstring(src)
except ET.ParseError as e: stop("Source XML is malformed: "+str(e))
anchors=["id='main-content'","id='preferred-section'","class='search-bar'","class='inquiry-form'","id='property-rating'"]
missing=[a for a in anchors if a not in src]
if missing: stop("Expected template anchors missing: "+", ".join(missing))
m=re.search(r"<html\b([^>]*)>",src,re.S)
if not m: stop("Root html element not found.")
attrs=re.sub(r"\s+expr:dir=(['\\"]).*?\1","",m.group(1))
attrs=re.sub(r"\s+expr:lang=(['\\"]).*?\1","",attrs)
out=src[:m.start()]+"<html"+attrs+" dir='rtl' lang='ar'>"+src[m.end():]
try: ET.fromstring(out)
except ET.ParseError as e: stop("Generated XML is malformed: "+str(e))
if any(a not in out for a in anchors): stop("A protected structural anchor was lost.")
OUTDIR.mkdir(parents=True,exist_ok=True); OUT.write_text(out,encoding="utf-8")
report={"status":"PASS","source":str(SRC.relative_to(ROOT)),"reference":str(REF.relative_to(ROOT)),"output":str(OUT.relative_to(ROOT)),"source_sha256":digest(raw),"reference_sha256":digest(ref),"output_sha256":digest(out.encode()),"checks":{"source_reference_byte_identical":True,"no_truncation_markers":True,"source_xml_well_formed":True,"output_xml_well_formed":True,"protected_anchors_preserved":True},"limitations":["Blogger import, Layout editor, prices, responsive behavior and links require live Blogger verification."]}
REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,ensure_ascii=False,indent=2))
