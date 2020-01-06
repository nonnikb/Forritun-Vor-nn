
loan = float(input("Input the cost of the item in $: "))
payment = 50.0
months = 1
interest = 0

if loan > 2499:
    print("Loan too high!")
    loan = 0.0
elif loan <= 1000:
    interest_rate = 0.015
else:
    interest_rate = 0.020

while loan > 0:
    tax = loan * interest_rate
    interest += tax
    if payment > loan:
        payment = payment - (payment - (loan + tax))
        loan = (loan + tax) - payment
    else:
        loan = (loan + tax) - payment
    print("Month: {} Payment: {} Interest paid: {} Remaining debt: {}".format(str(months), round(payment, 2), round(tax, 2), round(loan, 2)))
    loan = loan
    months = months + 1
print()
print("Number of months: {}".format(str(months -1)))
print("Total interest paid: {}".format(round(interest, 2)))
