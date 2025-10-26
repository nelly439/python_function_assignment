from functools import reduce

numbers = [1, 2, 3, 4]

def square_of_numbers(number1,number2):

	return number1 * number2

result = reduce(square_of_numbers,numbers)
print(result)