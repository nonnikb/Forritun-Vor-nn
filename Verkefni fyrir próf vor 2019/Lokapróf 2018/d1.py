def file_open(filename):
    with open(filename, "r") as my_data:
        list_of_data = []
        for line in my_data:
            my_line = line.replace("\n","").split(" ")
            list_of_data.append(my_line)
        return list_of_data

def list_to_dict(my_data):
    flyers_dict = {}
    for x in range(len(my_data)):
        person = my_data[x][0]
        country = my_data[x][1]

        if person not in flyers_dict:
            flyers_dict[person] = [country]
        else:
            if country not in flyers_dict[person]:
                flyers_dict[person].append(country)

    for name in sorted(flyers_dict):
        print("{}:".format(name))
        for country in sorted(flyers_dict[name]):
            print("\t{:>5}".format(country))

    country_count = 0
    for person, country in flyers_dict.items():
        if len(country) > country_count:
            country_count = len(country)
            max_flyer = person


    print("{} has been to {} countries".format(max_flyer, country_count))

def main():
    filename = "flights.txt"
    data = file_open(filename)
    list_to_dict(data)

main()
