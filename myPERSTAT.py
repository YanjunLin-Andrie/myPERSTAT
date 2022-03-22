from tkinter import Tk, StringVar, ttk
from tkinter import*
import tkinter as tk
import platform
import time;
import datetime

# main:
root = Tk()
root.title("PERSTAT")
root.geometry('900x3000+0+0')
root.configure(background = "black")


# collection:
roster = ["Goodman","McCORD","Martinez","Garr","Reyes","Fegurgur","Antoine","Simula","Singh","Johnson","Huber",
          "Lema","Young","Harris"]

# create a main frame
wrapper = LabelFrame(root)


mycanvas = Canvas(wrapper)
mycanvas.pack(side=LEFT, fill=BOTH,expand=1)

yscrollbar = ttk.Scrollbar(wrapper, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))


myframe = Frame(mycanvas, width = 900, height = 3000, bd=6, relief="raised" )
mycanvas.create_window((0,0), window=myframe, anchor="nw")
wrapper.pack(fill="both", expand="yes", padx=10, pady=10)

# create rows
Date = StringVar()
Date.set(time.strftime("%m/%d/%Y"))
value = StringVar()



lblNo= Label(myframe,font=('arial',10,'bold'), text="No.", bd=5)
lblNo.grid(row=0, column=0, sticky=W)
lblName = Label(myframe,font=('arial',10,'bold'), text="Name", bd=5, width = 5)
lblName.grid(row=0,column=1, sticky=W)
lblPresent = Label(myframe,font=('arial',10,'bold'), text="Present", bd=5)
lblPresent.grid(row=0,column=2, sticky=W)
lblNP = Label(myframe,font=('arial',10,'bold'), text="Reasons of Absent", bd=5, width = 25)
lblNP.grid(row=0,column=3, sticky=W)

btnArrow = Button(myframe, text='Reset', padx=2, pady=2, bd=5, fg='black', font = ('arial', 10, 'bold'), width = 11, height=1).grid(row = 0, column =4)
lblDate= Label(myframe, font=('arial',11,'bold'), textvariable=Date, padx=4,pady=4,bd=4,fg='black', bg = 'white', relief = 'sunken')
lblDate.grid(row=0, column=5, sticky=W)

for i in roster:
    lblNo = Label(myframe, font=('arial',10,'bold'), text=1+roster.index(i), bd=5)
    lblNo.grid(row=1+roster.index(i), column=0, sticky=W)

    lblName = Label(myframe, font = ('arial', 10,'bold'),text=i, padx=3, pady=1, bd=1, width = 12)
    lblName.grid(row=1+roster.index(i),column=1, sticky = W)

    lblPresent = Label(myframe,font=('arial',10,'bold'), text="P           ", padx=1, pady=1, bd=1, width = 12)
    lblPresent.grid(row=1+roster.index(i),column=2, sticky=W)
    check_box=ttk.Checkbutton(myframe)
    check_box.grid(row=1+roster.index(i), column = 2)

    box = ttk.Combobox(myframe, textvariable = value, state='readonly')
    box['values'] = ('Choose from the following', 'Appointment', 'Child Care', 'Vacation')
    box.current(0)
    box.grid(row=1+roster.index(i), column=3)


    lblempty1 = Label(myframe,font=('arial',10,'bold'), text="", padx=1, pady=1, bd=1, fg="black", width = 13)
    lblempty1.grid(row=1+roster.index(i),column=4, sticky=W)
    lblempty2 = Label(myframe,font=('arial',10,'bold'), text="", padx=1, pady=1, bd=1, fg="black", width = 12)
    lblempty2.grid(row=1+roster.index(i),column=5, sticky=W)

root.geometry("900x300")
root.resizable(False,False)
root.mainloop()
