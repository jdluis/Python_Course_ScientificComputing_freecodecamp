def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def print_all_category(expenses):
    print('Categorys: ')
    category_list = []

    for expense in expenses:
        category = expense["category"]

        if category not in category_list:
            category_list.append(category)
            
    print(', '.join(category_list))
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    expenses = [
        {"amount": 5 , "category": "ocio" },
        {"amount": 14 , "category": "ocio"},
        {"amount": 20 , "category": "food"},
        {"amount": 80 , "category": "food"},
        {"amount": 23 , "category": "transport"}
        ]
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Show all categorys')
        print('6. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print_all_category(expenses)

        elif choice == '6':
            print('Exiting the program.')
            break

if __name__ == '__main__':
    main()