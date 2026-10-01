"""6.	Create a dictionary containing:
Student_ID
Name
Department
Total_Classes
Classes_Attended
Create a DataFrame and calculate:
Attendance Percentage = (Classes_Attended / Total_Classes) × 100
Display students whose attendance is below 75%.
"""
import pandas as pd
student_data = {
    "Student _ID": [101, 102, 103, 104, 105],
    "Name": ["Yash", "Arjun", "Aditi", "Trisha", "Shreyas"],
    "Department": ["CSE", "ASE", "IT", "ENTC", "CIVIL"],
    "Total_Classes": [46, 55, 30, 42, 40],
    "Classes_Attended": [25, 50, 35, 29, 40]
}
df = pd.DataFrame(student_data)
print("Student DataFrame : \n",df)

df["Attendance_Percentage"] = df["Classes_Attended"] / df["Total_Classes"] * 100
print("\n---------- Attendance of each Student in % ---------- \n")
print(df["Attendance_Percentage"])

print("\nStudents who have attendance below 75% are :")
print(df["Attendance_Percentage"] < 75 )

