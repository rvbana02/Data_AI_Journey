class Amount:
    def __init__(self,bal,acc):
         self.balance=bal
         self.account_no=acc

    
    def debit(self,ammount):
                self.balance-=ammount
                print("Rs.",ammount,"is debited")
                print("Total balane",self.get_balance())

    def credit(self,ammount):
                self.balance+=ammount
                print("Rs.",ammount,"is credited")
                print("Total balane",self.get_balance())

    def get_balance(self):
        return self.balance
        


acc1=Amount(10000,1234)
acc1.debit(1000)
acc1.credit(58800)

