from tkinter import Tk, StringVar, ttk
from tkinter import*
import tkinter as tk
import time

# main:
#Designed backgroun and usage area of the app
root = Tk()
root.title("PERSTAT")
root.geometry('750x400+0+0')
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
myframe = Frame(mycanvas, width = 750, height = 400, bd=6, relief="raised" )
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


# Reset button for each row
def reset_this(pressed):
    # Reset the row's present count
    store_var[pressed].set(0)
    Present_counts(pressed)

    # Reset the row's combobox
    boxes[pressed].current(0)
    Reasons_counts(0)


# Reset all button 
def Reset():
    # iterate over the roster list
    for i in range(len(roster)):
    # clear present checkboxes
        store_var[i].set(0)
    
    # set all comboboxes to the default value at index 0
        boxes[i]['state'] = 'readonly'
        boxes[i].current(0)

        # Enable the present checkboxes
        checks[i]['state'] = 'normal'

    # set Total Present Count to 0
    present_count == 0
    lbltotal_present_count['text'] = present_count

    # set Total appointment count to 0
    lbltotal_appointment_count['text'] == 0
    lbltotal_appointment_count['text'] = appointment_count

    # set total child care count to 0
    lbltotal_child_care_count['text'] == 0
    lbltotal_child_care_count['text'] = child_care_count

    # set total vacation count to 0
    lbltotal_vacation_count['text'] == 0
    lbltotal_vacation_count['text'] = vacation_count


# display of the Reset button on the first row
btnReset = Button(myframe, text='Reset', padx=2, pady=2, bd=5, fg='black', font = ('arial', 10, 'bold'),
             width = 11, height=1, command= Reset).grid(row = 0, column =4)

#display current date
lblDate= Label(myframe, font=('arial',11,'bold'), textvariable=Date, padx=4,pady=4,bd=4,fg='black', bg = 'white', relief = 'sunken')
lblDate.grid(row=0, column=5, sticky=W)


# get all the counts of presence, 
present_count = 0 
# Calculate how many people are present in the roster
def Present_counts(index, present_count=present_count):
    # Get the combobox and reset button for the selected row
    box = boxes[index]
    
    # Check if the present box is selected for the certain row/person
    if store_var[index].get():
        # If checked
        # Disable the combobox
        box.current(0)
        box['state'] = 'disabled'
    
    if not store_var[index].get():
        # If not checked
        # Enable the combobox
        boxes[index]['state'] = 'readonly'

    # Calculate the present count of all boxes checked
    for i in store_var:
        if i.get():
            present_count += 1

    # Display the total count
    lbltotal_present_count['text'] = present_count


#count each occurance of each reasons from all boxes
appointment_count = 0
child_care_count = 0
vacation_count = 0

# Calculate how many people are absent from the roster for each reason
def Reasons_counts(
        result=None, 
        appointment_count = appointment_count, 
        child_care_count = child_care_count, 
        vacation_count = vacation_count
):
    # Check all the comboboxes
    for index in range(len(boxes)):

        # If the combobox does not equal to its default value:
        if boxes[index].get() != 'Choose from the following':
            # Locate the current checkbox
            check_box = checks[index]
            # Disable the checkbox in that row
            check_box['state'] = 'disabled'

            # Calculate the combobox count for each reasons
            if boxes[index].get() == 'Appointment':
                appointment_count += 1
            if boxes[index].get() == 'Child Care':
                child_care_count += 1
            if boxes[index].get() == 'Vacation':
                vacation_count += 1
            
        # If the combobox equals its default value
        if boxes[index].get() == 'Choose from the following':
            # Locate the current checkbox
            check_box = checks[index]
            # Enable the checkbox in that row
            check_box['state'] = 'normal'
    # Display all the totals       
    lbltotal_appointment_count['text'] = appointment_count
    lbltotal_child_care_count['text'] = child_care_count
    lbltotal_vacation_count['text'] = vacation_count

# Loop around the list of soldiers/student/workers that needs to track presence of to build the main body of the app to track each 
# person's status
boxes = []  # <-- Holds all of the comboboxes
checks = []  # <-- Holds all of the present checkboxes
resets = []  # <-- Holds all 'reset this' buttons
store_var = []  # <-- Holds the present count values

for i in roster:
    # Number of each person
    lblNo = Label(myframe, font=('arial',10,'bold'), text=1+roster.index(i), bd=5)
    lblNo.grid(row=1+roster.index(i), column=0, sticky=W)
    
    # Names of each person
    lblName = Label(myframe, font = ('arial', 10,'bold'),text=i, padx=3, pady=1, bd=1, width = 12)
    lblName.grid(row=1+roster.index(i),column=1, sticky = W)
    
    # Present check box for each person
    var = tk.IntVar()
    check_box=ttk.Checkbutton(
        myframe, 
        text = "P", 
        variable = var, 
        command=lambda index=roster.index(i): Present_counts(index)
    )
    check_box.grid(row=1+roster.index(i), column = 2)
    store_var.append(var)
    checks.append(check_box)
    
    # Absent reasons choice box for each person
    box = ttk.Combobox(myframe, state='readonly')
    # If the person is not present, enable user to choose absent reasons and disable the current checkbox
    box['values'] = ('Choose from the following', 'Appointment', 'Child Care', 'Vacation')
    box.current(0)
    box.grid(row=1+roster.index(i), column=3)
    box.bind("<<ComboboxSelected>>", lambda index=roster.index(i): Reasons_counts(index))
    boxes.append(box)

    # Reset button for each line
    btn_resets = Button(myframe,
                        text='Reset this row',
                        padx=2, pady=2, bd=5, fg='black',
                        font=('arial', 10, 'bold'),
                        width=11, height=1,
                        command=lambda index=roster.index(i): reset_this(index)
    )
    btn_resets.grid(row=1 + roster.index(i), column=4)
    resets.append(btn_resets)

    # empty cell to keep a nice format and appearance of the entire table
    lblempty2 = Label(myframe,font=('arial',10,'bold'), text="", padx=1, pady=1, bd=1, fg="black", width = 12)
    lblempty2.grid(row=1+roster.index(i),column=5, sticky=W)

# last rows of the table which summarizes the total number of presence and total number of people for each reason of absence
lbltotal_present = Label(myframe,font=('arial',14,'bold'), text="Total Present", bd=5)
lbltotal_present.grid(row=len(roster)+2,column=1, sticky=W)
lbltotal_present_count = Label(myframe,font=('arial',14,'bold'), bd=5, text = present_count)
lbltotal_present_count.grid(row=len(roster)+2,column=2, sticky=W)

lbltotal_appointment = Label(myframe,font=('arial',14,'bold'), text="Total Appointment", bd=5)
lbltotal_appointment.grid(row=len(roster)+3,column=1, sticky=W)
lbltotal_appointment_count = Label(myframe,font=('arial',14,'bold'), bd=5, text = appointment_count)
lbltotal_appointment_count.grid(row=len(roster)+3,column=2, sticky=W)

lbltotal_child_care = Label(myframe,font=('arial',14,'bold'), text="Total Child Care", bd=5)
lbltotal_child_care.grid(row=len(roster)+4,column=1, sticky=W)
lbltotal_child_care_count = Label(myframe,font=('arial',14,'bold'), bd=5, text = child_care_count)
lbltotal_child_care_count.grid(row=len(roster)+4,column=2, sticky=W)

lbltotal_vacation = Label(myframe,font=('arial',14,'bold'), text="Total Vacation", bd=5)
lbltotal_vacation.grid(row=len(roster)+5,column=1, sticky=W)
lbltotal_vacation_count = Label(myframe,font=('arial',14,'bold'), bd=5, text = vacation_count)
lbltotal_vacation_count.grid(row=len(roster)+5,column=2, sticky=W)

root.geometry("750x400")
root.resizable(True,True)
root.mainloop()
