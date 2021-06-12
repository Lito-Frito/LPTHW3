from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")
in_file = open(from_file).read()

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w').write(in_file)

print("Alright, all done.")
