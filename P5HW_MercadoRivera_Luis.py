
#Luis Mercado

# Nov 24, 2024

#P5HW

#This program creates a math quiz



import random

def generate_numbers():
    """Generate two random numbers."""
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    return num1, num2

def add_numbers():
    """Addition quiz."""
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    print(f"\n{num1}\n+ {num2}\n")
    attempts = 0
    
    while True:
        try:
            user_answer = int(input("Enter your answer: "))
            attempts += 1
            if user_answer == correct_answer:
                print(f"Congratulations! {num1} + {num2} = {correct_answer}")
                print(f"It took you {attempts} guesses.\n")
                break
            elif user_answer < correct_answer:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def subtract_numbers():
    """Subtraction quiz."""
    num1, num2 = generate_numbers()
    correct_answer = num1 - num2
    print(f"\n{num1}\n- {num2}\n")
    attempts = 0
    
    while True:
        try:
            user_answer = int(input("Enter your answer: "))
            attempts += 1
            if user_answer == correct_answer:
                print(f"Congratulations! {num1} - {num2} = {correct_answer}")
                print(f"It took you {attempts} guesses.\n")
                break
            elif user_answer < correct_answer:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def display_menu():
    """Display the menu options."""
    print("Math Quiz Menu")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Exit")

def main():
    """Main function to run the program."""
    while True:
        display_menu()
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == "1":
            add_numbers()
        elif choice == "2":
            subtract_numbers()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
