def hotel_cost(num_nights: int) -> int:
    """
    The function calculates the total cost of a hotel stay based on the number of nights.
    
    :param num_nights: The parameter `num_nights` represents the number of nights the customer will be
    staying at the hotel as per their input
    :return: the total cost of staying at a hotel for the given number of nights at a fixed rate.
    """
    per_night_cost = 224
    return num_nights * per_night_cost
    

def plane_cost(city_flight, destination, ticket):
    """
    This Python function calculates the cost of a plane ticket based on the departure city and
    destination.
    
    :param city_flight: The `city_flight` parameter represents the departure city for the flight as chosen by the user input.
    :param destination: The `destination` parameter in the `plane_cost` function represents the
    destination city to which the flight is headed. The function calculates the cost of the plane ticket
    based on the departure city (`city_flight`) and the destination city selected. The function contains
    specific ticket prices for different combinations of departure and destination
    :param ticket: The `plane_cost` function takes three parameters: `city_flight`, `destination`, and
    `ticket`. It calculates the cost of a plane ticket based on the selected departure city and
    destination
    :return: The function `plane_cost` is returning the cost of a plane ticket based on the input
    parameters `city_flight` and `destination`. The cost of the ticket is determined by the specific
    combination of departure city and destination selected within the function.
    """
   
    # Destination = Dubai
    # Bristol to Dubai
    if city_flight == 1 and destination == 1:
        ticket = 633
    # London Heathrow to Dubai
    elif city_flight == 2 and destination == 1:
        ticket = 547
    # Exeter to Dubai
    elif city_flight == 3 and destination == 1:
        ticket = 638
    # Manchester to Dubai
    elif city_flight == 4 and destination == 1:
        ticket = 583

    # Destination = Tokyo
    # Bristol to Tokyo
    elif city_flight == 1 and destination == 2:
        ticket = 678
    # London Heathrow to Tokyo
    elif city_flight == 2 and destination == 2:
        ticket = 597
    # Exeter to Tokyo
    elif city_flight == 3 and destination == 2:
        ticket = 879
    # Manchester to Tokyo
    elif city_flight == 4 and destination == 2:
        ticket = 879
    
    # Destination = Maldives
    # Bristol to Maldives
    elif city_flight == 1 and destination == 3:
        ticket = 975
    # London Heathrow to Maldives
    elif city_flight == 2 and destination == 3:
        ticket = 941
    # Exeter to Maldives
    elif city_flight == 3 and destination == 3:
        ticket = 1069
    # Manchester to Maldives
    elif city_flight == 4 and destination == 3:
        ticket = 958

    # Destination = Toronto
    # Bristol to Toronto
    elif city_flight == 1 and destination == 4:
        ticket = 671
    # London Heathrow to Toronto
    elif city_flight == 2 and destination == 4:
        ticket = 462
    # Exeter to Toronto
    elif city_flight == 3 and destination == 4:
        ticket = 1374
    # Manchester to Toronto
    elif city_flight == 4 and destination == 4:
        ticket = 588
    else:
        print("Error 1. Invalid Selection. Please enter the number of the corresponding airport.")
    return ticket
        
def car_rental(rental_days: int) -> int:
    """
    The function calculates the total cost of renting a Ford Mustang for a given number of days.
    
    :param rental_days: The number of days the car is being rented for as input by the user
    :return: the total cost of renting a Ford Mustang for the specified number of rental days.
    """
    ford_mustang_pd = 133
    return rental_days * ford_mustang_pd
  

def holiday_cost(hotel_cost, plane_cost, car_rental) -> int:
    """
    The function calculates the total cost of a holiday including hotel, plane, and car rental expenses.
    
    :param hotel_cost: as provided in main script by hotel_total, which takes the users input to calculate
    the cost of the hotel based on how many nights they want to stay
    :param plane_cost: as provided in main script by flight_cost, which takes the users input to calculate
    the cost of the plane ticket based on which departure city and destination city they chose
    :param car_rental: as provided in main script by car_total, which takes the users input to calculate
    the cost of the car rental based on how many days they said they would be renting a car for
    :return: the total cost of the holiday, which is calculated by adding the hotel cost, plane cost,
    and car rental cost.
    """
    total_cost = hotel_cost + plane_cost + car_rental
    return total_cost

def airport_name(city_flight: int):
    """
    The function "airport_name" takes an input representing a city flight and returns the corresponding
    airport name.
    
    :param city_flight: The parameter `city_flight` is expected to be an integer representing the number
    of the airport, as input by the user
    :return: the name of the airport based on the input city_flight to display to the user menu
    """
    city_flight = int(city_flight)
    if city_flight == 1:
        return "Bristol"
    elif city_flight == 2:
        return "London Heathrow"
    elif city_flight == 3:
        return "Exeter"
    elif city_flight == 4:
        return "Manchester"
    else:
        print("Error 2. Invalid Selection. Please enter the number of the corresponding airport.")

def destination_name(destination: int):
    """
    The function `destination_name` takes an integer input representing a destination and returns the
    corresponding name of the destination.
    
    :param destination: The parameter "destination" is an integer that represents the number of the
    destination airport
    :type destination: int
    :return: the name of the destination based on the inputted destination number.
    """
    destination = int(destination)
    if destination == 1:
        return "Dubai"
    elif destination == 2:
        return "Tokyo"
    elif destination == 3:
        return "Maldives"
    elif destination == 4:
        return "Toronto"
    else:
        print("Error 3. Invalid Selection. Please enter the number of the corresponding airport.")
