#22.	Create two sets representing technical skills of two employees. Find:
#	•	Common skills 
#	•	Skills unique to Employee 1 
#	•	Skills unique to Employee 2 
#	•	All available skills

emp1_skills = {"Python", "SQL", "Machine Learning", "Tableau"}
emp2_skills = {"Java", "SQL", "PowerBI", "Python"}

common_skills = emp1_skills & emp2_skills
unique_emp1 = emp1_skills - emp2_skills
unique_emp2 = emp2_skills - emp1_skills
all_skills = emp1_skills | emp2_skills

print("Employee 1 (Yash Joshi) skills:", emp1_skills)
print("Employee 2 (Prithvi Sutar) skills:", emp2_skills)
print("\nCommon skills:", common_skills)
print("Skills unique to Employee 1:", unique_emp1)
print("Skills unique to Employee 2:", unique_emp2)
print("All available skills:", all_skills)
