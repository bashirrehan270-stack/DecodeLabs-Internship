# Expense tracker system
import csv
import os


class Expense_Tracker:
    def __init__(self):
        self.file_name = "expense_record.csv"
        self.headers = ["Date", "Category", "Amount"]
        self.expenses = self.load_data()

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                return list(reader)
        else:
            return []

    def save_to_csv(self):
        with open(self.file_name, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(self.expenses)

    # adding expenses

    def add_expense(self, Date, Category, Amount):
        # Date = datetime.now().strftime("%d-%b-%Y")
        expense = {"Date": Date, "Category": Category, "Amount": Amount}
        # datetime = datetime.now().strftime( )
        self.expenses.append(expense)
        self.save_to_csv()
        print("Expense added successfully!")

    # view all expenses

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        for expense in self.expenses:
            print(
                f"Date: {expense['Date']}"
                f"Category: {expense['Category']}"
                f"Amount: {expense['Amount']}"
            )
        return self.expenses

    # to reomve expenses

    def remove_expense(self, Date, Category, Amount):
        for expense in self.expenses:
            if (
                expense["Date"] == Date
                and expense["Category"] == Category
                and str(expense["Amount"]) == str(Amount)
            ):
                self.expenses.remove(expense)
                self.save_to_csv()
                print("Expense removed successfully!")
                return

    print("Expense not found.")

    # view expense by mounth
    def monthly_expense(self):
        target_month = input("Enter the target month: ")
        total = 0

        for expense in self.expenses:
            if target_month in expense["Date"]:
                total += int(expense["Amount"])

        print(f"Total Expense for {target_month}: {total}")

    # fot total expenses

    def total_expenses(self):
        total = sum(int(expense["Amount"]) for expense in self.expenses)
        print(f"Total expenses: {total}")
        return total


tracker = Expense_Tracker()


while True:
    print("\n--------- Expense Tracker System ----------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Remove Expense")
    print("4. Monthly Expense")
    print("5. Total Expenses")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter the date: ")
        category = input("Enter expense category: ")
        amount = int(input("Enter expense amount: "))
        tracker.add_expense(date, category, amount)
    elif choice == "2":
        tracker.view_expenses()
    elif choice == "3":
        date = input("Enter the date: ")
        category = input("Enter expense category to remove: ")
        amount = int(input("Enter expense amount to remove: "))
        tracker.remove_expense(date, category, amount)
    elif choice == "4":
        tracker.monthly_expense()
    elif choice == "5":
        tracker.total_expenses()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
print("---------Final Report---------")
tracker.total_expenses()
