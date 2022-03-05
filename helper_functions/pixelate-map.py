from PIL import Image

width = 1000
height = 1000
pixelWidth = 5
pixelHeight = 5
nOfPixelsX = (int)(width/pixelWidth)
nOfPixelsY = (int)(height/pixelHeight)

originalPicturePath = "images\map\dark-map.png"
pixelatedPicturePath = "images\map\base-map.png"

#creates a pixelated map of the rally teritory for as a base
#takes dark-map.png and resizes it to needed amount of pixels. then saves it to base-map.png

img = Image.open(originalPicturePath)
imgSmall = img.resize((nOfPixelsX,nOfPixelsY),resample=Image.BILINEAR)
result = imgSmall.resize(img.size,Image.NEAREST)
result.save(pixelatedPicturePath)