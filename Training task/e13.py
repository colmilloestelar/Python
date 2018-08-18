#fibo

def fibo(n):
    a=0
    b=1
    aux=1

    while(n>0):
        print("r: "+str(aux))
        aux = a+b
        a = b
        b = aux
        n-=1

x = int(input("How many numbers you wanna generate from fibonacci"))
fibo(x)


