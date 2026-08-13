#25.	Store runs scored in 10 matches and calculate:
#	•	Total runs 
#	•	Highest score 
#	•	Lowest score 
#	•	Average score 

runs = (45, 82, 104, 12, 67, 89, 0, 53, 91, 76)

total_runs = sum(runs)
highest_score = max(runs)
lowest_score = min(runs)
avg_score = total_runs / len(runs)

print("Runs in 10 matches:", runs)
print("Total runs:", total_runs)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print(f"Average score: {avg_score:.2f}")
