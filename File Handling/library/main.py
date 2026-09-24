from books.details import book_details
from books.search import search_book

from members.details import member_details
from members.registration import register_member

from transactions.issue import issue_book
from transactions.return_book import return_book


print("----- LIBRARY APPLICATION -----")

print("\nBOOK INFORMATION")
book_details(101, "Python Programming", "John Smith")

print("\nBOOK SEARCH")
search_book("Python Programming")

print("\nMEMBER INFORMATION")
member_details(1, "Amit")

print("\nMEMBER REGISTRATION")
register_member("Amit")

print("\nTRANSACTION")
issue_book("Python Programming", "Amit")
return_book("Python Programming")