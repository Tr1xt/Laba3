from PIL import Image, ImageDraw

class Show(object):

	def __init__(self,name):
		self.name = name
		self.im = Image.open(self.name)

	def showimage(self):
		self.im.show()
