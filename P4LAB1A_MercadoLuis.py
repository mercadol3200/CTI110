# Save as P4LAB1A_MercadoLuis.py
import turtle

# Set up the screen and turtle
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Square and Triangle")

# Create the turtle
t = turtle.Turtle()
t.speed(1)  # Adjust the speed as desired
t.color("blue")  # Color of shapes
t.pensize(2)

# Draw a square using a for loop
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.right(90)     # Turn 90 degrees to the right

# Move to a different location to start drawing the triangle
t.penup()
t.goto(-150, 0)  # Adjust as needed to avoid overlap
t.pendown()

# Draw a triangle using a while loop
sides = 0
while sides < 3:
    t.forward(100)
    t.left(120)
    sides += 1

# Close the window when clicked
wn.exitonclick()
