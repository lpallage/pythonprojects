from OOPBankApp.Bank import Bank
from OOPBankApp.Customer import Customer

from OOPBankApp.Customer import Customer


class Account(Bank):
    def __init__(self, bankCode, bankName, branchName, location, accountID, customer, amount):
        super().__init__(bankCode, bankName, branchName, location)
        self._accountID = accountID
        self.customer = customer
        self._amount = amount

    @property
    def accID(self):
        return self._accountID

    @accID.setter
    def accID(self, id):
        self._accountID = id

    @property
    def accountBalance(self):
        return self._amount

    @accountBalance.setter
    def accountBalance(self, balance):
        if balance < 0:
            print('Invalid Balance.')
        else:
            self._amount = balance

    def getAccountInfo(self):
        print('Bank Account Customer Information {} {} {} {}'
              .format(self.customer.id, self.customer.name, self.accID, self.accountBalance))

    def deposit(self, money, message):
        while True:
            value = input("Enter an amount to deposit: ")
            try:
                money = float(value)
                self._amount = self._amount + money
                break
            except ValueError as e:
                print('Invalid amount. Please re-enter the amount')
        print('The account balance is :${}'.format(self.accountBalance))
        return self.accountBalance

    def withdraw(self, money):
        while True:
            value = input('Enter an amount to withdraw:  ')
            try:
                money = float(value)
                self.accountBalance = self.accountBalance - money
                break
            except ValueError as e:
                print('Invalid amount. Please re-enter')
        print('The withdrawal account balance is :${}'.format(money))
        return self.accountBalance

    def getBalance(self):
        print('The account balance is : ${}'.format(self.accountBalance))
