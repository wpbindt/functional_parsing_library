import string

from functional_parsing_library.asserts import assert_parsing_fails, assert_parsing_succeeds
from functional_parsing_library.strings.modules.digit import digit


def test_that_digit_does_not_parse_letters() -> None:
    assert_parsing_fails(digit, 'h')


def test_that_digit_does_parse_digits() -> None:
    assert_parsing_succeeds(digit, '3').with_result(3).with_remainder('')


def test_that_digit_does_parse_digits_with_remainder() -> None:
    assert_parsing_succeeds(digit, '34').with_result(3).with_remainder('4')


def test_that_digit_parses_all_digits() -> None:
    for d in string.digits:
        assert_parsing_succeeds(digit, d)
