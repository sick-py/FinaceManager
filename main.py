# finance_manager.py

import transactions
import storage
import os

FILE_PATH = 'Data/transactions.csv'

def main():
    if not os.path.exists('Data'):
        os.makedirs('Data')
        
    transaction_list = storage.load_transactions(FILE_PATH)

    while True:
        print("\n--- Finance Manager ---")
        print("1. Add a transaction")
        print("2. Display transactions")
        print("3. Display Income vs Expense")
        print("4. Display transactions in a period")
        print("5. Exit")


        choice = input("Enter your choice: ")

        if choice == '1':
            transactions.add_transaction(transaction_list)
            storage.save_transactions(transaction_list, FILE_PATH)
            storage.create_timestamped_backup(FILE_PATH)
        elif choice == '2':
            periodC = input("enter month/week/year: ")
            transactions.display_transactions_by_period(transaction_list, periodC)
        elif choice == '3':
            periodC = input("enter month/week/year: ")
            transactions.display_income_vs_expense_chart_by_period(transaction_list, periodC)
        elif choice == '4':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            transactions.display_income_vs_expense_chart_for_date_range(transaction_list, start_date, end_date)
            transactions.display_income_vs_expense_chart(transaction_list)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
