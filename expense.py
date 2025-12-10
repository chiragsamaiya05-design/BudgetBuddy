import mysql.connector
from datetime import datetime
import csv
import os
from openpyxl import Workbook


conn =mysql.connector.connect(
        host="localhost",
        user="root",
        password="ChiragSamaiya",      
        database="expense_tracker"
    )

cursor = conn.cursor()

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                       (username, password))
    conn.commit()
    print("Registration successful!\n")


def login():
     username = input("Enter username: ")
     password = input("Enter password: ")

     cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s",
                   (username, password))
     result = cursor.fetchone()

     if result:
        print("\nLogin successful!")
        return result[0]
     else:
        print("Invalid credentials.\n")
        return None

def convert_date(date_input):
    d = datetime.strptime(date_input, "%d-%m-%Y")   
    return d.strftime("%Y-%m-%d") 


def add_expense(user_id):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ").upper()
    description = input("Enter description: ").upper()
    date_input = input("Enter date (DD-MM-YYYY): ")
    date = convert_date(date_input)

    if not date:
        return 


    cursor.execute("""INSERT INTO expenses (user_id, amount, category, description, date)
                      VALUES (%s, %s, %s, %s, %s)""",
                   (user_id, amount, category, description, date))
    conn.commit()

    print("Expense added successfully\n")


def view_expenses(user_id):
     cursor.execute("SELECT id, amount, category, description, date FROM expenses WHERE user_id=%s",
                   (user_id,))
     rows = cursor.fetchall()

    
     for r in rows:
        print(f"ID: {r[0]} | Amount: ₹{r[1]} | Category: {r[2]} | Desc: {r[3]} | Date: {r[4]}")

def view_by_category(user_id):
    category = input("Enter category to filter: ").upper()

    cursor.execute("""
        SELECT id, amount, category, description, date 
        FROM expenses 
        WHERE user_id = %s AND category = %s
    """, (user_id, category))

    rows = cursor.fetchall()

    if not rows:
        print(f"No expenses found for category: {category}\n")
        return

    print(f"\nExpenses under category: {category}\n")
    for r in rows:
        print(f"ID: {r[0]} | Amount: ₹{r[1]} | Desc: {r[3]} | Date: {r[4]}")
    print()


def delete_expense(user_id):
    expense_id = input("Enter expense ID to delete: ")

    cursor.execute("DELETE FROM expenses WHERE id=%s AND user_id=%s",
                   (expense_id, user_id))
    conn.commit()

    print("Expense deleted!\n")


def update_expense(user_id):
    expense_id = input("Enter expense ID to update: ")

    amount = float(input("New amount: "))
    category = input("New category: ").upper()
    description = input("New description: ").upper()
    date_input = input("Enter date (DD-MM-YYYY): ")
    date = convert_date(date_input)

    if not date:
        return  


    cursor.execute("""UPDATE expenses
                      SET amount=%s, category=%s, description=%s, date=%s
                      WHERE id=%s AND user_id=%s""",
                   (amount, category, description, date, expense_id, user_id))
    conn.commit()

    print("Expense updated\n")

def report_csv(user_id):
  
   cursor.execute("""SELECT id, amount, category, description, date FROM expenses WHERE user_id = %s
""",(user_id,))
   
   rows= cursor.fetchall()

   if not rows:
        print("No expenses found to export.\n")
        return

   filename = f"{user_id}.csv"

   with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        writer.writerow(["ID", "Amount", "Category", "Description", "Date"])
        
        for row in rows:
            writer.writerow(row)

   print(f"CSV exported successfully → {filename}\n")
  
from openpyxl import Workbook

def report_excel(user_id):
    cursor.execute("SELECT id, amount, category, description, date FROM expenses WHERE user_id = %s",
                   (user_id,))
    rows = cursor.fetchall()

    if not rows:
        print("No expenses found to export.\n")
        return

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Expenses"

    sheet.append(["ID", "Amount", "Category", "Description", "Date"])

    for row in rows:
        sheet.append(row)

    filename = f"{user_id}.xlsx"
    workbook.save(filename)

    print(f"Excel exported successfully → {filename}\n")
def delete_account(user_id):
    print("\n WARNING: This will permanently delete your account and all expense records!")
    confirm = input("Type YES to confirm: ")

    if confirm.upper() != "YES":
        print("Account deletion cancelled.\n")
        return

    cursor.execute("DELETE FROM expenses WHERE user_id = %s", (user_id,))
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()

    print("Your account and all related data have been deleted permanently.\n")
    return "DELETED"


def menu(user_id):
    while True:
        print("""
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Get Report
6. Logout
7. Delete Account
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(user_id)
        elif choice == "2":
            while True:
                print("""
1. view Expenses
2. View Expenses by Category
3. Main Menu                    
""" )
                choice_view = input("Enter choice for view")
                if choice_view=="1":
                    view_expenses(user_id)
                elif choice_view=="2":
                    view_by_category(user_id)
                elif choice_view =="3":
                    print("Back to Main Menu")
                    break
                else:
                    print("Invalid Option/Choice\n")
        elif choice == "3":
            update_expense(user_id)
        elif choice == "4":
            delete_expense(user_id)
        elif choice =="5":
            while True:
               print("""
1.CSV
2.Excel
3.Main Menu
""")
               choice_report = input("Enter your choice: ")

               if choice_report=="1":
                   report_csv(user_id)
               elif choice_report=="2":
                   report_excel(user_id)
               elif choice_report =="3":
                   print("Back to Main Menu\n")
                   break
               else:
                     print("invalid option\n")           

            

        elif choice == "6":
         print("log out\n")
         break
        elif choice=="7":
            delete_account(user_id)
            break
        else:
            print("invalid option")

while True:
    print("""
1. Register
2. Login
3. Exit
""")
    option = input("Choose option: ")

    if option == "1":
        register()
    elif option == "2":
        user_id = login()
        if user_id:
            menu(user_id)
    elif option == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid input.\n")