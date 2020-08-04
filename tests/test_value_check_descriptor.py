import unittest
from descriptors.value_checking_descriptor import Cat

class TestValueCheckDescriptor(unittest.TestCase):
	cat = Cat(123456, "cat speaks meow meow")
	def test_cat_name(self):
		self.assertEqual(self.cat.name, 123456)
	
	def test_cat_speak(self):
		self.assertEqual(self.cat.speak, "cat speaks meow meow")

if __name__ == '__main__':
	unittest.main()