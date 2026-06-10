from database import create_tables

from author import add_author, view_authors
from book import add_book, view_books, search_book
from member import add_member, view_members
from issue import issue_book, return_book
from reports import (
    overdue_books,
    calculate_fine,
    most_borrowed_books,
    active_members
)

create_tables()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Author")
    print("2. View Authors")
    print("3. Add Book")
    print("4. View Books")
    print("5. Search Book")
    print("6. Register Member")
    print("7. View Members")
    print("8. Issue Book")
    print("9. Return Book")
    print("10. Overdue Books")
    print("11. Calculate Fine")
    print("12. Most Borrowed Books")
    print("13. Active Members")
    print("14. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_author()

    elif choice == "2":
        view_authors()

    elif choice == "3":
        add_book()

    elif choice == "4":
        view_books()

    elif choice == "5":
        search_book()

    elif choice == "6":
        add_member()

    elif choice == "7":
        view_members()

    elif choice == "8":
        issue_book()

    elif choice == "9":
        return_book()

    elif choice == "10":
        overdue_books()

    elif choice == "11":
        calculate_fine()

    elif choice == "12":
        most_borrowed_books()

    elif choice == "13":
        active_members()

    elif choice == "14":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")