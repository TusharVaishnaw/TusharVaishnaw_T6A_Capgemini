class Bank:
    balance=0
    name='not set'
    acc=0
    pin=0
    def __init__(self):
        self.name=input('enter ur name: ')
        self.acc=int(input('enter acc no.: '))
        self.pin=int(input('enter the 4 digit pin: '))
    def deposit(self):
        name=input('enter ur name: ')
        acc=int(input('enter acc no.: '))
        amount=int(input('enter amount deposit: '))
        pin=int(input('enter the 4 digit pin: '))
        if name==self.name and acc==self.acc and pin==self.pin:
            print('last balance:',self.balance)
            self.balance+=amount
        print('Success!!!','Current Balance: ',self.balance)

    def withdraw():
        name=input('enter ur name: ')
        acc=int(input('enter acc no.: '))
        amount=int(input('enter amount withdraw: '))
        pin=int(input('enter the 4 digit pin: '))
        if name==self.name and acc==self.acc and pin==self.pin:
            print('last balance:',balance)
            balance-=amount
        print('Success!!!','Current Balance: ',balance)

    def getbal(self):
        print("current balance: ",self.balance)
    def getdetails(self):
        n=int(input('enter acc no.: '))
        if n==self.acc:
            print(self.name,self.acc,self.pin,self.balance)
#3 objects customers
cust1=Bank()
a=int(input(f"choose one: 1. Create new acc 2. Deposit amount 3. Withdraw Balance 4. Check Balance "))
cust1=Bank()
if a==1:
    cust1=Bank()
elif a==2:
    cust1.deposit()
elif a==3:
    cust1.withdraw()
elif a==4:
    cust1.getbal()
elif a==5:
    cust1.getdetails()
else:
    print('invalid num')
print(cust1.acc)
