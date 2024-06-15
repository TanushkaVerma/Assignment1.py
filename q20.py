#Write a python program that takes a list of numbers and returns their sum.

input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [float(num) for num in input_numbers.split()]
sum_numbers = sum(numbers)
print("Sum of the numbers:", sum_numbers)
