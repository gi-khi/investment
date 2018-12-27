import boto3
import os
from botocore.exceptions import ClientError

class EMail:

    SENDER = "Kungyu Chen <ha1802000@gmail.com>"
    CHARSET = "UTF-8"

    def __init__(self):
        self.client = boto3.client('ses',
            region_name=os.getenv('AWS_REGION'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
        )

    def send(self, recipients, subject, content=""):
        try:
            response = self.client.send_email(
                Destination={
                    'ToAddresses': recipients
                },
                Message={
                    'Body': {
                        'Text': {
                            'Charset': self.CHARSET,
                            'Data': content,
                        },
                    },
                    'Subject': {
                        'Charset': self.CHARSET,
                        'Data': subject,
                    },
                },
                Source=self.SENDER,
            )
        except ClientError as e:
            raise e
        else:
            return response['MessageId']