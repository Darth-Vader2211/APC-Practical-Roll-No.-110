#28.	Create a dictionary containing names and phone numbers.
#Implement:
#	•	Add contact 
#	•	Search contact 
#	•	Update contact 
#	•	Delete contact 
#	•	Display all contacts

contacts = {
    "Yash": "9876543210",
    "Prithvi": "9123456789",
    "Harsh": "9988776655",
    "Ankit": "9555443322"
}

# Add contact
contacts["Trisha"] = "9444332211"

# Search contact
search_name = "Prithvi"
if search_name in contacts:
    print(f"{search_name}'s Phone: {contacts[search_name]}")

# Update contact
contacts["Yash"] = "9000000000"

# Delete contact
if "Harsh" in contacts:
    del contacts["Harsh"]

# Display all contacts
print("\nAll Contacts:")
for name, phone in contacts.items():
    print(f"{name}: {phone}")
