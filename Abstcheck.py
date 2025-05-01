from Abst import Payment;


class creditCardPayment(Payment):
    def makePayment(self,amount):
        print("Credit card payment of: ",amount)

class netBankingPayment(Payment):
    def makePayment(self,amount):
        print("Net banking payment of: ",amount)  


payment1 = creditCardPayment()
payment1.makePayment(1000)

payment2 = netBankingPayment()
payment2.makePayment(2000)