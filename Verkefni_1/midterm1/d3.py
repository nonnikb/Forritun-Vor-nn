n = int(input("How many integers? "))
avg = []
for x in range(n):
    inp = int(input("Input an int: "))
    avg.append(inp)

sort = sorted(avg)
cut_list = sort[1:]
math = (sum(cut_list) / len(cut_list))



print("The average is: {:.0f}".format(int(math)))

#123,876,456,888,960
#11,12,48,77,95,46,2