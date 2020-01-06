def open_file():
    '''
    Prompts the user for a file name.
    Returns the corresponding file stream or None if file not found
    '''
    try:
        file_name = input("Enter file name: ")
        file_stream = open(file_name)
        return file_stream
    except FileNotFoundError:
        return None

def split_file(open_file):
    for x in open_file:
        new = x.split("")


def main():
    file_stream = open_file()
    for x in file_stream:
        print(x)


main()
