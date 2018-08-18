def reverse(l):
    n = len(l)
    c = []

    while (n > 0):
        c.append(l[n-1])
        n-=1
    print(c)

a = []

a = input("Write some words to reverse it \n")

b = a.split(" ")
print( "\n ------ ** -------")
print (b)

reverse(b)




