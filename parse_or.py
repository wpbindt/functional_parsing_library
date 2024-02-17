import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from char import char
from parser import Parser, T, S, ParseResults


def or_2(parser_1: Parser[T], parser_2: Parser[S]) -> Parser[T | S]:
    def parser(to_parse: str) -> ParseResults[T | S]:
        try_1 = parser_1(to_parse)
        if len(list(try_1)) > 0:
            return try_1
        return parser_2(to_parse)

    return Parser(parser)


def or_(*parsers: Parser[T]) -> Parser[T]:
    raise NotImplementedError


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

    def test_or_(self) -> None:
        self.fail('Write tests for or_')
