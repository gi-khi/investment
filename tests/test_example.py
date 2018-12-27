import unittest
from example import World


class TestWorld(unittest.TestCase):

    def setUp(self):
        self.world = World()

    def test_welcome(self):
        self.assertEqual('hello world', self.world.welcome())


if __name__ == '__main__':
    unittest.main()
