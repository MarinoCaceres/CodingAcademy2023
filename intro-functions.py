
# Counting up from 1 to n

def countTo(n):
    i = 1
    while i < n+1:
        print(i)
        i += 1
    pass

countTo(int(input("Insert a number: ")))

# Returning an added value to print

def add7(a):
    return 7 + a
    pass

print(add7(6))
print(add7(-3))
print(add7(23))
