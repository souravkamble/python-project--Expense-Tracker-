import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as m

# Create a database connection
mydatabase=m.connect(host="localhost",user="root",password="manager",database="myproject")  

cursor=mydatabase.cursor()


# Create expenses table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        description TEXT,
        amount REAL
    )
''')
mydatabase.commit()

# Function to save an expense to the database
def save_expense():
    description = description_entry.get()
    amount = float(amount_entry.get())

    cursor.execute('INSERT INTO expenses (description, amount) VALUES (%s, %s)', (description, amount))
    mydatabase.commit()

    # Clear input fields after saving
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


# Function to show spending patterns
def show_spending_patterns():
    cursor.execute('SELECT description, amount FROM expenses')
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['Description', 'Amount'])


    # Perform data manipulation and analysis using pandas
    grouped_data = df.groupby('Description')['Amount'].sum().reset_index()



    # Visualize spending patterns using matplotlib
    plt.figure(figsize=(8, 6))
    plt.bar(grouped_data['Description'], grouped_data['Amount'])
    plt.xlabel('Expense Category')
    plt.ylabel('Total Amount')
    plt.title('Spending Patterns')
    plt.xticks(rotation=45)
    plt.show()


# # Create GUI window using tkinter
window = tk.Tk()
window.title('Expense Tracker')

description_label = tk.Label(window, text='Description')
description_label.pack(pady=20)
# description_label.grid()
description_entry = tk.Entry(window)
description_entry.pack(pady=15)

amount_label = tk.Label(window, text='Amount')
amount_label.pack(pady=10)
amount_entry = tk.Entry(window)
amount_entry.pack(pady=10)

save_button = tk.Button(window, text='Save Expense', command=save_expense)
save_button.pack(pady=20)

show_button = tk.Button(window, text='Show Spending Patterns', command=show_spending_patterns)
show_button.pack(pady=15)

window.mainloop()

# Close the database connection
mydatabase.close()

