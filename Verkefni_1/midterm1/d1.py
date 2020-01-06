high_number = int(input("Enter a number: "))
x = 3
y = 5


for i in range(1,high_number+1):
    if i % x == 0 and i % y == 0:
        print("FizzBuzz")
    elif i % x == 0:
        print("Fizz")
    elif i % y == 0:
        print("Buzz")
    else:
        print(i)