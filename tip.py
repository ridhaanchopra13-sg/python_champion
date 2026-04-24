def calculate_tip(money, perc):
	total = money * (1 + 0.01 * perc)
	total = round(total, 2)
	print(f"Please pay ${total}")
	return total

total_calc = calculate_tip(150, 20)