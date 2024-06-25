import string

from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.fmap import to_int
from functional_parsing_library.strings.char import char
from functional_parsing_library.strings.char_in import char_in
from functional_parsing_library.hacky_function_composition import o
from functional_parsing_library.combinators.sequence.many import many


digit = char_in(string.digits)
nonnegative_integer = to_int /o/ ''.join * many(digit)


def negate(x: int) -> int:
    return -x


negative_integer = negate * (char('-') > nonnegative_integer)
integer = nonnegative_integer | negative_integer


def test_that_we_can_parse_single_digits() -> None:
    assert_parsing_succeeds(integer, '3').with_result(3)


def test_that_we_can_parse_more_digits() -> None:
    assert_parsing_succeeds(integer, '33').with_result(33)


def test_that_we_can_parse_negative_integers() -> None:
    assert_parsing_succeeds(integer, '-3').with_result(-3)
