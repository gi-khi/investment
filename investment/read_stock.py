import requests
import json


class ReadStock:
    MAIL_LIST = ['ha1802000@gmail.com']

    def __init__(self, sms, email):
        self.sms = sms
        self.email = email

    def get_price(self):
        r = requests.get(
            'http://mis.tse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_0056.tw&json=1')
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
        print(u_spec)
        print(l_spec)
        if price <= l_spec:
            notify_msg = '0056 Stock price notice, lower bound matched: 24.36*0.95'
            print(notify_msg)
            # send mail
            self.email.send(self.MAIL_LIST, notify_msg, notify_msg)
            # send SMS
            # self.sms.send(msg=notify_msg)
        elif price >= u_spec:
            notify_msg = '0056 Stock price notice, upper bound matched: 24.36*1.05'
            print(notify_msg)
            # send mail
            self.email.send(self.MAIL_LIST, notify_msg, notify_msg)
            # send SMS
            # self.sms.send(msg=notify_msg)
        else:
            print('Test Case')
            notify_msg = 'Test SMS funtion'
            self.email.send(self.MAIL_LIST, notify_msg, notify_msg)
            # self.sms.send(msg=notify_msg)
