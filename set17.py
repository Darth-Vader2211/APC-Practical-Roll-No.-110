#17.	Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.

yash_subjects = {"Python", "Mathematics", "Statistics", "Data Analytics"}
prithvi_subjects = {"Python", "Physics", "Statistics", "Electronics"}

common_subjects = yash_subjects.intersection(prithvi_subjects)

print("Yash's subjects:", yash_subjects)
print("Prithvi's subjects:", prithvi_subjects)
print("Subjects studied by both students:", common_subjects)
