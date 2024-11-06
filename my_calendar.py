#!/bin/bash

import calendar
from tkinter import Tk, Label
root= Tk()
root.title("Calendar")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
label = Label(root, text=cal, padx=10, pady=10)
label.pack()
root.mainloop()

