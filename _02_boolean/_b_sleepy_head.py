"""
Use boolean variables to control program logic between two different code
paths.
"""
import turtle
from tkinter import messagebox, simpledialog,Tk

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    today = "Friday"

    if today == "Saturday" or today == "Sunday":
        weekend = True
        messagebox.showinfo(message = "It is the weekend!")
    else:
        weekend = False
        messagebox.showinfo(message = "Sadly, it is not the weekend.")

    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    score = 100
    if score >= 69.5:
        passed = True
        messagebox.showinfo(message = "You passed!")
    else:
        passed = False
        messagebox.showinfo(message = "Sadly, you didn't pass.")
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    color = "red"
    shape = "square"
    image = False
    if color == "red":
        if shape == "square":
            image = True
        else:
            image = False
    else:
        image = False
    #print(image)
    if image == True:

        mrgreen = turtle.Turtle()
        mrgreen.pencolor('red')
        mrgreen.pendown()
        for i in range (4):
            mrgreen.forward(100)
            mrgreen.right(90)


    pass
