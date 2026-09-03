with open("hello.txt", "r") as file:
    content = file.read()
    alphabets = "abcdefghijklmnopqurstuvwxyzABCDEFGHIJKLMNOPQURSTUVWXYZ"
    digits = "0123456789"
    spaces = " "
    special_characters = "!@#$%^&*()_+-=`~[]{}/.''""|;:<>?"
    alphabet_count = 0
    digit_count = 0
    space_count = 0
    special_character_count = 0
    
    for c in content:
        if c in alphabets:
            alphabet_count += 1
        elif c in digits:
            digit_count += 1
        elif c in spaces:
            space_count += 1
        elif c in special_characters:
            special_character_count += 1
    print("Total number of alphabets in hello.txt:", alphabet_count)
    print("Total number of digits in hello.txt:", digit_count)
    print("Total number of spaces in hello.txt:", space_count)
    print("Total number of special characters in hello.txt:", special_character_count)
    