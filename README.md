
BudgetBuddy – CLI Expense Tracker (Python + MySQL)

BudgetBuddy is a command-line based personal expense tracker built using Python and MySQL.
It helps users manage their expenses with features like adding, viewing, updating, deleting, exporting reports, visualizations, and monthly summaries.

 Features
 User Authentication

Register new users

Login using username + password

Delete account with confirmation

 Expense Management

Add new expense

View all expenses

Update expense

Delete expense

Local ID per user (IDs start from 1 for each user)

Accepts date in DD-MM-YYYY format

Automatically converts category & description to uppercase

✔ Search & Filters

Search expenses by description

View expenses by category

Sort expenses (amount/date)

Monthly expense report

Monthly summary breakdown

Date-range filters (planned)
 Reports

Export all expenses as CSV

Export all expenses as Excel (.xlsx)

Category-wise charts using Matplotlib & Seaborn (Pie Chart + Bar Chart)

 Analytics

Total monthly spending

Category-wise breakdown

Highest and lowest expense

Total transactions

 Database Structure (MySQL)
Table: users
Column	Type
id	INT (PK, AI)
username	VARCHAR(50)
password	VARCHAR(50)
Table: expenses
Column	Type
id	INT (PK, AI)
user_id	INT (FK)
amount	DECIMAL(10,2)
category	VARCHAR(50)
description	TEXT
date	DATE
local_id	INT

Technology Stack

Python 3

MySQL

mysql-connector-python

Pandas

Seaborn

Matplotlib

openpyxl

=======
# BudgetBuddy

*#  BudgetBuddy – Python + MySQL Expense Tracker

**BudgetBuddy** is a simple and efficient **expense tracking system** built using **Python** and **MySQL**.  
It helps users record, update, delete, and review their daily expenses with an easy-to-use command-line interface.

This project is perfect for beginners learning:
- Python programming  
- MySQL CRUD operations  
- Authentication system  
- CLI-based application structure  

---

##  Features

###  User Authentication
- Register new users  
- Secure login  
- User-specific expense records  

### Expense Manager
- Add new expenses  
- Update existing expenses  
- Delete expenses  
- View all recorded expenses in a clean table-style format  

###  Database Storage (MySQL)
- Stores users and expenses  
- Clean relational design  
- Prevents user data mixing  

---

## 🛠 Tech Stack

| Component | Technology |
|----------|------------|
| Backend  | Python 3   |
| Database | MySQL      |
| Library  | mysql-connector-python |
| UI       | CLI (Command Line) |

---

##  Project Structure

**

