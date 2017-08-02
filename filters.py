from PIL import Image, ImageDraw
import sys

def getImage(name):
 return Image.open(name)

def getPixels(somePic):
	return list(somePic.getdata())
	
def applyHueFilter(pixels,hue=(255,255,255)):
	huePixels = []
	for i in pixels:
		a,b,c = i
		d,e,f = hue
		gray = int((a*a+b*b+c*c)**(1/2))
		color = (gray*d//255,gray*e//255,gray*f//255)
		huePixels.append(color)
	return huePixels
def negativize(pixels):
	negaPixels = []
	for i in pixels:
		a,b,c = i
		color = (255-a,255-b,255-c)
		negaPixels.append(color)
	return negaPixels

name = sys.argv[1]
img = getImage(name)
newImg = Image.new('RGB',img.size,(0,0,0))
newImg.putdata(negativize(getPixels(img)))
newImg.save('n'+name)
newImg.show()

