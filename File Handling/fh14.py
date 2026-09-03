with open("hello.txt", 'r') as file:
    content = file.read()
    search_word = input("Enter the word to search: ")
    replace_word = input("Enyter word to replace search word with: ")
    updated_content = content.replace(search_word, replace_word)
    
with open("hello.txt", 'w') as file:
    file.write(updated_content)
    print("Word replaced successfully in hello.txt.")
    print("Updated content of hello.txt:")
    print(updated_content)