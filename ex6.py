types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." #5

print(x)
print(y)

print(f"I said: {x}") #1
print(f"I also said: '{y}'") #2

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}" #joke_evaluation is a string that takes in a variable. #3

print(joke_evaluation.format(hilarious)) #print joke_evaluation with it taking the variable 'hilarious' #4

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
