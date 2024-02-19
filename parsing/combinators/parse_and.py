import unittest
from typing import Any

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.strings.char import char
from parsing.parser import Parser, S, T, ParseResults, CouldNotParse


def and_2(parser_1: Parser[T], parser_2: Parser[S]) -> Parser[tuple[T, S]]:
    """
    and_2(p1, p2) parses p1 and p2 consecutively and returns a tuple with the results
    The Parser.__and__ is defined as this function, so and_2(p1, p2) is the same as p1 & p2
    """
    def parser(to_parse: str) -> ParseResults[tuple[T, S]] | CouldNotParse:
        pass

    return Parser(parser)


def and_(*parser: Parser[Any]) -> Parser[tuple[Any, ...]]:
    """
    and_(p1, p2, p3) parses p1, p2, p3 consecutively and returns a tuple with the results
    You don't have to, but it helps to implement fmap and and_2 first
    """


class TestParseAnd(unittest.TestCase):
    def test_fail_upon_nonsense(self) -> None:
        parser = char('a') & char('b')

        assert_parsing_fails(self, parser, 'dingeling')

    def test_fail_not_both_parsers_are_matched(self) -> None:
        parser = char('a') & char('b')

        assert_parsing_fails(self, parser, 'adingeling')

    def test_succeed_upon_successful_match(self) -> None:
        parser = char('a') & char('b')

        assert_parsing_succeeds(self, parser, 'abingeling').with_result(('a', 'b')).with_remainder('ingeling')

    def test_ampersand_is_ugly_beyond_two(self) -> None:
        parser = char('a') & char('b') & char('c')

        assert_parsing_succeeds(self, parser, 'abc').with_result((('a', 'b'), 'c'))

    def test_and_many_works_better_than_that(self) -> None:
        parser = and_(char('a'), char('b'), char('c'))

        assert_parsing_succeeds(self, parser, 'abcdefg').with_result(('a', 'b', 'c')).with_remainder('defg')
