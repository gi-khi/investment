import requests
import json

from investment.sms import SMS

class ReadStock:
    def get_price(self):
        r = requests.get('http://mis.tse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_0056.tw&json=1')
        print(r.url)
        print(r.text)

        source_j = json.loads(r.text)
        json_array = (source_j['msgArray'])
        targetPrice = ''
        for item in json_array:
            targetPrice = item['z']
        print(targetPrice)
        return float(targetPrice)

    def check_price(self, price):
        flow_percent = 0.05
        u_spec = 24.36*(1+flow_percent)
        l_spec = 24.36*(1-flow_percent)
        sms = SMS()
        if price <= l_spec:
            notify_msg = '0056 Stock price notice, lower bound matched: 24.36*0.95'
            print(notify_msg)
            # send mail
            # send SMS
            sms.send(msg=notify_msg)
        elif price >= u_spec:
            notify_msg = '0056 Stock price notice, upper bound matched: 24.36*1.05'
            print(notify_msg)
            # send mail
            # send SMS
            sms.send(msg=notify_msg)
        else:
            notify_msg = 'Test SMS funtion'
            sms.send(msg=notify_msg)

if __name__ == '__main__':
    ReadStock = ReadStock()
    price = ReadStock.get_price()
    ReadStock.check_price(price)