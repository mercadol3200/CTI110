
# Luis Mercado
 # 29 Sep 2024
 # P1HW1
 # This peojects creats a python file where you can imput mathematical expressions

# ----Calculating Exponents----
print("-----Calculating Exponenets----\n")

# Get the base value and exponent from the user
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

# Calculate the result
result = base ** exponent

# Print the result in the required format
print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

# ----Addition and Subtraction----
print("-----Addition and Subtraction----\n")

# Get the starting integer, integer to add, and integer to subtract
starting_integer = int(input("Enter a starting integer: "))
integer_to_add = int(input("Enter an integer to add: "))
integer_to_subtract = int(input("Enter an integer to subtract: "))

# Calculate the final result
final_result = starting_integer + integer_to_add - integer_to_subtract

# Print the result in the required format
print(f"\n{starting_integer} + {integer_to_add} - {integer_to_subtract} is equal to {final_result}\n")