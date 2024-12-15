
#Luis Mercado
# 17 NOV 24
# P5LAB
# This python simulates a selfcheckout machine




import random

def disperse_change(change):
    """
    Breaks down the given change amount into dollars, quarters, dimes, nickels, and pennies.
    Prints the quantities of each denomination.
    """
    # Convert change to cents for easier calculations
    change_in_cents = round(change * 100)
    
    # Calculate denominations
    dollars = change_in_cents // 100
    change_in_cents %= 100

    quarters = change_in_cents // 25
    change_in_cents %= 25

    dimes = change_in_cents // 10
    change_in_cents %= 10

    nickels = change_in_cents // 5
    change_in_cents %= 5

    pennies = change_in_cents

    # Print results
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

def main():
    # Generate random total amount owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed:.2f}")
    
    # Prompt user for payment
    while True:
        try:
            payment = float(input("Enter the amount you are paying: $"))
            if payment < total_owed:
                print("Payment must be greater than or equal to the total owed. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Calculate change
    change = round(payment - total_owed, 2)
    print(f"Change owed: ${change:.2f}")

    # Call disperse_change function
    disperse_change(change)

# Call main function
if __name__ == "__main__":
    main()
