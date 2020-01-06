def get_list():
    ''' Returns a list of strings input by a user. '''

    a_list = input('Enter a list separated with commas: ').split(',')
    return a_list


def make_sublists(a_list):
    ''' Returns a list of all the sublists of a_list '''
    length = len(a_list)
    sub_lists = [[]]
    for i in range(0, length):
        for j in range(i, length):
            a_slice = a_list[i:j + 1]
            sub_lists.append(a_slice)
    return sub_lists


# Main program starts here
a_list = get_list()
sub_lists = make_sublists(a_list)
print(sorted(sub_lists))