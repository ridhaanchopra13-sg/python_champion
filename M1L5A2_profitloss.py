
sale_amount = float(input("Enter the sale amount"))
actual_amount = float(input("Enter the actual amount"))
if sale_amount>actual_amount:
    profit = sale_amount-actual_amount
    print("Your profit is{0}".format(profit))
else:  
    print("NO PROFIT")