from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.parser import U, Parser, ParseResults, CouldNotParse
from parsing.strings.char import char


def char_does_not_match(parser: Parser[U]) -> Parser[str]:
    def parser_(to_parse: str) -> ParseResults[str] | CouldNotParse:
        result = parser(to_parse)
        if not isinstance(result, CouldNotParse):
            return CouldNotParse()
        return ParseResults(
            result=to_parse[0],
            remainder=to_parse[1:]
        )

    return Parser(parser_)


def test_parser_matches_stuff_not_matching_parser() -> None:
    parser = char_does_not_match(char('a'))

    assert_parsing_succeeds(parser, 'b').with_result('b')


def test_parser_does_not_match_parser() -> None:
    parser = char_does_not_match(char('a'))

    assert_parsing_fails(parser, 'a')
