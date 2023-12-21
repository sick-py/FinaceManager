# transactions.py
import matplotlib.pyplot as plt
from dateutil import parser, relativedelta
import datetime




def add_transaction(transactions):
    print("\n--- Add a Transaction ---")

    # Get transaction details from the user
    date = input("Enter the date (YYYY-MM-DD): ")
    type = input("Enter the type (income/expense): ")
    category = input("Enter the category (e.g., groceries, salary): ")
    amount = float(input("Enter the amount: "))

    # Create a dictionary for the transaction
    transaction = {
        "date": date,
        "type": type,
        "category": category,
        "amount": amount
    }

    # Add the transaction to the list
    transactions.append(transaction)
    print("Transaction added successfully.")

def display_transactions(transactions):
    print("\n--- Transaction List ---")
    if not transactions:
        print("No transactions available.")
        return

    for index, transaction in enumerate(transactions, start=1):
        print(f"{index}. Date: {transaction['date']}, "
              f"Type: {transaction['type']}, "
              f"Category: {transaction['category']}, "
              f"Amount: {transaction['amount']}")
        
def display_transactions_expense(transactions):
    if not transactions:
        print("No transactions available to display in a chart.")
        return

    # Aggregate amounts by category
    category_totals = {}
    for transaction in transactions:
        if transaction['type'] == 'expense':  # Consider only expenses for chart
            category = transaction['category']
            amount = float(transaction['amount'])
            category_totals[category] = category_totals.get(category, 0) + amount

    # Data for plotting
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    # Creating the bar chart
    plt.bar(categories, amounts)
    plt.xlabel('Category')
    plt.ylabel('Amount spent')
    plt.title('Expenses by Category')
    plt.show()
    
def display_income_vs_expense_chart(transactions):
    if not transactions:
        print("No transactions available to display in a chart.")
        return

    # Initialize totals
    total_income = 0
    total_expense = 0

    # Calculate totals
    for transaction in transactions:
        amount = float(transaction['amount'])
        if transaction['type'].lower() == 'income':
            total_income += amount
        elif transaction['type'].lower() == 'expense':
            total_expense += amount

    # Data for plotting
    categories = ['Income', 'Expense']
    amounts = [total_income, total_expense]

    # Creating the bar chart
    plt.figure(figsize=(8, 5))  # Optional: Adjust the figure size
    plt.bar(categories, amounts, color=['green', 'red'])
    plt.xlabel('Type')
    plt.ylabel('Total Amount')
    plt.title('Total Income vs Total Expense')
    plt.show()
    
def filter_transactions_by_period(transactions, period):
    filtered_transactions = []
    current_date = datetime.datetime.now()

    for transaction in transactions:
        transaction_date = parser.parse(transaction['date'])

        if period == 'month' and transaction_date.month == current_date.month and transaction_date.year == current_date.year:
            filtered_transactions.append(transaction)
        elif period == 'week' and transaction_date > current_date - relativedelta.relativedelta(weeks=1):
            filtered_transactions.append(transaction)
        elif period == 'year' and transaction_date.year == current_date.year:
            filtered_transactions.append(transaction)

    return filtered_transactions

def filter_transactions_by_date_range(transactions, start_date, end_date):
    filtered_transactions = []
    start_date_parsed = parser.parse(start_date)
    end_date_parsed = parser.parse(end_date)

    for transaction in transactions:
        transaction_date = parser.parse(transaction['date'])
        if start_date_parsed <= transaction_date <= end_date_parsed:
            filtered_transactions.append(transaction)

    return filtered_transactions

def display_income_vs_expense_chart_by_period(transactions, period):
    filtered_transactions = filter_transactions_by_period(transactions, period)
    display_transactions_expense(filtered_transactions)
    
def display_transactions_by_period(transactions, period):
    filtered_transactions = filter_transactions_by_period(transactions, period)    
    display_transactions(filtered_transactions)
    
def display_income_vs_expense_chart_for_date_range(transactions, start_date, end_date):
    filtered_transactions = filter_transactions_by_date_range(transactions, start_date, end_date)
    display_income_vs_expense_chart(filtered_transactions)