# Luis Mercado 
# NOV 10 2024
# Assignment P4HW2 - Payroll Calculation for Multiple Employees
# This program calculates regular and overtime pay for multiple employees, stores
# the totals for each pay category, and displays them after the user decides to stop.

# Initialize totals and counters
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

# Sentinel-controlled loop to gather employee data
while True:
    # Prompt for employee name
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    
    # Check for sentinel value to break the loop
    if employee_name.lower() == "done":
        break

    # Get pay rate and hours worked
    pay_rate = float(input(f"Enter hourly rate for {employee_name}: "))
    hours_worked = float(input(f"Enter hours worked for {employee_name}: "))
    
    # Initialize pay calculations
    overtime_pay = 0.0
    regular_pay = 0.0

    # Calculate regular and overtime pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = 40 * pay_rate
    else:
        regular_pay = hours_worked * pay_rate

    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay

    # Add to totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Display individual employee's pay details
    print(f"\nEmployee: {employee_name}")
    print(f"  Hours Worked: {hours_worked}")
    print(f"  Pay Rate: ${pay_rate:.2f}")
    print(f"  Overtime Pay: ${overtime_pay:.2f}")
    print(f"  Regular Pay: ${regular_pay:.2f}")
    print(f"  Gross Pay: ${gross_pay:.2f}\n")

# After loop ends, display totals
print("\nSummary of Payroll")
print("--------------------")
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular pay: ${total_regular_pay:.2f}")
print(f"Total gross pay for all employees: ${total_gross_pay:.2f}")
