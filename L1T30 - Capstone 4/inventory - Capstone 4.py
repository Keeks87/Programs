
from tabulate import tabulate

# the beginning of the class

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_country(self):
        return self.country
    
    def get_code(self):
        return self.code
    
    def get_product(self):
        return self.product

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f'Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}'

# shoe list
shoe_list = []

# functions outside the class
'''- read_shoes_data - This function will open the file
            inventory.txt and read the data from this file, then create a
            shoes object with this data and append this object into the
            shoes list. One line in this file represents data to create one
            object of shoes. You must use the try-except in this function
            for error handling. Remember to skip the first line using your
            code.'''
def read_shoes_data(file_name):
    try:
        with open(file_name, 'r+') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if i == 0:
                    continue
                country, code, product, cost, quantity = line.strip().split(',')
                cost = float(cost)
                quantity = int(quantity)
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    except FileNotFoundError:
        raise Exception("Inventory file not found: " + file_name)

'''- capture_shoes - This function will allow a user to capture
            data about a shoe and use this data to create a shoe object
            and append this object inside the shoe list.'''

def capture_shoes(file_name):
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

# this function will iterate over the shoes list and print the details of the shoes returned
def view_all():
    table = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_list]
    print(tabulate(table, headers=["Country", "Code", "Product", "Cost", "Quantity"]))

# This function will find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked.
def re_stock(code, qty): # Define the function 're_stock' which takes two parameters: 'code' and 'qty'
    for shoe in shoe_list: # Iterate over the list 'shoe_list'
        if shoe.code == code: # Check if the code of the current shoe matches the given code
            shoe.quantity += qty # If it matches, add 'qty' to the current shoe's quantity
            with open("inventory.txt", "w") as file: # Open the file 'inventory.txt' for writing
                for shoe in shoe_list: # Iterate over the updated list 'shoe_list'
                    file.write(f'{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n') # Write the updated information of each shoe in the format "country,code,product,cost,quantity"
            return f"Shoe with code {code} has been restocked with {qty} units." # Return a message indicating the success of the restocking process
    return f"Error: Shoe with code {code} not found." # If the shoe with the given code is not found, return an error message

# this function will search for a shoe from the list
def search_shoe(shoes, code): 
    for shoe in shoes:
        if shoe.code == code:
            return shoe
    return None

# this function will calculate the total value for each item
def value_per_item(shoes): 
    values = [] # Create an empty list to store the values of each shoe
    for shoe in shoes:
        cost = shoe.cost
        quantity = shoe.quantity
        value = cost * quantity
        values.append(value) # Add the calculated value to the list of values
    return values

# determine the product with the highest quantity and print this shoe as being for sale.
def highest_qty(shoes): 
  highest_shoe = shoes[0]
  for shoe in shoes:
    if shoe.quantity > highest_shoe.quantity:
      highest_shoe = shoe
  print(f"{highest_shoe.product} with code {highest_shoe.code} is for sale with the highest quantity of {highest_shoe.quantity}")

# main menu
if __name__ == "__main__":
    while True:
        print("Shoe Inventory System")
        print("1. Read Shoes Data")
        print("2. Capture Shoes")
        print("3. View All Shoes")
        print("4. Restock Shoes")
        print("5. Search Shoe")
        print("6. Value per item")
        print("7. Highest Quantity")
        print("8. Quit")
        choice = int(input("Enter your choice [1-8]: \n"))

        if choice == 1:
            read_shoes_data("inventory.txt")
        elif choice == 2:
            capture_shoes("inventory.txt")
        elif choice == 3:
            view_all()
        elif choice == 4:
            code = input("Enter the shoe code: ")
            qty = int(input("Enter the quantity to restock: "))
            re_stock(code, qty)
        elif choice == 5:
            code = input("Enter the shoe code: ")
            found_shoe = search_shoe(shoe_list, code)
            if found_shoe:
                print("Shoe found:", found_shoe)
            else:
                print("Shoe not found.")
        elif choice == 6:
            values = value_per_item(shoe_list)
            print("Value per item: ", values)
        elif choice == 7:
            highest_qty(shoe_list)
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please try again.")