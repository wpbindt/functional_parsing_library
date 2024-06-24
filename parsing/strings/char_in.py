from collections.abc import Container

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.check_for_empty_string import check_for_empty_string
from parsing.parser import Parser, ParseResults, CouldNotParse
from parsing.strings.pop_one_character import pop_one_character


def char_in(string: Container[str]) -> Parser[str]:
    @check_for_empty_string
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        if to_parse[0] not in string:
            return CouldNotParse()

        return pop_one_character(to_parse)

    return Parser(parser)


def test_char_in_fails_on_no_characters_specified() -> None:
    assert_parsing_fails(char_in(''), 'whatever')


def test_char_in_succeeds_on_right_character() -> None:
    assert_parsing_succeeds(char_in('w'), 'w').with_result('w')


def test_char_in_keeps_remainder() -> None:
    assert_parsing_succeeds(char_in('w'), 'whatever').with_remainder('hatever')


def test_char_in_only_parses_one() -> None:
    assert_parsing_succeeds(char_in('i'), 'ii').with_result('i')
