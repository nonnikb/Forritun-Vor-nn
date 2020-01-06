def count_elements(my_list):
    elements = {}
    for elem in my_list:
        if elem in elements.keys():
            elements[elem] += 1
        else:
            elements[elem] = 1
    return elements

print(count_elements(input("Enter a comma separated list: ").split(",")))