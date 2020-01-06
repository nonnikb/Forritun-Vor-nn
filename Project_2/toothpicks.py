def computerMove(numPicksLeft, human_number):
    cmpM = 0
    if numPicksLeft > 4:
        cmpM = 4 - human_number
    elif numPicksLeft == 4:
        cmpM = 3
    elif numPicksLeft == 3:
        cmpM = 2
    elif numPicksLeft == 2:
        cmpM = 1
    elif numPicksLeft == 1:
        print("You won!")
    return cmpM


def default():
    toothpicks = 23
    while toothpicks > 0:
        picks = int(input("There are {} toothpicks left. Pick 1, 2 or 3 toothpicks: ".format(str(toothpicks))))
        if 1 >= picks >= 3:
            print("Invalid input! Please pick again.")
            default()
        elif picks == 0:
            print("Invalid input! Please pick again.")
            default()
        else:
            toothpicks -= picks
        cp = computerMove(toothpicks, picks)
        print("I pick {} toothpicks".format(str(cp)))
        if toothpicks == 0:
            print('I won!')
        toothpicks -= cp


default()



