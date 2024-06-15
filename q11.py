#Write a python program that calculates the sum of the digits of a given 
#number.

number = input("Enter a number: ")
sum_of_digits = 0
for digit in number:
    if digit.isdigit():
        sum_of_digits += int(digit)
print("The sum of the digits of {} is {}.".format(number, sum_of_digits))
