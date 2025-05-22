from tracker_db import get_connections
from tkinter import *

def add_expense():
    amount = amount_entry.get()
    category = category_entry.get()
    expense_date = expense_dateE.get()
    description= description_entry.get()

    conn = get_connections()
    curser = conn.cursor()

    sql = "INSERT INTO expenses (amount, category, expense_date, description) VALUES (%s, %s, %s, %s)"
    values = (amount, category, expense_date, description)
    curser.execute(sql, values)
    conn.commit()
    curser.close()
    conn.close()

    results_label.config(text="Expense Added successfully!", fg="green")

def view_expense():
    conn = get_connections()
    cursor = conn.cursor()
    cursor.execute("SELECT amount, category, expense_date, description FROM expenses ORDER BY expense_date DESC")
    rows = cursor.fetchall()
    conn.close()
    cursor.close()

    expenses_text.delete("1.0", END)

    if not rows:
        expenses_text.insert(END, "No expenses found")
        return

    for row in rows:
        amount, category, expense_date, description = row
        expenses_text.insert(END, f"Amount: {amount}, Category: {category}, Date: {expense_date}, Description: {description}\n") 

window = Tk()
window.geometry("400x400")
window.title("Expense Tracker")
frame = Frame(window)
frame.pack()

amount_label = Label(frame, text="Amount")
amount_label.grid(row=0, column=0)
amount_entry = Entry(frame, font=("Consolas", 15))
amount_entry.grid(row=0,column=1)

category_label = Label(frame, text="category")
category_label.grid(row=1, column=0)
category_entry = Entry(frame, font=("Consolas", 15))
category_entry.grid(row=1,column=1)

expense_date = Label(frame, text="Expense date (yyyy-mm-dd)")
expense_date.grid(row=2, column=0)
expense_dateE = Entry(frame, font=("Consolas", 15))
expense_dateE.grid(row=2,column=1)

description_label = Label(frame, text="Description")
description_label.grid(row=3, column=0)
description_entry = Entry(frame, font=("Consolas", 15))
description_entry.grid(row=3,column=1)

button = Button(window, text="Add Expense", command=add_expense)
button.pack()

view_button = Button(window, text="View Expenses", command=view_expense)
view_button.pack()


results_label = Label(window, text="")
results_label.pack()

expenses_text = Text(window, height=15, width=60, font=("Consolas", 12))
expenses_text.pack()

window.mainloop()