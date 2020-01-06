def get_price_for_product(product_name):
    prices = {
        'egg': 0.25,
        'milk': 0.75,
        'bread': 3.5,
        'beef': 25.50,
        'tomatoes': 0.15,
        'lettuce': 2,
        'apple': 0.40
    }

    return prices[product_name]

# your code goes here...

def file_open(filename):
    try:
        with open(filename, "r") as my_data:
            data = []
            for line in my_data:
                my_line = line.replace("\n", "").split(",")
                data.append(my_line)
        return data
    except FileNotFoundError:
        quit()

def list_to_dict(data):
    my_dict = {}
    for x in range(len(data)):
        person = data[x][0]
        product = data[x][1]
        units = float(data[x][2])

        prices = get_price_for_product(product)
        cost = float(prices) * units
        if person not in my_dict:
            my_dict[person] = [cost]
        else:
            if cost not in my_dict:
                my_dict[person] += [cost]

    print(my_dict)
    print("{} spent {}$".format(person, cost))



def main():
    filename = "file.txt"
    data = file_open(filename)
    list_to_dict(data)


main()
