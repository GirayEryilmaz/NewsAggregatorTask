import unittest

import authentication


class TestAuthMethods(unittest.TestCase):

    def test_empty_credentials(self):
        self.assertFalse(authentication.check_credentials('',''))

    def test_nonsensical_credentials(self):
        self.assertFalse(authentication.check_credentials('wrong','credentials'))

    def test_valid_credentials(self):
        self.assertTrue(authentication.check_credentials('please','open'))

if __name__ == '__main__':
    unittest.main()
