turn = 0


def dimension_of_board():
    dimension = int(input("Input dimension of the board: "))
    if dimension >= 3:
        board = make_board(dimension)
        print_board(board)
        return board, dimension


def print_board(board):
    for row in board:
        line = ''
        for numbers in row:
            line += '{:>6}'.format(numbers)
        print(line)


def make_board(dimension):
    board = []
    numbers = []
    spots = dimension * dimension
    number = 0
    while number < spots:
        number += 1
        numbers.append(number)
        if number % dimension == 0:
            board.append(numbers)
            numbers = []
    return board


def play(board, turn):
    turn += 1
    if turn % 2 != 0:
        position = int(input("X position: "))
        player = 'X'
    else:
        position = int(input("O position: "))
        player = 'O'
    validposition(position, board, player)
    return board, player, turn


def validposition(position, board, player):
    for m in range(0, len(board)):
        row = board[m]
        for n in range(0, len(row)):
            number = row[n]
            if number == position:
                del row[n:n + 1]
                row.insert(n, player)
                del board[m:m + 1]
                board.insert(m, row)
                return board
    print("Illegal move!")
    play(board, turn)


def is_winner(board, player, dimension):
    winner_line = winner_list(dimension, player)
    if diagonal_down(board, winner_line):
        return True
    if diagonal_up(board, winner_line, dimension):
        return True
    if vertical(board, winner_line):
        return True
    if horizontal(board, winner_line, dimension):
        return True


def diagonal_down(board, winner_line):
    diagonal = []
    diagonal.append(board[0][0])
    place = 1
    for j in range(1, dimension):
        diagonal.append(board[j][place])
        place += 1
    if diagonal == winner_line:
        return True


def diagonal_up(board, winner_line, dimension):
    diagonal = []
    diagonal.append(board[0][dimension - 1])
    place = dimension - 2
    for j in range(1, dimension):
        diagonal.append(board[j][place])
        place -= 1
    if diagonal == winner_line:
        return True


def vertical(board, winner_line):
    for line in board:
        if line == winner_line:
            return True


def horizontal(board, winner_line, dimension):
    for line in range(0, dimension):
        horizontal = []
        for row in range(0, dimension):
            horizontal.append(board[row][line])
        if horizontal == winner_line:
            return True
        line += 1


def winner_list(dimension, player):
    the_list = []
    while 0 < dimension:
        the_list.append(player)
        dimension -= 1
    return the_list


def is_draw(board):
    for line in board:
        for number in line:
            number = str(number)
            if number in 'OX':
                continue
            else:
                return False
    return True


board, dimension = dimension_of_board()
not_done = True
while not_done:
    board, player, turn = play(board, turn)
    print_board(board)
    if is_winner(board, player, dimension):
        print("Winner is: " + player)
        break
    elif is_draw(board):
        print("Draw!")
        break