from collections.abc import Container

from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.parser import Parser, ParseResults, CouldNotParse


def char_not_in(characters: Container[str]) -> Parser[str]:
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        if len(to_parse) == 0:
            return CouldNotParse()
        if to_parse[0] in characters:
            return CouldNotParse()
        return ParseResults(
            result=to_parse[0],
            remainder=to_parse[1:],
        )

    return Parser(parser)


def test_char_not_in_matches_single_character() -> None:
    parser = char_not_in('abcdefg')
    assert_parsing_succeeds(parser, 'h').with_result('h')


def test_char_not_in_does_not_match_specified_character() -> None:
    parser = char_not_in('abcdefg')
    assert_parsing_fails(parser, 'a')


def test_char_not_in_does_not_match_empty_string() -> None:
    parser = char_not_in('adsf')
    assert_parsing_fails(parser, '')
