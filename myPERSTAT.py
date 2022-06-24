from tkinter import Tk, StringVar, ttk
from tkinter import *
import tkinter as tk
import time

# main:
# Designed background and usage area of the app
count = 0
root = Tk()
root.title("PERSTAT")
root.geometry('950x700+0+0')
root.configure(background="black")

# collection: list of soldiers/student/workers that needs to track presence of
roster = [
    "Goodman",
    "McCord",
    "Martinez",
    "Garr",
    "Reyes",
    "Fegurgur",
    "Antoine",
    "Simula",
    "Singh",
    "Johnson",
    "Huber",
    "Lema",
    "Young",
    "Harris"
]

# create a main frame

wrapper = LabelFrame(root)
mycanvas = Canvas(wrapper)
mycanvas.pack(side=LEFT, fill=BOTH, expand=1)

# Create the ability to scroll on the page
yscrollbar = Scrollbar(wrapper, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

# design of the background of the frame
myframe = Frame(mycanvas, width=950, height=700, bd=6, relief="raised")
myframe.pack(side=LEFT)
newframe = myframe
right_frame = Frame(mycanvas, width=170, height=600, bd=6, relief="raised")
right_frame.pack(side=RIGHT)

mycanvas.create_window((0, 0), window=newframe, anchor="nw")
wrapper.pack(fill="both", expand="yes", padx=10, pady=10)

# create rows
Date = StringVar()
Date.set(time.strftime("%m/%d/%Y"))

# 1st row of the table
lblNo = Label(newframe, font=('arial', 10, 'bold'), text="No.", bd=5)
lblNo.grid(row=0, column=0, sticky=W)
lblName = Label(newframe, font=('arial', 10, 'bold'), text="Name", bd=5, width=5)
lblName.grid(row=0, column=1, sticky=W)
lblPresent = Label(newframe, font=('arial', 10, 'bold'), text="Present", bd=5)
lblPresent.grid(row=0, column=2, sticky=W)
lblNP = Label(newframe, font=('arial', 10, 'bold'), text="Reasons of Absent", bd=5, width=25)
lblNP.grid(row=0, column=3, sticky=W)


# Reset button for each row
def reset_this(pressed):
    # Reset the row's present count
    store_var[pressed].set(0)
    Present_counts(pressed)

    # Reset the row's combobox
    boxes[pressed].current(0)
    Reasons_counts(0)


def Clear_vars():
    boxes.clear()
    checks.clear()
    resets.clear()
    store_var.clear()

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
    appointment_count == 0
    lbltotal_appointment_count['text'] = appointment_count

    # set total child care count to 0
    child_care_count == 0
    lbltotal_child_care_count['text'] = child_care_count

    # set total vacation count to 0
    vacation_count == 0
    lbltotal_vacation_count['text'] = vacation_count


def add_a_student():
    # Add Function
    def adding():
        # Reset the entire file
        Reset()
        Clear_vars()
        # Get new name
        new_roster_name = lblNew_Name.get()
        roster.append(new_roster_name)
        # Display all
        retrieve()

    rownum = len(roster) + 1

    # New Name button
    lblNew_Name = Entry(newframe, font=('arial', 10, 'bold'), text='New Name')
    lblNew_Name.grid(row=rownum, column=1, sticky=W)

    # Submit new name
    submit_btn = Button(newframe, text='Submit', command=adding)
    submit_btn.grid(row=rownum, column=5)


# display of the Reset button on the first row
Button(
    newframe,
    text='Reset',
    padx=2, pady=2,
    bd=5, fg='black',
    font=('arial', 10, 'bold'),
    width=11,
    height=1,
    command=Reset
).grid(row=0, column=4)

# display current date
lblDate = Label(newframe,
                font=('arial', 11, 'bold'),
                textvariable=Date,
                padx=4, pady=4, bd=4,
                fg='black',
                bg='white',
                relief='sunken'
                )
lblDate.grid(row=0, column=5, sticky=W)

# # Add button at the end of the list
Button(right_frame, text="Add Student", command=add_a_student).grid(row=5, column=2, sticky='W')

# get all the counts of presence, 
present_count = 0
# count each occurrence of each reasons from all boxes
appointment_count = 0
child_care_count = 0
vacation_count = 0


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


# Calculate how many people are absent from the roster for each reason
def Reasons_counts(
        result=None,
        appointment_count=appointment_count,
        child_care_count=child_care_count,
        vacation_count=vacation_count
):
    # Check all the comboboxes
    for index in range(len(boxes)):

        # If the combobox does not equal to its default value:
        if boxes[index].get() != 'Choose from the following':
            # print("Box Index", boxes[index])
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


# Loop around the list of soldiers/student/workers that needs to track presence of to build
# the main body of the app to track each
# person's status
boxes = []  # <-- Holds all of the comboboxes
checks = []  # <-- Holds all the present checkboxes
resets = []  # <-- Holds all 'reset this' buttons
store_var = []  # <-- Holds the present count values


def retrieve():
    for i in roster:
        # Number of each person
        lblNo = Label(newframe, font=('arial', 10, 'bold'), text=1 + roster.index(i), bd=5)
        lblNo.grid(row=1 + roster.index(i), column=0, sticky=W)

        # Names of each person
        lblName = Label(newframe, font=('arial', 10, 'bold'), text=i, padx=3, pady=1, bd=1, width=12)
        lblName.grid(row=1 + roster.index(i), column=1, sticky=W)

        # Present check box for each person
        var = tk.IntVar()
        check_box = ttk.Checkbutton(
            newframe,
            text="P",
            variable=var,
            command=lambda index=roster.index(i): Present_counts(index)
        )
        check_box.grid(row=1 + roster.index(i), column=2)
        store_var.append(var)
        checks.append(check_box)

        # Absent reasons choice box for each person
        box = ttk.Combobox(newframe, state='readonly')
        # If the person is not present, enable user to choose absent reasons and disable the current checkbox
        box['values'] = ('Choose from the following', 'Appointment', 'Child Care', 'Vacation')
        box.current(0)
        box.grid(row=1 + roster.index(i), column=3)
        box.bind("<<ComboboxSelected>>", lambda index=roster.index(i): Reasons_counts(index))
        boxes.append(box)

        # Reset button for each line
        btn_resets = Button(newframe,
                            text='Reset this row',
                            padx=2, pady=2, bd=5, fg='black',
                            font=('arial', 10, 'bold'),
                            width=11, height=1,
                            command=lambda index=roster.index(i): reset_this(index)
                            )
        btn_resets.grid(row=1 + roster.index(i), column=4)
        resets.append(btn_resets)

        # Delete button for the entire table
        btnDelete = ttk.Button(newframe, text="Delete Row", command=lambda: btnDelete.pack_forget(), takefocus=True)
        btnDelete.grid(row=1 + roster.index(i), column=5, sticky=W)


lbltotal_present = Label(right_frame, font=('arial', 14, 'bold'), text="Total Present", bd=5)
lbltotal_present.grid(row=1, column=1, sticky=W)
lbltotal_present_count = Label(right_frame, font=('arial', 14, 'bold'), bd=5, text=present_count)
lbltotal_present_count.grid(row=1, column=2, sticky=W)

lbltotal_appointment = Label(right_frame, font=('arial', 14, 'bold'), text="Total Appointment", bd=5)
lbltotal_appointment.grid(row=2, column=1, sticky=W)
lbltotal_appointment_count = Label(right_frame, font=('arial', 14, 'bold'), bd=5, text=appointment_count)
lbltotal_appointment_count.grid(row=2, column=2, sticky=W)

lbltotal_child_care = Label(right_frame, font=('arial', 14, 'bold'), text="Total Child Care", bd=5)
lbltotal_child_care.grid(row=3, column=1, sticky=W)
lbltotal_child_care_count = Label(right_frame, font=('arial', 14, 'bold'), bd=5, text=child_care_count)
lbltotal_child_care_count.grid(row=3, column=2, sticky=W)

lbltotal_vacation = Label(right_frame, font=('arial', 14, 'bold'), text="Total Vacation", bd=5)
lbltotal_vacation.grid(row=4, column=1, sticky=W)
lbltotal_vacation_count = Label(right_frame, font=('arial', 14, 'bold'), bd=5, text=vacation_count)
lbltotal_vacation_count.grid(row=4, column=2, sticky=W)

root.geometry("950x700")
root.resizable(True, True)
retrieve()
root.mainloop()
