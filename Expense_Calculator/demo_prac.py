# cursor.execute('SELECT date, amount FROM expenses')
#         rows = cursor.fetchall()
#         df = pd.DataFrame(rows, columns=['date', 'amount'])

#         # Perform data manipulation and analysis using pandas
#         grouped_data = df.groupby('date')['amount'].sum().reset_index()

#         # Visualize spending patterns using matplotlib
#         plt.figure(figsize=(8, 6))
#         plt.bar(grouped_data['date'], grouped_data['amount'])
#         plt.xlabel('Expense Category')
#         plt.ylabel('Total amount')
#         plt.title('Spending Patterns')
#         plt.xticks(rotation=45)
#         plt.show()