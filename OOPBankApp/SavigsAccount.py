#Saving Account class

from OOPBankApp.Account import Account

class SavingAccount:
    def __init__(self, bankCode, bankName, branchName, location, accountID, customer, amount,SMinBalance):
        super(Account, self).__init__()
        self._simBalance = SMinBalance

    @property
    def sim(self):
        return self._simBalance

    @sim.setter
    def sim(self, amount):
        self._simBalance = amount

    def getSavingAccountInfo(self):
        pass

    def deposit(self, money, message):
        pass

    def withdraw(self, money):
        pass

    def getBalance(self):
        pass
