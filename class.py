class BankAccount(object): 
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance


	def withdrawl(self):
		withdrawl = float(raw_input("How much do you wish to withdrawl? "))
		self.balance-= withdrawl

	def deposit(self):
		deposit = float(raw_input("How much do you wish to deposit? "))
		self.balance+= deposit

money = BankAccount("whitney", 250)

money.withdrawl()
print money.balance

money.deposit()
print money.balance

