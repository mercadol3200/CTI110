# Luis Mercado
# 6 October 2024
# P2LAB2
# This program tells you how many gallons of gas you need for the cars listed





# Create a dictionary with automobile models and their MPG
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get all keys from the dictionary
keys = vehicle_mpg.keys()
# Print the keys
print(keys)

# Prompt the user to enter a vehicle from the dictionary
vehicle = input("Please enter one of the vehicles from the list (Camaro, Prius, Model S, Silverado): ")

# Check if the entered vehicle is in the dictionary
if vehicle in vehicle_mpg:
    # Display the MPG for the vehicle entered
    mpg = vehicle_mpg[vehicle]
    print(f"The MPG for the {vehicle} is {mpg}.")
    
    # Prompt the user to enter the number of miles they will drive
    miles = float(input(f"Enter the number of miles you will drive the {vehicle}: "))
    
    # Calculate the gallons of gas needed
    gallons_needed = miles / mpg
    
    # Display the gallons needed, rounded to two decimal places
    print(f"You will need {gallons_needed:.2f} gallons of gas to drive {miles} miles in the {vehicle}.")
else:
    print("The vehicle you entered is not in the dictionary. Please check the spelling and try again.")
