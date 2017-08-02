from PIL import Image, ImageDraw

def getImage(name):
 return Image.open(name)

def getPixels(somePic):
	return list(somePic.getdata())
	
def compress(pixels):
	result = []
	result.append([pixels[0],1])
	counter = 0
	for i in range(1,len(pixels)):
		if(result[counter][0]==pixels[i]):
			result[counter][1]+=1
		else:
			counter+=1
			result.append([pixels[i],1])
	return result

'''
format for compressed imgs text:
	255,0,0:3#123,155,155:9#(3,4)  not that it's ever touched manually if not wished.
'''
def genTxt(compressedImg):
	finalStr = ''
	for i in compressedImg[:-1]:
		finalStr+=str(i[0][0])+','+str(i[0][1])+','+str(i[0][2])+':'+str(i[1])+'#'
	return finalStr+'#'+str(compressedImg[len(compressedImg)-1])
def parseTxt(compressedTxt):
	compressedImg = []
	for i in compressedTxt.split('#')[:-1]:
		tuple = i.split(':')
		pixel =(int(tuple[0].split(',')[0]),int(tuple[0].split(',')[1]),int(tuple[0].split(',')[2]))
		compressedImg.append([pixel,int(tuple[1])])
	return compressedImg

	
class CompressedImage():
	def __init__(self,name):
		print(name[-3:])
		if(name[-3:]=='jpg'):
				
			self.img = getImage(name)
			self.size = self.img.size
			self.compressed = compress(getPixels(self.img))+[self.size]
			with open(name+'.txt','w') as outputTxt:
				outputTxt.write(genTxt(self.compressed))
				if(len(genTxt(self.compressed))>len(str(self.compressed))):
					print('we dun fucked up dude')
				outputTxt.close()
			print(str(self.size)+' '+str( self.size[0]*self.size[1] )+' '+str(len(self.compressed)))
		elif(name[-3:]=='txt'):
			with open(name,'r') as imgTxt:
				workStr = imgTxt.read()
				sizeStr = workStr.split('#')[len(workStr.split('#'))-1][1:-1].split(',')
				self.size = (int(sizeStr[0]),int(sizeStr[1]))
				self.compressed = parseTxt(workStr)
				print(self.compressed)
				self.img = self.build()
				
	def __str__(self):
		str(self.size)+' '+str( self.size[0]*self.size[1] )+' '+str(len(self.compressed))
	def build(self):
		img = Image.new('RGB',self.size,(0,0,0,0))
		values = []
		for i in self.compressed[:-1]:
			for j in range(i[1]):
				values.append(i[0])
		img.putdata(values)		
		img.show()
		return img


