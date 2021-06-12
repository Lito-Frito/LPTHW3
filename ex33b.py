#This is completely right!!!!! This is for SD #5
def ex33b():
    i = 0
    start = int(input("Choose a number to start with> "))
    stop = int(input("Choose a number to stop with: "))
    add_on = int(input("What do we increase by? "))
    print()

    numbers = []
    for i in range(start, stop, add_on):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("\nThe numbers: ")

    for num in numbers:
        print(num)
    return num

print("We will now run the test f(x)")

ex33b()
