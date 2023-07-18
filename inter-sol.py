print("I can fin the intersection between two linear lines")
print("y(1) = ax + b")
print("y(2) = cx + d")

a = float(input("What is a: "))
b = float(input("What is b: "))
c = float(input("What is c: "))
d = float(input("What is d: "))

if a == c:
    print("There is no intersection between these two lines")
else:
    x = (d-b)/(a-c)
    y = a*x+b

print("The intersection point is:", (x,y))