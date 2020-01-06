
def int_list(x):
    y = []
    for i in x:
        y.append(int(i))
    return y

def sum_no_three(my_list):
    sum_of_threes = 0
    for i in my_list:
        a = i
        while True:
            if a == 3 or a < 0:
                break
            elif a != 3:
                a -= 10
        if a != 3:
            sum_of_threes += i
    return sum_of_threes

# DO NOT change any code below this comment
str_inp = input("Enter a list of comma-separated integers: ").split(",")
print(f"The original list: {str_inp}")
int_inp = int_list(str_inp)
print(f"The list as integers: {int_inp}")
print(f"The result of sum_no_three: {sum_no_three(int_inp)}")