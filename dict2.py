#2.	Create a dictionary containing employee information and display the value associated with a specified key.
employee = {
    "id": 101,
    "name": "Yash Joshi",
    "department": "Business Analytics",
    "salary": 5000000
}

key = input("Enter the key to display its value: ")
if key in employee:
    print(f"{key}: {employee[key]}")
else:
    print("Key not found.")