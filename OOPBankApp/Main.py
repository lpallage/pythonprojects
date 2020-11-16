from OOPBankApp.Bank import Bank
from OOPBankApp.Customer import Customer
from OOPBankApp.Account import Account
from OOPBankApp.SavigsAccount import SavingAccount


class Main:
    def __init__(self, message):
        pass

    if __name__ == '__main__':
        chase = Bank('None', 'None', 'None', 'None')

        print('=' * 50)
        '''
        while True:
            bankcode = input('Please enter the bank code: ')
            if bankcode.isalnum():
                chase.code = bankcode
                break
            else:
                print('Invalid bank code. Please re-enter code.')
        bankname = input('Please enter the bank name: ')
        chase.name = bankname
        branchname = input('Please enter the branch name: ')
        chase.branch = branchname
        loc = input('Please enter the location: ')
        chase.loc = loc'''

        print('=' * 50)
        chase.printBankInfo()

        cust = Customer("112222", 'None', 'None','None')

        print('*' * 50)

        acc1 = Account("1","2","3","4","5", cust,0)
        acc1.getAccountInfo()
        acc1.deposit(0,'none')
        acc1.withdraw(0)
        acc1.getBalance()

        #bankCode, bankName, branchName, location, customer, accountID, SMinBalance

        sav1 = SavingAccount("1","2","3","4",cust, "6",acc1.accountBalance,0)
        sav1.deposit(0, 'true')
        sav1.withdraw(0)
