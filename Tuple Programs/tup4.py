#4.	Create a tuple of colors. Check whether a given color exists in the tuple

colors = ("Red", "Green", "Blue", "Yellow", "Purple")
search_color = input("Enter a color to search: ")

if search_color in colors:
    print(f"{search_color} exists in the tuple.")
else:
    print(f"{search_color} does not exist in the tuple.")
