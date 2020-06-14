from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
root = Tk()
root.title("STUUDENT MANAGMENT")
connection = sqlite3.connect("student4.db")

TABLE_NAME = "database4"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"
Student_Email = "Student_email"
connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   Student_Email + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")

applabel=Label(root,text="Student Managment System",fg="#06a099",font=("Times new roman",30),width=35)
applabel.grid(row=0,columnspan=2, padx=(10,10),pady=(30,0))

class Student:
    studentName = ""
    collegeName = ""
    phoneNumber = 0
    address = ""
    email =""
    def __init__(self,StudentName,CollageName,phoneNumber,address,email):
        self.StudentName= StudentName
        self.CollegeName= CollegeName
        self.phoneNumber= phoneNumber
        self.address= address
        self.email= email
        
namelabel=Label(root,text="Enter your Name", width=40 , anchor='w',
                     font=("Time new roman", 12)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0)) 

collegelabel=Label(root,text="Enter your College", width=40 , anchor='w',
                     font=("Time new roman", 12)).grid(row=2, column=0, padx=(10,0),
                                                pady=(30, 0)) 

phonelabel=Label(root,text="Enter your Phone Number", width=40 , anchor='w',
                     font=("Time new roman", 12)).grid(row=3, column=0, padx=(10,0),
                                                pady=(30, 0)) 

addresslabel=Label(root,text="Enter your Adress", width=40 , anchor='w',
                     font=("Time new roman", 12)).grid(row=4, column=0, padx=(10,0),
                                                pady=(30, 0)) 

emaillabel=Label(root,text="Enter your Email", width=40 , anchor='w',
                     font=("Time new roman", 12)).grid(row=5, column=0, padx=(10,0),
                                                pady=(30, 0))

nameEntry = Entry(root, width = 30)
collegeEntry = Entry(root, width = 30)
phoneEntry = Entry(root, width = 30)
addressEntry = Entry(root, width = 30)
emailEntry  = Entry(root, width = 30)

nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
collegeEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
phoneEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
addressEntry.grid(row=4, column=1, padx=(0,10), pady = 20)
emailEntry.grid(row=5, column=1, padx=(0,10), pady = 20)

def takenameinput():
    global nameEntry , collegeEntry , phoneEntry, addressEntry, emailEntry
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE, Student_Email
    
    username = nameEntry.get()
    nameEntry.delete(0,END)
    collegename = collegeEntry.get()
    collegeEntry.delete(0,END)
    phone = phoneEntry.get()
    phoneEntry.delete(0,END)
    address = addressEntry.get()
    addressEntry.delete(0,END)
    email = emailEntry.get()
    emailEntry.delete(0,END)
    
    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                       Student_Email + ", " +
                       STUDENT_PHONE + " ) VALUES ( '"
                       + username + "', '" + collegename + "', '"
                       + email + "','" +
                       address + "', " + (phone) + " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")
def destoryrootwindow():
    root.destroy()
    secondwindow = Tk()
    secondwindow.title("Display Result")
    appLabel = Label(secondwindow, text="Student Management System",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()
    
    tree = ttk.Treeview(secondwindow)
    tree["columns"] = ("one", "two", "three", "four", "five")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="College Name")
    tree.heading("three", text="Address")
    tree.heading("four", text="Phone Number")
    tree.heading("five", text="EMAIL")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[5], row[4]))
        i = i + 1

    tree.pack()
    secondwindow.mainloop()
    
button = Button(root, text="Save", command=lambda :takenameinput())
button.grid(row=6, column=0, pady=30)

displayButton = Button(root, text="Display result", command=lambda :destoryrootwindow())
displayButton.grid(row=6, column=1)

root.mainloop()