def calculate_total(user_price, user_cups):
    total = user_price * user_cups
    return total

# 1. Let the user decide the values
user_price = float(input("Enter the price per cup: "))
user_cups = int(input("Enter how many cups you want: "))

# 2. Call your function using the user's choices
result = calculate_total(user_price, user_cups)

# 3. Print the final answer
print("Your total is:", result)