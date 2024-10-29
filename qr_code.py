import qrcode
from qrcode.constants import ERROR_CORRECT_L

data = input("Masukan disini untuk generate QR: ")
qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white")
img.save("qrcode2.png")
