from typing import cast

from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.parser import Parser, S, U, ParseResults, CouldNotParse
from parsing.strings.word import word


def lookahead(parser: Parser[S], look_for: Parser[U]) -> Parser[S]:
    def parser_(to_parse: str) -> ParseResults[S] | CouldNotParse:
        result_combined = (parser < look_for)(to_parse)
        if isinstance(result_combined, CouldNotParse):
            return result_combined
        return parser(to_parse)

    return Parser(parser_)


def test_that_lookahead_looks_ahead() -> None:
    parser = lookahead(word('a'), look_for=word('b'))

    assert_parsing_succeeds(parser, 'ab').with_result('a')


def test_that_lookahead_fails_when_lookahead_not_ahead() -> None:
    parser = lookahead(word('a'), look_for=word('b'))
    expected_failure_message = cast(CouldNotParse, word('b')('')).reason

    assert_parsing_fails(parser, 'a').with_reason(expected_failure_message)


def test_that_lookahead_keeps_remainder() -> None:
    parser = lookahead(word('a'), look_for=word('b'))

    assert_parsing_succeeds(parser, 'ab').with_remainder('b')
