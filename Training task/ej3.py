a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,1]
x = []

z = int(input("Numero max"))

for element in a:
    if(element<z):
        print (element)
        x.append(element)

print(x)

