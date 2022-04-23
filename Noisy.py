from PIL import Image, ImageDraw
import random

class Nois(object):

	def __init__(self):
		self.im = Image.open('4002470663.jpg')
		self.draw = ImageDraw.Draw(self.im)
		self.pix = self.im.load()
		self.width = self.im.size [0]
		self.height = self.im.size[1]


	def redrow(self,x,y,colors):
		self.draw.point((x,y),(colors[0],colors[1],colors[2]))


	def initredrow(self):
		for x in range(self.width):
			for y in range(self.height):
				pixels = self.encode(self.pix[x,y])
				colors = self.decode(pixels)
				self.redrow(x,y,colors)

	def showimage(self):
		self.initredrow()
		self.im.show()

	def encode(self,pixel):
		rgb = []
		for i in range(len(pixel)):
			color = f"{pixel[i]:08b}"
			#for i in range(25): полное зашумление картинки (Занимает многовато времени)
			rand = random.randint(0,7)
			randbit = str(random.randint(0,1))
			rgblist = list(color)
			rgblist[rand] = randbit
			color = "".join(rgblist)
			rgb.append(color)
		return(rgb)

	def decode(self,pixels):
		color = []
		for i in pixels:
			color.append(int(i[:],2))
		return(color)

proga = Nois()
proga.showimage()

