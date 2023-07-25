# 1) lesser_of_two_evens: Write a function that returns the lesser of two given numbers if
# both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            print(a)
        else: 
            print(b)
    
    elif a > b:
        print(a)
    else: 
        print(b)

lesser_of_two_evens(2,4) #returns 2
lesser_of_two_evens(2,5) #returns 5

# 2) makes_twenty: Given two integers, return True if the sum of the integers is 20 or if one
# of the integers is 20. If not, return False

def makes_twenty(a,b):
    if a == 20 or b == 20:
        return True
    if a + b == 20:
        return True
    else:
        return False
    


print(makes_twenty(20,10)) #True
print(makes_twenty(10,10)) #True
print(makes_twenty(2,3)) #False

# 3) master_yoda: Given a sentence, return a sentence with the words reversed

def master_yoda(sentence):
    l = sentence.split(" ")
    yoda = l[::-1]
    return " ".join(yoda)

print((master_yoda("We are ready"))) #should return "ready are We"

# 4) blackjack: Given a list of integers between 1 and 11, if their sum is less than or
# equal to 21, return their sum. If their sum exceeds 21 and there's an eleven,
# reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds
# 21, return "BUST"

def blackjack(cards):
    sum = 0
    for num in cards:
        sum += num

    if sum <= 21:
        return sum

    if sum > 21 and 11 in cards:
        return sum - 10
    
    if sum > 21:
        return "BUST"


print(blackjack([2,2,5,9])) #returns 18
print(blackjack([4,9,11])) #returns 14
print(blackjack([7,10,10])) #returns "BUST"

# 5) spy_game: Write a function that takes in a list of integers and returns True if it
# contains 007 in order

def spy_game(numbers):
    i = 0
    s = 1
    while i < len(numbers):
        if s == 1:
            if numbers[i] == 0:
                s += 1

        if s == 2:
            if numbers[i] == 0:
                s += 1

        if s == 3:
            if numbers [i] == 7:
                return True
        i += 1   
    return False




print(spy_game([1,2,4,0,0,7,5])) #True
print(spy_game([1,0,2,4,0,5,7])) #True
print(spy_game([1,7,2,0,4,5,0])) #False

# 6) factorial: Write a function that takes an integer n and returns n-factorial.

def factorial(n):
    i = 1
    nf = 1
    while i < n+1:
        nf *= i
        i += 1
    return nf

print(factorial(2)) #returns 2
print(factorial(6)) #returns 720

# 7) The Fibonacci sequence goes 1 1 2 3 5 8 13 21 34 55 89 …
# Each number in the sequence is the sum of the previous two numbers. The rules are:
# fibonacci(0) is 1
# fibonacci(1) is 1
# fibonacci(n) is fibonacci(n-1) + fibonacci(n-2)
# fibonacci: Write a function that computes the nth number in the sequence.

def fibonacci(n):
    l = [1,1]

    for i in range(2,n+1):
        l += {(l[i-1]) + (l[i-2])}

    return l[n]

print(fibonacci(7)) #should print 21

# 8) a) Write a function called makeChange that computes how to make a certain amount of
# money with as few coins of different sizes as possible.

def makeChange(amount):
    coin_values = [25,10,5,1] #quarters, dimes, nickels, and pennies
    coin_counts = [0,0,0,0]
    
    for i in range(len(coin_values)):
        coin_counts[i] = amount // coin_values[i]
        amount = amount % coin_values[i]
        
    return coin_counts

print(makeChange(25)) #should return [1,0,0,0]
print(makeChange(19)) #should return [0,1,1,4]
print(makeChange(83)) #should return [3,0,1,3]

# b) Write a modified version of makeChange that allows the caller to pass in the values of
# the coins that should be used. Each coin is allowed to be worth any positive integer
# amount of money, and there can be any amount of coins. Assume there is always a coin
# worth 1, even when it's not included in the list argument.

def mC(amount,coin_values=[25,10,5,1]): #default coin values
    coin_counts = [0,0,0,0]
    
    for i in range(len(coin_values)):
        coin_counts[i] = amount // coin_values[i]
        amount = amount % coin_values[i]
    
    return coin_counts

print(mC(25)) #should still return [1,0,0,0]
print(mC(25,[7,2])) #should return [3,2,0] – the 0 is for the implicit 1-coin
print(mC(468,[100,10,1])) #should return [4,6,8]