class Loan:
    def __init__(self, amount, interestRate, numPayments):
        self.amount = amount
        self.intrestRate = interestRate
        self.numPayments = numPayments


    def displaySchedule(self):
        sum_of_instalment = 0
        payment_sum = 0
        intrst_sum = 0
        print("{:>3}{:>15}{:>15}{:>15}{:>15}".format("No.", "Balance", "Instalment", "Interest", "Total payment"))
        print("-"*64)
        instalment = self.amount / self.numPayments
        for x in range(1, self.numPayments + 1):
            intrest = self.amount * (self.intrestRate / 100) * 1/12
            total_payment = intrest + instalment
            print("{:>3}{:>15.2f}{:>15.2f}{:>15.2f}{:>15.2f}".format(x, self.amount, instalment, intrest, total_payment))
            self.amount -= instalment
            sum_of_instalment += instalment
            payment_sum += total_payment
            intrst_sum += intrest
        print("-" * 64)
        print("{:>33.2f}{:>15.2f}{:>15.2f}".format(sum_of_instalment, intrst_sum, payment_sum))


def main():
    amount = float(input("Principal: "))
    interestRate = float(input("Interest rate: "))
    numPayments = int(input("Number of payments: "))

    myLoan = Loan(amount, interestRate, numPayments)
    myLoan.displaySchedule()


main()