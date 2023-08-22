from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt1
import mysql.connector as m

def demo4():
    # Create a database connection
    mydatabase=m.connect(host="localhost",user="root",password="manager",database="myprj")  
    cursor=mydatabase.cursor()

    # Create expenses table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Income (id INTEGER PRIMARY KEY AUTO_INCREMENT,description TEXT,amount REAL,date1 DATE)
    ''')
    mydatabase.commit()

    def save_income():
        description1 = description_entry1.get()
        amount1 = float(incomeEntry.get())
        date2 = dateEntry1.get()
        
        cursor.execute('INSERT INTO Income (description, amount, date1) VALUES (%s, %s, %s)', (description1, amount1,date2))
        mydatabase.commit()
        
        description_entry1.delete(0,END)
        incomeEntry.delete(0,END)
        dateEntry1.delete(0,END)
    
    def show_income_patterns():
        
        cursor.execute('SELECT description, amount FROM Income')
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=['description', 'amount'])

        # Perform data manipulation and analysis using pandas
        grouped_data = df.groupby('description')['amount'].sum().reset_index()

        # Visualize spending patterns using matplotlib
        plt1.figure(figsize=(8, 6))
        plt1.bar(grouped_data['description'], grouped_data['amount'])
        plt1.xlabel('Income Category')
        plt1.ylabel('Total amount')
        plt1.title('income Patterns')
        plt1.xticks(rotation=45)
        plt1.show()

    #creating GUI
    window4 =Tk()
    window4.title(" window 4")
    window4.config(background="#13F3FF")
    window4.geometry("550x300+550+280")

    #creating labels

    incomelabel = Label(window4,text="Enter Income",font=("Comic Sans MS", 15))
    incomelabel.place(x=50,y=85)

    incomeEntry =Entry(window4,font=("Comic Sans MS", 15))
    incomeEntry.place(x=250,y=85)
    
    description_label1 = Label(window4, text='Description',font=("Comic Sans MS", 15))
    description_label1.place(x=50,y=25)

    description_entry1 = Entry(window4,font=("Comic Sans MS", 15))
    description_entry1.place(x=250,y=25)
    
    datelabel1 = Label(window4,text="Date",font=("Comic Sans MS", 15))
    datelabel1.place(x=50,y=145)

    dateEntry1 =Entry(window4,font=("Comic Sans MS", 15))
    dateEntry1.place(x=250,y=145)

    saveincomebutton = Button(window4,text ="Save Income",font=("Comic Sans MS", 15),command =save_income)
    saveincomebutton.place(x=50,y=205)

    showipatternbutton = Button(window4,text ="Show Income Pattern",font=("Comic Sans MS", 15),command=show_income_patterns)
    showipatternbutton.place(x=250,y=205)

    window4.mainloop()