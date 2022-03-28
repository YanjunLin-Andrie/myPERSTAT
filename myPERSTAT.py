from tkinter import Tk, StringVar, ttk
from tkinter import*
import tkinter as tk
import platform
import time
import datetime

# main:
#Designed backgroun and usage area of the app
root = Tk()
root.title("PERSTAT")
root.geometry('900x3000+0+0')
root.configure(background = "black")


# collection: list of soldiers/student/workers that needs to track presence of
roster = ["Goodman","McCORD","Martinez","Garr","Reyes","Fegurgur","Antoine","Simula","Singh","Johnson","Huber",
          "Lema","Young","Harris"]

# create a main frame
# create a scroll bar to the right of the frame
wrapper = LabelFrame(root)
mycanvas = Canvas(wrapper)
mycanvas.pack(side=LEFT, fill=BOTH,expand=1)

yscrollbar = ttk.Scrollbar(wrapper, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

# design of the background of the frame
myframe = Frame(mycanvas, width = 900, height = 3000, bd=6, relief="raised" )
mycanvas.create_window((0,0), window=myframe, anchor="nw")
wrapper.pack(fill="both", expand="yes", padx=10, pady=10)

# create rows
Date = StringVar()
Date.set(time.strftime("%m/%d/%Y"))

#1st row of the table 
lblNo= Label(myframe,font=('arial',10,'bold'), text="No.", bd=5)
lblNo.grid(row=0, column=0, sticky=W)
lblName = Label(myframe,font=('arial',10,'bold'), text="Name", bd=5, width = 5)
lblName.grid(row=0,column=1, sticky=W)
lblPresent = Label(myframe,font=('arial',10,'bold'), text="Present", bd=5)
lblPresent.grid(row=0,column=2, sticky=W)
lblNP = Label(myframe,font=('arial',10,'bold'), text="Reasons of Absent", bd=5, width = 25)
lblNP.grid(row=0,column=3, sticky=W)


# Reset button 
def Reset():
    check_box.deselect()
    box.current(0)

btnReset = Button(myframe, text='Reset', padx=2, pady=2, bd=5, fg='black', font = ('arial', 10, 'bold'),
             width = 11, height=1, command= Reset).grid(row = 0, column =4)

#display current date
lblDate= Label(myframe, font=('arial',11,'bold'), textvariable=Date, padx=4,pady=4,bd=4,fg='black', bg = 'white', relief = 'sunken')
lblDate.grid(row=0, column=5, sticky=W)

# Loop around the list of soldiers/student/workers that needs to track presence of to build the main body of the app to track each 
# person's status
boxes = []

for i in roster:
    lblNo = Label(myframe, font=('arial',10,'bold'), text=1+roster.index(i), bd=5)
    lblNo.grid(row=1+roster.index(i), column=0, sticky=W)

    lblName = Label(myframe, font = ('arial', 10,'bold'),text=i, padx=3, pady=1, bd=1, width = 12)
    lblName.grid(row=1+roster.index(i),column=1, sticky = W)

    store_var = []
    var = tk.IntVar()
    check_box=ttk.Checkbutton(myframe, text = "P", variable = var)
    check_box.grid(row=1+roster.index(i), column = 2)
    store_var.append(var)

    box = ttk.Combobox(myframe, state='readonly')
    box['values'] = ('Choose from the following', 'Appointment', 'Child Care', 'Vacation')
    box.current(0)
    box.grid(row=1+roster.index(i), column=3)

    boxes.append(box)

# empty cells to keep a nice format and appearance of the entire table
    lblempty1 = Label(myframe,font=('arial',10,'bold'), text="", padx=1, pady=1, bd=1, fg="black", width = 13)
    lblempty1.grid(row=1+roster.index(i),column=4, sticky=W)
    lblempty2 = Label(myframe,font=('arial',10,'bold'), text="", padx=1, pady=1, bd=1, fg="black", width = 12)
    lblempty2.grid(row=1+roster.index(i),column=5, sticky=W)

# get all the counts of presence, 

def Present_counts():
#count how many are present from the check box   
    present_count = 0    
    for i in store_var:
        if i.get():
            present_count += 1
    return present_count



#count each occurance of each reasons from all boxes
def Reasons_counts():
    appointment_count = 0
    child_care_count = 0
    vacation_count = 0
    for i in roster:
        if boxes[roster.index(i)].get() == 'Appointment':
            appointment_count += 1
        if boxes[roster.index(i)].get() == 'Child Care':
            child_care_count += 1
        if boxes[roster.index(i)].get() == 'Vacation':
            vacation_count += 1
    return appointment_count, child_care_count, vacation_count

# last rows of the table which summarizes the total number of presence and total number of people for each reason of absence
lbltotal_present = Label(myframe,font=('arial',14,'bold'), text="Total Present", bd=5)
lbltotal_present.grid(row=len(roster)+2,column=1, sticky=W)
lbltotal_present_count = Label(myframe,font=('arial',14,'bold'), command = Present_counts, bd=5)
lbltotal_present_count.grid(row=len(roster)+2,column=2, sticky=W)

lbltotal_appointment = Label(myframe,font=('arial',14,'bold'), text="Total Appointment", bd=5)
lbltotal_appointment.grid(row=len(roster)+3,column=1, sticky=W)
lbltotal_appointment_count = Label(myframe,font=('arial',14,'bold'), bd=5)
lbltotal_appointment_count.grid(row=len(roster)+3,column=2, sticky=W)

lbltotal_child_care = Label(myframe,font=('arial',14,'bold'), text="Total Child Care", bd=5)
lbltotal_child_care.grid(row=len(roster)+4,column=1, sticky=W)
lbltotal_child_care_count = Label(myframe,font=('arial',14,'bold'), bd=5)
lbltotal_child_care_count.grid(row=len(roster)+4,column=2, sticky=W)

lbltotal_vacation = Label(myframe,font=('arial',14,'bold'), text="Total Vacation", bd=5)
lbltotal_vacation.grid(row=len(roster)+5,column=1, sticky=W)
lbltotal_vacation_count = Label(myframe,font=('arial',14,'bold'), bd=5)
lbltotal_vacation_count.grid(row=len(roster)+5,column=2, sticky=W)



root.geometry("900x300")
root.resizable(False,False)
root.mainloop()
