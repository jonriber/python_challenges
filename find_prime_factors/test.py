import unittest

from find_prime_factors import get_prime_numbers

class PrimeFuncTest(unittest.TestCase):
    
    @unittest.skip('pular')
    def test_func(self):

        first = get_prime_numbers(10)
        self.assertEqual(first,10)

        second = get_prime_numbers(-1)
        self.assertEqual(second,-1)

        third = get_prime_numbers('a')
        self.assertNotEquals(third,10)
        #self.assertRaises()

    def test_prime_func_1(self):
        result = get_prime_numbers(10)
        self.assertEqual(result,[2,5])

    def test_prime_func_2(self):
        result = get_prime_numbers(20)
        self.assertEqual(result,[2,2,5])

if __name__ == '__main__':
    unittest.main()