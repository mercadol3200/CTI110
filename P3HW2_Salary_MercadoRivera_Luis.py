# Luis Mercado
# 20 OCT 2024
# P3HW2 - Salary Calculation
# A brief description of the project: This program calculates an employee's gross pay
# including regular and overtime pay based on hours worked and pay rate.

# Pseudocode:
# 1. Ask the user to enter the employee's name
# 2. Ask the user to enter the number of hours worked this week
# 3. Ask the user to enter the employee's pay rate
# 4. Check if the employee has worked overtime (more than 40 hours)
# 5. If the employee worked overtime, calculate the overtime pay (1.5 times regular rate)
# 6. Calculate the pay for regular hours (up to 40 hours)
# 7. Calculate the gross pay (regular pay + overtime pay)
# 8. Display the employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours, and gross pay

# Function to calculate salary
def calculate_salary():
    # Step 1: Ask for employee's name
    employee_name = input("Enter employee's name: ")
    
    # Step 2: Ask for the number of hours worked this week
    hours_worked = float(input("Enter number of hours worked: "))
    
    # Step 3: Ask for employee's pay rate
    pay_rate = float(input("Enter employee's pay rate: "))

    # Step 4: Check if there are overtime hours (more than 40 hours)
    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)  # Overtime pay is 1.5 times regular pay
    else:
        regular_hours = hours_worked
        overtime_hours = 0
        overtime_pay = 0

    # Step 6: Calculate pay for regular hours
    regular_pay = regular_hours * pay_rate

    # Step 7: Calculate gross pay (regular pay + overtime pay)
    gross_pay = regular_pay + overtime_pay

    # Step 8: Display results
    print("\nEmployee name:", employee_name)
    print(f"Pay rate: ${pay_rate:.2f}")
    print(f"Number of hours worked: {hours_worked}")
    print(f"Overtime hours: {overtime_hours}")
    print(f"Overtime pay: ${overtime_pay:.2f}")
    print(f"Pay for regular hours: ${regular_pay:.2f}")
    print(f"Gross pay: ${gross_pay:.2f}")


# Example usage
if __name__ == "__main__":
    calculate_salary()
