p = input("What would you like your pyramid to be made out of: ")
n = int(input("Please insert a number: "))

for i in range(n):
    print(p * (i+1))

for i in range(n-1,0,-1):
    print(p * i)