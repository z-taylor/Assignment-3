# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Assignment3A.py
num = int(input("Enter a positive number: "))
if num > 0:
    current_number = 0
    for column in range(num):
        for row in range(column + 1):
            current_number += 1
            print(current_number, end=" ")
        print("")
else:
    print("Invalid number")