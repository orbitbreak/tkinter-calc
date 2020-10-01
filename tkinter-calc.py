from tkinter import *

calc = Tk()
calc.title("CrappyCalc")
calc.config(bg="grey")

# default size of window
calc.geometry("300x500")

# avoid stretching of Window
calc.maxsize(300,500)
calc.minsize(300,500)

buttons = [
    '7', '8', '9', '*', 'C',
    '4', '5', '6', '/', 'Neg',
    '1', '2', '3', '-', '$',
    '0', '.', '=', '+', '@']

# set up GUI
row = 1
col = 0
for i in buttons:
    button_style = 'raised'
    action = lambda x=i: click_event(x)
    Button(calc, text=i, width=1,height=5, relief=button_style, command=action,font="arial 13 bold") \
        .grid(row=row, column=col, sticky='nesw',padx =1,pady=1)
    col += 1
    if col > 4:
        col = 0
        row += 1

display = Entry(calc, width=50, bg="white")
display.grid(row=0, column=0, columnspan=5,pady=5)


def click_event(key):
    # = -> calculate results
    if key == '=':
        # safeguard against integer division
        if '/' in display.get() and '.' not in display.get():
            display.insert(END, ".0")

        # attempt to evaluate results
        try:
            result = eval(display.get())
            display.insert(END, " = " + str(result))
        except:
            display.insert(END, "   Error, use only valid chars")

    # C -> clear display		
    elif key == 'C':
        display.delete(0,END)


    # $ -> clear display		
    elif key == '$':
        display.delete(0, END)
        display.insert(END, "$$$$C.$R.$E.$A.$M.$$$$")


    # @ -> clear display		
    elif key == '@':
        display.delete(0, END)
        display.insert(END, "wwwwwwwwwwwwwwwwebsite")


    # neg -> negate term
    elif key == 'neg':
        if '=' in display.get():
            display.delete(0, END)
        try:
            if display.get()[0] == '-':
                display.delete(0)
            else:
                display.insert(0, '-')
        except IndexError:
            pass

    # clear display and start new input		
    else:
        if '=' in display.get():
            display.delete(0, END)
        display.insert(END, key)


# RUNTIME
calc.mainloop()
