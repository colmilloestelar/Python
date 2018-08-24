#guess number computer
l = []
tip=""
first = 0
last = 100


x = input("Lets play, think a number from 0 to 100 and i will try to find it :D \n"
              "just type y for play or another key for leave \n")
while(x=='y'):
    r = int((first + last) / 2)

    z = input("Is your number"+str(r)+'? \n type y for yes or any key for no')

    if(z == 'y'):
        print("Nice")
        break
    else:
        l.append(r)

    tip = input("Is your number bigger (type b) or smaller (tip s) ?")

    #if number is smaller r/2
    if(tip == 's'):
        last = r
    else:
        first = r
print("I say all of this: ")
print(l)






