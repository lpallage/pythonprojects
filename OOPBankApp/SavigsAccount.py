#Saving Account class

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
            _simBalance = input('Enter amount to save: ')
            try:
                money = float(_simBalance)
                self.accountBalance = self.accountBalance + money
                break
            except ValueError:
                print('Please enter a dollar amount')
        print('The balance is in the account : {}$'.format(self.accountBalance))


    def getSavingAccountInfo(self, money, message):
        pass

    def withdraw(self, money):
        pass

    def getBalance(self):
        pass
