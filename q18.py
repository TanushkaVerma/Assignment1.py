#Write a python program that checks if two strings are anagrams of each 
#other. 

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")
