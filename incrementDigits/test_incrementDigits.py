import unittest
from incrementDigits import *

class TestIncrementDigits(unittest.TestCase):

	def setUp(self):
		# pseudo userInput, will be used until can get input into sublime working
		self.userInput = 123

	def tearDown(self):
		pass

	def test_isInvalidInput(self):
		self.assertEqual(isInvalidInput(-0), False)
		self.assertEqual(isInvalidInput(-1), True)
		self.assertEqual(isInvalidInput("afesg"), True)

	def test_howManyDigits(self):
		self.assertEqual(howManyDigits(123), 3)
		self.assertEqual(howManyDigits(0), 1)

	def test_splitNumToArrayOfDigits(self):
		self.assertEqual(splitNumToArrayOfDigits(0), [0])
		self.assertEqual(splitNumToArrayOfDigits(10), [1,0])
		self.assertEqual(splitNumToArrayOfDigits(1000000000), [1,0,0,0,0,0,0,0,0,0])

	def test_coalesceListToNumber(self):
		self.assertEqual(coalesceListToNumber([0]), 1)
		self.assertEqual(coalesceListToNumber([9]), 10)
		self.assertEqual(coalesceListToNumber([1,0]), 21)
		self.assertEqual(coalesceListToNumber([9,9]), 1010)
		self.assertEqual(coalesceListToNumber([9,9,8]), 10109)
		
if (__name__ == '__main__'):
	unittest.main()
