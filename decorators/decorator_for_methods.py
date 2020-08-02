"""
Decorator is a function which creates a wrapper around a function
Wrapper is like a normal function except that it allows to run
piece of code befor the execution of a function.
"""

# Lets write a decorator to print fn name before a function execution

from functools import wraps

def debug(func):
	func_name = func.__qualname__
	@wraps(func)
	def wrapper_function(*args, **kwargs):
		print("Running method: %s" % func_name)
		return func(*args, **kwargs)
	return wrapper_function

@debug
def add(a, b):
	return a + b
@debug
def sub(a, b):
	return a - b

if __name__ == "__main__":
	print(add(3, 4))
	print(sub(4, 3))