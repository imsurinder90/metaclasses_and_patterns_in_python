import unittest
from descriptors.simple_descriptors import Cat

class TestSimpleDescriptor(unittest.TestCase):
	cat = Cat("Small cat", "meow meow meow")
	def test_cat_name(self):
		self.assertEqual(self.cat.name, "Small cat")
	
	def test_cat_speak(self):
		self.assertEqual(self.cat.speak, "meow meow meow")

if __name__ == '__main__':
	unittest.main()