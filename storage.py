# storage.py

import csv
import datetime

def save_transactions(transactions, filepath):
    with open(filepath, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'type', 'category', 'amount'])
        writer.writeheader()
        writer.writerows(transactions)

def load_transactions(filepath):
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

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
