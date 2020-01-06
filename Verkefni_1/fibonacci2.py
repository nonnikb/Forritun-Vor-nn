num = int(input("Input a number: "))
f1 = 0
f2 = 1
for x in range(num):
    print(f1,end=' ')
    fn = f1 + f2
    f1 = f2
    f2 = fn

