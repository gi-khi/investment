import boto3
from config import ACCESS_KEY, SECRET_KEY

class SMS():
    def __init__(self):
        self.sns = boto3.client('sns', 
                                region_name='eu-west-1',
                                aws_access_key_id=ACCESS_KEY,
                                aws_secret_access_key=SECRET_KEY)   
    
    def send(self, phone='+886912078059', msg=''):
        print('send SMS to {0}'.format(phone))
        self.sns.publish(PhoneNumber = phone,
                         Message = msg)

if __name__ == '__main__':
    sms = SMS()
    sms.send(msg='test sms from AWS SMS service')
