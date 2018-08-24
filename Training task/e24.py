def print_hor():
    print(" ---" * board_size)

def print_ver():
    print("|   " * (board_size+1))

board_size = int(input("Enter size of game board"))

for i in range(board_size):
    print_hor()
    print_ver()
print_hor()