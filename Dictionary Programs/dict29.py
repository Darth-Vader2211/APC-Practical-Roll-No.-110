#29.	Create a dictionary containing book IDs and book names.
#Implement:
#	•	Add a book 
#	•	Search a book 
#	•	Remove a book 
#	•	Display all books 
#	•	Count total books

books = {
    101: "Python Programming",
    102: "Data Structures",
    103: "Web Development"
}

# Add a book
books[104] = "Machine Learning"

# Search a book
search_id = 102
if search_id in books:
    print(f"Book ID {search_id}: {books[search_id]}")

# Remove a book
if 103 in books:
    del books[103]

# Display all books
print("\nAll Books:")
for b_id, title in books.items():
    print(f"ID: {b_id}, Title: {title}")

# Count total books
print(f"\nTotal books: {len(books)}")
