print("ian sucks balls")


expenses = {}

# add expense
def add_expense(name, due_date):
    expenses[name] = due_date
    print(f"Expense '{name}' added with due date {due_date}.")

# displays expense menu
def display_menu():
    while True:
        # prints menu options
        print("\nExpense Menu")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Calculating Total Expenses")
        print("4. Deleting Expenses")
        print("5. Exit")
        
        choice = input("Enter your choice (1-4):")
        if choice == '1':
             # expense name and due date
            name = input("Enter the expense name: ")
            amount = float(input("Enter the amount of the expense: $"))
            due_date = input("Enter date (DD/MM/YYYY): ")
            add_expense(name, due_date)

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
