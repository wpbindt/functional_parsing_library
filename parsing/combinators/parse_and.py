from typing import Any

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.strings.char import char
from parsing.parser import Parser, S, T, ParseResults, CouldNotParse


def and_2(parser_1: Parser[T], parser_2: Parser[S]) -> Parser[tuple[T, S]]:
    def parser(to_parse: str) -> ParseResults[tuple[T, S]] | CouldNotParse:
        result_1 = parser_1(to_parse)
        if isinstance(result_1, CouldNotParse):
            return result_1
        result_2 = parser_2(result_1.remainder)
        if isinstance(result_2, CouldNotParse):
            return result_2
        return ParseResults((result_1.result, result_2.result), result_2.remainder)

    return Parser(parser)


def and_(*parser: Parser[Any]) -> Parser[tuple[Any, ...]]:
    if len(parser) == 1:
        return (lambda x: (x,)) * parser[0]
    return (lambda x: (x[0], *x[1])) * (parser[0] & and_(*parser[1:]))


def test_fail_upon_nonsense() -> None:
    parser = char('a') & char('b')

    assert_parsing_fails(parser, 'dingeling')


def test_fail_not_both_parsers_are_matched() -> None:
    parser = char('a') & char('b')

    assert_parsing_fails(parser, 'adingeling')


def test_succeed_upon_successful_match() -> None:
    parser = char('a') & char('b')

    assert_parsing_succeeds(parser, 'abingeling').with_result(('a', 'b')).with_remainder('ingeling')


def test_ampersand_is_ugly_beyond_two() -> None:
    parser = char('a') & char('b') & char('c')

    assert_parsing_succeeds(parser, 'abc').with_result((('a', 'b'), 'c'))


def test_and_many_works_better_than_that() -> None:
    parser = and_(char('a'), char('b'), char('c'))

    assert_parsing_succeeds(parser, 'abcdefg').with_result(('a', 'b', 'c')).with_remainder('defg')
