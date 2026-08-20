#30.	Create a tuple containing patient records:
#	•	Patient ID 
#	•	Name 
#	•	Age 
#	•	Blood Group 
#Perform the following operations:
#	•	Display all records 
#	•	Search for a patient by ID 
#	•	Count the total number of patients 
#	•	Display patients with a specific blood group 

patients = (
    (101, "Yash Joshi", 21, "O+"),
    (102, "Prithvi Sutar", 22, "A+"),
    (103, "Harsh Sutar", 20, "O+"),
    (104, "Ankit Sharma", 23, "B+"),
    (105, "Trisha Sharma", 21, "A+")
)

# Display all records
print("All Patient Records:")
for p in patients:
    print(f"ID: {p[0]}, Name: {p[1]}, Age: {p[2]}, Blood Group: {p[3]}")

# Search for a patient by ID
search_id = 102
print(f"\nSearching for Patient ID {search_id}:")
found = False
for p in patients:
    if p[0] == search_id:
        print(f"Found: ID: {p[0]}, Name: {p[1]}, Age: {p[2]}, Blood Group: {p[3]}")
        found = True
        break
if not found:
    print("Patient not found.")

# Count total number of patients
total_patients = len(patients)
print(f"\nTotal number of patients: {total_patients}")

# Display patients with a specific blood group
target_bg = "O+"
print(f"\nPatients with Blood Group '{target_bg}':")
for p in patients:
    if p[3] == target_bg:
        print(f"ID: {p[0]}, Name: {p[1]}")
