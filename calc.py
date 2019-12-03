from tkinter import *
root = Tk()
root.title('Kat Calc')
e = Entry(root,width=30,borderwidth=2,fg='black',bg='white')
e.grid(row=0,column=1,columnspan=2)

reset = 0

def click_button(number):
    if reset == 1:
        reset = 0
        clear_button()
        return
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clear_button():
    e.delete(0,END)

def add_button():
    first_num = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_num)
    e.delete(0,END)

def equal_button():
    global reset
    reset = 1
    second_num = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0,f_num+int(second_num))
    if math == 'subtraction':
        e.insert(0,f_num-int(second_num))
    if math == 'multiplication':
        e.insert(0,f_num*int(second_num))
    if math == 'division':
        e.insert(0,f_num/int(second_num))

def subtract_button():
    first_num = e.get()
    global f_num
    global math
    f_num = int(first_num)
    math = 'subtraction'
    e.delete(0,END)

def multiply_button():
    first_num = e.get()
    global f_num
    global math
    f_num = int(first_num)
    math = 'multiplication'
    e.delete(0,END)

def divide_button():
    first_num = e.get()
    global f_num
    global math
    f_num = int(first_num)
    math = 'division'
    e.delete(0,END)

# number buttons
button0 = Button(root,text='0',padx=40,pady=20,bg='#dbdbdb',fg='black',command=lambda: click_button(0))
button1 = Button(root,text='1',padx=40,pady=20,bg='#dbdbdb',fg='black',command=lambda: click_button(1))
button2 = Button(root,text='2',padx=40,pady=20,bg='#dbdbdb',fg='black',command=lambda: click_button(2))
button3 = Button(root,text='3',padx=40,pady=20,bg='#dbdbdb',fg='black',command=lambda: click_button(3))
button4 = Button(root,text='4',padx=40,pady=20,bg='#dbdbdb',fg='black',command=lambda: click_button(4))
button5 = Button(root,text='5',padx=40,pady=20,bg='#dbdbdb',fg='black',command=lambda: click_button(5))
button6 = Button(root,text='6',padx=40,pady=20,bg='#dbdbdb',fg='black',command=lambda: click_button(6))
button7 = Button(root,text='7',padx=40,pady=20,bg='#dbdbdb',fg='black',command=lambda: click_button(7))
button8 = Button(root,text='8',padx=40,pady=20,bg='#dbdbdb',fg='black',command=lambda: click_button(8))
button9 = Button(root,text='9',padx=40,pady=20,bg='#dbdbdb',fg='black',command=lambda: click_button(9))
add_b = Button(root,text='+',padx=37,pady=20,bg='#dbdbdb',fg='black',command=add_button)
subtract_b = Button(root,text='-',padx=39,pady=20,bg='#dbdbdb',fg='black',command=subtract_button)
multiply_b = Button(root,text='*',padx=39,pady=20,bg='#dbdbdb',fg='black',command=multiply_button)
divide_b = Button(root,text='/',padx=39,pady=20,bg='#dbdbdb',fg='black',command=divide_button)
equal_b = Button(root,text='=',padx=39,pady=20,bg='#4D8BF1',command=equal_button)
clear_b = Button(root,text='C',padx=39,pady=20,bg='#f2747b',command=clear_button)

# adding buttons
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
add_b.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
subtract_b.grid(row=2,column=3)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
multiply_b.grid(row=3,column=3)

clear_b.grid(row=4,column=0)
button0.grid(row=4,column=1)
equal_b.grid(row=4,column=2)
divide_b.grid(row=4,column=3)

root.mainloop()