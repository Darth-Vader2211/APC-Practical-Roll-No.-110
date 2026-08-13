#23.	Create a set containing available books and another set containing requested books. Determine which requested books are available.

available_books = {"Python Programming", "Data Structures", "Web Development", "Database Systems", "Operating Systems"}
requested_books = {"Python Programming", "Machine Learning", "Web Development", "Computer Networks"}

available_requested = available_books & requested_books

print("Available books:", available_books)
print("Requested books:", requested_books)
print("Requested books that are available:", available_requested)
