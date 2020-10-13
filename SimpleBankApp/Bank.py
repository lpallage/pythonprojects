# Bank Application

class Bank:
    def __init__(self, IFSC_Code, bankName, branchname, loc):
        self.IFSC_Code = IFSC_Code
        self.bankName = bankName
        self.branchName = branchname
        self.loc = loc

    def printBankInfo(self):
        print("The Code : " + self.IFSC_Code + " Bank Name : "
              + self.bankName + " Branch Name : " + self.branchName
              + " The Location: " + self.loc)


class Customer:
    def __init__(self, customerID, custName, address, contactDetails):
        self.customerID = customerID
        self.custName = custName
        self.address = address
        self.contactDetails = contactDetails

    def printCustomer(self):
        print("The customer ID :" + self.customerID + " The Customer Name: "
              + self.custName + " Address : " + self.address
              + " Contact Details : " + self.contactDetails)


class Account(Bank):
    balance = 0

    def __init__(self, accountID, customer, IFSC_Code, bankName, branchname, loc):
        self.accountID = accountID
        self.customer = customer
        super().__init__(IFSC_Code, bankName, branchname, loc)

    def getAccountInfo(self):
        print("Balance is : " + self.balance)

    def deposit(self, amount):
        if amount == 0:
            message = 'false'
        else:
            self.balance = amount + self.balance
            message = 'true'
            print(f"Deposit the amount : " + str(self.balance) + " " + message)

    def withdraw(self, withdrawAmount):
        if withdrawAmount == 0:
            print("Please enter greater than $0 to withdraw from account")
        else:
            self.balance = self.balance - withdrawAmount
            print("You withdraw Amount is : " + str(withdrawAmount))
        return self.balance

    def moneytoAccount(self):
        while True:
            try:
                enterAmount = float(input('Enter an amount to deposit: '))
                if enterAmount <= 0:
                    print("Please enter a valid amount to deposit")
                    False
                else:
                    break
            except ValueError:
                print("Invalid amount. Please enter a positive value: ")
        self.balance = enterAmount + self.balance
        print("You deposit : " + str(self.balance))


class SavingAccount(Account):
    def __init__(self, SMinBalance, accountID, customer, IFSC_Code, bankName, branchname, loc):
        self._SMinBalance = SMinBalance
        super().__init__(accountID, customer, IFSC_Code, bankName, branchname, loc)

    def getSavingAccountInfo(self):
        print("Saving Account Balance is : " + self.balance)


# Execute the Program

class Main:
    def __init__(self):
        pass

    if __name__ == '__main__':
        code: str = input('Enter The IFSC Code :')
        bankName: str = input('Enter The Bank Name: ')
        branch: str = input('Enter The Branch : ')
        location: str = input('Enter the location :')

        # bank = Bank(code, bankName, branch, location)
        # bank.printBankInfo()

        custID: str = input('Enter Customer ID: ')
        custName: str = input('Customer Name : ')
        custAddress: str = input('Customer Address : ')
        custContactInfo: str = input('Customer Contact Info: ')

        # lalith = Customer(custID, custName, custAddress, custContactInfo)
        # lalith.printCustomer()

        acctID: str = input('Account ID : ')
        money = input("Enter an amount: ")
        depositAmount = int(money)
        newAcc = Account(acctID, custID, code, bankName, branch, location)
        newAcc.deposit(depositAmount)

        takeOut = input("Enter an amount to withdraw: ")
        takeOutAmount = int(takeOut)
        newAcc.withdraw(takeOutAmount)
        newAcc.moneytoAccount()
