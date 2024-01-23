#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import json
from datetime import datetime

def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        expenses = []
    return expenses

def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)

def add_expense(expenses, category, amount):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expense = {'timestamp': timestamp, 'category': category, 'amount': amount}
    expenses.append(expense)
    print(f"Expense added: {category} - ${amount}")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
    else:
        print("===== Expenses =====")
        for expense in expenses:
            print(f"{expense['timestamp']} | {expense['category']} | ${expense['amount']}")

def expense_tracker():
    expenses = load_expenses()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, category, amount)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            save_expenses(expenses)
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    expense_tracker()


# In[ ]:




