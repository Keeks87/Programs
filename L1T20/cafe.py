menu = ["coffee", "tea", "pastry", "sandwich"]
stock = {"coffee": 10, "tea": 5, "pastry": 7, "sandwich": 8}
price = {"coffee": 2.5, "tea": 1.5, "pastry": 3.0, "sandwich": 5.0}

# Initialize variable to store total stock worth
total_stock_worth = 0

# Iterate through menu items
for item in menu:
    # Add the total value of current item to total_stock_worth
    total_stock_worth += stock[item] * price[item]

# Print the final value of total_stock_worth
print("Total stock worth in the cafe: $" + str(total_stock_worth))
