#5.	Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.

students = {"Yash", "Prithvi", "Harsh", "Ankit", "Trisha"}
name = input("Enter a student name to check: ")

if name in students:
    print(f"{name} exists in the set.")
else:
    print(f"{name} does not exist in the set.")
