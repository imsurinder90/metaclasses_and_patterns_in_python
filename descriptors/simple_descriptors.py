"""
Descriptors helps us create class attribues in a different
way to allow more flexibility/feature for a Integer/Float
or String or any data types. It accepts the class varible
defined and then assign it to the Class __dict__
"""

from inspect import Parameter, Signature

def make_signature(args):
	return Signature(
				Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
			for name in args)

class AnimalMeta(type):
	def __new__(cls, clsname, bases, clsdict):
		clsobj = super().__new__(cls, clsname, bases, clsdict)
		sig = make_signature(clsobj._fields)
		setattr(clsobj, "_fields", sig)
		return clsobj

class Animal(metaclass=AnimalMeta):
	_fields = []
	def __init__(self, *args, **kwargs):
		bound_args = self._fields.bind(*args, **kwargs)
		for key, val in bound_args.arguments.items():
			setattr(self, key, val)

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

class Cat(Animal):
	_fields = ["name", "speak"]
	name = Descriptor('name')
	speak = Descriptor('speak')

if __name__ == "__main__":
	cat = Cat("cat", "meow")
	cat.speak = "meow meow"
	print(cat.speak)
	# del cat.speak

