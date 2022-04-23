from PIL import Image, ImageDraw

class Show(object):

	def __init__(self):
		self.im = Image.open('4002470663.jpg')

	def showImage(self):
		self.im.show()


proga = Show()
proga.showImage()