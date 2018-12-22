from investment.read_stock import ReadStock

if __name__ == '__main__':
    ReadStock = ReadStock()
    price = ReadStock.get_price()
    ReadStock.check_price(price)