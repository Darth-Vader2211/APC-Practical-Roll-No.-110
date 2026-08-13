#7.	Create a tuple of employee IDs and find the index of a given ID.

emp_ids = (101, 102, 103, 104, 105)
search_id = int(input("Enter employee ID to find its index: "))

if search_id in emp_ids:
    idx = emp_ids.index(search_id)
    print(f"Employee ID {search_id} is at index {idx}.")
else:
    print("Employee ID not found.")
