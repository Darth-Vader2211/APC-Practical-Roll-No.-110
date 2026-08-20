#7.	Create a dictionary containing student records and find the total number of key-value pairs.

student_records = {
    "Yash": {"roll_number": 12345, "department": "Computer Science", "marks": 85},
    "Prithvi": {"roll_number": 67890, "department": "Electrical Engineering", "marks": 90},
    "Harsh": {"roll_number":  54321, "department": "Mechanical Engineering", "marks": 78},
    "Ankit": {"roll_number": 98765, "department": "Civil Engineering", "marks": 92},
    "Trisha": {"roll_number": 24680, "department": "Business Analytics", "marks": 88}
}
total_pairs = len(student_records)
print("Total Number of Key-value pairs in the dictionary is:",total_pairs)