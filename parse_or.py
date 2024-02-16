import unittest

from char import char
from parser import Parser, T, S


def or_2(parser_1: Parser[T], parser_2: Parser[S]) -> Parser[T | S]:
    def parser(to_parse: str) -> list[tuple[T | S, str]]:
        try_1 = parser_1(to_parse)
        if len(try_1) > 0:
            return try_1
        return parser_2(to_parse)

    return Parser(parser)


def or_(*parsers: Parser[T]) -> Parser[T]:
    pass


class TestOr(unittest.TestCase):
    def test_parsing_neither_fails(self) -> None:
        a = char('a')
        b = char('b')
        parser = a | b
        self.assertListEqual(parser('c'), [])

    def test_parsing_first_succeeds(self) -> None:
        a = char('a')
        b = char('b')
        parser = a | b
        self.assertListEqual(parser('a'), [('a', '')])

    def test_parsing_second_succeeds(self) -> None:
        a = char('a')
        b = char('b')
        parser = a | b
        self.assertListEqual(parser('b'), [('b', '')])

    def test_that_remainder_remains(self) -> None:
        a = char('a')
        b = char('b')
        parser = a | b
        self.assertListEqual(parser('bingo'), [('b', 'ingo')])

    def test_or_(self) -> None:
        self.fail('Write tests for or_')
