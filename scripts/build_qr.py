"""Create a QR code for the configured public site URL."""
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/".tools"/"python"))
import qrcode
import qrcode.image.svg
from PIL import Image
import zxingcpp
url=json.loads((ROOT/"content.json").read_text(encoding="utf-8"))["site_url"]
if not url.startswith("https://") or "github.io" not in url:
    raise ValueError("Set the confirmed GitHub Pages HTTPS URL before generating the QR code.")
qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=24,border=4)
qr.add_data(url);qr.make(fit=True)
out=ROOT/"assets"
qr.make_image(fill_color="#101c34",back_color="white").save(out/"jihoon-lee-qr.png")
qr.make_image(image_factory=qrcode.image.svg.SvgPathFillImage).save(out/"jihoon-lee-qr.svg")
decoded=zxingcpp.read_barcode(Image.open(out/"jihoon-lee-qr.png"))
assert decoded and decoded.text==url,"QR decoding failed"
print("QR verified: "+decoded.text)
