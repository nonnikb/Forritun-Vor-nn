def open_file(filename):
    try:
        with open(filename, "r") as my_data:
            my_list = []
            for line in my_data:
                my_line = line.replace("\n", "").split(",")
                my_list.append(my_line)
            return my_list
    except FileNotFoundError:
        print("File not found")
        quit()




filename = "chess-top-100.csv"

print(open_file(filename))