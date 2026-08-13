#22.	Create tuples containing:
#	•	Employee ID 
#	•	Name 
#	•	Salary 
#Display all employee information.

emp1 = (101, "Yash Joshi", 85000)
emp2 = (102, "Prithvi Sutar", 65000)
emp3 = (103, "Harsh Sutar", 45000)

employees = (emp1, emp2, emp3)

print("Employee Information:")
for emp in employees:
    print(f"ID: {emp[0]}, Name: {emp[1]}, Salary: ₹{emp[2]}")
