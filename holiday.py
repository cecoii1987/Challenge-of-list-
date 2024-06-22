# As per good practice we start by defining the functions
def hotel_cost(num_nights):# 1st function was defining hotel cost
    if city_flight == 'Valencia': # We used if-elif and else option as per task hint
        return num_nights * 25 # The hotel cost for Valencia
    elif city_flight == 'New York':
        return num_nights * 100 # The hotel cost if the user goes to New York
    elif city_flight == 'Cyprus':
        return num_nights * 75 # The hotal cost if the user goes to Cyprus
    else:
        return 0 # If none of the above the cost will be 0
  
def plane_cost(city_flight): # Then we defined the second option which is plane cost in function of destination
    if city_flight == 'Valencia': # We used if-elif and else option as per task hint
        return 150 # If flight is to Valencia the cost will be 150
    elif city_flight == 'New York':
        return 750 # If flight is from New York the price will be 750
    elif city_flight == 'Cyprus':
        return 350 # If the flight is from Cyprus cost will be 350
    else:
        return 0 # If none of the above the cost will be 0
    
def car_rental(rental_days): # the 3rd function is related to car rental cost
    if city_flight == 'Valencia': # We used if-elif and else option as per task hint
        return rental_days * 15 # Car Rental cost if user goes to Valencia
    elif city_flight == 'New York':
        return rental_days * 90 # Car Rental cost if user goes to New York
    elif city_flight == 'Cyprus':
        return rental_days * 50 # Car Rental cost if user goes to Cyprus
    else:
        return 0 # If none of the above the cost will be 0

def holiday_cost(nights, city, days): # 4th option is the total cost of holidays
    nights = hotel_cost(num_nights) # we define new variable that will not confuse variables with functions
    city = plane_cost(city_flight)
    days = car_rental(rental_days)
    total_cost = nights + city + days # that is the expression for the whole cost of holidays
    return total_cost

#Then we get the input from user for the 3 variables
city_flight = input('Please chose 1 destination of the 3 options: Valencia, New York and Cyprus: ')
num_nights = int(input('Please enter how many nights will you be staying at the hotel: '))
rental_days = int(input('Please enter the number of days you will be hiring a car for: '))
#And use the print function to use the program
print(hotel_cost(num_nights))
print(plane_cost(city_flight))
print(car_rental(rental_days))
print(holiday_cost(num_nights, city_flight, rental_days))
#Then we will put a statement that will print all variables in a phrase
print(f'The cost of holidays for {str(num_nights)} nights in the city of {city_flight}, when the car is hired for {str(rental_days)} days is {holiday_cost(num_nights, city_flight, rental_days)}')

