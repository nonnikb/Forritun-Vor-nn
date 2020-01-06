def collect_list(listi, num):
    while num > 0:
        try:
            num = input('Enter an integer: ')
            num = int(num)
            my_list.append(int(num))
            num -= 1
        except ValueError:
            print('Please, integers only')

    return my_list


def split_list(listi):
    posnum = [n for n in my_list if n >= 0 and n % 2 == 0]
    posnum1 = list(posnum)
    oddnum = [i for i in my_list if i not in posnum1]

    return list(posnum), list(oddnum)

n = int(input("Enter the list length: "))
my_list = []

collect_list(my_list, n)

print(f"List, after splitting is: {split_list(my_list)}")