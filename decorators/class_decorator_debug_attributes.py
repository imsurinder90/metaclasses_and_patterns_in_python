"""
Decorator to debug class methods
This decorator gets access to following:
1. instance attributes
2. instance methods
3. class methods
4. static methods
but do not have access to class variable

But, what if we want to debug more than 1 class? Here comes the concept of
Metaclass, with the help of metaclass we can debug all classes associated
to it.
"""

def debugattrs(cls):
	"""This decorator gets access to all attributes of class
	whether it is varible or method"""
	original_getattribute = cls.__getattribute__
	def __getattribute__(self, name):
		print('called attribute %s' % name)
		return original_getattribute(self, name)
	cls.__getattribute__ = __getattribute__

	return cls

@debugattrs
class FooBar:
	_temp = []
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def bar(self, c, d):
		pass

	@classmethod
	def class_method_foo(cls):
		pass

	@staticmethod
	def static_method_foo():
		pass

if __name__ == "__main__":
	foobar = FooBar(3, 7)
	foobar.a
	foobar.bar(33, 34)
	foobar.class_method_foo()
	foobar.static_method_foo()
	FooBar._temp
