import sqlite3

def add_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    title = input("Enter book title: ")
    author_id = int(input("Enter author id: "))
    quantity = int(input("Enter quantity: "))

    cursor.execute(
        "INSERT INTO books (title, author_id, quantity) VALUES (?, ?, ?)",
        (title, author_id, quantity)
    )

    conn.commit()
    conn.close()

    print("Book added successfully!")

def view_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT books.book_id,
               books.title,
               authors.author_name,
               books.quantity
        FROM books
        JOIN authors
        ON books.author_id = authors.author_id
    """)

    books = cursor.fetchall()

    print("\n--- Books List ---")

    for book in books:
        print(book)

    conn.close()

def search_book():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    title = input("Enter book title: ")

    cursor.execute("""
        SELECT books.book_id,
               books.title,
               authors.author_name,
               books.quantity
        FROM books
        JOIN authors
        ON books.author_id = authors.author_id
        WHERE books.title LIKE ?
    """, ('%' + title + '%',))

    books = cursor.fetchall()

    if books:
        print("\n--- Search Results ---")
        for book in books:
            print(book)
    else:
        print("Book not found!")

    conn.close()