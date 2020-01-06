
def get_move():
    title = []
    print("1. Input a movie title")
    print("2. Give up")
    choice = input("Pick an action: ")
    if choice == '2':
        return choice
    elif choice == '1':
        movie = input("Enter a movie title: ").lower()
        title.append(movie)
        if title[0:3] == ['t','h','e']:
            title.pop(0)
            title.pop(1)
            title.pop(2)
            return title
    else:
        print("Invalid input, what would you like to do?")
        get_move()


def play():
    while True:
        movie = []
        new_movie = []
        print("Player 1, it is your turn!")
        player_1 = get_move()
        for x in player_1:
            if player_1 == '2':
                print("\nPlayer 2 wins!")
                quit()
            else:
                movie.append(x)

        print("Player 2, it is your turn!")
        player_2 = get_move()
        for x in player_2:
            if player_2 == '2':
                print("\nPlayer 1 wins!")
                quit()
            else:
                new_movie.append(x)

        if movie[0:3] == ['t','h','e']:
            movie.pop(0)
            movie.pop(1)
            movie.pop(2)
        elif new_movie[0:3] == ['t','h','e']:
            new_movie.pop(0)
            new_movie.pop(1)
            new_movie.pop(2)

        if movie[-1] != new_movie[0]:
            print("Invalid input, what would you like to do?")
            get_move()

def main():
        while True:
            play()






main()