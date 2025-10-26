from functools import reduce

numbers = [ 3, 5, 9, 2, 8]

def find_the_largest(num,number):

	if num > number:
		return num
	else:
		return number

result = reduce(find_the_largest,numbers)
print(result)