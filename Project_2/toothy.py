def ai_move(toothpicks_left, user_num):
    ai_num = -1
    if toothpicks_left == 1:
        ai_num = 1
    if 2 <= toothpicks_left <= 4:
        ai_num = toothpicks_left - 1
    if toothpicks_left > 4:
        ai_num = 4 - user_num
    print("I pick  {}  toothpicks".format(ai_num))
    return ai_num


def get_user_num(toothpicks_left):
    user_num = int(input("There are {} toothpicks left.\nPick 1, 2 or 3 toothpicks: ".format(toothpicks)))
    while user_num > toothpicks_left or user_num < 1 or user_num > 3:
        print("Invalid input! Please pick again!")
        user_num = int(input("There are {} toothpicks left.\nPick 1, 2 or 3 toothpicks: ".format(toothpicks)))
    return user_num

toothpicks = 23

while toothpicks > 0:
    user_num = get_user_num(toothpicks)
    toothpicks -= user_num
    if toothpicks == 0:
        print("I pick 0 toothpicks")
        print("I won!")
    else:
        ai_num = ai_move(toothpicks, user_num)
        toothpicks -= ai_num
        if toothpicks == 0:
            print("You won!")