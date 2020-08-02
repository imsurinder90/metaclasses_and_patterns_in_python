"""
Using Inheritance, we can omit __init__
Class level attributes and values(passed through Object initialization)
are bind to class in __init__ method using
setattr(class, attribute, value_passed)
Limitations:
1. Keyword args are not supported
2. Missing calling signature
It is fixed using Signature Binding
"""

class Animal:
	_fields = [] # optional
	def __init__(self, *args):
		if len(args) != len(self._fields):
			raise TypeError("Wrong # args")
		# zip(self._fields, args) -> {'name': 'my cat', 'speak': 'meow'}
		for name, val in zip(self._fields, args):
			setattr(self, name, val)

class Cat(Animal):
	_fields = ["name", "speak"]

class Dog(Animal):
	_fields = ["nickname", "is_pet"]

cat = Cat("my cat", "meow")
print(cat.speak)
dog = Dog("Bruno", "yeah")
print(dog.nickname)

import inspect
print(inspect.signature(Cat)) # returns (*args)
