def max_profit(prices):
	if len(prices) < 2:
		return "No profit can be made."
	max_profit = 0
	buy_day = 0
	sell_day = 0
	min_price = prices[0]
	for i in range(1, len(prices)):
		if prices[i] < min_price:
			min_price = prices[i]
			buy_day = i
		else:
			profit = prices[i] - min_price
			if profit > max_profit:
				max_profit = profit
				sell_day = i
	if buy_day >= sell_day:
		return f"{max_profit} (Should buy on {buy_day + 1}(price = {prices[buy_day]}) day and wait for the stock price to rise)"
	else:
		return f"{max_profit} (Buy on day {buy_day + 1} (price = {prices[buy_day]}) and sell on day {sell_day + 1} (price = {prices[sell_day]}))"


#Usage
print("Enter the stock prices list elements seperated by commas: ")
while(True):
	input_str = input()
	my_list = input_str.split(",")
	try:
		prices = [int(num) for num in my_list]
	except ValueError:
		prices = []
		print("ValueError: Prices cannot have spaces between them, Try again: ")
	if prices != []:
		break


print(max_profit(prices))
