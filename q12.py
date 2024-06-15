#Write a python program that calculates the sum of the digits of a given 
#number. 

num = input("Enter a number: ")
sum_of_digits = 0
for digit in num:
    sum_of_digits += int(digit)
print(f"The sum of digits in {num} is: {sum_of_digits}")
