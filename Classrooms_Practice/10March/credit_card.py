class Credit_card:
    def pay(self,amount):
        print(f'Rs {amount} paid by credit card')
class UPI:
    def pay(self,amount):
        print(f'Rs {amount} paid by  UPI')
class Cash:
    def pay(self,amount):
        print(f'Rs {amount} paid by cash')

pmt = [Credit_card(),UPI(),Cash()]
for i in pmt:
    i.pay(300)
