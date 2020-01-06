MIN = 1
MAX = 10


def first_pos():
    pos = int(input("Enter a position between {} and {}: ".format(MIN, MAX)))
    if 1 <= pos <= 10:
        return pos
    else:
        print("Invalid input")
        first_pos()


def user_move(num):
    RIGHT = "r"
    LEFT = "l"
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    move = input("Enter your choice: ").lower()
    while MIN < num < MAX:
        if move == RIGHT:
            num += 1
            print("New position is {}".format(num))
            user_move(num)
        elif move == LEFT:
            num -= 1
            print("New position is {}". format(num))
            user_move(num)
        else:
            print("New position is {}".format(num))
            quit()

def main():
    num = first_pos()
    user_move(num)

main()

