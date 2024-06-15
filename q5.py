#Write a program that takes a string input from the user and writes it to a 
#text file. 

input_string = input("Enter a string: ")
file_path = "output.txt"
with open(file_path, 'w') as file:
    file.write(input_string)
print(f'String "{input_string}" has been written to {file_path}.')
