books = {}


def add_book(book_id, name):
    books[book_id] = {
        "name": name,
        "available": True
    }


def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued")
    else:
        print("Book not available")


def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned")


def search_book(name):
    for book in books.values():
        if book["name"].lower() == name.lower():
            print("Book found:", book["name"])


def display_available():
    for book in books.values():
        if book["available"]:
            print(book["name"])


add_book(1, "Python")
add_book(2, "Java")
add_book(3, "C++")

issue_book(1)
return_book(1)

search_book("Python")

print("Available Books:")
display_available()