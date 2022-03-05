from PIL import Image

#to test - put in file path values

width = 1000
height = 1000
pixelWidth = 5
pixelHeight = 5
nOfPixelsX = (int)(width/pixelWidth)
nOfPixelsY = (int)(height/pixelHeight)

originalPicturePath = "dark-map.png" 
pixelatedPicturePath = "base-map.png"

#creates a pixelated map of the rally teritory for as a base
#takes Original Picture and resizes it to needed amount of pixels. then saves it to Pixelated Picture

img = Image.open(originalPicturePath)
imgSmall = img.resize((nOfPixelsX,nOfPixelsY),resample=Image.BILINEAR)
result = imgSmall.resize((width,height), Image.LANCZOS)
result.save(pixelatedPicturePath)