import unittest
from decorators.decorator_for_methods import add, sub

class TestMethodDecorator(unittest.TestCase):
	def test_add(self):
		self.assertEqual(add(1, 2), 3)

	def test_sub(self):
		self.assertEqual(sub(3, 2), 1)

	def test_sub_not_equal(self):
		self.assertNotEqual(sub(3, 2), 0)

if __name__ == '__main__':
	unittest.main()
