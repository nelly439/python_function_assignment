prices = [100, 200, 300]

def get_ten_percent(price):

	return double(price * 1.10)

result = list(map(get_ten_percent, prices))
print(result)