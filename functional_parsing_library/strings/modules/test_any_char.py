from functional_parsing_library.asserts import assert_parsing_fails, assert_parsing_succeeds
from functional_parsing_library import any_char


def test_that_any_char_fails_on_empty_string() -> None:
    assert_parsing_fails(any_char, '').with_reason('String to parse is empty')


def test_that_any_char_succeeds_on_a_character() -> None:
    assert_parsing_succeeds(any_char, 'abc').with_result('a').with_remainder('bc')
