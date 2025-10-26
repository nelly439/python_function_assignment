names = ['level', 'world', 'madam', 'python']

def filter_palinfrom(name):

	return name [ : : -1] == name

result = list(filter(filter_palinfrom,names))
print(result)