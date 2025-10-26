words = [(1, 'A'), (4, 'B'), (2, 'C')]

def get_largest_tuple(word):
	return word[0] > 2

result = list(filter(get_largest_tuple,words))
print(result)