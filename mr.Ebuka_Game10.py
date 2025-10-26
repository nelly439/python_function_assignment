def get_numbers_divisible_by_three_and_five(numbers):
	return numbers % 3 == 0 and numbers % 5 == 0

result = list(filter(get_numbers_divisible_by_three_and_five, range(1,51)))
print(result)