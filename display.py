from budget import map_expense_to_budget_category
import matplotlib.pyplot as plt
import transactions

def plot_expenses(expenses, period="month"):
    # Aggregate amounts by category
    filted_expenses = transactions.filter_transactions_by_period(expenses, period)
    categories = {}
    for expense in filted_expenses:
        category = expense['Type']
        amount = float(expense['Amount'])
        categories[category] = categories.get(category, 0) + amount

    # Sort categories by amount, from highest to lowest
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)

    # Separate the category names and amounts
    notes = [expense['Note'] for expense in expenses]  # Assuming each expense has a 'Note' key
    
    category_names, amounts = zip(*sorted_categories)
    colors = ['green' if map_expense_to_budget_category(name).startswith('Needs') else 'blue' for name in category_names]

    # Creating the bar chart with colored bars
    plt.figure(figsize=(10, 6))
    bars = plt.bar(category_names, amounts, color=colors)
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.title('Expenses by Category (High to Low)')

   
     # Adding notes inside each bar
    for bar, note in zip(bars, notes):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval/2, note, ha='center', va='center', color='black')

    plt.show()
    

  


