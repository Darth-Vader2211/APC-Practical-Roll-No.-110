input_file = open("hello.txt", "r")
output_file = open("uppercase.txt", "w")

for line in input_file:
    output_file.write(line.upper())

input_file.close()
output_file.close()

print("File converted to uppercase.")