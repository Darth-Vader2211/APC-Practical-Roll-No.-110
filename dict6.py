#6.	Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.
employee_dictionary = {
    101: "Yash Joshi",
    102: "Prithvi Sutar",
    103: "Harsh Sutar",
    104: "Ankit Sharma",
    105: "Trisha Sharma"
}
employee_id = int(input("Enter the employee ID to check: "))
if employee_id in employee_dictionary:
    print(f"Employee found: {employee_dictionary[employee_id]}")
else:
    print("Employee not found.")