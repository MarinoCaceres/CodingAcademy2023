#word length loop

i = input("Give me a word: ")
x = 0

while x < len(i):
    print(i[x])
    x += 1

#list length loop

i = ("Tree",True,4,"Car")
x = 0

while x < len(i):
    print(i[x])
    x += 1

#sentence string loop

i = ("My ","name ","is ","Marino.")
x = 0
sentence = ""

while x < len(i):
    sentence += i[x]
    x += 1
print(sentence)

#number list addition loop

i = (1,23,1984,2020,-3.5,87)
x = 0
sum = 0

while x < len(i):
    sum += i[x]
    x += 1
print(sum)
print("Average:",sum/len(i))

#biggest number on a list search loop

i = (1,2,3,87,23,11)
x = 0
biggest = i[0]

while x < len(i):    
    if biggest < i[x]:
        biggest = i[x]
    x += 1
print(biggest)

#smallest number on a list search loop

i = (1,2,3,87,23,11)
x = 0
biggest = i[0]

while x < len(i):    
    if biggest > i[x]:
        biggest = i[x]
    x += 1
print(biggest)