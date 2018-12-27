import unittest
from botocore.exceptions import ClientError
from investment.aws_email import EMail


class TestEMail(unittest.TestCase):

    def test_send(self):
        email = EMail()
        self.assertRaises(ClientError, email.send, [
                          "dinos80152@gmail.com"], "test", "test")


if __name__ == '__main__':
    unittest.main()
