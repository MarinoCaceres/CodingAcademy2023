print("I am a Quadratic Equation Solver")
print("ax^2 + bx + c = 0")

a = float(input("What is a: "))
b = float(input("What is b: "))
c = float(input("What is c: "))

if a == 0:
    print("That is not a Quadratic Equation")

else:
    d=(b**2-4*a*c)**(0.5)
    x1=(-b + d)/2*a
    x2=(-b - d)/2*a
    print("The first root is:",x1)
    print("The second root is:",x2)