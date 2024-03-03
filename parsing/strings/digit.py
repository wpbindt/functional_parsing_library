import string

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.fmap import to_int
from parsing.strings.char_in import char_in


digit = to_int * char_in(string.digits)


def test_that_digit_does_not_parse_letters() -> None:
    assert_parsing_fails(digit, 'h')


def test_that_digit_does_parse_digits() -> None:
    assert_parsing_succeeds(digit, '3').with_result(3).with_remainder('')


def test_that_digit_does_parse_digits_with_remainder() -> None:
    assert_parsing_succeeds(digit, '34').with_result(3).with_remainder('4')


def test_that_digit_parses_all_digits() -> None:
    for d in string.digits:
        assert_parsing_succeeds(digit, d)
