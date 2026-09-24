from patient.details import patient_details
from patient.registration import register_patient

from doctor.details import doctor_details
from doctor.appointment import book_appointment

from billing.bill import calculate_bill
from billing.payment import make_payment

from medical_records.records import add_record
from medical_records.history import view_history


print("----- HOSPITAL MANAGEMENT SYSTEM -----")

print("\nPATIENT INFORMATION")
patient_details("Amit", 20, "Fever")
register_patient("Amit")

print("\nDOCTOR INFORMATION")
doctor_details("Dr. Patil", "General Medicine")
book_appointment("Amit", "Dr. Patil")

print("\nMEDICAL RECORD")
add_record("Amit", "Fever")
view_history("Amit")

print("\nBILLING")
bill = calculate_bill(500, 1000)
make_payment(bill)