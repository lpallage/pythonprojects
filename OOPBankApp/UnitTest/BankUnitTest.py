import unittest
from unittest import TestCase
from unittest import mock
from OOPBankApp.Customer import Customer


class TestCustomer(TestCase):

    def setUp(self):
        self.cust = Customer('None', 'None', 'None', 'None')

    def test_ID(self):
        self.cust.id = '1125111'
        self.assertEqual(self.cust.id, '1125111', 'Successful Test')
        self.cust.id = '11122233'
        self.assertEqual(self.cust.id, '11122233', 'Successful Test')

    def test_Name(self):
        self.cust.name = 'Lalith Pallage'
        self.assertEqual(self.cust.name, 'Lalith Pallage', 'Successful Test')

    def test_Address(self):
        self.cust.address = '10335 Sierra Ridge Ln Parker CO 80134'
        self.assertEqual(self.cust.address, '10335 Sierra Ridge Ln Parker CO 80134', 'Successful Test')


if __name__ == '__main__':
    unittest.main()
