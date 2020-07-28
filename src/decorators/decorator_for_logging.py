"""
Write decorator for logging such as logging function name before
running function
"""
from functools import wraps
import logging

def debug(func):
	log = logging.getLogger(func.__module__)
	log.setLevel(logging.WARNING)
	func_name = func.__qualname__
	@wraps(func)
	def wrapper_function(*args, **kwargs):
		log.warning("Running method: %s", func_name)
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
