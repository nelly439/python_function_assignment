from functools import reduce

def sum_of_numbers(numbers,number):

	return numbers + number

result = reduce(sum_of_numbers,range (1,50))
print(result)