from investment.read_stock import ReadStock
from investment.sms import SMS
from investment.aws_email import EMail

if __name__ == '__main__':
    ReadStock = ReadStock(SMS(), EMail())
    price = ReadStock.get_price()
    ReadStock.check_price(price)
