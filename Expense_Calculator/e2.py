from tkinter import*
#creating GUI
mywindow =Tk()
mywindow.title("sk's window")
mywindow.geometry("800x500")


# creating lable and its entry

expenselabel = Label(mywindow,text="Expenses")
expenselabel.grid(row = 0,column=0)

expenseEntry =Entry(mywindow)
expenseEntry.grid(row =1,column =0)

savebutton=Button(mywindow,text ="Save Expenses")
savebutton.grid(row=2,column=0)

incomelabel = Label(mywindow,text="Income")
incomelabel.grid(row=0,column=2)

incomelabelEntry =Entry(mywindow)
incomelabelEntry.grid(row=1,column=2)

savebutton1 =Button(mywindow,text ="Save Income")
savebutton1.grid(row=2,column =2)

datelabel = Label(mywindow,text="Date")
datelabel.grid(row=0,column=4)
dateEntry =Entry(mywindow)
dateEntry.grid(row=1,column=4)

savebutton2 = Button(mywindow,text="Svae Date")
savebutton2.grid(row=2,column=4)



mywindow.mainloop()


