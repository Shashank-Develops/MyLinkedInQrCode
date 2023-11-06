import qrcode
from PIL import Image
# used for changing functionality---> eg border ,error etc
qr = qrcode.QRCode(version=1,
       error_correction=qrcode.constants.ERROR_CORRECT_H,
       box_size=10,border=4,)

qr.add_data("https://www.linkedin.com/in/shashank-dhauni-6b773a240/")
qr.make(fit=True)
img = qr.make_image(fill_color = "purple",back_color="blue")
img.save("MyLinkendIn.png")       