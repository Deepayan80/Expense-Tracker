import csv
from datetime import datetime

def add_expense():
    try: 
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount please enter a number")
        return
    
    category = input("Enter category: ").strip()
    note = input("Enter note (optional): ").strip()
    date = datetime.now().strftime("%y-%m-%d")

    file_exists = False
    try:
        with open("expense.csv", "r"):
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open("expense.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["amount", "category", "date", "note"])

        writer.writerow([amount,category,date,note])
    
    print("Expense added succefully")

def view_expense():
    try:
        with open("expense.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("No expense found")
                return

            print("=========== All Expense ============")
            header = rows[0]
            data = rows[1 : ] 

            for row in data: 
                amount, category, date, note = row
                print(f"Amount: {amount} | Category: {category} | Date: {date} | Note: {note}")
    
    except FileNotFoundError:
        print("No expense file found. Please add expense first")

def calculate_total():
    try:
        with open("expense.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("No expenses found")
                return
            
            total = 0
            data = rows[1:]

            for row in data:
                amount = float(row[0])
                total += amount

            print(f"\nTotal Spending: {total}")

    except FileNotFoundError:
        print("No expense file found. Please enter expense first")

    except ValueError:
        print("Error in data format. Please check your file")

def category_summary():
    try:
        with open("expense.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        if len(rows) <= 1:
            print("No expenses found")
            return
        
        data = rows[1: ]
        category_totals = {}

        for row in data:
            amount = float(row[0])
            category = row[1].strip()

            if category in category_totals:
                category_totals[category] += amount

            else:
                category_totals[category] = amount

        print("============= Category Wise Spending ==============")
        for category, total in category_totals.items():
            print(f"{category} : {total}")

    except FileNotFoundError:
        print("No expense file found. please add expense first")

    except ValueError:
        print("Error in data format please check your file.")

def main():
    while True:
        print("=========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Spending")
        print("4. Category Wise Spending")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            #print("Add Expense Selected")
            add_expense()

        elif choice == 2:
            #print("View Expense Selected")
            view_expense()

        elif choice == 3:
            #print("Total Spending Selected")
            calculate_total()

        elif choice == 4:
            #print("Category Wise Spending Selected")
            category_summary()

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Enter a valid choice")

if __name__ == "__main__" :
    main()