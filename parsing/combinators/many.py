import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.parser import Parser, T
from parsing.strings.char import char


def some(parser: Parser[T]) -> Parser[list[T]]:
    """
    Parses 0 or more repetitions of whatever parser parses
    Implement char first (for the tests)
    """


def many(parser: Parser[T]) -> Parser[list[T]]:
    """
    Parses 1 or more repetitions of whatever parser parses
    Implement some, fmap, and and_2 first
    """


class TestSome(unittest.TestCase):
    def test_some_parses_one(self) -> None:
        parser = some(char('a'))

        assert_parsing_succeeds(self, parser, 'a').with_result(['a'])

    def test_some_parses_more(self) -> None:
        parser = some(char('a'))

        assert_parsing_succeeds(self, parser, 'aa').with_result(['a', 'a'])

    def test_some_parses_none(self) -> None:
        parser = some(char('a'))

        assert_parsing_succeeds(self, parser, 'h').with_result([]).with_remainder('h')


class TestMany(unittest.TestCase):
    def test_many_fails_to_parse_unparsable(self) -> None:
        parser = many(char('a'))

        assert_parsing_fails(self, parser, 'b')

    def test_many_parses_one(self) -> None:
        parser = many(char('a'))

        assert_parsing_succeeds(self, parser, 'a').with_result(['a'])

    def test_many_parses_two(self) -> None:
        parser = many(char('a'))

        assert_parsing_succeeds(self, parser, 'aa').with_result(['a', 'a'])
