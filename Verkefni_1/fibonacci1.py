f1 = 0
f2 = 1
count = 0

num = int(input("Input a number: "))

if num == 1:
    print("The {}. number in the fibonacci sequence is: {}".format(num, f2))
    quit()
else:
    while count < num:

        fn = f1 + f2
        f1 = f2
        f2 = fn
        count+=1

print("The {}. number in the fibonacci sequence is: {}".format(num, f1))