b = ("#")*10
x = 0
stair = ""

while x < len(b):
    stair += b[x*-1]
    x += 1
    print(stair)