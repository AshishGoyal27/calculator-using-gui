import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Calculator")
frame0 = tk.Frame(root,bd=16,bg='gray60',relief='raise')
frame0.pack(side='top')

label = tk.Label(frame0,font=('arial',50,'bold'),width=9,bg='midnight blue',fg='white',
                 text = 'Calculator').grid(row=0,column=0)
def result():
    if var.get()==1:
        qty1=float(firstnum.get())
        qty2=float(secondnum.get())
        res = qty1 + qty2
        total.set(res)
    elif var.get()==2:
        qty1=float(firstnum.get())
        qty2=float(secondnum.get())
        res = qty1 - qty2
        total.set(res)
    elif var.get()==3:
        qty1=float(firstnum.get())
        qty2=float(secondnum.get())
        res = qty1 * qty2
        total.set(res)
    elif var.get()==4:
        qty1=float(firstnum.get())
        qty2=float(secondnum.get())
        res = qty1 / qty2
        total.set(res)
    elif var.get()==5:
        qty1=float(firstnum.get())
        qty2=float(secondnum.get())
        res = qty1 % qty2
        total.set(res)
    elif var.get()==6:
        qty1=float(firstnum.get())
        qty2=float(secondnum.get())
        res = qty1 ** qty2
        total.set(res)
    else:
        qty1=float(firstnum.get())
        qty2=float(secondnum.get())
        res = qty1 // qty2
        total.set(res)
def Exit():
    qexit = messagebox.askyesno("calc","Do you want to exit the system")
    if qexit > 0:
        root.destroy()
        return
def Reset():
    firstnum.set("")
    secondnum.set("")
    total.set("")
        
var=tk.IntVar()
firstnum=tk.IntVar()
secondnum=tk.IntVar()
total=tk.IntVar()

frame1 = tk.Frame(root,bg='gray70',bd=16,relief='raise')
frame1.pack(side='top')
frame_i1 = tk.Frame(frame1,bg='cyan',bd=16,relief='raise')
frame_i1.pack(side='left',ipadx=8)

add=tk.Radiobutton(frame_i1,text='Addition',variable=var,value=1,bg='cyan',
                   font=('helvetica',12,'bold')).grid(row=0,sticky=tk.W)
sub=tk.Radiobutton(frame_i1,text='Subtraction',variable=var,value=2,bg='cyan',
                   font=('helvetica',12,'bold')).grid(row=1,sticky=tk.W)
mul=tk.Radiobutton(frame_i1,text='Multiply',variable=var,value=3,bg='cyan',
                   font=('helvetica',12,'bold')).grid(row=2,sticky=tk.W)
div=tk.Radiobutton(frame_i1,text='Divide',variable=var,value=4,bg='cyan',
                   font=('helvetica',12,'bold')).grid(row=3,sticky=tk.W)
frame_i2 = tk.Frame(frame1,bd=16,bg='cyan',relief='raise')
frame_i2.pack(side='right',ipadx=6)
modulus=tk.Radiobutton(frame_i2,text='Modulus',variable=var,value=5,bg='cyan',
                   font=('helvetica',12,'bold')).grid(row=0,sticky=tk.W)
exp=tk.Radiobutton(frame_i2,text='Exponent',variable=var,value=6,bg='cyan',
                   font=('helvetica',12,'bold')).grid(row=1,sticky=tk.W)
floor_div=tk.Radiobutton(frame_i2,text='Floor_division',variable=var,value=7,bg='cyan',
                   font=('helvetica',12,'bold')).grid(row=2,sticky=tk.W)
space=tk.Label(frame_i2,text='                                       ',bg='cyan',
                   font=('helvetica',12,'bold'),fg='grey').grid(row=3,sticky=tk.W)
frame2 = tk.Frame(root,bd=16,bg='green2',relief='raise')
frame2.pack(side='top',ipadx=11)
labelfirst = tk.Label(frame2,font=('helvetica',12,'bold'),bg='green2',
                      text="enter first number").grid(row=1,column=0,sticky=tk.W)
txtfirst = tk.Entry(frame2,font=('helvetica',12,'bold'),
                      textvariable=firstnum).grid(row=1,column=1)
labelsecond = tk.Label(frame2,font=('helvetica',12,'bold'),bg='green2',
                      text="enter second number").grid(row=2,column=0,sticky=tk.W)
txtsecond = tk.Entry(frame2,font=('helvetica',12,'bold'),
                      textvariable=secondnum).grid(row=2,column=1)
labelresult = tk.Label(frame2,font=('helvetica',12,'bold'),bg='green2',
                      text="Result is").grid(row=3,column=0,sticky=tk.W)
txtresult = tk.Entry(frame2,font=('helvetica',12,'bold'),
                      textvariable=total).grid(row=3,column=1)
frame3 = tk.Frame(root,bd=2,bg='gray70',relief='raise')
frame3.pack(side='top')
result=tk.Button(frame3,text='Get result',bg='gold',font=('helvetica',12,'bold'),command=result).grid(row=0,column=0)
reset=tk.Button(frame3,text='Reset',bg='gold',font=('helvetica',12,'bold'),command=Reset).grid(row=0,column=1)
Exit=tk.Button(frame3,text='Exit',bg='gold',font=('helvetica',12,'bold'),command=Exit).grid(row=0,column=2)
root.mainloop()

