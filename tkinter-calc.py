from tkinter import *

#Title of the program.
calc =Tk()
calc.title("CrappyCalc")

#Interface of the program.
buttons = [
'7',  '8',  '9',  '*',  'C',
'4',  '5',  '6',  '/',  'Neg',
'1',  '2',  '3',  '-',  '$',
'0',  '.',  '=',  '+',  '@' ]

# set up GUI
row = 1
col = 0
for i in buttons:
    button_style = 'raised'
    action = lambda x = i: click_event(x)
    Button(calc, text = i, width = 7, height = 7, relief = button_style, command = action) \
		.grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 4:
        col = 0
        row += 1

display = Entry(calc, width = 40, bg = "white")
display.grid(row = 0, column = 0, columnspan = 5)

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
        display.delete(0,END)
        display.insert(END, "$$$$C.$R.$E.$A.$M.$$$$")
		

	# @ -> clear display		
    elif key == '@':
        display.delete(0,END)
        display.insert(END, "wwwwwwwwwwwwwwwwebsite")		

		
	# neg -> negate term
    elif key == 'neg':
        if '=' in display.get():
            display.delete(0,END)
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
            display.delete(0,END)
        display.insert(END, key)

# RUNTIME
calc.mainloop()
