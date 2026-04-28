import qrcode

# Data you want to encode
data = input("Enter your link:")

# Create QR code
qr = qrcode.make(data)

# Save the image
qr.save("qrcode.png")

print("QR code generated and saved as qrcode.png")