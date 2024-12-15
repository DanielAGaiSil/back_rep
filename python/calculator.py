import tkinter as tk #For the GUI

#The space for calculations
calculation = ""

#Function to add operations to the calculator
def add_to_calculation(symbol):
    #Makes the variable global since we need it elsewhere too
    global calculation
    #This makes it so even if we type an int, it will become a str
    calculation += str(symbol)
    #Deletes the whole content of text result
    txt_result.delete(1.0, "end")
    #Adds the string calculation to the right thing
    txt_result.insert(1.0, calculation)
    pass

#Evaluates the calculation
def evaluate_calculation():
    global calculation
    #Why try? Because if there are any errors (like dividing by 0)
    try:
        #Evaluates (or basically does) the calculation even though it's a string
        calculation = str(eval(calculation))
        txt_result.delete(1.0, "end")
        txt_result.insert(1.0, calculation)
    
    #We can catch the error with exepct
    except:
        clear_field()
        txt_result.insert(1.0, "Error")
        pass

#Clears up the currect calculation
def clear_field():
    global calculation
    calculation = ""
    txt_result.delete(1.0, "end")
    pass

#Creates the main window
window = tk.Tk()

#Window's size
window.geometry("300x300")

#Shows the result
txt_result = tk.Text(window, height = 2, width = 16, font = ("Arial", 22))

#Makes it so the result grid is the same size as all the buttons together
txt_result.grid(columnspan = 5)

#Making the buttons display the right text, and making them work too
#Also, lambda is used so the function doesn't get called right away,
#Which basically means that the function will only work when used
#This bit also makes the button work
btn_1 = tk.Button(window, text = "1", command = lambda: add_to_calculation(1), width= 5, font = ("Arial", 14))
#Makes the button appear (on the right place, of course)
btn_1.grid(row = 2, column = 1)
btn_2 = tk.Button(window, text = "2", command = lambda: add_to_calculation(2), width= 5, font = ("Arial", 14))
btn_2.grid(row = 2, column = 2)
btn_3 = tk.Button(window, text = "3", command = lambda: add_to_calculation(3), width= 5, font = ("Arial", 14))
btn_3.grid(row = 2, column = 3)
btn_4 = tk.Button(window, text = "4", command = lambda: add_to_calculation(4), width= 5, font = ("Arial", 14))
btn_4.grid(row = 3, column = 1)
btn_5 = tk.Button(window, text = "5", command = lambda: add_to_calculation(5), width= 5, font = ("Arial", 14))
btn_5.grid(row = 3, column = 2)
btn_6 = tk.Button(window, text = "6", command = lambda: add_to_calculation(6), width= 5, font = ("Arial", 14))
btn_6.grid(row = 3, column = 3)
btn_7 = tk.Button(window, text = "7", command = lambda: add_to_calculation(7), width= 5, font = ("Arial", 14))
btn_7.grid(row = 4, column = 1)
btn_8 = tk.Button(window, text = "8", command = lambda: add_to_calculation(8), width= 5, font = ("Arial", 14))
btn_8.grid(row = 4, column = 2)
btn_9 = tk.Button(window, text = "9", command = lambda: add_to_calculation(9), width= 5, font = ("Arial", 14))
btn_9.grid(row = 4, column = 3)
btn_0 = tk.Button(window, text = "0", command = lambda: add_to_calculation(0), width= 5, font = ("Arial", 14))
btn_0.grid(row = 5, column = 2)
btn_plus = tk.Button(window, text = "+", command = lambda: add_to_calculation("+"), width= 5, font = ("Arial", 14))
btn_plus.grid(row = 2, column = 4)
btn_minus = tk.Button(window, text = "-", command = lambda: add_to_calculation("-"), width= 5, font = ("Arial", 14))
btn_minus.grid(row = 3, column = 4)
btn_mult = tk.Button(window, text = "*", command = lambda: add_to_calculation("*"), width= 5, font = ("Arial", 14))
btn_mult.grid(row = 4, column = 4)
btn_div = tk.Button(window, text = "/", command = lambda: add_to_calculation("/"), width= 5, font = ("Arial", 14))
btn_div.grid(row = 5, column = 4)
btn_open = tk.Button(window, text = "(", command = lambda: add_to_calculation("("), width= 5, font = ("Arial", 14))
btn_open.grid(row = 5, column = 1)
btn_close = tk.Button(window, text = ")", command = lambda: add_to_calculation(")"), width= 5, font = ("Arial", 14))
btn_close.grid(row = 5, column = 3)
#Removed lambda since we don't take any parameter, no () since we don't want to call the function, we want to pass it
btn_equal = tk.Button(window, text = "=", command = evaluate_calculation, width= 11, font = ("Arial", 14))
btn_equal.grid(row = 6, column = 3, columnspan = 2)
btn_clear = tk.Button(window, text = "C", command = clear_field, width= 11, font = ("Arial", 14))
btn_clear.grid(row = 6, column = 1, columnspan = 2)

#Starts the window loop, basically so the window appears on loop while it's open
window.mainloop()