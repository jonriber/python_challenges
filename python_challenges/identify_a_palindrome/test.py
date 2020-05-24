import unittest

from find_a_palindrome import check_palindrome

class FindAPalindromeTest(unittest.TestCase):
    @unittest.skip('jump')
    def test_func_initial_return(self):
        result = check_palindrome('jonts')
        self.assertEquals(result,'jonts')

    def test_palindrome_func(self):
        result  = check_palindrome('level')
        self.assertEquals(result,'level')
        
if __name__ == '__main__':
    unittest.main()