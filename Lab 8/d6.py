def create_flyers_dict(filename):
    flyers = {}
    content = open(filename, "r")
    for line in content:
        name, country = line.split()
        if name not in flyers:
            flyers[name] = {country}
        else:
            flyers[name].add(country)
    content.close()
    return flyers

def print_dict(flyers):
    for name in sorted(flyers.keys()):
        print("{}: ".format(name))
        for country in sorted(flyers[name]):
            print("\t{}".format(country))

def visited_most_countries(flyers):
    countries_count = 0
    for flyer, countries in flyers.items():
        if len(countries) > countries_count:
            countries_count = len(countries)
            max_flyer = flyer

    return max_flyer

def print_most_visited(flyer, number_of_countries):
    print()
    print("{} has been to {} countries".format(flyer, number_of_countries))

def main():
    flyers = create_flyers_dict("flights.txt")
    print_dict(flyers)
    flyer = visited_most_countries(flyers)
    print_most_visited(flyer, len(flyers[flyer]))

main()