import qrcode

# Define the personal data
data = {
    "name": "Mario Rossi",
    "email": "mariorosssi@gmail.com",
    "phone": "0123456789",
    "address": "San Paolo, 23 Berlin"
}

# Define the data structure as vCard
data_str = f"BEGIN:VCARD\n\
VERSION:3.0\n\
N:{data['name']}\n\
EMAIL:{data['email']}\n\
TEL:{data['phone']}\n\
ADR:{data['address']}\n\
END:VCARD"

# Create the QR code object
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the data to the QR code object
qr.add_data(data_str)

# Generate the QR code as an image file
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
