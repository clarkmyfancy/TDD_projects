from random_word import RandomWords
# # 
# def isConnectionToRandomWordLibraryPossible():
# 	try:
# 		r = RandomWords()
# 	except:
# 		raise ConnectionError("Cannot connect to RandomWords library")


def getRandomWord():
	r = RandomWords()
	return r.get_random_word()