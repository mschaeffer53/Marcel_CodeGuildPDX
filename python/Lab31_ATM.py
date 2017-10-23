'''
Lab 31 - ATM
Marcel Schaeffer
10/23/17
'''


class ATM:
    def __init__(self): #initialize with default $0 balance & .1% interest rate
        self.balance = 0
        self.interest_rate = .001
        self.ledger = ''

    def check_balance(self): #check the balance
        return(self.balance)

    def deposit(self, amount): #deposit to account
        self.balance += amount
        self.ledger += ('You deposited $' + str(amount) + '.\n') #update ledger

    def check_withdrawal(self, amount): #check to see if withdrawal amount wont overdraw account
        if (self.balance - amount) >= 0:
            return True
        else:
            return False

    def withdraw(self, amount): #withdraw amount if check withdrawal is True
        if self.check_withdrawal(amount) is True:
            self.balance -= amount
            self.ledger += ('You withdrew $' + str(amount) + '.\n') #update ledger
        else:
            print('This will overdraw your account.')

    def calc_interest(self): #Calc simple interest on balance
        interest = self.balance*self.interest_rate
        return interest

    def print_transactions(self): #print the transaction ledger
        return self.ledger

new_account = ATM()
print(ATM.check_balance(new_account))
print(ATM.deposit(new_account, 100000))
print(ATM.check_withdrawal(new_account, 2050))
print(ATM.withdraw(new_account, 2550))
print(ATM.calc_interest(new_account))
print(ATM.print_transactions(new_account))
print(ATM.check_balance(new_account))