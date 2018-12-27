from investment.read_stock import ReadStock
from investment.aws_email import EMail
from unittest.mock import Mock
import unittest

class TestReadStock(unittest.TestCase):

    def test_get_price(self):
        readStock = self.read_stock_factory()
        price = readStock.get_price()
        self.assertLess(price, 100)

    def test_check_price(self):
        readStock = self.read_stock_factory()
        readStock.check_price(25)
        readStock.email.send.assert_called_once()

    def test_check_price_lower_bound(self):
        readStock = self.read_stock_factory()
        readStock.check_price(23)
        readStock.email.send.assert_called_once()

    def test_check_price_upper_bound(self):
        readStock = self.read_stock_factory()
        readStock.check_price(26)
        readStock.email.send.assert_called_once()

    def read_stock_factory(self):
        smsmock = Mock()
        emailmock = Mock()
        return ReadStock(smsmock, emailmock)

if __name__ == '__main__':
   unittest.main()
