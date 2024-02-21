# Task 16 - Practical Task 

from hol_func import plane_cost, hotel_cost, car_rental, airport_name, holiday_cost, destination_name

print("~~~~~~~~~~~~~~~~~~~ ☼ Welcome to Heinz Holidays ☼ ~~~~~~~~~~~~~~~~~~~\n")

while True: 

    # Displays menu to user
    while True:
        ticket = 0
        # Exception handling to make sure the user only inputs numbers
        # and that entering text won't end or break the program
        while True:
            try:
                city_flight = input("""Where would you like to fly from? Please select from below:               
1. Bristol
2. London Heathrow
3. Exeter
4. Manchester\n
: """)
                city_flight = int(city_flight)
                break
            except ValueError:
                print("Please enter a valid number.")
                print("-"*70)

        # Exception handling to make sure the user can only input numbers from the menu
        if city_flight > 4 or city_flight <= 0:
            print("Error 0. Invalid Selection. Please enter the number of the corresponding airport.")
            print("-"*70)
            continue
        
        # Exception handling to make sure the user only inputs numbers
        # and that entering text won't end or break the program
        while True:
            try:
                print("►"*80)
                destination = input("""Where would you like to go? Please select from below::
        1. Dubai
        2. Tokyo
        3. Maldives
        4. Toronto
                                    
        : """)
                destination = int(destination)
                break
            except ValueError:
                print("Please enter a valid number.")
                print("-"*70)   

        # Exception handling to make sure the user can only input numbers from the menu
        if destination > 4 or destination <= 0:
            print("Error 01. Invalid Selection. Please enter the number of the corresponding airport.")
            print("-"*70)
            continue 
        
        # Calculates the flight cost based on the above inputs using func flight_cost()
        flight_cost = plane_cost(city_flight, destination, ticket)
        break
    
    # Exception handling with inputs that need to be numbers
    while True:
        try:
            print("••••••••••••••••••••••••• Total Nights •••••••••••••••••••••••••\n")
            num_nights = int(input("How many nights would you like to stay for? Enter 0 for none: "))
            print("\n•••••••••••••••••••••••••• Car Rental ••••••••••••••••••••••••••")
            rental_days = int(input("\nHow many days would you like to rent a car for? Enter 0 for none: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Setting the value for to be used by the function later
    hotel_total = 0
    while True:
        # Displaying a costing breakdown menu with exception handling
        print("\n~~~~~~~~~~~~~~~~~~~ ☼ Holiday Cost Breakdown ☼ ~~~~~~~~~~~~~~~~~~~ ")
        if num_nights == 0:
            print("Hotel not required.")
            break
        else:  
            hotel_total = hotel_cost(num_nights)
            print(f"Your hotel total cost is: \t\t\t\t£{hotel_total}")
            break

    car_total = 0
    while True:
        if rental_days == 0:
            print("Car hire not required.")
            break
        else:
            car_total = car_rental(rental_days)
            print(f"Your car rental cost is: \t\t\t\t£{car_total}\n")
            break
    
    # Using functions to accurately display the names of the airports the user has input
    airport = airport_name(city_flight)
    dest = destination_name(destination)
    print(f"Your plane ticket from {airport} to {dest} will cost: \t£{flight_cost}")

    # Calculating and displaying the total cost of
    total_cost = holiday_cost(hotel_total, flight_cost, car_total)
    print("—"*80)
    print(f"The total cost of your holiday is: \t\t\t£{total_cost}")
    print("—"*80)
  
    if input("Press enter to calculate another trip or type anything to quit: "):
        print("\tThank you for travelling with Heinz Holidays! Bon Voyage!\n")
        break
    