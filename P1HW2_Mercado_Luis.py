# Luis Mercado
# 29 Sep 2024
# P1HW2
# This program helps you create a budget

("This program calculates and displays travel expenses\n")

# Get the budget and destination from the user
budget = int(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")

# Get expenses from the user
fuel_cost = int(input("\nHow much do you think you will spend on gas? "))
accommodation_cost = int(input("Approximately, how much will you need for accommodation/hotel? "))
food_cost = int(input("Last, how much do you need for food? "))

# Calculate remaining balance
total_expenses = fuel_cost + accommodation_cost + food_cost
remaining_balance = budget - total_expenses

# Display travel expenses summary
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}\n")
print(f"Fuel: {fuel_cost}")
print(f"Accomodation: {accommodation_cost}")
print(f"Food: {food_cost}\n")
print(f"Remaining Balance: {remaining_balance}")
