numbers = ['123', '456', '789', 'abc', 'def']

def sum_numberic_string(numbers):

	number = [int(item) for item in numbers if item.isdigit()]
	return sum(number)
result = sum_numberic_string(numbers)
print(result)

	