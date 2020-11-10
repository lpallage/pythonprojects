# Created on 09/22/2020

class Bank:
    def __init__(self, bankCode, bankName, branchName, location):
        self._bankCode = bankCode
        self._bankName = bankName
        self._branchName = branchName
        self._location = location

    @property
    def code(self):
        return self._bankCode

    @code.setter
    def code(self, bCode):
        self._bankCode = bCode

    @property
    def name(self):
        return self._bankName

    @name.setter
    def name(self, bName):
        self._bankName = bName

    @property
    def branch(self):
        return self._branchName

    @branch.setter
    def branch(self, braName):
        self._branchName = braName

    @property
    def loc(self):
        return self._location

    @loc.setter
    def loc(self, place):
        self._location = place

    def printBankInfo(self):
        print("The Bank Code is : {} \nAnd the Bank Name : {}  \nIn the branch : {} \nAt the location: {}"
              .format(self.code, self.name, self.branch, self.loc))
