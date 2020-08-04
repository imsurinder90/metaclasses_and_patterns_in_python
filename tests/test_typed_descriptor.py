import unittest
from descriptors.typed_descriptor import Cat

class TestTypedDescriptor(unittest.TestCase):
	cat = Cat(23, "meow meow")
	def test_cat_name(self):
		self.assertEqual(self.cat.name, 23)
	
	def test_cat_speak(self):
		self.assertEqual(self.cat.speak, "meow meow")

if __name__ == '__main__':
	unittest.main()