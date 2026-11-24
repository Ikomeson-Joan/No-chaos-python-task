


word = input ('Enter a word: ')

number_of_vowels = 0
number_of_consonants = 0

for character in word:

	vowel_sample = "aeiou"

	if character in vowel_sample:
		number_of_vowels += 1

	else:
		number_of_consonants += 1

print ('Number of vowels is', number_of_vowels)

print ('Number of consonants is', number_of_consonants)
