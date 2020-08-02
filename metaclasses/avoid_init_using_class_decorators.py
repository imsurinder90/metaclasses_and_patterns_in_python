"""
With the help of decorators we can make our class look
simple. Here we define __init__ method of Animal class
which binds the values of variables name and speak.
Class level decorator @add_signature takes in class
variables and creates variables using Signature module.
It also makes these parameters both as args and kwargs.
"""
from inspect import Parameter, Signature

def make_signature(fields):
	return Signature(
				Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
			for name in fields)

def add_signature(*args):
	def wrapper_function(cls):
		cls._signature = make_signature(args)
		return cls
	return wrapper_function


class Animal:
	_signature = make_signature([])
	def __init__(self, *args, **kwargs):
		bound_args = self._signature.bind(*args, **kwargs)
		for key, val in bound_args.arguments.items():
			setattr(self, key, val)

@add_signature("name", "speak")
class Cat(Animal):
	pass

@add_signature("nickname", "is_pet")
class Dog(Animal):
	pass

cat = Cat("my cat", speak="meow")
print(cat.speak)
dog = Dog("Bruno", is_pet="yeah")
print(dog.nickname)

import inspect
print(inspect.signature(Dog)) # returns (*args) but should return (name, is_pet)