formatter = "{} {} {} {}" #takes a variable; makes a var a string; has string take in 4 vars

print(formatter.format(1, 2 , 3, 4)) #you use '.format' to tell python to take this string/f(x) and run it w/w.e vars you want
print(formatter.format("one", 'two', 'three', 'four')) #e.g. run formatter with these 4 new strings
print(formatter.format(True, False, False, True)) #e.g. run formatter with these logic statements
print(formatter.format(formatter, formatter, formatter, formatter)) #e.g run formatter with itself 4x
print(formatter.format(
    "\n\nCode fragment downloaded: \n\n///\n  [Function: True]\n     {{Yosa.Buson(print):}}",
    "\n     {{Light of the moon}}",
    "\n     {{Moves west, flowers' shadows}}",
    "\n     {{Creep Eastward}}\n  [Function: True]\n///"
)) #e.g. run formatter with these 4 strings that start on new lines
