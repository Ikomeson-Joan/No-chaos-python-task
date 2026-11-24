

number = int(input('Enter a valid number or -1 to end: '))

count = 1
total = 0

while (number != -1):

	total += number
	average = total/count
	count += 1

	print(average)

	number = int(input('Enter a valid number or -1 to end: '))
