from investment.read_stock import ReadStock
import unittest

class TestReadStock(unittest.TestCase):

    def setUp(self):
        self.readStock = ReadStock()

    def test_get_and_check_price(self):
        price = self.readStock.get_price()
        self.readStock.check_price(price)
        assert price>0.0

if __name__ == '__main__':
   unittest.main()
