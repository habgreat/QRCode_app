import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=5,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img =qr.make_image(fill_color="black", back_color="white")
    img.save("Habtamu's Linkedin.png")

generate_qrcode("https://www.linkedin.com/in/habtamu-debel-833360221/")