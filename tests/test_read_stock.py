from investment.read_stock import ReadStock
import unittest

class TestReadStock(unittest.TestCase):

    def setUp(self):
        self.readStock = ReadStock()

    def test_get_price(self):
        assert self.readStock.get_price()>0.0

if __name__ == '__main__':
   unittest.main()
