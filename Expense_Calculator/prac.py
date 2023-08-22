# query = "SELECT date, SUM(amount) FROM your_table GROUP BY date"
# cursor.execute(query)
# rows = cursor.fetchall()
# dates = [row[0] for row in rows]
# amounts = [row[1] for row in rows]
# plt.bar(dates, amounts)
# plt.xlabel('Date')
# plt.ylabel('Amount')
# plt.title('Daily Amounts')
# plt.xticks(rotation=45)
# plt.show()
# db.close

# *******************************************************
# cursor.execute('SELECT date, amount FROM expenses')

# **********************************************************

import matplotlib.pyplot as plt

# Some example data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 18]

# Plotting the data
plt.plot(x, y)

# Rotating x-axis tick labels by 45 degrees
plt.xticks()

# Display the plot
plt.show()
# ***************************************
#function to show the spending pattern
    def show_spending_patterns():
        cursor.execute('SELECT description, SUM(amount) FROM expenses1 GROUP BY descrip')
        rows = cursor.fetchall()
        # df = pd.DataFrame(rows, columns=['date', 'amount'])
        dates = [row[0] for row in rows]
        amounts = [row[1] for row in rows]

        # Perform data manipulation and analysis using pandas
        # grouped_data = df.groupby('date')['amount'].sum().reset_index()
        # dates = [date.strptime(date, '%Y-%m-%d').date() for date in dates]

        # Visualize spending patterns using matplotlib
        plt.figure(figsize=(8, 6))
        plt.bar(grouped_data['date'], grouped_data['amount'])
        plt.xlabel('Expense Category')
        plt.ylabel('Total amount')
        plt.title('Spending Patterns')
        plt.xticks(rotation=45)
        plt.show()


