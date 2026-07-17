# Expense tracker system


class Expense_Tracker:
    def __init__(self):
        self.expenses = []

    # adding expenses

    def add_expense(self, amount, category):
        expense = {"amount": amount, "category": category}
        self.expenses.append(expense)
        print("Expense added successfully!")

    # view all expenses

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        for expense in self.expenses:
            print(f"Amount: {expense['amount']},\
                  Category: {expense['category']}")
        return self.expenses

    # to reomve expenses

    def remove_expense(self, amount, category):
        for expense in self.expenses:
            if expense["amount"] == amount and expense["category"] == category:
                self.expenses.remove(expense)
                print("Expense removed successfully!")
                return
        print("Expense not found.")

    # fot total expenses

    def total_expenses(self):
        total = sum(expense["amount"] for expense in self.expenses)
        print(f"Total expenses: {total}")
        return total


tracker = Expense_Tracker()


while True:
    print("\n--------- Expense Tracker System ----------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Remove Expense")
    print("4. Total Expenses")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        tracker.add_expense(amount, category)
    elif choice == "2":
        tracker.view_expenses()
    elif choice == "3":
        amount = int(input("Enter expense amount to remove: "))
        category = input("Enter expense category to remove: ")
        tracker.remove_expense(amount, category)
    elif choice == "4":
        tracker.total_expenses()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
print("---------Final Report---------")
tracker.total_expenses()
