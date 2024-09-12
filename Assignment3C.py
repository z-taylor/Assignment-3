# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Assignment3C.py
for num in range (25):
    num+=1
    print(f"{num}({"E" if (num%2)==0 else "O"})", end="")
    print("") if num%5==0 else print(end="")