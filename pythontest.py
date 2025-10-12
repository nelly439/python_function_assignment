def get_first_and_last_String(string):
	if len(string) < 2:
		return ""

	return string[0] + string[1] + string[-2] + string[-1]


print(get_first_and_last_String("semicolon"))


def add_String(string):

	if len(string) < 3:
		return string

	if string.endswith ('ing'):
		return string + 'ly'

	else:
		return string + 'ing'


print(add_String("dating"))


def get_vowel(string):
	vowels = 'a,e,i,o,u'

	result = [char for char in string if char in vowels] 
	return result

print(get_vowel("semicolon"))


def get_smallest_number(number):
	minimum_num = number[0]  
	for count in number[1:]:  
		if count < minimum_num: 
			minimum_num = count
			return minimum_num

my_list = [3, 4, 6, 1, 8]
minimum_value = get_smallest_number(my_list)
print(minimum_value)

def get_largest_number(number):
	largest_num = number[0] 
 
	for count in number[1:]:  
		if count > largest_num: 
			largest_num = count
	return largest_num

my_list = [3, 4, 6, 1, 8]
largest_value = get_largest_number(my_list)
print(largest_value)


def get_square_of_number(numbers):

	squares = [number ** 2 for number in numbers]
	return squares

my_list = [2, 3, 4, 5]
square_values = get_square_of_number(my_list)
print(square_values)

def get_sum_square(numbers):

	square= [number ** 2 for number in numbers]

my_list = [2, 3, 4, 5]
square_values = get_square_of_number(my_list)
total_of_squares = sum(square_values)
print(total_of_squares)



