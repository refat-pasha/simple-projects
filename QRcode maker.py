import qrcode as qr

print("Website name:")
x = input()
print("File name and format (ex=google.png) to save:")
y = input()
img = qr.make(x)
img.save(y)


