import unittest

class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_key(self):
        self.assertEqual('value', 'value')