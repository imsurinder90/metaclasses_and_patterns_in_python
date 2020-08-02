"""
Descriptors and metaclass: Now with the help of metaclass
we need not to specify attribute name while creating class,
previously attributes are written at 3 places and now 
only specify ones.
Previously:
class Cat(Animal):
	_fields = ["name", "speak"]
	name = PosInteger('name')
	speak = SizedRegexString('speak', maxlen=4, pat="[A-Z]+$")
Now:
class Cat(Animal):
	name = PosInteger()
	speak = SizedRegexString(maxlen=4, pat="[A-Z]+$")
"""

import re
from collections import OrderedDict
from simple_descriptors import make_signature, Descriptor

class AnimalMeta(type):
	@classmethod
	def __prepare__(cls, clsname, bases):
		return OrderedDict()
	def __new__(cls, clsname, bases, clsdict):
		attrs = [key for key, value in clsdict.items() if isinstance(value, Descriptor)]
		for name in attrs:
			clsdict[name].name = name

		clsobj = super().__new__(cls, clsname, bases, clsdict)
		sig = make_signature(attrs)
		setattr(clsobj, "_fields", sig)
		return clsobj

class Animal(metaclass=AnimalMeta):
	_fields = []
	def __init__(self, *args, **kwargs):
		bound_args = self._fields.bind(*args, **kwargs)
		for key, val in bound_args.arguments.items():
			setattr(self, key, val)


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
	"""
	Using Metaclass we don't need to specify _fields here
	Also, in PosInteger we need not to specify name
	"""
	name = PosInteger()
	speak = SizedRegexString(maxlen=4, pat="[A-Z]+$")

def test(a, b=10):
	pass
# if __name__ == '__main__':
cat = Cat(1, "MEOW")
print(cat.name)
# cat.speak = "meow" # ValueError: Invalid String
print(cat.speak)

# import sys
# print(sys.modules['simple_descriptors'])
# <module 'simple_descriptors' from 'D:\\projects\\python metaclasses and patterns\\src\\descriptors\\simple_descriptors.py'>

# print(Descriptor.__module__) # >> simple_descriptors
# print(re.__name__) # >> re
# print(re.__file__) # C:\Program Files\Python38-32\lib\re.py
# print(Cat.__doc__) # print documentation of module defined at top
# print(help(type))
class Spice(object):

	def __getattribute__(self, name):
		print("Value of variable %s" % (name))
		return super().__getattribute__(name)

	def __setattr__(self, name, value):
		print("Setting attribute value {%s: %s}" % (name, value))
		super().__setattr__(name, value)

	def __repr__(self):
		return "called from class: %s" % self.__class__.__name__

sp = Spice()
sp.a = 10
print(sp.a)
print(sp)
# print(help(type))
