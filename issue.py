import sqlite3
from datetime import date

def issue_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    book_id = int(input("Enter Book ID: "))
    member_id = int(input("Enter Member ID: "))

    cursor.execute(
        "SELECT quantity FROM books WHERE book_id=?",
        (book_id,)
    )

    book = cursor.fetchone()

    if book is None:
        print("Book not found!")
        conn.close()
        return

    if book[0] <= 0:
        print("Book not available!")
        conn.close()
        return

    issue_date = date.today().isoformat()

    cursor.execute("""
        INSERT INTO book_issues
        (book_id, member_id, issue_date, return_date)
        VALUES (?, ?, ?, NULL)
    """, (book_id, member_id, issue_date))

    cursor.execute("""
        UPDATE books
        SET quantity = quantity - 1
        WHERE book_id = ?
    """, (book_id,))

    conn.commit()
    conn.close()

    print("Book issued successfully!")

#Return book
def return_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    issue_id = int(input("Enter Issue ID: "))

    cursor.execute("""
        SELECT book_id
        FROM book_issues
        WHERE issue_id=? AND return_date IS NULL
    """, (issue_id,))

    issue = cursor.fetchone()

    if issue is None:
        print("Issue record not found!")
        conn.close()
        return

    book_id = issue[0]
    return_date = date.today().isoformat()

    cursor.execute("""
        UPDATE book_issues
        SET return_date=?
        WHERE issue_id=?
    """, (return_date, issue_id))

    cursor.execute("""
        UPDATE books
        SET quantity = quantity + 1
        WHERE book_id=?
    """, (book_id,))

    conn.commit()
    conn.close()

    print("Book returned successfully!")