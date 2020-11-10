# Date
# Name

class Customer:
    def __init__(self, customerID, customerName, customerAddress, contactDetails):
        self._customerID = customerID
        self._customerName = customerName
        self._customerAddress = customerAddress
        self._contactDetails = contactDetails

    @property
    def id(self):
        return '{}'.format(self._customerID)

    @id.setter
    def id(self, custID):
        self._customerID = custID

    @property
    def name(self):
        return '{}'.format(self._customerName)

    @name.setter
    def name(self, custName):
        self.__class__._customerName = custName

    @property
    def address(self):
        return '{}'.format(self._customerAddress)

    @address.setter
    def adress(self, custAddress):
        self._customerAddress = custAddress

    @property
    def phone(self):
        return '{}'.format(self._contactDetails)

    @phone.setter
    def phone(self, contact):
        self._contactDetails = contact

    def printCustomer(self):
        print('The Customer ID is :% 1d , Customer Name: % 2d , and the Customer Address: %d, phone number : %d',
              self.id, self.name, self.address, self.phone)