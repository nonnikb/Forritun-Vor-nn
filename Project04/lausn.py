def get_chessplayers(filename):
    try:
        with open(filename, "r") as chess_players:
            my_dict = ()
            for line in chess_players:
                print(line, end="")
                """my_line = line.replace("[\n", "").split(";")
                key = find_key(my_line[1])
                value = find_value(my_line)
                my_dict[key] = value"""
            return my_dict
    except FileNotFoundError:
        print("File not found")
        pass
def main():
    filename = "chess-top-100.csv"
    chess_players = get_chessplayers(filename)
    #print(line)
main()