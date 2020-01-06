import random

# Constants
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
QUIT = 'q'

def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)


def get_move():
    move = input("Enter weapon (r/p/s): ")
    while move not in ['r', 'p', 's', 'q']:
        move = input("Enter weapon (r/p/s): ")
    return move

#def get_ai_move():
#    aimove = ai_moves[randint(0, 2)]
#    return aimove

def who_wins(move, tie, user, computer):
    ai_moves = [ROCK, PAPER, SCISSORS]
    aimove = random.choice(ai_moves)
    print("Computer weapon: {}".format(aimove))
    print("User weapon: {}".format(move))
    if move == aimove:
        tie += 1
        print("Tie!")
    elif move == ROCK:
        if aimove == PAPER:
            computer += 1
            print("Computer wins!")
        else:
            user += 1
            print("User wins!")
    elif move == PAPER:
        if aimove == SCISSORS:
            computer += 1
            print("Computer wins!")
        else:
            user += 1
            print("User wins!")
    elif move == SCISSORS:
        if aimove == ROCK:
            computer += 1
            print("Computer wins!")
        else:
            user += 1
            print("User wins!")
    elif move == QUIT:
        print("User won: {}".format(user))
        print("Computer won: {}".format(computer))
        print("Tie: {}".format(tie))
        quit()

    return tie, user, computer


def main():
    tie = 0
    user = 0
    computer = 0
    random_seed()
    while True:
        move = get_move()
        if move == QUIT:
            print("User won: {}".format(user))
            print("Computer won: {}".format(computer))
            print("Tie: {}".format(tie))
            quit()
        tie, user, computer = who_wins(move, tie, user, computer)


main()