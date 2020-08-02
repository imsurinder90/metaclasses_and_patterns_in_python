import unittest
from decorators.class_decorator import TestClass

class TestClasDecorator(unittest.TestCase):
	def test_add(self):
		self.assertEqual(TestClass.add(3, 4), 7)

	def test_sub(self):
		self.assertEqual(TestClass.sub(4, 3), 1)

if __name__ == '__main__':
	unittest.main()