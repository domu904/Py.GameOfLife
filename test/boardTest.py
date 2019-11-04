import unittest


class BoardTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())



if __name__ == '__main__':
    unittest.main()
