"""
With the help of metaclass we can make our class look
simple. Metaclass creates a class object and assigns
_fields to it.
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

class Cat(Animal):
	_fields = ["name", "speak"]

class Dog(Animal):
	_fields = ["nickname", "is_pet"]

cat = Cat("my cat", "meow")
print(cat.name)
dog = Dog("Bruno", "yeah")
print(dog.nickname)