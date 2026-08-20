#19.	Create two sets:
#	•	Students present in the morning session 
#	•	Students present in the afternoon session 
#	Find:
#	•	Students present in both sessions 
#	•	Students present only in the morning 
#	•	Students present only in the afternoon 
#	•	Students present in at least one session

morning_session = {"Yash", "Prithvi", "Harsh"}
afternoon_session = {"Prithvi", "Ankit", "Trisha"}

both_sessions = morning_session & afternoon_session
only_morning = morning_session - afternoon_session
only_afternoon = afternoon_session - morning_session
at_least_one = morning_session | afternoon_session

print("Morning session:", morning_session)
print("Afternoon session:", afternoon_session)
print("\nStudents present in both sessions:", both_sessions)
print("Students present only in the morning:", only_morning)
print("Students present only in the afternoon:", only_afternoon)
print("Students present in at least one session:", at_least_one)
