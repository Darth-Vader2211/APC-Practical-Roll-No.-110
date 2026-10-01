"""4.	Create a dictionary containing:
Patient ID
Patient Name
Age
Disease
Medical Charges
Convert the dictionary into a DataFrame and:
1.	Display patients above 60 years. 
2.	Find the average medical charge. 
3.	Find the maximum medical charge. 
4.	Display patients whose medical charges are greater than ₹50,000. 
"""
import pandas as pd
dict = {
    "Patient_ID":[101, 102, 103, 104, 105],
    "Patient_Name" :["Arjun","Aditi","Trisha","Yash","Shreyas"],
    "Age":[82, 65, 24, 20, 71],
    "Disease":["Fever","Cold","Cough","Headache","Stomach Pain"],
    "Medical_Charges":[200000, 150000, 30000, 25000, 51000]
}

df = pd.DataFrame(dict)
print("-----Patient Data-----")
print(df)

print("Patients above 60 years :\n")
print(df[df["Age"] > 60])

avg_medical_charge = df["Medical_Charges"].mean()
max_medical_charge = df["Medical_Charges"].max()

print(f"Average Medical Charge: ₹{avg_medical_charge}")
print(f"Maximum Medical Charge: ₹{max_medical_charge}")

print("Patients with Medical Charges greater than ₹50,000:")
print(df[df["Medical_Charges"] > 50000])