"""
Using Sized descriptor, use can be restricted to enter
a string with some limit
"""
from simple_descriptors import Animal, Descriptor

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

class Sized(Descriptor):
	"""docstring for Sized"""
	def __init__(self, *args, maxlen, **kwargs):
		self.maxlen = maxlen
		super().__init__(*args, **kwargs)
		
	def __set__(self, instance, value):
		if len(value) > self.maxlen:
			raise ValueError("Too big")
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

class SizedString(String, Sized):
	pass

class Cat(Animal):
	_fields = ["name", "speak"]
	name = PosInteger('name')
	speak = SizedString('speak', maxlen=4)

cat = Cat(1, "meow")
print(cat.name)
cat.speak = "meow"
# cat.speak = "meow meow" # ValueError: Too big
print(cat.speak)