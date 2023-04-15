#You will need to create four functions:
#hotel_cost — This function will take the number of nights a user will be staying at a hotel
#as an argument, and return a total cost for the hotel stay (You can choose the price per night
#charged at the hotel).
#plane_cost — This function will take the city you are flying to as an argument and return a cost 
#for the flight (Hint: use if/else if statements in the function to retrieve a price based on the chosen city).
#car_rental — This function will take the number of days the car will be hired for as an argument and return the
#total cost of the car rental.
#holiday_cost — This function will take three arguments: the number of nights a user will be staying in a hotel,
#the city the user will be flying to, and the number of days that the user will be hiring a car for. Using these
#three arguments, you can call all three of the above functions with respective arguments and finally return a
#total cost for your holiday.
#Print out all the details about the holiday in a meaningful way!
#Try using your program with different combinations of input to show its compatibility with different options.

# This function takes the number of nights as an argument and returns the total cost for hotel stay
def hotel_cost(nights):
    return nights * 150

# This function takes the city as an argument and returns the cost for the flight
def plane_cost(city):    
    if city == "New York":
        return 500
    elif city == "Paris":
        return 700
    elif city == "Tokyo":
        return 800
    else:
        return 0

# This function takes the number of days as an argument and returns the total cost for car rental
def car_rental(days):
    return days * 30

# This function takes three arguments: number of nights, city, and number of days.
# It calls the above three functions with respective arguments and returns the total cost for the holiday
def holiday_cost(nights, city, days):    
    return hotel_cost(nights) + plane_cost(city) + car_rental(days)

# Get the values for number of nights, city, and number of days from the user
nights = int(input("Enter the number of nights: "))
city = input("Enter the city: ")
days = int(input("Enter the number of days for car rental: "))

# Calculate the costs for the holiday
holiday_cost = holiday_cost(nights, city, days)
hotel_cost = hotel_cost(nights)
plane_cost = plane_cost(city)
car_rental_cost = car_rental(days)

# Print the details about the holiday in a meaningful way
print("Holiday cost: " + str(holiday_cost))
print("Hotel cost: " + str(hotel_cost))
print("Plane cost: " + str(plane_cost))
print("Car rental cost: " + str(car_rental_cost))
