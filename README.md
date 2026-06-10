# Library Management System

A menu-driven Library Management System developed using **Python** and **SQLite**. This project helps manage books, authors, members, book issues, returns, and reports.

## Features

* Add and View Authors
* Add and View Books
* Search Books by Title
* Register and View Members
* Issue Books
* Return Books
* Automatic Book Quantity Management
* Overdue Books Report
* Fine Calculation (₹5 per day after 30 days)
* Most Borrowed Books Report
* Active Members Report

## Technologies Used

* Python
* SQLite3
* SQL Queries
* Foreign Keys
* JOIN Operations

## Database Tables

### Authors

* author_id
* author_name

### Books

* book_id
* title
* author_id
* quantity

### Members

* member_id
* member_name
* phone

### Book Issues

* issue_id
* book_id
* member_id
* issue_date
* return_date

## Project Structure

library_management_system/

├── database.py

├── author.py

├── book.py

├── member.py

├── issue.py

├── reports.py

├── main.py

└── library.db

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Sridhar-manukonda23/Library-Management-System.git
   ```

2. Navigate to the project folder:

   ```bash
   cd Library-Management-System
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Sample Functionalities

* Manage authors and books
* Register library members
* Issue and return books
* Track available book quantities
* Generate reports and fines

## Learning Outcomes

* Python Programming
* SQLite Database Management
* CRUD Operations
* Foreign Key Relationships
* SQL JOIN Queries
* Menu-Driven Application Development

## Author

Sridhar Manukonda

GitHub: https://github.com/Sridhar-manukonda23
