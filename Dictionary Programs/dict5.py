#5.	Create a dictionary of cities and their populations. Remove a specified city from the dictionary.
cities_population = {
    "New York": 8419600,
    "Los Angeles": 3980400,
    "Chicago": 2716000,
    "Houston": 2328000,
    "Phoenix": 1690000
}
city_to_remove = input("Enter the name of the city to remove: ")
if city_to_remove in cities_population:
    del cities_population[city_to_remove]
    print("Entered has been removed from the dictionary.")
else:
    print("City not found in the dictionary.")