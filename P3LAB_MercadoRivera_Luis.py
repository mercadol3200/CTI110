# Luis Mercado
# 20 Oct 2024
# P3LAB
# this program calculates amounts







def calculate_change(amount):
    # Convert to cents (by multiplying by 100 and rounding to nearest integer)
    total_cents = int(round(amount * 100))

    # Determine number of dollars, quarters, dimes, nickels, and pennies
    dollars = total_cents // 100
    total_cents %= 100

    quarters = total_cents // 25
    total_cents %= 25

    dimes = total_cents // 10
    total_cents %= 10

    nickels = total_cents // 5
    total_cents %= 5

    pennies = total_cents

    # Output the results with correct singular/plural forms, skipping 0 values
    if dollars > 0:
        if dollars == 1:
            print("1 dollar")
        else:
            print(f"{dollars} dollars")

    if quarters > 0:
        if quarters == 1:
            print("1 quarter")
        else:
            print(f"{quarters} quarters")

    if dimes > 0:
        if dimes == 1:
            print("1 dime")
        else:
            print(f"{dimes} dimes")

    if nickels > 0:
        if nickels == 1:
            print("1 nickel")
        else:
            print(f"{nickels} nickels")

    if pennies > 0:
        if pennies == 1:
            print("1 penny")
        else:
            print(f"{pennies} pennies")


# Example usage:
if __name__ == "__main__":
    amount = float(input("Enter an amount of money: "))
    calculate_change(amount)
