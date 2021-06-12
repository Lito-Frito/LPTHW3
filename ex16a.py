from sys import argv

script, filename = argv

print(f"We're going to erase {filename}." + "\nIf you don't want that, hit CTRL-C (^C)." + "\nIf you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
#note, you do NOT need to write truncate() because .write() will delete it for you and replace with desired input

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + '\n' + line2 + '\n' + line3)

print("And finally, we close it.")
target.close()
