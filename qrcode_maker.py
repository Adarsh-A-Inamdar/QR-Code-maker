import qrcode

img = qrcode.make(
    input("Enter the url to make Qr-Code:")
)
img.save('myQrcode.png')
img.show()