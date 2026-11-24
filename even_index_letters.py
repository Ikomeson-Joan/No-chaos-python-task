

word = input('Enter a word: ')
length = len(word)
even_index_letters = ""

for count in range (0, length, 2):
	
	even_index_letters += word[count]

print (even_index_letters)