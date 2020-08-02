"""
Using Parameter and Signature from inspect module to make signature
which supports both positional arguments and keyword arguments.
Two steps:
1. Tell Signature about the args/kwargs
from inspect import Parameter, Signature
fields = ["name", "speak"]
params = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) /
			for name in fields]
sig = Signature(params)
2. Bind values passed in __init__
def func(*args, **kwargs):
	bound_args = sig.bind(*args, **kwargs)
	for key, val in bound_args.arguments.items():
		print(key, "=", val)
>>> func("cat", speak="meow")
"""
from inspect import Parameter, Signature

def make_signature(fields):
	return Signature(
				Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
			for name in fields)

class Animal:
	_signature = make_signature([])
	def __init__(self, *args, **kwargs):
		bound_args = self._signature.bind(*args, **kwargs)
		for key, val in bound_args.arguments.items():
			setattr(self, key, val)

class Cat(Animal):
	_signature = make_signature(["name", "speak"])

class Dog(Animal):
	_signature = make_signature(["nickname", "is_pet"])

cat = Cat("my cat", speak="meow")
print(cat.speak)
dog = Dog("Bruno", is_pet="yeah")
print(dog.nickname)

import inspect
print(inspect.signature(Dog)) # returns (*args) but should return (name, is_pet)