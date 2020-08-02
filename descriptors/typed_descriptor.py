"""
Create a typed descriptor which imposes certain
rules on a field for a user.
For example: age = Int("age") It will restricts
user from entering any value other than integer type.
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

class Integer(Typed):
	typ = int

class Float(Typed):
	typ = float

class String(Typed):
	typ = str

class Cat(Animal):
	_fields = ["name", "speak"]
	name = Integer('name')
	speak = String('speak')

cat = Cat(23, "meow")
print(cat.name)
# cat.name = "3h" # TypeError: Expected <class 'int'>
cat.speak = "meow meow"
print(cat.speak)