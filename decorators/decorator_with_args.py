"""
Parameterized decorator whic takes a parameter as an
argument. It is helpful when each function needs a
different message to print
Decorator with args
	@decorator(args)
	def func():
		pass
	func = decorator(args)(func)
"""
from functools import wraps, partial

def debug(func=None, *, prefix=""):
	if func is None:
		return partial(debug, prefix=prefix)

	msg = "%s - method: %s" % (prefix, func.__qualname__)
	@wraps(func)
	def wrapper_function(*args, **kwargs):
		print(msg)
		return func(*args, **kwargs)
	return wrapper_function

@debug(prefix="Addition of two numbers")
def add(a, b):
	return a + b

@debug(prefix="Subtraction of two numbers")
def sub(a, b):
	return a - b

print(add(3, 4))
print(sub(4, 3))
