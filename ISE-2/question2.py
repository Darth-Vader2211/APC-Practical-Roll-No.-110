import pandas as pd

df = pd.read_csv("employee.csv")
print("Employee Data:")
print(df)

sal = int(input("Enter minimum salary:"))
exp = int(input("Enter minimum Experience:"))
dept = input("Enter department:")

filtered_data = [(df["Salary"] >= sal) &
                 (df["Experience"] >= exp) & 
                 (df["Department"] == dept)
                 ]

print("\nFiltered Data :")
print(filtered_data)

