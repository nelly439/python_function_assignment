from functools import reduce

words = ['I', 'Love', 'Python']

def convert_to_string(word,letter):

	return word + ' ' + letter
result = reduce(convert_to_string, words)
print(result)