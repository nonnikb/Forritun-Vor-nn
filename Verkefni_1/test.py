total_coins = 0.00
candy_cost = 1.50
n = 0.05
d = 0.10
q = 0.25
D = 1.00

while total_coins < candy_cost:
    print("A packet of candy costs $ 1.50. You have inserted $",("%.2f"%total_coins),end='.'"\n")
    new_coin = input("Please insert coins:")
    print("\tn - Nickel")
    print("\td - Dime")
    print("\tq - Quarter")
    print("\tD - Dollar")
    if new_coin == 'n':
        total_coins += n
    elif new_coin == 'd' :
        total_coins += d
    elif new_coin == 'D' :
        total_coins += D
    elif new_coin == 'q':
        total_coins += q
    else:
        print("'"+new_coin+"'"" is not a valid coin.")
if total_coins > candy_cost:
    left = total_coins - candy_cost
print("Enjoy your candies. Your change is $",("%.2f"%left),+"Please visit again.")