"""2.	Create a dictionary containing:
Employee ID
Employee Name
Department
Salary
Experience
Convert it into a Pandas DataFrame and:
1.	Display employees with salary greater than ₹50,000. 
2.	Find the average salary. 
3.	Find the highest salary. 
4.	Find the employee with the highest experience.
"""
import pandas as pd
dict1 = {
    "Employee_ID": [201, 202, 203, 204, 205],
    "Employee_Name":["Yash", "Arjun", "Shreyas", "Trisha", "Aditi"],
    "Department":["HR", "Finance", "IT", "Marketing", "Sales"],
    "Salary":[45000, 55000, 60000, 48000, 52000],
    "Experience":[3, 5, 8, 2, 6]
}
df = pd.DataFrame(dict1)
print("Employee Data:")
print(df)

print("\nEmployees with sSalary greater than 50000:")
print(df["Salary"]>50000)

Avg_Sal = df["Salary"].mean()
Highest_Sal = df["Salary"].max()
Highest_Exp = df["Experience"].max()

print("\nAverage Salary :",Avg_Sal)
print("\nHighest Salary :",Highest_Sal)
print("\nHighest Experience :",Highest_Exp)

