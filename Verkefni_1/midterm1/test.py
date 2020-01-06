n = int(input("How many integers? "))
avg = 0
low = 999999999
for x in range(n):
    inp = int(input("Input an int: "))
    if inp < low:
        low = inp
    avg += inp
without_lowest = avg - low
dividing_num = n - 1
math = without_lowest / dividing_num
print("The average is: {}".format(round(int(math))))

