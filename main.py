from tkinter import *

# Function to handle the pressing of a button (numbers or operators)
def button_press(num):
    # Access the global equation_text variable
    global equation_text
    # Append the pressed button's value to the equation string
    equation_text += str(num)
    # Update the equation label to reflect the current equation
    equation_label.set(equation_text)

# Function to evaluate the equation when the equals button is pressed
def equals():
    global equation_text

    try:
        # Evaluate the expression in equation_text
        total = str(eval(equation_text))
        # Update the equation label with the result
        equation_label.set(total)
        # Set equation_text to the result, allowing further calculations
        equation_text = total
    except SyntaxError:
        # Handle any syntax errors (e.g., if the equation is incomplete)
        equation_label.set("Syntax Error")
        equation_text = ""
    except ZeroDivisionError:
        # Handle division by zero errors
        equation_label.set("Arithmetic Error")
        equation_text = ""

# Function to clear the equation
def clear():
    global equation_text
    # Clear the equation_text variable
    equation_text = ""
    # Clear the equation label
    equation_label.set("")

# Create the main window for the application
window = Tk()
window.title("Calculator Programme")
window.geometry("500x500")

# Initialize the equation_text variable to hold the current equation
equation_text = ""

# Create a StringVar to update the label displaying the equation
equation_label = StringVar()

# Create a label widget to display the equation or result
label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2)
label.pack()

# Create a frame to hold the buttons
frame = Frame(window)
frame.pack()

# Create buttons for the digits and grid them within the frame
button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

# Create buttons for the arithmetic operations and grid them within the frame
plus = Button(frame, text='+', height=4, width=9, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=3)

# Create the equals button and grid it within the frame
equal = Button(frame, text='=', height=4, width=9, font=35, command=equals)
equal.grid(row=3, column=2)

# Create the decimal button and grid it within the frame
decimal = Button(frame, text='.', height=4, width=9, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

# Create the clear button outside the frame and pack it below the frame
clear_button = Button(window, text='clear', height=4, width=9, font=35, command=clear)
clear_button.pack()

# Start the Tkinter event loop
window.mainloop()
