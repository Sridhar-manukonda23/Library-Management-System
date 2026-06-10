import sqlite3
from datetime import datetime

def overdue_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT issue_id, book_id, member_id, issue_date
        FROM book_issues
        WHERE return_date IS NULL
    """)

    records = cursor.fetchall()

    print("\n--- Overdue Books ---")

    found = False

    for record in records:
        issue_id, book_id, member_id, issue_date = record

        issue_date = datetime.strptime(issue_date, "%Y-%m-%d")
        days = (datetime.today() - issue_date).days

        if days > 30:
            print(record)
            found = True

    if not found:
        print("No overdue books.")

    conn.close()


def calculate_fine():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    issue_id = int(input("Enter Issue ID: "))

    cursor.execute("""
        SELECT issue_date
        FROM book_issues
        WHERE issue_id=? AND return_date IS NULL
    """, (issue_id,))

    record = cursor.fetchone()

    if not record:
        print("Issue record not found!")
        conn.close()
        return

    issue_date = datetime.strptime(record[0], "%Y-%m-%d")
    days = (datetime.today() - issue_date).days

    if days > 30:
        fine = (days - 30) * 5
    else:
        fine = 0

    print("Fine Amount: ₹", fine)

    conn.close()

def most_borrowed_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT books.title,
               COUNT(book_issues.book_id) AS total_issues
        FROM book_issues
        JOIN books
        ON books.book_id = book_issues.book_id
        GROUP BY books.book_id
        ORDER BY total_issues DESC
    """)

    records = cursor.fetchall()

    print("\n--- Most Borrowed Books ---")

    for record in records:
        print(record)

    conn.close()

def active_members():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT members.member_id,
                        members.member_name
        FROM members
        JOIN book_issues
        ON members.member_id = book_issues.member_id
        WHERE book_issues.return_date IS NULL
    """)

    records = cursor.fetchall()

    print("\n--- Active Members ---")

    for record in records:
        print(record)

    conn.close()
