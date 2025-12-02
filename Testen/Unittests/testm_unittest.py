import unittest
import math

class Test(unittest.TestCase):

	# A1 
	def test_addition(self):
		self.assertEqual(1+1, 2) 

	# A2 - A4
	#@unittest.expectedFailure
	def test_sqrt(self):
		self.assertAlmostEqual(math.sqrt(10)**2, 10)

	# A5
	def test_sqrt_of_negative_value(self):
		with self.assertRaises(ValueError):
			math.sqrt(-1)
   
	def test_failure1(self):
		print("lots\nof\nstuff")
		self.assertTrue(False)

	def test_failure2(self):
		print("still\nmore\nstuff")
		self.assertTrue(False)