#divisor
l = []

div = int(input("Give a number for get divisor"))
div2 = div/2

while (div2>1):
    if(div % div2 == 0):
        l.append(int(div2))
    div2-=1

print(l)


