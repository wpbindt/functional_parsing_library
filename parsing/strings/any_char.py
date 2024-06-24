from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.check_for_empty_string import check_for_empty_string
from parsing.parser import CouldNotParse, Parser, ParseResults
from parsing.strings.pop_one_character import pop_one_character


@check_for_empty_string
def _any_char(to_parse: str) -> ParseResults[str] | CouldNotParse:
    return pop_one_character(to_parse)


any_char = Parser(_any_char)


def test_that_any_char_fails_on_empty_string() -> None:
    assert_parsing_fails(any_char, '').with_reason('String to parse is empty')


def test_that_any_char_succeeds_on_a_character() -> None:
    assert_parsing_succeeds(any_char, 'abc').with_result('a').with_remainder('bc')
