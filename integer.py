import string
import unittest

from asserts import assert_parsing_succeeds
from char import char
from char_in import char_in
from hacky_function_composition import o
from many import many


digit = char_in(string.digits)
nonnegative_integer = int /o/ ''.join * many(digit)
negate = lambda x: -x
negative_integer = negate * (char('-') > nonnegative_integer)
integer = nonnegative_integer | negative_integer


class TestInteger(unittest.TestCase):
    def test_that_we_can_parse_single_digits(self) -> None:
        assert_parsing_succeeds(self, integer, '3').with_result(3)

    def test_that_we_can_parse_more_digits(self) -> None:
        assert_parsing_succeeds(self, integer, '33').with_result(33)

    def test_that_we_can_parse_negative_integers(self) -> None:
        assert_parsing_succeeds(self, integer, '-3').with_result(-3)
