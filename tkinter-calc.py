import tkinter as tk
import math

calc = tk.Tk()
calc.title("CrappyCalc")

buttons = [
    '7', '8', '9', '*', 'C',
    '4', '5', '6', '/', '^',
    '1', '2', '3', '-', '%',
    '0', '.', '=', '+', '√']

# set up GUI
row = 1
col = 0
for i in buttons:
    button_style = 'raised'
    action = lambda x=i: click_event(x)
    tk.Button(calc, text=i, width=7, height=7, relief=button_style, command=action) \
        .grid(row=row, column=col, sticky='nesw', )
    col += 1
    if col > 4:
        col = 0
        row += 1

display = tk.Entry(calc, width=40, bg="white")
display.grid(row=0, column=0, columnspan=5)


def click_event(key):
    # = -> calculate results
    if key == '^':
        key = '**'



    if key == '=':
        # safeguard against integer division

        if '/' in display.get() and '.' not in display.get():
            display.insert(tk.END, ".0")

        if '√' in display.get():
            a = display.get().replace('√', '')
            b = math.sqrt(int(a))
            display.insert(tk.END, "=" + str(b))
        else:
        # attempt to evaluate results
            try:
                result = eval(display.get())
                display.insert(tk.END, " = " + str(result))
            except:
                display.insert(tk.END, "   Error, use only valid chars")

    # C -> clear display
    elif key == 'C':
        display.delete(0, tk.END)

    # clear display and start new input
    else:
        if '=' in display.get():
            display.delete(0, tk.END)
        display.insert(tk.END, key)


# RUNTIME
calc.mainloop()
