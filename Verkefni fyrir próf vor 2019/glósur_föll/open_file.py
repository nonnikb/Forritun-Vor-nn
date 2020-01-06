def open_file(filename):  #open file and add to list
    try:
        with open(filename, "r") as my_data:
            data = []
            for line in my_data:
                my_line = line.replace("\n", "").split(",")
                data.append(my_line)
        return data
    except FileNotFoundError:
        quit()