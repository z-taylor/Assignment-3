# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Assignment3B.py
run = True
hasTreasure = False
while run:
    move = input("You are in a room. Choose a direction to move in (north, south, east, west): ").lower()
    match move:
        case move if move=="north":
            action = input("You move north and find a river. What will you do? (swim/build a raft): ").lower()
            if action == "swim":
                print("You swim across the river and find a hidden treasure.")
                hasTreasure = True
                run = True if input("Would you like to continue playing? (yes/no): ").lower() == "yes" else False
            elif action == "build a raft":
                print("You ride down the river and reach a waterfall, and you jump off the raft at the last moment. You walk back up the river and end back up at the room you started at.")
                run = True if input("Would you like to continue playing? (yes/no): ").lower() == "yes" else False
            else:
                print("Invalid action")
        case move if move=="south":
            action = input("You move south and discover a dense forest. What will you do?(climb a tree/walk deeper): ").lower()
            if action=="climb a tree":
                print("You see an abandoned cabin far away and you go to explore it.")
                run = True if input("Would you like to continue playing? (yes/no): ").lower() == "yes" else False
            elif action=="walk deeper":
                print("You walk too deep into the forest and get lost. Game over!")
                run = False
            else:
                print("Invalid action")
        case move if move=="east":
            action = input("You move east and encounter a mountain. What will you do? (climb the mountain/go around it): ").lower()
            if action == "climb the mountain":
                print("You climb the mountain and find an abandoned castle.")
                run = True if input("Would you like to continue playing? (yes/no): ").lower() == "yes" else False
            elif action == "go around it":
                print("You walk around the mountain and find your way back to civilization. You win!")
                run = False
            else:
                print("Invalid action")
        case move if move=="west":
            action = input("You find a cave. What do you do?(Explore the cave/walk past it): ")
            if action == "explore the cave":
                print("You enter the cave and find a sleeping dragon.")
                run = True if input("Would you like to continue playing? (yes/no): ").lower() == "yes" else False
            elif action == "walk past it":
                if hasTreasure == True:
                    print("You walk past the cave and come across a gang of pirates who steal the treasure you found earlier.")
                    hasTreasure = False
                elif hasTreasure == False:
                    print("You walk past the cave and come across a gang of pirates, but they leave you alone because you do not have anything valuable on you.")
                run = True if input("Would you like to continue playing? (yes/no): ").lower() == "yes" else False
        case _:
            print("Invalid movement input")
print("Thank you for playing!")