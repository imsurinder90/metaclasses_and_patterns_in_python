"""
What if we wish to apply decorator for all the methods of a class??
It's possible with the help of class decorator.
Limitation: Class decorator do not work for class methods and
static methods

Let's see how setattr works before we use class decorator
Syntax : setattr(obj, var, val)

Parameters :
obj : Object whose which attribute is to be assigned.
var : object attribute which has to be assigned.
val : value with which variable is to be assigned.
"""
from functools import wraps
def debug(func):
	msg = "Calling method: %s" % (func.__qualname__)
	@wraps(func)
	def wrapper_function(*args, **kwargs):
		# print(msg)
		return func(*args, **kwargs)
	return wrapper_function

def debugmethods(cls):
	# vars(cls) -> {'add': <function TestClass.add at 0x0118EC40>,}
	# print(vars(cls))
	for name, val in vars(cls).items():
		if callable(val):
			setattr(cls, name, debug(val))
	return cls

@debugmethods
class TestClass(object):

	def add(a, b):
		return a + b

	def sub(a, b):
		return a - b

	@classmethod
	def foo(cls):
		return 'foo'

if __name__ == "__main__":
	print(TestClass.add(3, 4))
	print(TestClass.sub(4, 3))
	print(TestClass.foo()) # Class decorator is not working for cls methods