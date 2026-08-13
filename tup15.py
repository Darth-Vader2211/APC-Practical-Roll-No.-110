#15.	Create a nested tuple containing student details and display each record.

student_records = (
    (12345, "Yash", "Computer Science", 85),
    (67890, "Prithvi", "Electrical Engineering", 90),
    (54321, "Harsh", "Mechanical Engineering", 78),
    (98765, "Ankit", "Civil Engineering", 92),
    (24680, "Trisha", "Business Analytics", 88)
)

print("Student Records:")
for record in student_records:
    print(f"Roll: {record[0]}, Name: {record[1]}, Dept: {record[2]}, Marks: {record[3]}")
