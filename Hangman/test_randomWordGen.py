import unittest 
from randomWordGen import *
from Player import *

class TestRandomWordGen(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_getRandomWord(self):
		self.assertIsNotNone(getRandomWord())

	# below commented code was attempt at handling the case where 
		# there could not be established a connection 
		#between the randomword library and machine

	# def test_isConnectionToRandomWordLibraryPossible(self):
	# 	self.assertRaises(ConnectionError, getRandomWord)

class TestPlayer(unittest.TestCase):

	def setUp(self):
		self.player = Player()

	def tearDown(self):
		del self.player

	def test_makeNewGuess(self):
		self.assertIsNotNone(self.player.makeNewGuess())


if __name__ == '__main__':
	unittest.main()