import unittest
import math

class Test(unittest.TestCase):

	def test_addition(self):
		self.assertEqual(1+1, 2) 

	def test_sqrt(self):
		self.assertEqual(math.sqrt(10)**10, 10)