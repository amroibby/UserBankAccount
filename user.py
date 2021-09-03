class BankAccount:
    
    def __init__(self,name, int_rate, balance): 
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
    	self.balance -= amount
    def display_account_info(self):
        print(f'you have {self.balance}')
    # def yield_interest(self):
        print(f'your interest is {self.int_rate}')
mike = BankAccount("Mike",0,100)

mike.deposit(50)
mike.display_account_info()