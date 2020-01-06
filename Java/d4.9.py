"""Búðu til forrit sem tekur við einni heiltölu x og reiknar x!"""

num = int(input("Enter x: "))
factorial = 1
for x in range(1, num+1):
    factorial *= x

print(factorial)

