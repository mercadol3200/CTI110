# Save as P4LAB1B_MercadoLuis.py
import turtle

# Set up the screen and turtle
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Initials")

# Create the turtle
t = turtle.Turtle()
t.speed(1)
t.color("green")  # Choose your color
t.pensize(3)

# Draw the first initial, e.g., 'F'
t.forward(50)     # Draw the top line
t.backward(50)    # Go back to starting point
t.right(90)
t.forward(100)    # Draw the vertical line
t.left(90)
t.forward(50)     # Draw middle line of 'F'

# Move to the right for the second initial
t.penup()
t.goto(100, 0)  # Adjust as needed to space letters out
t.pendown()

# Draw the second initial, e.g., 'L'
t.left(90)
t.forward(100)    # Draw the vertical line
t.left(90)
t.forward(50)     # Draw the bottom line of 'L'

# Close the window when clicked
wn.exitonclick()
