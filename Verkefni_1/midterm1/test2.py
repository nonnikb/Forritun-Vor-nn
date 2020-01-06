def open_file(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found")

filename = input("Enter filename: ")
open_file(filename)