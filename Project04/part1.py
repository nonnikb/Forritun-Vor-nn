def open_file(filename):
    try:
        with open(filename, "r") as my_data:
            my_dict = {}
            for line in my_data:
                my_line = line.replace("\n", "").split(";")
                key = find_key(my_line[1])
                value = find_value(my_line)
                my_dict[key] = value
            return my_dict
    except FileNotFoundError:
        print("File not found")
        pass

def find_key(full_name):
    last_name, first_name = full_name.split(",")
    return "{} {}".format(first_name.strip(), last_name.strip())

def find_value(about_chess_player):
    ranking = int(about_chess_player[0].strip())
    country = about_chess_player[2].strip()
    points = int(about_chess_player[3].strip())
    birth_year = int(about_chess_player[4].strip())
    my_list = [ranking, country, points, birth_year]
    return my_list

def dict_by_country(chess_player_dict):
    country_dict = {}
    for key, value in chess_player_dict.items():
        country = value[1]
        if country not in country_dict:
            country_dict[country] = [key]
        else:
            country_dict[country].append(key)
    return country_dict

def print_output(chess_player_dict, country_dict):
    header = "Players by country:"
    print(header)
    print("-"*len(header))
    for key, value in sorted(country_dict.items()):
        average = get_average(chess_player_dict, value)
        print("{} ({}) ({:.1f}):".format(key, len(value), average))
        for x in value:
            print("{:>40}{:>10d}".format(x, chess_player_dict[x][2]))

def get_average(dict, names):
    sum = 0
    for name in names:
        sum += dict[name][2]
    sum_output = sum / len(names)
    return sum_output

def main():
    filename = input("Enter filename: ")
    chess_player_dict = open_file(filename)
    country_dict = dict_by_country(chess_player_dict)
    print_output(chess_player_dict, country_dict)

main()