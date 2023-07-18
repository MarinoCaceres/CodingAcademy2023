x = "y"
while x == "y":
    start = int(input("Please insert a starting number: "))
    steps = 0
    current = start

    print("Starting Number: ",start)

    while current != 1:
        if current % 2 == 0:
            current /= 2
        else:
            current = 3 * current + 1
        
        steps += 1
        print("Step",steps,":",current)
        
        if current == 1:
            print("<It took a total of",steps,"steps in order for",start,"to reach 1>")
            x = input("Do you wish to try with another number? (y/n) ")