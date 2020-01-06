def common_cities(my_cities, friend_cities):
    my_cities = list(my_cities)
    friend_cities = list(friend_cities)
    common_cities = list(set(my_cities).intersection(friend_cities))
    print(common_cities)


my_cities = input("Enter a list of the cities you have visited: ").split(",")
friend_cities = input("Enter a list of the cities your friend has visited: ").split(",")
common_list = common_cities(sorted(my_cities), sorted(friend_cities))