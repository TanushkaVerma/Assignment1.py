#Write a program that reads data from a CSV file and prints it to the 
#console. 

import csv
file_path = "data.csv"
with open(file_path, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(', '.join(row))
