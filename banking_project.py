class Banking:
    def __init__(self,user_name,initial_balance):
        self.name=user_name
        self.balance=initial_balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
        return amount
    def get_balance(self):
        return self.balance
    
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            return amount
        else:
            return f"insufficient balance"
        
ostad=Banking("ostad",10000)
print(f"Acount name: {ostad.name}")
print(f"Initial Balance: {ostad.balance}")
print(f"Deposit balance: {ostad.deposit(500)}")
print(f"After deposit, your balance is: {ostad.get_balance()}")
print(f"Withdraw balance: {ostad.withdraw(1000)}")
print(f"After withdraw, your balance is: {ostad.get_balance()}")        