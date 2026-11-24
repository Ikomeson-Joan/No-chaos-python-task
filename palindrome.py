

word = input('Enter a word: ')
count = len(word)
letters = ""

for count in range (len(word)-1, -1, -1):
	
	letters += word[count]

if (word == letters):
	print (word, 'is a palindrome')
else:
	print (word, 'is not a palindrome')
