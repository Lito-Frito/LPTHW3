from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

input()
print ("Now closing the file...")
txt.close()
print("Closed!")

input()
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

input()
print("Now closing your file...")
txt_again.close()
print("Closed!")
