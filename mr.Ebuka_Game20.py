numbers = [(1, 2), (3, 4), (5, 6)]

def sum_of_element(number1):

	return sum(number1)
	

def element_greater_than_five(number2):

	return number2 > 5


sums = list(map(sum_of_element, numbers))

result = list(filter(element_greater_than_five, sums))
print(result)