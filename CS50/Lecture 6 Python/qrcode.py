import os 
import qrcode

img = qrcode.make("https://youtu.be/bhqvydu37grv")

img.save("qr.png, PNG")

os.system("open qr.png")