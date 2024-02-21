import string

from asserts import assert_parsing_succeeds
from parsing.strings.char import char
from parsing.strings.char_in import char_in
from hacky_function_composition import o
from parsing.combinators.many import many


digit = char_in(string.digits)
nonnegative_integer = int /o/ ''.join * many(digit)
negate = lambda x: -x
negative_integer = negate * (char('-') > nonnegative_integer)
integer = nonnegative_integer | negative_integer


def test_that_we_can_parse_single_digits() -> None:
    assert_parsing_succeeds(integer, '3').with_result(3)


def test_that_we_can_parse_more_digits() -> None:
    assert_parsing_succeeds(integer, '33').with_result(33)


def test_that_we_can_parse_negative_integers() -> None:
    assert_parsing_succeeds(integer, '-3').with_result(-3)
