word = input('Enter a word: ')
count = len(word)
letters = ""

for count in range (len(word)-1, -1, -1):
	
	print(word[count], end='')