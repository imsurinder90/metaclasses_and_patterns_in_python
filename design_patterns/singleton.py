"""
Singleton pattern creates only one instance of class
Here we created two objects for Counter class and both
objects are allocated same address on heap. If an Object
of a class is already present, that object is returned
"""

def Singleton(cls):
	_instances = {}
	def getinstance():
		if cls not in _instances:
			_instances[cls] = cls()
		return _instances[cls]
	return getinstance

@Singleton
class Counter(object):
	def __init__(self):
		if not hasattr(self, 'val'):
			self.val = 0
	def get(self):
		return self.val
	def incr(self):
		self.val += 1

def main():
	"""
	>>> obj = Counter()
	>>> obj2 = Counter()
	>>> obj == obj2
	True
	"""

if __name__ == "__main__":
	import doctest
	doctest.testmod()