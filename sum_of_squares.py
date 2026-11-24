
number = 432

divisor = 100
sum_of_squares = 0

while (divisor >= 1):

	digit = number // divisor

	number = number % divisor
	divisor = divisor // 10
	sum_of_squares += (digit**2)


if (sum_of_squares == number):
print(sum_of_squares)

