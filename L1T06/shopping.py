#Create a new pyhton file in this folder called shopping.py
#Once this is done, ask the user to enter the names of three products
#now ask for the price of each product. Each product must have two decimal values.
#Calculate the total of all three products.
#Calculate the average price of the three products. (Hint: you may want to look up round())
#Then print out the following sentence after perfomring your calculations:
#"The Total of [product1], [product2], [product3] is Rxx,xx and the average price of the items is Rxx,xx."

#Ask the user to enter the names of three products

product1 = input("Please enter a product name")
product2 = input("Please enter a product name")
product3 = input("Please enter a product name")

#Ask for the price of each product to two decimal places

price_product1 = float(input("please enter price for 1st product including cents"))
price_product2 = float(input("please enter price for 2nd product including cents"))
price_product3 = float(input("please enter price for 3rd product including cents"))

#Total of all three products.

sum_products = price_product1 + price_product2 + price_product3
#print(sum_products)

#Average price of the three products

average_price = round((sum_products) / 3)
#print(average_price)

#Print sentence with calculations:

variables_sentence = "The Total of {}, {} and {} is R {} and the average price of the items is R {}".format(product1,product2,product3,sum_products,average_price)
print(variables_sentence)


#line 33 (variable_sentence took me a long time to figure out. I used link https://matthew-brett.github.io/teaching/string_formatting.html to assist me in the end)