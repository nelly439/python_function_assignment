names = ['john', 'mary', 'steve']

def first_letter_of_each_names(names):

	return list(map(str.capitalize, names))

result = first_letter_of_each_names(names)
print(result)