# storage.py

import csv
import datetime
        
def input_income(incomes):
    income_input = input("Enter income details (type, amount, date, period, note): ")
    type, amount, date, period, *note = (income_input.split(',') + [''] * 5)[:5]
    note = note[0] if note else 'No notes'  # Default note

    incomes.append({
        "Type": type.strip() or 'Unknown Type',
        "Amount": float(amount.strip()) if amount.strip() else 0,
        "Date": date.strip() or '2023-01-01',  # Default date
        "Period": float(period.strip()) if period.strip() else 30,  # Default period
        "Note": note.strip()
    })


def input_assets(assets):
    asset_input = input("Enter asset details (type, expectation, date, note): ")
    type, value, date, *note = (asset_input.split(',') + [''] * 4)[:4]
    note = note[0] if note else 'No notes'

    assets.append({
        "Type": type.strip() or 'Unknown Asset',
        "Expectation": float(value.strip()) if value.strip() else 0,
        "Date": date.strip() or '2023-01-01',
        "Note": note.strip()
    })

def input_expenses(expenses):
    expense_input = input("Enter expense details (type, amount, date, period, note): ")
    type, amount, date, period, *note = (expense_input.split(',') + [''] * 5)[:5]
    note = note[0] if note else 'No notes'

    expenses.append({
        "Type": type.strip() or 'Unknown Expense',
        "Amount": float(amount.strip()) if amount.strip() else 0,
        "Date": date.strip() or '2023-01-01',
        "Period": float(period.strip()) if period.strip() else 0,
        "Note": note.strip()
    })



def save_to_csv(data, filename, fieldnames):
    with open(filename, 'a', newline='') as csvfile:  # Use 'a' for append mode
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:  # Write header only if file is empty
            writer.writeheader()
        writer.writerows(data)

def load_from_csv(filename):
    datas = []
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                datas.append(row)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty income data.")
    return datas


def create_timestamped_backup(filepath):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_filepath = f"Data/Backup/transactions_backup_{timestamp}.csv"
    try:
        with open(filepath, 'r') as file:
            data = file.read()
        with open(backup_filepath, 'w') as backup_file:
            backup_file.write(data)
    except FileNotFoundError:
        pass  # If the original file doesn't exist, no backup is created
