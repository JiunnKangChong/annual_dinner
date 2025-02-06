import qrcode

# URL of the page where users will submit their name
url = 'http://127.0.0.1:80/'  # Change this URL if you deploy the app online

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Create the image
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode.png')  # Save the QR code as 'qrcode.png'
