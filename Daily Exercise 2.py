#Carson Cave - Python Daily Exercise 2 - 2-16-2018


# 2. Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. Clue input()

name = input("What is your name: ")
age = input("What is your age: ")

print ("Your name is " + name + " and you will turn 100 in " + (100 - int(age)) + " years")