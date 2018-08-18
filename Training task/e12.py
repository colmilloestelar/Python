a = [5, 10, 15, 20, 25]

def ext(l):
    n = len(l)
    if(n >= 1):
        print(str(l[0])+" - "+str(l[n-1]))
    else:
        print("List too small")

ext(a)
