from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
x = input("Add a 4th var: ")
print(f"You're 4th var is {x}. Meh, kinda lame :/",)
