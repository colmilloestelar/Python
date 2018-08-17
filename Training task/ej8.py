#rock paper scissors
play=True
p1 = 0
p2 = 0

while (play):
    p1 = input("player 1 chose your item r, p or s")

    if(p1 !='r' and p1 !='p' and p1 !='s' ):
        print("wrong option you lose p2 win")
        break
    else:
        p2 = input("player 2 chose your item r, p or s")

    if (p2 != 'r' and p2 != 'p' and p2 != 's'):
        print("wrong option you lose p1 win")
        break
    else:
        if(p1==p2):
            print("DRAW")
        elif(p1 == 'r' and p2 == 's'):
            print("P1 win")
        elif(p1 == 'p' and p2 == 'r'):
            print("P1 WIN")
        elif(p1 == 's' and p2 == 'p'):
            print("P1 WIN")
        else:
            print("P2 win")

    more = input("play more? y = yes another = no")
    if(more != 'y'):
        play = False



