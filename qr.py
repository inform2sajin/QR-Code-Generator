# Import the qrcode library
import qrcode as qr

# Create a QRCode with specific parameter
features = qr.QRCode(version=1,box_size=45,border=4)

# Add the data to be encoded in the QR code - in this case this is my github profile URL
features.add_data('https://github.com/inform2sajin')
features.make(fit=True)

# Create an image from the QR code with specific color
# fil_color = "black" : You can change the color
# back_color = "white" : Background color of QR code - You can change the color.
qr_image = features.make_image(fil_color="black",back_color="white")

# Save the generated QR image to a file named 'githubimg.png'
qr_image.save('githubimg.png')


