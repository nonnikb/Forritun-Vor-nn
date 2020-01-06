def invalid_input():
    print("1. Input a movie title")
    print("2. Give up")
    decision = int(input("Pick an action: "))
    return decision



def print_menu(counter):
    if counter % 2 == 0:
        print("Player 2, it is your turn!")
    else:
        print("Player 1, it is your turn!")
    print("1. Input a movie title")
    print("2. Give up")
    decision = int(input("Pick an action: "))
    return decision

def edit_movie(new_movie):
    if new_movie[0:4] == "the ":
        new_movie = new_movie[4:]
    return new_movie


def play_game(movie,counter):
    if movie == "":
        new_movie = input("Enter a movie title: ")
        return new_movie
    else:
        new_movie = input("Enter a movie title: ")
        print()
        new_movie = edit_movie(new_movie)
        while new_movie[0] != movie[-1]:
            print("Invalid input, what would you like to do? ")
            decision = invalid_input()
            if decision == 1:
                play_game(movie,counter)
            else:
                print("Player {} wins!".format(counter))
        return new_movie



def main():
    decision = 1
    counter = 0
    last_movie = ""
    while decision ==1:
        counter += 1
        decision = print_menu(counter)
        if decision == 1:
            new_movie = play_game(last_movie,counter)
        last_movie = edit_movie(new_movie)
    if decision == 2:
        print(("\nPlayer {} wins!".format(counter)))
    else:
        invalid_input()


main()
