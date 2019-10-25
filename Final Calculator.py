from tkinter import *
root=Tk()
root.title("Digital Calculator")
  
text_field=Entry(root,width=32,borderwidth=5,justify='right',bg="powder blue",bd=10,font="arial 12 bold")
text_field.grid(row=0,column=0,columnspan=4)


def btn_click(num):
    current=text_field.get()
    text_field.delete(0, END)
    text_field.insert(0,str(current)+str(num))
           
def btn_clickd(dec):
    current=text_field.get()
    text_field.delete(0, END)
    text_field.insert(0,str(current)+dec)
    
def btn_clear():
    text_field.delete(0, END)
    #text_field.insert(0,"0")
    
def btn_del():
    length=len(text_field.get())
    text_field.delete(length-1,'end')
    if length==1:
        text_field.insert(0,'0')
    
def btn_add():
    first_number=text_field.get()
    global pre_num
    global math
    math="addition"
    pre_num=float(first_number)
    text_field.delete(0,END)
    
def btn_equal():
    try:
        second_number=text_field.get()
        text_field.delete(0,END)
        if math=="addition":
            text_field.insert(0,pre_num + float(second_number))
        if math=="multiply":
            text_field.insert(0,pre_num * float(second_number)) 
        if math=="subtraction":
            text_field.insert(0,pre_num - float(second_number))
        if math=="divide":
            text_field.insert(0,pre_num / float(second_number))
    except:
        text_field.insert(0,"NOT DEFINED")
    
def btn_subtract():
    first_number=text_field.get()
    global pre_num
    global math
    math="subtraction"
    pre_num=float(first_number)
    text_field.delete(0,END)

def btn_multiply():
    first_number=text_field.get()
    global pre_num
    global math
    math="multiply"
    pre_num=float(first_number)
    text_field.delete(0,END)

def btn_divide():
    first_number=text_field.get()
    global pre_num
    global math
    math="divide"
    pre_num=float(first_number)
    text_field.delete(0,END)
    
button_1=Button(root,text="1",padx=23,pady=10,command=lambda: btn_click(1),bg="black",fg="white",bd=5,font="arial 12 bold")
button_2=Button(root,text="2",padx=23,pady=10,command=lambda: btn_click(2),bg="black",fg="white",bd=5,font="arial 12 bold")
button_3=Button(root,text="3",padx=23,pady=10,command=lambda: btn_click(3),bg="black",fg="white",bd=5,font="arial 12 bold")
button_4=Button(root,text="4",padx=23,pady=10,command=lambda: btn_click(4),bg="black",fg="white",bd=5,font="arial 12 bold")
button_5=Button(root,text="5",padx=23,pady=10,command=lambda: btn_click(5),bg="black",fg="white",bd=5,font="arial 12 bold")
button_6=Button(root,text="6",padx=23,pady=10,command=lambda: btn_click(6),bg="black",fg="white",bd=5,font="arial 12 bold")
button_7=Button(root,text="7",padx=23,pady=10,command=lambda: btn_click(7),bg="black",fg="white",bd=5,font="arial 12 bold")
button_8=Button(root,text="8",padx=23,pady=10,command=lambda: btn_click(8),bg="black",fg="white",bd=5,font="arial 12 bold")
button_9=Button(root,text="9",padx=23,pady=10,command=lambda: btn_click(9),bg="black",fg="white",bd=5,font="arial 12 bold")
button_0=Button(root,text="0",padx=65,pady=10,command=lambda: btn_click(0),bg="black",fg="white",bd=5,font="arial 12 bold")
button_decimal=Button(root,text=".",padx=24,pady=10,command=lambda: btn_clickd("."),bg="black",fg="white",bd=5,font="arial 12 bold")

button_m=Button(root,text="AC",padx=15,pady=10,command=btn_clear,bg="black",fg="white",bd=5,font="arial 12 bold")


button_add=Button(root,text="+",padx=22,pady=10,command=btn_add,bg="black",fg="white",bd=5,font="arial 12 bold")
button_subtract=Button(root,text="-",padx=23,pady=10,command=btn_subtract,bg="black",fg="white",bd=5,font="arial 12 bold")
button_multiply=Button(root,text="*",padx=23,pady=10,command=btn_multiply,bg="black",fg="white",bd=5,font="arial 12 bold")
button_divide=Button(root,text="/",padx=25,pady=10,command=btn_divide,bg="black",fg="white",bd=5,font="arial 12 bold")
button_equal=Button(root,text="=",padx=23,pady=42,command=btn_equal,bg="black",fg="white",bd=5,font="arial 12 bold")
DEL=Button(root,text="DEL",padx=12,pady=10,command=btn_del,bg="black",fg="white",bd=5,font="arial 12 bold")

button_m.grid(row=1,column=0)
button_divide.grid(row=1,column=2)
button_multiply.grid(row=1,column=3)
button_subtract.grid(row=2,column=3)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_add.grid(row=3,column=3)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_equal.grid(row=4,column=3,rowspan=2)

button_0.grid(row=5,column=0,columnspan=2)
button_decimal.grid(row=5,column=2)
DEL.grid(row=1,column=1)

root.resizable(0,0)
root.mainloop()

