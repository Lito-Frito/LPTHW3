i = 0
numbers = []

while i < 4:
    print(f"At the top i is {i}")
    numbers.append(i)

    #  Increments i by 1 each iteration
    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
