# Save as P4LAB2_MercadoLuis.py

def multiplication_table(num):
    """Displays the multiplication table for the given number from 1 to 12."""
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

# Main program loop
while True:
    try:
        # Ask the user for an integer
        user_input = int(input("Please enter an integer: "))

        # Check if the input is zero or positive
        if user_input >= 0:
            print(f"\nMultiplication table for {user_input}:")
            multiplication_table(user_input)  # Display the multiplication table

        else:
            print("Cannot accept negative values.")

    except ValueError:
        print("Please enter a valid integer.")

    # Ask if the user wants to run the program again
    run_again = input("\nDo you want to run the program again? (yes/no): ").strip().lower()
    if run_again != "yes":
        print("Exiting the program.")
        break
