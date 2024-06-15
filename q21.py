#Write a python program that counts the occurrences of a specific element 
#in a list. 

input_list = input("Enter a list of elements separated by spaces: ")
elements = input_list.split()
element_to_count = input("Enter the element to count: ")
count = elements.count(element_to_count)
print("The element '{}' occurs {} times in the list.".format(element_to_count, count))
