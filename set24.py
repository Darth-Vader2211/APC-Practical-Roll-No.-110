#24.	Store visitor IDs from two different days in separate sets. Determine:
#	•	Unique visitors across both days 
#	•	Returning visitors 
#	•	Visitors who came only on the first day 
#	•	Visitors who came only on the second day
#	•	Create sets representing products belonging to different categories. Find products that belong to both categories.

day1_visitors = {101, 102, 103, 104, 105}
day2_visitors = {103, 105, 106, 107}

unique_visitors = day1_visitors | day2_visitors
returning_visitors = day1_visitors & day2_visitors
only_day1 = day1_visitors - day2_visitors
only_day2 = day2_visitors - day1_visitors

print("Day 1 Visitors:", day1_visitors)
print("Day 2 Visitors:", day2_visitors)
print("\nUnique visitors across both days:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors only on Day 1:", only_day1)
print("Visitors only on Day 2:", only_day2)

# Product categories analysis
electronics = {"Laptop", "Mobile Phone", "Smart Watch", "Headphones"}
gadgets = {"Mobile Phone", "Smart Watch", "Drone", "VR Headset"}
both_categories = electronics & gadgets

print("\nElectronics category:", electronics)
print("Gadgets category:", gadgets)
print("Products belonging to both categories:", both_categories)
