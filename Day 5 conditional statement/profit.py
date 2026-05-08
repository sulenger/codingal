actual_cost = float(input("Enter Actual cost: ")) 
sale_amount = float(input("Enter Sales amount: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No profit !!!!!!")
    