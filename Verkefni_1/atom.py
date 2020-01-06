i = int(input("Give me an int >=0: "))

bin = []

if i % 2 == 0:
    bin.append(0)
elif i % 2 == 1:
    bin.append(1)

print("the binary of {} is {}".format(i, ''.join(bin)))