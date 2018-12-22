from investment.aws_email import EMail
import unittest

class TestEMail(unittest.TestCase):

    def test_send(self):
        email = EMail()
        email.send(["dinos80152@gmail.com"], "test", "test")

if __name__ == '__main__':
   unittest.main()