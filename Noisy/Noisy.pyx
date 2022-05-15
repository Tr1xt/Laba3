# cython: language_level=3

from PIL import Image, ImageDraw
from tqdm.gui import trange
import random

class Nois(object):
	
	def __init__(self,name):
		cdef int width
		cdef int height
		self.name = name
		self.im = Image.open(name)
		self.draw = ImageDraw.Draw(self.im)
		self.pix = self.im.load()
		self.width = self.im.size [0]
		self.height = self.im.size[1]

	def initredrow(self):
		cdef int x
		cdef int y
		cdef int i 
		cdef list rgb
		cdef list spisok
		cdef int rand1
		cdef str color
		for x in trange(self.width):
			for y in range(self.height):
				rgb = list(self.pix[x,y])
				for i in range(3):
					color = f"{rgb[i]:08b}"
					rand1 = round(random.random()*7)
					rand2 = self.recurs(rand1)
					if color[rand1] == '1':
						color = color[:rand1] + "0" + color[rand1+1:]
						rgb[i] = (int(color[:],2))
						continue

					if color[rand1] == '0': 
						color = color[:rand1] + "1" + color[rand1+1:]
						rgb[i] = (int(color[:],2))
						continue

					if color[rand2] == '1':
						color = color[:rand2] + "0" + color[rand2+1:]
						rgb[i] = (int(color[:],2))
						continue

					if color[rand2] == '0': 
						color = color[:rand2] + "1" + color[rand2+1:]
						rgb[i] = (int(color[:],2))
						continue

					

				self.draw.point((x,y),(rgb[0],rgb[1],rgb[2]))


	def recurs(self,rand1):
		rand = round(random.random()*7)
		if rand1 == rand:
			self.recurs(rand)
		else:
			return rand

	def showimage(self):
		self.initredrow()
		self.im.show()

