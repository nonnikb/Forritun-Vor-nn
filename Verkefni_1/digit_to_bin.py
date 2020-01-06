digit = int(input("Give me an integer >= 0: "))
original = digit
bin = ''
while digit:
    if digit == 0:
        bin += 0
    elif digit & 1 == 1:
        bin = "1" + bin
    else:
        bin = "0" + bin
    digit //= 2

print("The binary of {} is {}".format(original, bin))