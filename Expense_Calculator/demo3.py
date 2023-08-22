from tkinter import *
import matplotlib.pyplot as plt
import mysql.connector as m

def demo3():
    # Create a database connection
    mydatabase=m.connect(host="localhost",user="root",password="manager",database="myprj")  
    cursor=mydatabase.cursor()

    # Create expenses table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses1 (id INTEGER PRIMARY KEY AUTO_INCREMENT,description TEXT,
    amount REAL,date1 DATE)
    ''')
    mydatabase.commit()

    # Function to save an expense to the database
    def save_expense():
       
        description = description_entry.get()
        amount = float(expenseEntry.get())
        date1 = dateEntry.get()

        cursor.execute('INSERT INTO expenses1 (Description, Amount, Date1) VALUES (%s, %s, %s)',
                        (description, amount,date1))
        mydatabase.commit()

        # Clear input fields after saving
        description_entry.delete(0,END)
        expenseEntry.delete(0,END)
        dateEntry.delete(0,END)
    
    #function to show the spending pattern
    def show_spending_patterns():
        
        cursor.execute('SELECT date1, SUM(amount) FROM expenses1 GROUP BY date1')
        rows = cursor.fetchall()
        dates = [row[0] for row in rows]
        amounts = [row[1] for row in rows]
        
        # Visualize spending patterns using matplotlib
        plt.bar(dates, amounts)
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title('Daily Amounts')
        plt.xticks(rotation=45)
        plt.show()
        
    #creating GUI
    window3 =Tk()
    window3.title(" window 3")
    window3.geometry("550x300+550+280")
    window3.config(background="#74b9ff")


    # creating lable and its entry
    expenselabel = Label(window3,text="Expenses",font=("Comic Sans MS", 15))
    expenselabel.place(x=50,y=85)

    expenseEntry =Entry(window3,font=("Comic Sans MS", 15))
    expenseEntry.place(x=250,y=85)

    description_label = Label(window3, text='Description',font=("Comic Sans MS", 15))
    description_label.place(x=50,y=25)

    description_entry = Entry(window3,font=("Comic Sans MS", 15))
    description_entry.place(x=250,y=25)

    datelabel = Label(window3,text="Date",font=("Comic Sans MS", 15))
    datelabel.place(x=50,y=145)
    dateEntry =Entry(window3,font=("Comic Sans MS", 15))
    dateEntry.place(x=250,y=145)

    savebutton=Button(window3,text ="Save Expenses",font=("Comic Sans MS", 15),command=save_expense)
    savebutton.place(x=50,y=205)

    savebutton1=Button(window3,text ="Show Expenses Pattern",font=("Comic Sans MS", 15),command=show_spending_patterns)
    savebutton1.place(x=250,y=205)

    window3.mainloop()

