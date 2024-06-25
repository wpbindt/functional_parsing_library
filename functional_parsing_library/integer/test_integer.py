from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.integer.integer import integer


def test_that_we_can_parse_single_digits() -> None:
    assert_parsing_succeeds(integer, '3').with_result(3)


def test_that_we_can_parse_more_digits() -> None:
    assert_parsing_succeeds(integer, '33').with_result(33)


def test_that_we_can_parse_negative_integers() -> None:
    assert_parsing_succeeds(integer, '-3').with_result(-3)
