
#start at 40
#print all the even numbers counting down to 0

x = 40
while not x == 0:
    print(x)
    x -= 2

#print the sequence:
# 0
# 1
# 2
# repeated 5 times

p = 0
while p<5:
    print(0)
    print(1)
    print(2)
    p+=1


# ask for an input word until
# the input word starts with "A"

w = "Not a word that starts with A"
while not (w[0] == "a" or w[0] == "A"):
    w = input("Enter a word: ")