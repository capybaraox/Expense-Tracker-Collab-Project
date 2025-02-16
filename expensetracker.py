print("ian sucks balls")


# Dictionary to store expenses
expenses = {}


# add expense
def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: $"))
    date = input("Date(DD/MM/YYYY): ")
    #it adds the expense under the same category and creates another list if it doesnt exist
    expenses.setdefault(category, []).append((amount, date))
    print("Expense Added\n")

#view expenses
def view_expense():
    if not expenses:
        print("No expenses.\n")
        return
    #formatting for a header to display expenses
    print("Category\tAmount\tDate")
    print("-" * 30)
    for category, records in expenses.items():
        for amount, date in records:
            print(f"{category}: ${amount} on {date}")


def display_menu():
    while True:
        print("\nExpense Menu")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Calculating Total Expenses")
        print("4. Deleting Expenses")
        print("5. Exit")
        
        choice = input("Enter your choice (1-4):")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            calculating_total()
        elif choice == '4':
            deleting_expense()
        elif choice == '5':
            print("Thank you for using The Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")
      
        
display_menu()

