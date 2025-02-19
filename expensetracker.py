#store expenses
expenses = {}

#adds expense
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


def deleting_expense():
    #check if there are any expenses
    if not expenses:
        print("No expenses to delete.\n")
        return

    #print existing categories
    print("\nAvailable categories:")
    categories = list(expenses.keys())
    for x, category in enumerate(categories, 1):
        print(f"{x}. {category}")
    #ask user to choose a category to delete from and print out the expenses under that category    
    try:
        choice = int(input("\nEnter the number of the category to delete from: "))
        if 1 <= choice <= len(categories):
            category = categories[choice - 1]
            print(f"\nExpenses in {category}:")
            records = expenses[category]
            for x, (amount, date) in enumerate(records, 1):
                print(f"{x}. ${amount} on {date}")
            #ask user to choose an expense to delete and delete it   
            record_choice = int(input("\nEnter the number of the expense to delete: "))
            if 1 <= record_choice <= len(records):
                del records[record_choice - 1]
                if not records:
                    del expenses[category]
                print("Expense deleted successfully!")
            else:
                print("Invalid expense number.")
        else:
            print("Invalid category number.")
    except ValueError:
        print("Please enter valid numbers.")

#Calculates total expenses. If dictionary is empty, display "No expenses to calculate"
def total_expense():
    if not expenses:
        print("No expenses to calculate.\n")
        return
    
    #Loops through the categories and their amounts and adds them to the total
    total= 0
    for records in expenses.values():
        #Adds up "amount" values in expenses, but ignores "date" values
        for amount, _ in records:
            total += amount
    
    print(f"\nTotal Expenses: ${total:.2f}\n")
    
#shows options for tracker
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
            total_expense()
        elif choice == '4':
            deleting_expense()
        elif choice == '5':
            print("Thank you for using The Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")
      
        
display_menu()

