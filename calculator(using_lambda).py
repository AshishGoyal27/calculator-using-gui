import tkinter as tk

#to see every action performed on calculator in python output shell ,remove comment sign('#') from all 3 print statement.
def btnclick(numbers):
    global expression
    expression = expression + str(numbers)
    text_input.set(expression)
    #print(expression)
def btnclear():
    global expression
    expression = ""
    text_input.set("")
    #print(expression)
def btnequal():
    global expression
    calculate_expression = str(eval(expression))
    text_input.set(calculate_expression)
    expression = ""
    #print(calculate_expression)

cal = tk.Tk()
cal.title("calculator")
expression=""
text_input = tk.StringVar()

e = tk.Entry(cal,font=('arial',20,'bold'),text=text_input,bd=30,
             bg="thistle2",justify="right").grid(columnspan=4)
#========================row1========================================
b7=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             text='7',bg="purple3",command=lambda:btnclick(7)).grid(row=1,column=0)
b8=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             bg="purple3",text='8',command=lambda:btnclick(8)).grid(row=1,column=1)
b9=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             bg="purple3",text='9',command=lambda:btnclick(9)).grid(row=1,column=2)
b_A=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',18,'bold'),
             bg="purple3",text='+',command=lambda:btnclick("+")).grid(row=1,column=3)
#========================row2============================================
b4=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             text='4',bg="purple3",command=lambda:btnclick(4)).grid(row=2,column=0)
b5=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             bg="purple3",text='5',command=lambda:btnclick(5)).grid(row=2,column=1)
b6=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             bg="purple3",text='6',command=lambda:btnclick(6)).grid(row=2,column=2)
b_S=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             bg="purple3",text='-',command=lambda:btnclick("-")).grid(row=2,column=3)
#========================row3==============================================
b1=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             text='1',bg="purple3",command=lambda:btnclick(1)).grid(row=3,column=0)
b2=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             bg="purple3",text='2',command=lambda:btnclick(2)).grid(row=3,column=1)
b3=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             bg="purple3",text='3',command=lambda:btnclick(3)).grid(row=3,column=2)
b_M=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',19,'bold'),
             bg="purple3",text='*',command=lambda:btnclick("*")).grid(row=3,column=3)
#=========================row4==============================================
b0=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             text='0',bg="purple3",command=lambda:btnclick(0)).grid(row=4,column=0)
b_C=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             bg="purple3",text='C',command=btnclear).grid(row=4,column=1)
b_E=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             bg="purple3",text='=',command=btnequal).grid(row=4,column=2)
b_D=tk.Button(cal,padx=16,bd=8,fg='cyan2',font=('arial',20,'bold'),
             bg="purple3",text='/',command=lambda:btnclick("/")).grid(row=4,column=3)
cal.mainloop()
