import unittest
from descriptors.descriptors_and_metaclass import Cat

class TestMetaclassDescriptor(unittest.TestCase):
	cat = Cat(5, "MEOW")
	def test_cat_name(self):
		self.assertEqual(self.cat.name, 5)
	
	def test_cat_speak(self):
		self.assertEqual(self.cat.speak, "MEOW")

	def test_cat_speak_set_attr(self):
		# TODO: Here we wish to capture if assignment
		# raises ValueError
		# self.cat.speak = "3" # raises ValueError 
		self.assertRaises(ValueError, setattr, self.cat, "speak", "MEOW")
		# with self.assertRaises(ValueError):
		# 	self.cat.speak="MEOW"

if __name__ == '__main__':
	unittest.main()