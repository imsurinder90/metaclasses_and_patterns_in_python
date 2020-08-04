import unittest
from descriptors.sized_descriptor import Cat

class TestSizedDescriptor(unittest.TestCase):
	cat = Cat(1, "meow")
	def test_cat_name(self):
		self.assertEqual(self.cat.name, 1)
	
	def test_cat_speak(self):
		self.assertEqual(self.cat.speak, "meow")

if __name__ == '__main__':
	unittest.main()