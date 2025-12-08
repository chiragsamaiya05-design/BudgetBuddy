import mysql.connector
from datetime import datetime


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


def add_expense(user_id):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD): ")

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
   

def delete_expense(user_id):
    expense_id = input("Enter expense ID to delete: ")

    cursor.execute("DELETE FROM expenses WHERE id=%s AND user_id=%s",
                   (expense_id, user_id))
    conn.commit()

    print("Expense deleted!\n")


def update_expense(user_id):
    expense_id = input("Enter expense ID to update: ")

    amount = float(input("New amount: "))
    category = input("New category: ")
    description = input("New description: ")
    date = input("New date (YYYY-MM-DD): ")

    cursor.execute("""UPDATE expenses
                      SET amount=%s, category=%s, description=%s, date=%s
                      WHERE id=%s AND user_id=%s""",
                   (amount, category, description, date, expense_id, user_id))
    conn.commit()

    print("Expense updated\n")


def menu(user_id):
    while True:
        print("""
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Logout
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(user_id)
        elif choice == "2":
            view_expenses(user_id)
        elif choice == "3":
            update_expense(user_id)
        elif choice == "4":
            delete_expense(user_id)
        elif choice == "5":
         print("log out\n")
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