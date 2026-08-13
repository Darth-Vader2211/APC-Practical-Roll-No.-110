#25.	Represent the friends of two users using sets. Find:
#	•	Mutual friends 
#	•	Friends unique to User 1 
#	•	Friends unique to User 2 
#	•	Total unique friends

user1_friends = {"Prithvi", "Harsh", "Ankit", "Trisha"}
user2_friends = {"Harsh", "Ankit", "Akash", "Atharv"}

mutual_friends = user1_friends & user2_friends
unique_user1 = user1_friends - user2_friends
unique_user2 = user2_friends - user1_friends
total_unique = user1_friends | user2_friends

print("User 1 (Yash) Friends:", user1_friends)
print("User 2 Friends:", user2_friends)
print("\nMutual friends:", mutual_friends)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total unique friends:", total_unique)
