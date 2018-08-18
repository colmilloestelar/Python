#cow and bulls game
import random

play = True
x = str(random.randint(1,9999))
x2 = int(x)
l = len(x)


if (l == 3):
    x = "0" + x
elif(l == 2):
    x = "00" + x
elif(l == 1):
    x = "000" + x

print (x[0],x[1],x[2],x[3])

while(play):
    cow = 0
    bull = 0

    user = input("write a 4 digit number 0001 to 9999 \n")

    if(x == user):
        print("4 cows you win")
        break
    else:
        if(x[0] == user[0]):
            cow+=1
        else:
            bull+=1
        if(x[1] == user[1]):
            cow+=1
        else:
            bull+=1
        if(x[2] == user[2]):
            cow+=1
        else:
            bull+=1
        if(x[3] == user[3]):
            cow+=1
        else:
            bull+=1
    print("You have \n cows:" + str(cow) +"\n Bulls:"+ str(bull))




