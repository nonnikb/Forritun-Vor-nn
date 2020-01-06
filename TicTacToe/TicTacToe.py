def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9] #stærð á borðinu
    end = False
    win_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) # 3 í röð til að vinna

    def size(): #prentar út borðið
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print() #auka bil

    def check_board(): #athuga hvort það sé winner eða draw
        count = 0
        for a in win_combo:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Winner is: X")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Winner is : O")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("Draw")
                return True

    def choose_number(): #numer a board
        while True:
            a = input()
            try:
                a = int(a)
                a -= 1
                if a in range(0, 9): #ef numer er a borði setja x/o þar
                    return a
                else:
                    print("Number not on board") # ef numer of hátt eða lágt
                    continue
            except ValueError:
                print("Please input a number on the board") #ef látin er inn bókstafur
                continue

    def player_1(): #nr1. velja stað á borði
        n = choose_number()
        if board[n] == "X":
            print("You can't go there. Try again")
            player_1()
        else:
            board[n] = "X"

    def player_2(): #nr.2 velja stað á borði
        n = choose_number()
        if  board[n] == "O":
            print("You can't go there. Try again")
            player_2()
        else:
            board[n] = "O"




    while not end: #þegar spilið er ennþá í gangi
        size()
        end = check_board() #athuga hvort það sé winner
        if end is True:
            break
        print("Player 1 choose where to place X: ")
        player_1()
        print()
        size()
        end = check_board()
        if end is True:
            break
        print("Player 2 choose where to place O: ")
        player_2()
        print()

tic_tac_toe()