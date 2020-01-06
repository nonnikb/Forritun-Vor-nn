def to_list(string):
    string_list = []
    string = string.replace(","," ").split(" ")
    for x in string:
        string_list.append(x)
    return string_list

# The main program starts here - DO NOT change it

the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)