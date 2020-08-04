"""
Define string with a regex pattern. This type of field
will restrict user for entering any string other than
the one matches with regex string.
"""
import re
try:
	from simple_descriptors import Animal, Descriptor
except:
	from .simple_descriptors import Animal, Descriptor

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

class Regex(Descriptor):
	"""Define Regex for String field"""
	def __init__(self, *args, pat, **kwargs):
		self.pat = re.compile(pat)
		super().__init__(*args, **kwargs)

	def __set__(self, instance, value):
		if not self.pat.match(value):
			raise ValueError("Invalid String")
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

class SizedRegexString(String, Sized, Regex):
	pass

class Cat(Animal):
	_fields = ["name", "speak"]
	name = PosInteger('name')
	speak = SizedRegexString('speak', maxlen=4, pat="[A-Z]+$")

if __name__ == '__main__':
	cat = Cat(1, "MEOW")
	print(cat.name)
	# cat.speak = "meow" # ValueError: Invalid String
	print(cat.speak)