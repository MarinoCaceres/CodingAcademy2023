op = input("What operation do you want to do (+,-,*,/): ")

while op == "+" or op == "-" or op == "*" or op == "x" or op == "/":
    
    x = float(input("First Number: "))
    y = float(input("Second Number: "))

    if op == "+":
        print("Result:",x+y)

    if op == "-":
        print("Result:",x-y)

    if op == "*" or op =="x":
        print("Result:",x*y)

    if op == "/": 
        if y == 0:
            print("Cannot divide by 0")
        else:
            print("Result:",x/y)

print("That is not a valid operation")