def unique_list(lis):
    lis = set(lis)
    lis = list(lis)
    lis.sort()
    return lis


lis = input("Enter a comma separated list: ").split(",")

print(unique_list(lis))