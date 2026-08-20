#25.	Create a dictionary containing student names and marks. Develop a program to:
#	•	Add a student 
#	•	Update marks 
#	•	Delete a student 
#	•	Search for a student 
#	•	Display all students 
#	•	Find the highest marks 
#	•	Calculate the average

students = {
    "Yash": 89,
    "Prithvi": 92,
    "Harsh": 78,
    "Ankit": 95,
    "Trisha": 88
}

# Add a student
students["Akash"] = 90
print("Added Akash with marks 90.")

# Update marks
students["Yash"] = 91
print("Updated Yash's marks to 91.")

# Delete a student
if "Harsh" in students:
    del students["Harsh"]
    print("Deleted Harsh.")

# Search for a student
search_name = "Prithvi"
if search_name in students:
    print(f"Found {search_name} with marks: {students[search_name]}")
else:
    print(f"{search_name} not found.")

# Display all students
print("\nAll Students:")
for name, marks in students.items():
    print(f"{name}: {marks}")

# Find the highest marks
highest_student = max(students, key=students.get)
print(f"\nHighest marks: {students[highest_student]} (by {highest_student})")

# Calculate average
avg_marks = sum(students.values()) / len(students)
print(f"Average marks: {avg_marks:.2f}")
