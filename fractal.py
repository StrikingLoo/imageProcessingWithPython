from PIL import Image, ImageDraw
import datetime


def generateMandelbrot(size,maxIts,name):
	#the 70% float is added for purely aesthetic reasons
	img = Image.new('RGB',(7*size*7//10,4*size),(0,255,0,0))
	#final res = size^2 * 28 *.7 = 19.6 * size *size 
	values = []
	print(datetime.datetime.now().time())
	for line in range(img.height):
		
		for column in range(img.width):
			y0 = float(line/img.height)*3.5 -2.0 
			x = 0
			y = 0 #these two iterate 
			
			x0 = float(column/img.width)*2 - 1.5 #the substracted value is so that it's centered
			iteration = 0
			while( (x*x+y*y) < 4 and iteration<maxIts ):
				xtemp = x*x - y*y + x0
				y = 2*x*y +y0
				x = xtemp
				iteration+=1
			if iteration<maxIts:
				a = ((iteration*255)//maxIts)
				if a<255//4:
					values.append( (0,2*a,2*a) )
				elif a<255//2:
					values.append( (0,255,0) )
				else:
					values.append((0,255,255))
			else:
				values.append( (255,255,255) )
				
	img.putdata(values)
	print(datetime.datetime.now().time())
	img.save('./'+name+'.jpg')
	img.show()

generateMandelbrot(100,500,'ultimateFractal')

'''
For each pixel (Px, Py) on the screen, do:
{
  x0 = scaled x coordinate of pixel (scaled to lie in the Mandelbrot X scale (-2.5, 1))
  y0 = scaled y coordinate of pixel (scaled to lie in the Mandelbrot Y scale (-1, 1))
  x = 0.0
  y = 0.0
  iteration = 0
  max_iteration = 1000
  while (x*x + y*y < 2*2  AND  iteration < max_iteration) {
    xtemp = x*x - y*y + x0
    y = 2*x*y + y0
    x = xtemp
    iteration = iteration + 1
  }
  color = palette[iteration]
  plot(Px, Py, color)
}
'''