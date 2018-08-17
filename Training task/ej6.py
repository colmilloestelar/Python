#palindrome ex: ana

a = ['b','c','d','c','b','a']
n = len(a)-1
aux = 0
x=True

print("n mide "+str(n))
while(n>n/2):
    if(a[n] != a[aux]):
        print("No palindrome")
        x=False
        n=0
    else:
        n-=1
        aux+=1
if(x):
    print("Si palindrome")
