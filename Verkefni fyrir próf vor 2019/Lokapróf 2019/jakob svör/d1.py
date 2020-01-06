def open_file(file_name):
    try:
        my_dict = {}
        content = open(file_name, "r")
        for line in content:
            size, name = line.strip().split("-")
            size = int(size)
            name = name.strip()
            if name not in my_dict:
                my_dict[name] = (size)
        content.close()
        return my_dict
    except FileNotFoundError:
        return None

def print_info(dict_):
    print("Printing all directories")
    for name in sorted(dict_.keys()):
        print("{} is {} bytes".format(name, dict_[name]))
    print()

def print_biggest(dict_):
    big = 0
    for name, size in sorted(dict_.items()):
        if size > big:
            big = size
            biggest_directory = name

    print("The biggest directory is: {}".format(biggest_directory))


def print_average(dict_):
    sum_of = 0
    n_numbers = 0
    average_size = 0
    for size in dict_.values():
        sum_of += size
        n_numbers += 1
    average_size = sum_of/n_numbers

    print("The average directory size is: {:.2f} bytes.".format(average_size))


def main():
    # 1. lesa inn skrá
    file_name = input("Enter name of file: ")
    file_stream = open_file(file_name)
    if file_stream:
        print_info(file_stream)
        print_biggest(file_stream)
        print_average(file_stream)
    else:
        print("File not found!")




main()