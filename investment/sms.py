import os
import boto3

class SMS():
    def __init__(self):
        self.sns = boto3.client('sns', 
                                region_name=os.getenv('AWS_REGIN'),
                                aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                                aws_secret_access_key=os.getenv('AWS_SECRET_KEY'))   
    
    def send(self, phone=os.getenv('PHONE'), msg=''):
        print('send SMS to {0}'.format(phone))
        self.sns.publish(PhoneNumber = phone,
                         Message = msg)

if __name__ == '__main__':
    sms = SMS()
    sms.send(msg='test sms from AWS SMS service')
