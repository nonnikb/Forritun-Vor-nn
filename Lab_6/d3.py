def count_letters():
    my_str = input("Enter a string: ").lower()
    my_tupl = ()
    for x in my_str:
        if x.isalpha():
            count = my_str.count(x)
            my_tupl += ((x, count),)
    print(my_tupl)

count_letters()