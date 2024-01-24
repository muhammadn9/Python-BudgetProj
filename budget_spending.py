# Budget Spending Information Project

# Initialize empty dictionary to store expenses
expenses = {}

# Function to add an expense
def add_expense(category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

# Function to view total spending
def view_total_spending():
    total_spending = sum(expenses.values())
    print(f"Total Spending: ${total_spending}")

# Function to view expenses by category
def view_expenses_by_category():
    print("Expenses by Category:")
    for category, amount in expenses.items():
        print(f"{category}: ${amount}")

# Main program loop
while True:
    print("\nBudget Spending Information System")
    print("1. Add Expense")
    print("2. View Total Spending")
    print("3. View Expenses by Category")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: $"))
        add_expense(category, amount)
        print("Expense added successfully!")

    elif choice == "2":
        view_total_spending()

    elif choice == "3":
        view_expenses_by_category()

    elif choice == "4":
        print("Exiting Budget Spending Information System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
