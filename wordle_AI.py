
wordset = set()
letter_dict = {}
valid_word = True

myword = input("\nEnter your word\n")
myword = myword.strip()

num_of_lettters = len(myword)

doc_to_open = ""

if num_of_lettters == 5:
	doc_to_open = "fives.txt"
elif num_of_lettters ==6:
	doc_to_open = "sixes.txt"
elif num_of_lettters == 7:
	doc_to_open = "sevens.txt"
elif num_of_lettters == 8:
	doc_to_open = "eights.txt"
else:
	print("The word doesn't have the correct number of letters.")
	valid_word = False

if valid_word:
	f = open(doc_to_open, "r")
	for x in f:
		if(x.strip() != ""):
			z = x.strip()
			wordset.add(z)

def countLetters():
	letter_dict.clear()
	for word in wordset:
		for char in word:
			if char in letter_dict.keys():
				letter_dict[char] += 1
			else:
				letter_dict[char] = 1


def findBestWord():
	biggest_total = 0
	retval = ""
	for word in wordset:
		actual_word = word
		word = set(word)
		total = 0
		for char in word:
			total += letter_dict[char]
		if total > biggest_total:
			retval = actual_word
			biggest_total = total
	return retval

def removeWithLetter(letter):
	copyW = set()
	for y in wordset:
		if letter not in y:
			copyW.add(y)
	return copyW

def keepWithLetter(letter):
	copyW = set()
	for y in wordset:
		if letter in y:
			copyW.add(y)
	return copyW

def keepWithLetterInPlace(letter, p): # p is place  word is my word
	copyW = set()
	for y in wordset:       # y is each character
		if y[p] == letter:
			copyW.add(y)
	return copyW

def removeWithLetterInPlace(letter, index):
	copyW = set()
	for y in wordset:
		if y[index] != letter:
			copyW.add(y)
	return copyW


counter = 1
not_done = True
if not valid_word or myword not in wordset:
	not_done = False
	print("That is not in the list of valid words.")
#while not_done and counter < 20:
while not_done:
	print("counter =",counter)

	countLetters()
	best_word = findBestWord()
	print("best word:",best_word, "   ", len(wordset)," words remaining")

	not_done = not (best_word == myword)

	if not_done:
		# compare best_word to myword
		index = 0
		for x in best_word:   # x is letter in computer's guess
			if x == myword[index]:
				wordset = keepWithLetterInPlace(x,index)	
			elif x in myword:
				wordset = keepWithLetter(x)
				wordset = removeWithLetterInPlace(x,index)
			else:
				wordset = removeWithLetter(x)
			index += 1


	counter += 1

