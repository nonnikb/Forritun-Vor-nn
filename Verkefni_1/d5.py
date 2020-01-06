"""Write a program that computes the "to the power" calculation of a given number,
where the base and exponent are given by the user. Your program should take two egers,
one for the base, and another for the exponent.
Allow the user to repeat the calculaton as often as he/she wishes.
"""
cont = 'y'
below = 0
while cont == 'y':
    base = int(input("Base: "))
    exp = int(input("Exponent: "))
    ans = base
    if exp < 0:
        for x in range(abs(exp-1), base, -1):
            ans *= base
            print(ans)
        ans = 1/ans

    elif exp > 0:
        for x in range(exp-1):
            ans *= base
    else:
        ans = 1

    print('{:.1f} to the power {:.1f} = {}'.format(base, exp, float(ans)))
    cont = input("Continue? ").lower()
    if cont != 'y':
        break
    else:
        continue
