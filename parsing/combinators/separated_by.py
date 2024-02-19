import unittest
from typing import Any

from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.parser import Parser, T
from parsing.strings.char import char
from parsing.strings.word import word


def separated_by(parser: Parser[T], separator: Parser[Any]) -> Parser[list[T]]:
    """
    It helps to implement fmap, some, and_2, and ignore_left first
    Parses a sequence of one or more matches for parser, separated by matches for separator
    returns a list of the results
    """


def some_separated_by(parser: Parser[T], separator: Parser[Any]) -> Parser[list[T]]:
    """
    It helps to implement or_2, separated_by, word, and fmap first
    Parses a sequence of zero or more matches for parser, separated by matches for separator
    returns a list of the results
    """


class TestSeparatedBy(unittest.TestCase):
    def test_separated_by_fails_on_no_match(self) -> None:
        separator = char(',')
        parser = separated_by(word('hi'), separator)
        assert_parsing_fails(self, parser, '')

    def test_separated_by_succeeds_on_one_match(self) -> None:
        separator = char(',')
        parser = separated_by(word('hi'), separator)
        assert_parsing_succeeds(self, parser, 'hi').with_result(['hi'])

    def test_separated_by_succeeds_on_two_matches(self) -> None:
        separator = char(',')
        parser = separated_by(word('hi'), separator)
        assert_parsing_succeeds(self, parser, 'hi,hi').with_result(['hi', 'hi'])

    def test_some_separated_by_succeeds_on_no_match(self) -> None:
        separator = char(',')
        parser = some_separated_by(word('hi'), separator)
        assert_parsing_succeeds(self, parser, '').with_result([])

    def test_some_separated_by_succeeds_on_one_match(self) -> None:
        separator = char(',')
        parser = some_separated_by(word('hi'), separator)
        assert_parsing_succeeds(self, parser, 'hi').with_result(['hi'])

    def test_some_separated_by_succeeds_on_two_matches(self) -> None:
        separator = char(',')
        parser = some_separated_by(word('hi'), separator)
        assert_parsing_succeeds(self, parser, 'hi,hi').with_result(['hi', 'hi'])
