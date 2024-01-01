import transactions

def set_budget(incomes, budget_categories, period="month"): # we can set the period to week, month, year
    filted_incomes = transactions.filter_transactions_by_period(incomes, period)
    
    total_income = sum(float(item['Amount']) for item in filted_incomes) 
    
    budget = {}

    for category, percentage in budget_categories.items():
        budget[category] = total_income * percentage

    return budget


def compare_budget_to_spending(budget, expenses, period = "month"):
    spending = {}
    filted_expenses = transactions.filter_transactions_by_period(expenses, period)

    # Initialize spending dictionary
    for category in budget.keys():
        spending[category] = 0

    # Sum expenses by category
    for expense in filted_expenses:
        # You might need to map your expense types to budget categories here
        category = map_expense_to_budget_category(expense['Type'])
        spending[category] += float(expense['Amount'])

    # Compare spending to budget
    for category in budget.keys():
        print(f"{category}: Budgeted: ${budget[category]:.2f}, Spent: ${spending[category]:.2f}")
        if spending[category] > budget[category]:
            print(f"Over budget in {category} by ${spending[category] - budget[category]:.2f}")
        else:
            print(f"Under budget in {category} by ${budget[category] - spending[category]:.2f}")

def map_expense_to_budget_category(expense_type):
    # This is a simplified example. You'll need to define your own mapping logic.
    if expense_type.startswith("expense-need-"):
        return 'Needs'
    else:
        return 'Wants'

def get_savings():
    return 0