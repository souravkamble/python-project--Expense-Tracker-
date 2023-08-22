from tkinter import *
import tkinter.font as font
from demo3 import *
from demo4 import *
import demo4
import demo3


def demo2():

    def validate1():
    
        demo3.demo3()
    
    def validate2():
    
        demo4.demo4()
    
    #creating window
    window2 = Tk(className='Window 2')
    window2.geometry("550x300+550+280")
    window2.resizable(False,False)
    window2.config(background="#81ECEC")

    # create button 
    button1 = Button(window2, text='ADD Expenses', bg='#293241', fg='white',font=("Comic Sans MS", 15),command=validate1)
    button2 = Button(window2,text="ADD Income",bg="#293241",fg="white",font=("Comic Sans MS", 15),command=validate2)

    button1.place(x=200,y=90)
    button2.place(x=205,y=160)
    
    #mainloop
    window2.mainloop() 