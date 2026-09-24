def load_books():
    file = open("books.txt", "r")
    books = []

    for line in file:
        book_id, title, author, status = line.strip().split(",")
        books.append([book_id, title, author, status])

    file.close()
    return books


def save_books(books):
    file = open("books.txt", "w")

    for book in books:
        file.write(",".join(book) + "\n")

    file.close()


def add_book(books):
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    books.append([book_id, title, author, "Available"])
    save_books(books)

    print("Book added successfully.")


def search_book(books):
    book_id = input("Enter Book ID to search: ")

    for book in books:
        if book[0] == book_id:
            print("Book Found:")
            print("ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("Status:", book[3])
            return

    print("Book not found.")


def issue_book(books):
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book[0] == book_id:
            if book[3] == "Available":
                book[3] = "Issued"
                save_books(books)
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
            return

    print("Book not found.")


def return_book(books):
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book[0] == book_id:
            book[3] = "Available"
            save_books(books)
            print("Book returned successfully.")
            return

    print("Book not found.")


def display_available(books):
    print("\nAvailable Books:")

    for book in books:
        if book[3] == "Available":
            print(book[0], book[1], book[2])


books = load_books()

while True:

    print("\n--- Book Management System ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book(books)

    elif choice == "2":
        search_book(books)

    elif choice == "3":
        issue_book(books)

    elif choice == "4":
        return_book(books)

    elif choice == "5":
        display_available(books)

    elif choice == "6":
        break

    else:
        print("Invalid choice.")