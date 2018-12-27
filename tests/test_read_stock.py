import unittest
from unittest.mock import Mock
from investment.read_stock import ReadStock


class TestReadStock(unittest.TestCase):

    def test_get_price(self):
        read_stock = self.create_read_stock()
        price = read_stock.get_price()
        self.assertLess(price, 100)

    def test_check_price(self):
        read_stock = self.create_read_stock()
        read_stock.check_price(25)
        read_stock.email.send.assert_called_once()

    def test_check_price_lower_bound(self):
        read_stock = self.create_read_stock()
        read_stock.check_price(23)
        read_stock.email.send.assert_called_once()

    def test_check_price_upper_bound(self):
        read_stock = self.create_read_stock()
        read_stock.check_price(26)
        read_stock.email.send.assert_called_once()

    @staticmethod
    def create_read_stock():
        smsmock = Mock()
        emailmock = Mock()
        return ReadStock(smsmock, emailmock)


if __name__ == '__main__':
    unittest.main()
