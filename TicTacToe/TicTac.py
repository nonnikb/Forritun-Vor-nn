def valid_size():
    while True:
        try:
            size = int(input("Input dimension of the board: "))
            if size > 2:
                return size
        except ValueError:
            continue


def make_board(size):
    board = []
    counter = 1
    for i in range(size):
        temp_list = []
        for x in range(size):
            temp_list.append(counter)
            counter += 1
        board.append(temp_list)
    return board

def print_board(board):
    for li in board:
        for x in li:
            print('{:>5}'.format(x), end="")
        print("")

def make_move(board, choice, player):
    for ix, x in enumerate(board):
        for tn, n in enumerate(x):
            if n == choice:
                board[ix][tn] = player
                return board


def victory(board):
    my_check_list = []
    counter = 0
    for x in range(len(board)):
        check = my_check_list.append(board[x][counter])
        counter += 1
        if counter >= len(board):
            if same(my_check_list):
                return True
    return False


def same(my_list):
    my_num = my_list[0]
    counter = 0
    while counter <= len(my_list):
        for x in my_list:
            if x == my_num:
                return True
    return False



def main():
    size = valid_size()
    board = make_board(size)
    moves = 1
    max_moves = size**2
    while True:
        for current_player in ["X", "O"]:
            print_board(board)
            choice = int(input(current_player + " position: "))
            board = make_move(board, choice, current_player)
            if moves == max_moves:
                print_board(board)
                print("Draw!")
                quit()
            if victory(board):
                print_board(board)
                print("Winner is: {}".format(current_player))
                quit()
            moves += 1

main()