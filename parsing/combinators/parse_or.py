from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.strings.char import char
from parsing.parser import Parser, T, S, ParseResults, CouldNotParse


def or_2(parser_1: Parser[T], parser_2: Parser[S]) -> Parser[T | S]:
    def parser(to_parse: str) -> ParseResults[T | S] | CouldNotParse:
        try_1 = parser_1(to_parse)
        if not isinstance(try_1, CouldNotParse):
            return try_1
        return parser_2(to_parse)

    return Parser(parser)


def test_parsing_neither_fails() -> None:
    a = char('a')
    b = char('b')
    parser = a | b
    assert_parsing_fails(parser, 'c')


def test_parsing_first_succeeds() -> None:
    a = char('a')
    b = char('b')
    parser = a | b
    assert_parsing_succeeds(parser, 'a').with_result('a')


def test_parsing_second_succeeds() -> None:
    a = char('a')
    b = char('b')
    parser = a | b
    assert_parsing_succeeds(parser, 'b').with_result('b')


def test_that_remainder_remains() -> None:
    a = char('a')
    b = char('b')
    parser = a | b
    assert_parsing_succeeds(parser, 'bingo').with_remainder('ingo')
