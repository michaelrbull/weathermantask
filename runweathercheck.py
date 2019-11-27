###
# Import both the list of sunny cities and the corresponding flight numbers 
# from both the flight and weather program.

from weather_services import sunny_cities
from flight_services import sunny_flight_num

# Prints both lists but tidied up with string concentation.

print("Sunny Cities: " + str(sunny_cities))
print("Flight Numbers: " + str(sunny_flight_num))

# Below is User Input Code and Specific City Options. 
# Currently not being used as it made testing and exception handling awkward.

#############################################################################

# Function to ask user which specific city they want to fly to instead of all sunny cities. Runs for loop based on user input and print flight numbers
# for that city.

'''def specific_city():

    print("Ok, what specific city would you like us to check instead?")
    usercity = input("")
    print("Great, checking for flight numbers for " + usercity + ".")
    
    # An empty list is created to then more the user input data into
    # (the city they want to travel to)'''

'''user_city_list = []
user_city_list.append(usercity)
user_flight_number = []'''  
    
# This For Loop checks all the cities the user has requested flight data
# for, sees if there is a match in the flight fixtures API. If so, it
# pulls the flight information through and stores the flight number into
# user_flight_number variable.

'''try:
    for city in user_city_list:
        flight_pull = requests.get("http://localhost:5002/" + city.lower())
        flight_info = json.loads(flight_pull.text)
    for flight in flight_info:
        user_flight_number.append(flight["flight"])
        print("Flight Name: " + str(user_city_list))
        print("Flight Numbers: " + str(user_flight_number))
except json.decoder.JSONDecodeError:
    print('No flights found for ' + usercity + ". Please enter another city.")'''

    
# Function to ask user their name and store in a variable to be used when referencing the user.      

'''def enter_name():
    print("Enter name: ")
    global newname
    newname = str(input(""))'''

# Function which asks user if they want to see all currently sunny cities and corresponding flight numbers. 
# runs specific_city function if user says no.

'''def flight_num_questions(): 
    print("Hi, " + newname + " do you want to see all currently sunny cities and flight numbers?")
    global user_input
    user_input = input()'''

# Runs function to ask user their name and to ask what flights do they need.

'''enter_name()
flight_num_questions()'''

# Runs functions based on user input. If user wants sunny cities, it runs sunny cities function.

'''if user_input == str("y"):
    sunnycities_sunnyweather()'''

# If user wants wants a specific city, it runs specific_city function.

'''elif user_input == str("n"):
    specific_city()'''