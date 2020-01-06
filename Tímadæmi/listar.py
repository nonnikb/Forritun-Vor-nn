numbers = []

numbers2 = list()

numbers3 = [1, 5, 4, 8, 7]

items = [1, 2, 6.5, "babar", True, [1, 2, 3]]

items.append("melon")

items.insert(0, "Sitrona")
#print(items[3])
#print(items)

def add_to_list(value, my_list):
    my_list.append(value)

my_list = [1,2,3,4]
add_to_list(385, my_list)

print(my_list)