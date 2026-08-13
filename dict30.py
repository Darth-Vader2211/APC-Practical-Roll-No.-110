#30.	Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.

students = {
    "Yash": "Computer Science",
    "Prithvi": "Electrical Engineering",
    "Harsh": "Computer Science",
    "Ankit": "Mechanical Engineering",
    "Trisha": "Electrical Engineering"
}

grouped = {}
for student, dept in students.items():
    if dept not in grouped:
        grouped[dept] = []
    grouped[dept].append(student)

print("Original dictionary:", students)
print("Grouped by department:", grouped)
