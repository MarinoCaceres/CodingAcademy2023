
l = [2,3,70,-5,4]
sum = 0

for num in l:
    if num % 2 == 0:
        sum += num
    if num % 2 != 0:
        sum -= num

print (sum)