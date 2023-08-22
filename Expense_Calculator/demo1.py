from tkinter import *
import tkinter.font as font
from demo2 import *
import demo2


def validateLogin():
    myFont = font.Font(family='Helvetica',size=20)
    if(usernameEntry.get()=="sourav" and userpasswordEntry.get()=="sourav123"):
        demo2.demo2()
    else:
        resultlabel.config(fg="red",font=myFont)
        resultlabel["text"]="Invalid User"
    

#window1
window1 = Tk()  
# window1.geometry("800x600+400+100")  
window1.geometry("800x600") 
window1.state('zoomed')
window1.title('Log in page for Expenses Tracker')

#Define Image
bg =PhotoImage(file="finance_team.png")

#label
mylabel = Label(window1,image =bg)
mylabel.place(x=0,y=0,relwidth =1,relheight=1)

welcomelabel = Label(window1,text="Welcome to the Expenses Tracker By Sourav", 
font=("Comic Sans MS", 25), fg='#595959', bg='#E2EBD5')
welcomelabel.place(x=460, y=200)

usernamelabel = Label(window1,text="Username", font=("Comic Sans MS", 15))
usernamelabel.place(x=570, y=370)
usernameEntry = Entry(window1, font=("Comic Sans MS", 15))
usernameEntry.place(x=680, y=370)

#entry for user input
userpasswordlabel = Label(window1,text="Password",font=("Comic Sans MS", 15))
userpasswordlabel.place(x=570, y=450)
userpasswordEntry = Entry(window1,font=("Comic Sans MS", 15),show='*')
userpasswordEntry.place(x=680, y=450)

#submit button
loginButton = Button(window1, text="Login",font=("Comic Sans MS", 15) ,command=validateLogin)
loginButton.place(x=710, y=500)
#place label, entry, and button in grid
resultlabel=Label(window1)
resultlabel.place(x=680,y=570)
#main loop
window1.mainloop()