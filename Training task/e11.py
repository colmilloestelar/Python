def prime(num):
    isPrime = True
    num2 = (int(num/2))

    while (num2 > 1):
        if(num % num2 == 0):
            print("valor n2 = "+str(num2))
            isPrime = False
            return isPrime
        else:
            num2-=1

    return isPrime

#main:
n = int(input("enter a number to check"))

r = prime(n)

if(r):
    print(str(n)+"is prime")
else:
    print(str(n)+"is not prime")


