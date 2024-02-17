import unittest
from typing import Callable

from asserts import assert_parsing_succeeds, assert_parsing_fails
from char import char
from parser import Parser, T, S, ParseResults


def fmap(function: Callable[[T], S], parser: Parser[T]) -> Parser[S]:
    def parser_(to_parse: str) -> ParseResults[S]:
        return [
            (function(result), remainder)
            for result, remainder in parser(to_parse)
        ]

    return Parser(parser_)


class TestFMap(unittest.TestCase):
    def test_that_fmap_still_fails_to_parse_unparsable_stuff(self) -> None:
        parser = int * char('3')

        assert_parsing_fails(self, parser, 'h')

    def test_that_fmap_successfully_parses_parsable_stuff(self) -> None:
        parser = int * char('3')

        assert_parsing_succeeds(self, parser, '3')

    def test_that_fmap_maps_parsed_stuff(self) -> None:
        parser = int * char('3')

        assert_parsing_succeeds(self, parser, '3').with_result(3)

    def test_with_a_different_function(self) -> None:
        parser = (lambda x: x + 90) * (int * char('3'))

        assert_parsing_succeeds(self, parser, '3').with_result(93)
