class bank:
        def __init__(self,owner, balance):
            self.owner = owner
            self.balance = balance
            
        def __str__(self):
            return f"account owner: {self.owner}\naccount balance: {self.balance}"

        def deposit(self, price):
            self.balance = self.balance + price
            return f"balance updated: {self.balance}"

        def withdraw(self, wtd_amt):
            if wtd_amt <= self.balance:
                self.balance = self.balance - wtd_amt
                return f"balance current:{self.balance}\nwithdrawal accepted"
            elif wtd_amt >self.balance:
                return "funds unavailable"
            else:
                return "error"

acct = bank('Ram', 100)
print(acct)
print(acct.balance)
acct.deposit(100)
print(acct.balance)
acct.withdraw(150)
print(acct.balance)
acct.withdraw(250)
print(acct.balance)

        


            