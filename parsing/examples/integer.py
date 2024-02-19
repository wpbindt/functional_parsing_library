import unittest

from asserts import assert_parsing_succeeds
from parsing.parser import Parser

integer: Parser[int] = ...
"""
This parser should parse both positive and negative integers.
Handy prerequisites: or_2, char, ignore_left, fmap, many, char_in
"""


class TestInteger(unittest.TestCase):
    def test_that_we_can_parse_single_digits(self) -> None:
        assert_parsing_succeeds(self, integer, '3')

    def test_that_parse_results_get_cast_properly(self) -> None:
        assert_parsing_succeeds(self, integer, '3').with_result(3)

    def test_that_we_can_parse_more_digits(self) -> None:
        assert_parsing_succeeds(self, integer, '33').with_result(33)

    def test_that_we_can_parse_negative_integers(self) -> None:
        assert_parsing_succeeds(self, integer, '-3')

    def test_that_negative_integers_get_the_right_sign(self) -> None:
        assert_parsing_succeeds(self, integer, '-3').with_result(-3)
