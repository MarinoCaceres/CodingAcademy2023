print("I am a Simple Equations Calculator")
op = input("What operation do you want to do (+,-,*,/,**): ")

while op != "+" and op != "-" and op != "*" and op != "x" and op != "/" and op != "q" and op != "Q" and op != "h" and op != "H" and op != "**" and op != "^":
        print("That is not a valid operation")
        op = input("Please insert a valid operation: ")

while not op == "q" and not op == "Q":
    
    while op == "h" or op == "H":
        print("Valid Operations:")
        print("+: Addition (x+y)")
        print("-: Substration (x-y)")
        print("*|x: Multiplication (x*y)")
        print("/: Division (x/y)")
        print("**|^: Exponent (x**y)")
        print("Q|q: Quit")
        print("H|h: Help")
        op = input("Please insert your input: ")

    while op == "+" or op == "-" or op == "*" or op == "x" or op == "/" or op == "**" or op == "^":
        
        if op == "+" or op == "-" or op == "*" or op == "x" or op == "/":
            x = float(input("First Number: "))
            y = float(input("Second Number: "))

        if op == "**" or op == "^":
            x = float(input("Base Number: "))
            y = float(input("Exponent: "))

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

        if op == "**" or op == "^":
            print ("Result:",x**y)

        if op != "q" and op != "Q":
            op = input("What operation do you want to do (+,-,*,/,**): ")
            
            while op == "h" or op == "H":
                print("Valid Operations:")
                print("+: Addition (x+y)")
                print("-: Substration (x-y)")
                print("*|x: Multiplication (x*y)")
                print("/: Division (x/y)")
                print("**|^: Exponent (x**y)")
                print("Q|q: Quit")
                print("H|h: Help")
                op = input("Please insert your input: ")

            while op != "+" and op != "-" and op != "*" and op != "x" and op != "/" and op != "q" and op != "Q" and op != "h" and op != "H" and op != "**" and op != "^":
                print("That is not a valid operation")
                op = input("Please insert a valid operation: ")