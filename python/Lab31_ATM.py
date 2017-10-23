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
        # print(self.balance)
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
        print(interest)

    def print_transactions(self): #print the transaction ledger
        print(self.ledger)

atm = ATM()

#ATM repl

print('I am an ATM...')
while True:
    quit_commands = ['done', 'exit', 'quit']
    option = input(
        'What would you like to do? \nOptions: check balance, deposit, withdraw, calculate interest, print transactions, done')

    if option in quit_commands:
        break

    if option == 'check balance':
        print(atm.check_balance())

    elif option == 'deposit':
        deposit_amt = int(input('How much would you like to deposit? '))
        atm.deposit(deposit_amt)

    elif option == 'withdraw':
        withdrawal_amt = int(input('How much would you like to withdraw? '))
        atm.withdraw(withdrawal_amt)

    elif option == 'calculate interest':
        atm.calc_interest()

    elif option == 'print transactions':
        atm.print_transactions()
