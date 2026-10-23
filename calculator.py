import tkinter # the tkinter library is imported to create the GUI for the calculator
import math
button_values = [
    ['AC', '+/-', '%', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '√', '=']
]

right_symbols = ['÷', '×', '-', '+', '='] # a list of symbols that are used in the calculator
top_symbols = ['AC', '+/-', '%', ''] #a list of symbols that are used in the calculator

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_light_gray="#D4D4D2"
color_black="#1C1C1C"
color_dark_gray="#505050"
color_orange="#FF9500"
color_white="#FFFFFF"

#window creation
window = tkinter.Tk() # a window is created using the tkinter library
window.title("Calculator")
window.resizable(False, False) # the window is set to not be resizable

frame = tkinter.Frame(window) # a frame is created using the tkinter library
label = tkinter.Label(frame, text="0", font=("Arial", 45), bg=color_black, fg=color_white, anchor="e",
                       width=column_count)
 # a label is created using the tkinter library

label.grid(row=0, column=0, columnspan=column_count, sticky="we") # the label is placed in the grid

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30), width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))# a button is created using the tkinter library
        if value in top_symbols:
            button.config(bg=color_light_gray, fg=color_black) # the button is configured to have a light gray background and black text
        elif value in right_symbols:
            button.config(bg=color_orange, fg=color_white) # the button is configured to have an orange background and white text
        else:
            button.config(bg=color_dark_gray, fg=color_white) # the button is configured to have a dark gray background and white text
        button.grid(row=row + 1, column=column) # the button is placed in the grid

frame.pack()

#A+B, A-B, A*B, A/B
A=0;
operator=None;
B=None;

def clear_all():
    global A, B, operator
    A=0;
    operator=None;
    B=None;

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)
    

def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B=label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)       

                clear_all()     
        elif value in "+-×÷":
            if operator is None:
                A=label["text"]
                label["text"] = "0"
                B="0"
            operator = value    
        


    elif value in top_symbols:
        if value == "AC":
         clear_all()
         label["text"] = "0"

        elif value == "+/-":
         result = float(label["text"]) * -1
         label["text"] = remove_zero_decimal(result)

        elif value == "%":
         result = float(label["text"])/100
        label["text"] = remove_zero_decimal(result)

    elif value == "√": 
        try:
            result = math.sqrt(float(label["text"]))
            result = round(result, 7) 
            label["text"] = remove_zero_decimal(result)
        except ValueError:
            label["text"] = "Error"

    else:# digit or decimal point
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
           if label["text"] == "0":
               label["text"] = value
           else:
               label["text"] += value
#center the window on the screen
window.update()# update the window with the new size dimensions
window_width = window.winfo_width() # get the width of the window
window_height = window.winfo_height() # get the height of the window
screen_width = window.winfo_screenwidth() # get the width of the screen
screen_height = window.winfo_screenheight() # get the height of the screen

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(width)x(height)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()