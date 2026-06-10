import sqlite3

def add_author():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    author_name = input("Enter author name: ")

    cursor.execute(
        "INSERT INTO authors (author_name) VALUES (?)",
        (author_name,)
    )

    conn.commit()
    conn.close()

    print("Author added successfully!")

def view_authors():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()

    print("\n--- Authors List ---")
    for author in authors:
        print(author)

    conn.close()