import sqlite3

def add_member():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    member_name = input("Enter member name: ")
    phone = input("Enter phone number: ")

    cursor.execute(
        "INSERT INTO members (member_name, phone) VALUES (?, ?)",
        (member_name, phone)
    )

    conn.commit()
    conn.close()

    print("Member registered successfully!")

def view_members():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()

    print("\n--- Members List ---")

    for member in members:
        print(member)

    conn.close()