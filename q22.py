#Write a python program that returns the minimum and maximum values 
#in a list of numbers.

list1 = input("Enter a list of elements separated by spaces: ")
elements = [ int(num) for num in list1.split()]
maximum = max(elements)
minimum = min(elements)
print (maximum)
print(minimum)
