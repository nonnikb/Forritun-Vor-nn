def list_to_tuple(a_list):
    try:
        return tuple([int(x) for x in a_list])
    except ValueError:
        print("Error. Please enter only integers.")
        return tuple()

a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)