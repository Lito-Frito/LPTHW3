from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read()) #print and then .read in that order so you can print whole file

def rewind(f):
    f.seek(0) #seek looks for the place you designated, via number, in the file

def print_a_line(line_count, f):
    print(line_count, f.readline()) #readline returns exactly one line from the file

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1 #the 1 doesn't tell Python where to start. it's only 1 because the programmer is letting you know what line you're on.
#however, has to be a number, strings/letters are interpreted as another variable
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
