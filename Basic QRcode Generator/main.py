import qrcode

img = qrcode.make('https://github.com/CanKrbsoglu?tab=repositories')
type(img)
img.save("qrtest1.png")