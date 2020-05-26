import unittest
from sort_a_string import sort_a_string


class TestFunc(unittest.TestCase):

    #@unittest.skip('pular')
    def test_func_return(self):
        result = sort_a_string('uma palavra a bola')

        self.assertEqual(result,'a bola uma palavra')

    def test_number_as_argument(self):
        result = sort_a_string(20)

        self.assertEqual(result,'20')

if __name__ == '__main__':
    unittest.main()
