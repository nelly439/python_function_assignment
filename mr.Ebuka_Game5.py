numbers = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]

def sum_of_list(list):
	return [sum(list1) for list1 in list]

result = sum_of_list(numbers)
print(result)


def sum_of_list(list):
	return [sum(list1) for list1 in list +1]

result = sum_of_list(numbers)
print(result)