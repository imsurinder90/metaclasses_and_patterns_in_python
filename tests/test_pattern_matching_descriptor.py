import unittest
from descriptors.pattern_matching_descriptor import Cat

class TestPatternMatchingDescriptor(unittest.TestCase):
	cat = Cat(4, "MEOW")
	def test_cat_name(self):
		self.assertEqual(self.cat.name, 4)
	
	def test_cat_speak(self):
		self.assertEqual(self.cat.speak, "MEOW")

if __name__ == '__main__':
	unittest.main()