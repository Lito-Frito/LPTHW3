print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # this printed the string 10 times, duh

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print( end1 + end2 + end3 + end4 + end5 + end6, end=' ')
#the comma is needed so you can correctly use 'end='. Without comma, error.
#What end does is tell Python to print the next string in-line while adding
#Whatever you typed in-between end=____. Cool stuff.

#Second P3 uses "end= 'string stuff'" to say, "Print the first string, then add
#'string stuff' at the end of the string, then print the second string in-line
print(end7 + end8 + end9 + end10 + end11 + end12)
print("test", end='...')
print('ys')
print('yes')
#See? 'test' and '...' are printed in-line with 'ys', while 'yes' is not.
