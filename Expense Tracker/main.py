import csv
from datetime import datetime

def load_expense(filename):
    try:
        with open(filename, mode="r") as f:
            reader = csv.DictReader(f)
            data = list(reader)
            print("Loaded expenses:", data)  # Debug print
            return data
    except FileNotFoundError:
        print("File not found. Returning empty list.")
        return []

def save_expense(filename, expenses):
    with open(filename, mode="w", newline='') as f:
        fieldnames = ['expense_id', 'date', 'amount', 'description']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)
        print("Saved expenses:", expenses)  # Debug print

def generate_uniqueid(expenses):
    if not expenses:
        return 1
    return max(int(expense['expense_id']) for expense in expenses) + 1

def add_expense(filename):
    expenses = load_expense(filename)
    expense_id = generate_uniqueid(expenses)
    date = input("Enter date (YYYY-MM-DD): ")
    amount = float(input("Enter amount of expenditure: "))
    description = input("Enter description of your expense: ")

    expenses.append({
        'expense_id': str(expense_id),
        'date': date,
        'amount': amount,
        'description': description
    })
    save_expense(filename, expenses)
    print("Expense added successfully!")

def view_expense(filename):
    expenses = load_expense(filename)
    if not expenses:
        print("No expenses found")
        return

    for expense in expenses:
        print(f"ID: {expense['expense_id']}, Date: {expense['date']}, Amount: {expense['amount']}, "
              f"Description: {expense['description']}")

def delete_expense(filename):
    expenses = load_expense(filename)
    if not expenses:
        print("No expenses found")
        return

    expense_id = input("Enter expense id: ")
    expenses = [expense for expense in expenses if expense['expense_id'] != expense_id]
    save_expense(filename, expenses)
    print("Expense deleted successfully")

def generate_report(filename):
    expenses = load_expense(filename)
    if not expenses:
        print("No expenses found")
        return

    description_report = {}
    for expense in expenses:
        description = expense['description']
        amount = float(expense['amount'])
        if description in description_report:
            description_report[description] += amount
        else:
            description_report[description] = amount

    print("Expense Report by Description")
    for description, amount in description_report.items():
        print(f"Description: {description}, Amount: {amount}")

def main():
    filename = "expenses.csv"
    
    while True:
        print("\nWelcome to the Expense Tracker!")
        print("Enter 'Add' to Add Expense")
        print("Enter 'View' to View Expense")
        print("Enter 'Delete' to Delete Expense")
        print("Enter 'Generate' to Generate Report")
        print("Enter 'Exit' to Exit")

        command = input("Enter your command: ")
        if command == "Add":
            add_expense(filename)
        elif command == "View":
            view_expense(filename)
        elif command == "Delete":
            delete_expense(filename)
        elif command == "Generate":
            generate_report(filename)
        elif command == "Exit":
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
