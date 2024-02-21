from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.parser import Parser, ParseResults, CouldNotParse


def char(c: str) -> Parser[str]:
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        if len(to_parse) == 0 or to_parse[0] != c:
            return CouldNotParse()
        return ParseResults(c, to_parse[1:])

    return Parser(parser)


def test_that_empty_strings_do_not_parse() -> None:
    assert_parsing_fails(char('h'), '')


def test_that_parsing_a_different_character_fails() -> None:
    h_parser = char('h')
    assert_parsing_fails(h_parser, 'n')


def test_that_parsing_h_succeeds() -> None:
    h_parser = char('h')
    assert_parsing_succeeds(h_parser, 'h').with_result('h')


def test_that_parsing_h_with_remainder_gives_remainder() -> None:
    h_parser = char('h')
    assert_parsing_succeeds(h_parser, 'hoi').with_remainder('oi')
