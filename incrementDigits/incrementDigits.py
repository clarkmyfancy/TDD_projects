def getStringFromUserAndCastToInt():
	userInput = raw_input("Enter a number: ")
	if isInvalidInput(userInput):
		userInput = getStringFromUserAndCastToInt()
	return int(userInput)

def isInvalidInput(x):
	try: 
		newInput = int(x)
		print(newInput)
		if newInput < 0:
			print("Input should a positive number.")
			return True
		return False
	except:
		print("Input should a positive number.")
		return True

def howManyDigits(x):
	x = abs(x)
	if x == 0:
		return 1

	numDigits = 0
	while x > 0:
		x //= 10
		numDigits += 1
	return numDigits

def incrementDigit(x):
	return x+1

def splitNumToArrayOfDigits(x):
	if x == 0:
		return [0]
	individualDigits = []
	numDigits = howManyDigits(x)
	for i in range(0, numDigits):
		lastDigit = x%10
		x //= 10
		x == 0
		individualDigits.append(lastDigit)
	return individualDigits[::-1]

def coalesceListToNumber(inputList): 
	coalescedNumber = 0
	inputList = inputList[::-1]
	multiplier = 1
	for x in inputList:
		coalescedNumber += incrementDigit(x)*multiplier
		if x == 9:
			multiplier *= 100
		else:
			multiplier *= 10

	return coalescedNumber

def main():
	userInput = getStringFromUserAndCastToInt()
	digitsFromUserInput = splitNumToArrayOfDigits(userInput)
	incrementedNumber = coalesceListToNumber(digitsFromUserInput)
	print(incrementedNumber)


if __name__ == '__main__':
	main()


