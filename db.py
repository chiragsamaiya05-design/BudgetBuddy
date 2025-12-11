import mysql.connector as conn

def get_connection():
    return conn.connect(
        host="localhost",
        user="root",
        password="ChiragSamaiya",
        database="expense_tracker"
    )
