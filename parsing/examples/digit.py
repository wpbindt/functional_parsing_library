import string
import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.parser import Parser


digit: Parser[int] = ...
"""
This parser should match single digits, and return the corresponding integer. Try defining it in
terms of parsers you've already implemented, by using fmap.
"""


class TestDigit(unittest.TestCase):
    def test_that_digit_does_not_parse_letters(self) -> None:
        assert_parsing_fails(self, digit, 'h')

    def test_that_digit_does_parse_digits(self) -> None:
        assert_parsing_succeeds(self, digit, '3').with_result(3).with_remainder('')

    def test_that_digit_does_parse_digits_with_remainder(self) -> None:
        assert_parsing_succeeds(self, digit, '34').with_result(3).with_remainder('4')

    def test_that_digit_parses_all_digits(self) -> None:
        for d in string.digits:
            with self.subTest(d):
                assert_parsing_succeeds(self, digit, d)
