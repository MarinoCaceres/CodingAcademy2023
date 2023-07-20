
#adding evens, substracting odds

l = [2,3,70,-5,4]
sum = 0

for num in l:
    if num % 2 == 0:
        sum += num
    if num % 2 != 0:
        sum -= num

print("The result is:",sum)

#generate a new list with no duplicates

l = ["Mike","Bob","John","John","Bob","Eric","Mike","Adam"]

u = []

for name in l:
    if not name in u:
        u += [name]

print("The unique list of names is:",u)

#find and print the words that contain at least 5 different letters

l = ["adjustment","bottom","character","church","detect","evolve","governor","honor","indeed","insurance"]

#for each word in the list:
#	figure out how many different (non-duplicate) letters it has
#	if that's 5 or more print the word

print("The words that have more than 5 unique letters are:")

for word in l:
    result = []
    for letter in word:
        if not letter in result:
            result += [letter]
    
    letter_count = len(result)
    if letter_count >= 5:
        print("-",word)