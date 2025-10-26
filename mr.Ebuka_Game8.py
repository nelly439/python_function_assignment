words = ['cat', 'Elephant', 'tiger', 'lion']


def get_number_greater_than_five(word):

	return len(word) > 5

result = list(filter(get_number_greater_than_five,words))
print(result)