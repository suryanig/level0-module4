"""
Write a program to return the correct letter grade
"""
from tkinter import messagebox, simpledialog,Tk

# The teacher wants you to write a program that converts the score on 2
# 100 point tests to a letter grade. The teacher wants you to average the
# score from the 2 tests and print out the letter grade back to the user.
# The letter grades are assigned as follows:
#   A = 89.5 to 100
#   B = 79.5 to less than 89.5
#   C = 69.5 to less than 79.5
#   D = 59.5 to less than 69.5
#   F = less than 59.5
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Ask the user for their score on the FIRST test and store their
    #  score in a variable
    first = simpledialog.askinteger(title='First Test Score', prompt="What was the score of your first test?")
    # TODO) Ask the user for their score on the SECOND test and store their
    #  score in a variable
    second = simpledialog.askinteger(title='Second Test Score', prompt="What was the score of your second test?")
    # TODO) Take the average score of both tests (total score / 2)
    average = (first + second)/2
    # TODO) Use if statements to check the average score and print the
    #  corresponding letter grade back to the user. Also, give a different
    #  message according to their grade. Example, for an 'A' grade:
    #  "Wow! You must have studied really hard for those tests!"

    if average >= 89.5 and average <= 100:
        messagebox.showinfo(message="Wow you got an A! You must have studied really hard for those tests!")
    elif average >= 79.5 and average < 89.5:
        messagebox.showinfo(message="Wow you got a B! That is really good.")
    elif average >= 69.5 and average < 79.6:
        messagebox.showinfo(message="You got a C! Good effort.")
    elif average >= 59.5 and average < 69.5:
        messagebox.showinfo(message = "That's a D! Try harder next time.")
    elif average < 59.5 and average >= 0:
        messagebox.showinfo(message = "That's an F! You failed.")
    else:
        messagebox.showinfo(message="Sorry, that's not a possible grade you can get.")
    pass
