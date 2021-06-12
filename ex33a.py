#This is completely correct per SD #4

def ex33a():
    i = 0
    stop = int(input("Choose a number to stop with: "))
    add_on = int(input("What do we increase by? "))
    print()

    numbers = []
    while i < stop:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += add_on
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("\nThe numbers: ")

    for num in numbers:
        print(num)
    return num

print("We will now run the test f(x)")

ex33a()
