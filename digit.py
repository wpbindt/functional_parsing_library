import unittest

from char_in import char_in


digit = int * char_in('0123456789')


class TestDigit(unittest.TestCase):
    def test_that_digit_does_not_parse_letters(self) -> None:
        self.assertListEqual(digit('h'), [])

    def test_that_digit_does_parse_digits(self) -> None:
        self.assertListEqual(digit('3'), [(3, '')])

    def test_that_digit_does_parse_digits_with_remainder(self) -> None:
        self.assertListEqual(digit('34'), [(3, '4')])
