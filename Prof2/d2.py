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


def open_file():
    #filename = input("Enter filename: ")
    fh = open("file.txt", "r")
    print(fh.readline())
    return fh.readline()

def to_dict(open_file):
    the_dict = {}
    my_str = open_file.split(",")
    the_dict["Name"] = my_str[0]
    the_dict["item"] = my_str[1]
    the_dict["units"] = my_str[2]
    print(open_file)
    print(my_str)
    print(the_dict)
    return the_dict



open_file()
to_dict(open_file())
