# https://docs.python.org/3/library/unittest.html
# https://github.com/python/cpython/blob/3.8/Lib/unittest/__init__.py

import unittest

class TestStringMethods(unittest.TestCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')	# check expected result

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())	# verify condition
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		#check that s.split fails when the seperator is not a string
		with self.assertRaises(TypeError):	# verify a specific exception gets raised
			s.split(2)

if __name__ == '__main__':
	unittest.main()	# provide a command-line interface