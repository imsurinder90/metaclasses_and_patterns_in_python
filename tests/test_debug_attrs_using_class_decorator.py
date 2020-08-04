import unittest
from decorators.class_decorator_debug_attributes import FooBar

class TestLoggingDecorator(unittest.TestCase):
	foobar = FooBar(3, 7)
	def test_get_attribute(self):
		self.assertEqual(self.foobar.a, 3)

if __name__ == '__main__':
	unittest.main()