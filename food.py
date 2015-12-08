class Food(object):
	def __init__(self, name, weight, taste, recipe):
		self.name = name
		self.weight = weight
		self.taste = taste
		self.recipe = recipe

	def print_recipe(self):
		print self.recipe

	def print_name(self):
		print self.name

	def print_description(self):
		print self.name
		print self.weight
		print self.taste
		print self.recipe

	def double_recipe(self):
		self.weight=self.weight*2 


marinara = Food("Pasta marinara", 1, "yummy", "Boil tomatoes")

marinara.print_recipe()
marinara.print_name()
marinara.print_description()
marinara.double_recipe()
marinara.print_description()
