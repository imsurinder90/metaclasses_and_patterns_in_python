"""
To debug number of classes and its methods, we can do this
by creating a metaclass and allow other classes to inherit from it.
Once a class object is created inside metaclass, we can wrap that
instance of a class with the debugmethods wrapper function.
"""

def debugmethods(cls):
	"""This decorator gets access to all attributes of class
	whether it is varible or method"""
	original_getattribute = cls.__getattribute__
	def __getattribute__(self, name):
		print('called attribute %s' % name)
		return original_getattribute(self, name)
	cls.__getattribute__ = __getattribute__

	return cls

########## - This is syntax for creating a metaclass #########
class debugmeta(type):
	"""
	This is a metaclass inheriting from type class. Any class inherting
	from this will be called in __new__ method of this class which
	helps in getting access to the class object of inherited classes.
	"""
	def __new__(cls, clsname, bases, clsdict):
		clsobj = super().__new__(cls, clsname, bases, clsdict)
		if clsname != 'Base':
			clsobj = debugmethods(clsobj)
		return clsobj

class Base(metaclass=debugmeta):
	pass

class A(Base):
	def a_foo(self):
		pass
	
	@staticmethod
	def a_static_foo():
		pass

class B(Base):
	def b_foo(self):
		pass
	
	@staticmethod
	def b_static_foo():
		pass

	@classmethod
	def b_class_foo(cls):
		pass

a = A()
a.a_foo()
a.a_static_foo()

b = B()
b.b_foo()
b.b_static_foo()
b.b_class_foo()
