import unittest

from integer_addition import add_integers


class IntegerAdditionTest(unittest.TestCase):

    def test_add_same_sign_negative(self):
        number_1 = -9
        number_2 = -20

        result = add_integers(number_1, number_2)
        self.assertEqual(result, -29, 'expected sum of -29')

    def test_add_same_sign_positive(self):
        number_1 = 10
        number_2 = 1

        result = add_integers(number_1, number_2)
        self.assertEqual(result, 11, 'expected sum of 11')

    def test_add_different_signs(self):
        number_1 = 10
        number_2 = -1

        result = add_integers(number_1, number_2)
        self.assertEqual(result, 9, 'expected sum of 10')

    def test_add_zeros(self):
        number_1 = 0
        number_2 = 0

        result = add_integers(number_1, number_2)
        self.assertEqual(result, 0, 'expected sum of 0')

    def test_add_zero_to_positve(self):
        number_1 = 0
        number_2 = 90

        result = add_integers(number_1, number_2)
        self.assertEqual(result, 90, 'expected sum of 90')

    def test_add_zero_to_negative(self):
        number_1 = 0
        number_2 = -89

        result = add_integers(number_1, number_2)
        self.assertEqual(result, -89, 'expected sum of -89')

if __name__ == '__main__':
    unittest.main()
