#24.	Store temperatures of seven days in a tuple and determine:
#	•	Maximum temperature 
#	•	Minimum temperature 
#	•	Average temperature

temperatures = (32.5, 34.0, 31.8, 35.2, 33.6, 30.4, 36.1)

max_temp = max(temperatures)
min_temp = min(temperatures)
avg_temp = sum(temperatures) / len(temperatures)

print("Weekly Temperatures (°C):", temperatures)
print(f"Maximum temperature: {max_temp}°C")
print(f"Minimum temperature: {min_temp}°C")
print(f"Average temperature: {avg_temp:.2f}°C")
