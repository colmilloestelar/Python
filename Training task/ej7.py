a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
c = []

for i in a:
    if (i %2 == 0):
        b.append(i)
    else:
        c.append(i)

print(b)
print(c)