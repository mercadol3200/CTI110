# Luis Mercado
# 20 Oct 2024
# P3HW1 - Debugging
# A brief description of the project: This program calculates the average of six module grades
# and displays the corresponding letter grade based on the average.

# This program takes a number grade, determines the average, and displays the letter grade for the average.

# Enter grades for six modules

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: Determine the lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total_sum = sum(grades)
avg = total_sum / len(grades)

# Output lowest, highest, sum, and average
print(f"\nLowest Grade: {low}")
print(f"Highest Grade: {high}")
print(f"Sum of Grades: {total_sum}")
print(f"Average: {avg:.2f}")

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
