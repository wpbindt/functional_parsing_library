from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.parser import CouldNotParse, Parser, ParseResults
from parsing.pop_one_character import pop_one_character


def _any_char(to_parse: str) -> ParseResults[str] | CouldNotParse:
    if len(to_parse) == 0:
        return CouldNotParse('String to parse is empty')

    return pop_one_character(to_parse)


any_char = Parser(_any_char)


def test_that_any_char_fails_on_empty_string() -> None:
    assert_parsing_fails(any_char, '').with_reason('String to parse is empty')


def test_that_any_char_succeeds_on_a_character() -> None:
    assert_parsing_succeeds(any_char, 'abc').with_result('a').with_remainder('bc')
