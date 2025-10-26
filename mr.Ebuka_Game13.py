numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def  square_numbers(number):
	return number * number

result = list(map(square_numbers, numbers))
print(result)