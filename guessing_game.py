

random_number = 13
counter = 1

user_input = int(input('Pick a number: '))


while (user_input != random_number):

	counter += 1

	user_input = int(input('Pick a number: '))

print ('The user made', counter, 'guesses')