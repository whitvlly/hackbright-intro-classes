class Plant(object):
	def __init__(self, name, color, size, bloom):
		self.name = name
		self.color = color
		self.size = size
		self.bloom = bloom

	def print_name(self):
		print self.name

	def print_color(self):
		print self.color

	def print_size(self):
		print self.size

	def print_bloom(self):
		print self.bloom



flora = Plant("Rose", "red", "dozen", "blooming")

flora.print_name()
flora.print_color()
flora.print_size()
flora.print_bloom()