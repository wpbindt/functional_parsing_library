import string
import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from char_in import char_in


digit = int * char_in(string.digits)


class TestDigit(unittest.TestCase):
    def test_that_digit_does_not_parse_letters(self) -> None:
        assert_parsing_fails(self, digit, 'h')

    def test_that_digit_does_parse_digits(self) -> None:
        assert_parsing_succeeds(self, digit, '3').with_result(3).with_remainder('')

    def test_that_digit_does_parse_digits_with_remainder(self) -> None:
        assert_parsing_succeeds(self, digit, '34').with_result(3).with_remainder('4')
