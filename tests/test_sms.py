from investment.sms import SMS
import unittest
from botocore.exceptions import ClientError

class TestSMS(unittest.TestCase):

    def test_send(self):
        sms = SMS()
        self.assertRaises(ClientError, sms.send, "+886900000000", "test")

if __name__ == '__main__':
    unittest.main()
