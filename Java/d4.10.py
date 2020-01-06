"""Forrit sem tekur við n og leggur saman 1**3 upp í n**3"""

num = int(input("Enter your number: "))
sum = 0

for x in range(num+1):
    sum += x**3

print(sum)