"""
Descriptor to define a Positive Integer, Positive Float
with rules. We create a Typed descriptor whic checks
for type of value defined by User. If a user has
entered string value for Integer type, It will raise
a TypeError.
"""
from simple_descriptors import Animal

class Descriptor:
	"""
	Descriptors actually update values of class variables
	by updating its values in instance.__dict__
	"""
	def __init__(self, name=None):
		self.name = name

	def __set__(self, instance, value):
		instance.__dict__[self.name] = value

	def __delete__(self, instance):
		raise AttributeError("can't delete")

class Typed(Descriptor):
	ty = object
	def __set__(self, instance, value):
		if not isinstance(value, self.typ):
			raise TypeError("Expected %s" % self.typ)
		super().__set__(instance, value)

class Positive(Descriptor):
	def __set__(self, instance, value):
		if value < 0:
			raise ValueError('Expected value >= 0')
		super().__set__(instance, value)

class Integer(Typed):
	typ = int

class Float(Typed):
	typ = float

class String(Typed):
	typ = str

# Create Mixin class
class PosInteger(Integer, Positive):
	pass

class PosFloat(Float, Positive):
	pass

class Cat(Animal):
	_fields = ["name", "speak"]
	name = PosInteger('name')
	speak = String('speak')

# cat = Cat(-1, "meow") # ValueError: Expected value > 0
cat = Cat(1, "meow")
print(cat.name)
cat.speak = "meow meow"
print(cat.speak)