from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.check_for_empty_string import check_for_empty_string
from parsing.parser import U, Parser, ParseResults, CouldNotParse
from parsing.strings.pop_one_character import pop_one_character
from parsing.strings.char import char


def char_does_not_match(parser: Parser[U]) -> Parser[str]:
    @check_for_empty_string
    def parser_(to_parse: str) -> ParseResults[str] | CouldNotParse:
        result = parser(to_parse)
        if not isinstance(result, CouldNotParse):
            return CouldNotParse()

        return pop_one_character(to_parse)

    return Parser(parser_)


def test_parser_matches_stuff_not_matching_parser() -> None:
    parser = char_does_not_match(char('a'))

    assert_parsing_succeeds(parser, 'b').with_result('b')


def test_parser_does_not_match_parser() -> None:
    parser = char_does_not_match(char('a'))

    assert_parsing_fails(parser, 'a')
