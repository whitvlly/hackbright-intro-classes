class Animal(object):
	def __init__(self, name, breed, color, weight, fur):
		self.name = name
		self.breed = breed
		self.color = color
		self.weight = weight
		self.fur = fur

	def print_name(self):
		print self.name


	
	def print_animalkind(self):
		print self.breed	
		print self.color

	def print_animalweight(self):
		print self.weight
	def has_fur(self):
		print self.fur

dog = Animal("spot", "Lab", "yellow", 80, True)	
cat = Animal("felix", "persian", "black", 10, True)
toad = Animal("Mr. Toad", "Forest Toad", "Brown", 8, False)

dog.print_name()
cat.print_animalkind()
toad.print_animalweight()
dog.has_fur()
cat.has_fur()
toad.has_fur()

