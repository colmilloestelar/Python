import random

play = True
a = random.randint(1, 9)

while(play):

    x = int(input("Try to guess the secret number"))

    if(a == x):
        end = input("WOW you do it, write y for try another or another key for leave")
        if (end != "y"):
            play = False
        else:
            a = random.randint(1,9)
    else:
        end = input("You fail but you can try again,"
                    " just write y or another key for leave")
        if(end !="y"):
            play = False
