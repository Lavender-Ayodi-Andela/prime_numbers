import unittest

from type_of_data import data
class type_of_data(unittest.TestCase):
	def test_string1(self):
		self.assertEqual(type_of_data("boy"), "This is a string")

	def test_string2(self):
		self.assertEqual(type_of_data("1"), "This is a string")

	def test_integer(self):
		self.assertEqual(type_of_data(101), "This is an integer")

	def test_float(self):
		self.assertEqual(type_of_data(3.5), "This is a float")

	def test_boolean1(self):
		self.assertEqual(type_of_data(True), "This is a Boolean Value")

	def test_boolean2(self):
		self.assertEqual(type_of_data(False), "This is a Boolean Value")

	def list1(self):
		self.assertEqual(type_of_data([1,2,3,4]),"This is a List" )

	def list1(self):
		self.assertEqual(type_of_data(['cat', 'dog', 'horse']),"This is a List" )

	def dictionary1(self):
		self.assertEqual(type_of_data({'key1':1,'key2':2,'key3':3,'key4':4}),"This is a Dictionary" )

	def dictionary1(self):
		self.assertEqual(type_of_data({'key1':orange,'key2':apple,'key3':plums}),"This is a Dictionary" )
		
