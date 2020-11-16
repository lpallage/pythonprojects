# Saving Account class

from OOPBankApp.Account import Account


class SavingAccount(Account):
    def __init__(self, bankCode, bankName, branchName, location, customer, accountID, amount, SMinBalance):
        super().__init__(bankCode, bankName, branchName, location, customer, accountID, amount)
        self._simBalance = SMinBalance

    @property
    def sim(self):
        return self._simBalance

    @sim.setter
    def sim(self, amount):
        self._simBalance = amount

    def deposit(self, money, message):
        while True:
            sim = input('Enter amount to save: ')
            try:
                money = float(sim)
                self.accountBalance = self.accountBalance + money
                break
            except ValueError:
                print('Please enter a dollar amount')
        print('The balance is in the account : {}$'.format(self.accountBalance))

    def getSavingAccountInfo(self):
        pass

    def withdraw(self, money):
        while True:
            sim = input('Enter an amount to withdraw: $')
            try:
                money = float(sim)
                if money > self.accountBalance:
                    print('Amount is greater than available balance')
                    False
                else:
                    self.accountBalance = self.accountBalance - money
                    break;
            except ValueError:
                print('Invalid value. Please re-enter')
        print('New balance in the account :${}'.format(self.accountBalance))

    def getBalance(self):
        print('Your account balance is :${}'.format(self.accountBalance))
