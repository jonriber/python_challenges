import unittest
from sort_a_string import sort_a_string


class TestFunc(unittest.TestCase):

    #@unittest.skip('pular')
    def test_func_return(self):
        result = sort_a_string('uma palavra a bola')

        self.assertEqual(result,'a bola palavra uma')

    def test_number_as_argument(self):
        result = sort_a_string(20)

        self.assertEqual(result,None)

    def test_word_capitalized(self):
        result = sort_a_string('touro CASA A a Bola')
        self.assertEqual(result,'A a Bola CASA touro')

    def test_single_character(self):
        result = sort_a_string('palavra')
        self.assertEqual(result,'palavra')

if __name__ == '__main__':
    unittest.main()
