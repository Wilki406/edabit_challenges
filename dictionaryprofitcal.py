def profit(info):
	[a, b, c]=info.values()
	return round((b-a)*c)


d = {'cost_price': 32.67, 'sell_price': 45.00, 'inventory': 1200}


[a, b, c]=d.values()
print(round((b-a)*c))
profit(d)
