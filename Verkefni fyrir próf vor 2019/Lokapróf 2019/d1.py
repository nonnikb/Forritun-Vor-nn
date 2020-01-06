
def file_open(filename):
    try:
        with open(filename, "r") as my_data:
            data = []
            for line in my_data:
                my_line = line.replace("\n", "").split("-")
                data.append(my_line)
        return data
    except FileNotFoundError:
        quit()

def list_to_dict(data):
    my_dict = {}
    for x in range(len(data)):
        size = data[x][0]
        directory = data[x][1]

        if directory not in my_dict:
            my_dict[directory] = [size]

    print("Printing all directories")
    for x in sorted(my_dict):
            print("{} is {} bytes".format(directory[x], size[x]))

    """biggest = 0
    for size, directory in my_dict.items():
        if len(size) > biggest:
            biggest = int(size)
            big_dir = directory
    print("{}{}".format(biggest, big_dir))"""


def get_avg(data):
    avg_list = []
    for x in range(len(data)):
        avg_size = float(data[x][0])
        avg_list.append(avg_size)
    print("The average directory size is: {:.2f}".format(sum(avg_list) / len(avg_list)))

"""def get_biggest(data):
    size = 0
    print(data)"""


def main():
    filename = input("Enter name of file: ")
    filestream = file_open(filename)
    list_to_dict(filestream)
    get_avg(filestream)
    #get_biggest(filestream)

main()