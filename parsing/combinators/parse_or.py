import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.strings.char import char
from parsing.parser import Parser, T, S, ParseResults, CouldNotParse


def or_2(parser_1: Parser[T], parser_2: Parser[S]) -> Parser[T | S]:
    """
    or_2(p1, p2) parses either what p1 parses or what p2 parses, in that order
    equivalent to p1 | p2 because of how Parser.__or__ is implemented
    """
    def parser(to_parse: str) -> ParseResults[T | S] | CouldNotParse:
        pass

    return Parser(parser)


class TestOr(unittest.TestCase):
    def test_parsing_neither_fails(self) -> None:
        a = char('a')
        b = char('b')
        parser = a | b
        assert_parsing_fails(self, parser, 'c')

    def test_parsing_first_succeeds(self) -> None:
        a = char('a')
        b = char('b')
        parser = a | b
        assert_parsing_succeeds(self, parser, 'a').with_result('a')

    def test_parsing_second_succeeds(self) -> None:
        a = char('a')
        b = char('b')
        parser = a | b
        assert_parsing_succeeds(self, parser, 'b').with_result('b')

    def test_that_remainder_remains(self) -> None:
        a = char('a')
        b = char('b')
        parser = a | b
        assert_parsing_succeeds(self, parser, 'bingo').with_remainder('ingo')
