tuple_list = ['python', 'java', 'c++']

def convert_to_uppercase(word):
	return word.upper()
result = list(map(convert_to_uppercase, tuple_list))
print(result)