#26.	Create a dictionary containing employee names and salaries. Find:
#	•	Highest salary 
#	•	Lowest salary 
#	•	Average salary 
#	•	Employees earning more than ₹50,000

employees = {
    "Yash Joshi": 85000,
    "Prithvi Sutar": 65000,
    "Harsh Sutar": 45000,
    "Ankit Sharma": 52000,
    "Trisha Sharma": 48000
}

highest_emp = max(employees, key=employees.get)
lowest_emp = min(employees, key=employees.get)
avg_salary = sum(employees.values()) / len(employees)
high_earners = [emp for emp, sal in employees.items() if sal > 50000]

print(f"Highest salary: ₹{employees[highest_emp]} ({highest_emp})")
print(f"Lowest salary: ₹{employees[lowest_emp]} ({lowest_emp})")
print(f"Average salary: ₹{avg_salary:.2f}")
print("Employees earning more than ₹50,000:", high_earners)
