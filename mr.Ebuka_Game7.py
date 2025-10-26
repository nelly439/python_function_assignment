def get_even_number(number):
	return number % 2 == 0

result = list(filter(get_even_number, range(1,21)))
print(result)