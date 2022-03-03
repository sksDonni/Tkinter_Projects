import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the selected list box value
def getListboxValue():
	itemSelected = listBoxOne.curselection()
	return itemSelected



root = Tk()

# This is the section of code which creates the main window
root.geometry('720x485')
root.configure(background='#F0F8FF')
root.title('Hello, I\'m the main window')


# This is the section of code which creates the a label
Label(root, text='Education', bg='#F0F8FF', font=('helvetica', 22, 'italic')).place(x=9, y=55)


# This is the section of code which creates the a label
Label(root, text='University Visvesvaraya College Of Engineering', bg='#F0F8FF', font=('helvetica', 16, 'italic')).place(x=103, y=101)


# This is the section of code which creates the a label
Label(root, text='Information Science and Engineering', bg='#F0F8FF', font=('helvetica', 16, 'italic')).place(x=106, y=136)


# This is the section of code which creates the a label
Label(root, text='2019-2023', bg='#F0F8FF', font=('helvetica', 12, 'italic')).place(x=107, y=176)


# This is the section of code which creates the a label
Label(root, text='Suchih Krishna S Donni', bg='#F0F8FF', font=('helvetica', 24, 'italic')).place(x=162, y=8)


# This is the section of code which creates the a label
Label(root, text='Projects', bg='#F0F8FF', font=('helvetica', 22, 'italic')).place(x=11, y=216)


# This is the section of code which creates a listbox
listBoxOne=Listbox(root, bg='#F0F8FF', font=('helvetica', 18, 'italic'), width=0, height=0)
listBoxOne.insert('0', 'Sudo Writes - \nMERN stack Blog Application')
listBoxOne.insert('1', 'FlaskCards - Spaced Repitition Tool')
listBoxOne.insert('2', 'Omdena - Covid 19 economic impact')
listBoxOne.place(x=107, y=254)

Label(root, text='Skills', bg='#F0F8FF', font=('helvetica', 22, 'italic')).place(x=7, y=350)


# This is the section of code which creates the a label
Label(root, text='Mern stack, python, Sql, data Science, ML', bg='#F0F8FF', font=('helvetica', 16, 'italic')).place(x=82, y=384)

root.mainloop()
