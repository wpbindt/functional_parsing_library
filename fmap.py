import unittest
from typing import Callable

from char import char
from parser import Parser, T, S


def fmap(function: Callable[[T], S], parser: Parser[T]) -> Parser[S]:
    def parser_(to_parse: str) -> list[tuple[S, str]]:
        return [
            (function(result), remainder)
            for result, remainder in parser(to_parse)
        ]

    return Parser(parser_)


class TestFMap(unittest.TestCase):
    def test_that_fmap_still_fails_to_parse_unparsable_stuff(self) -> None:
        parser = int * char('3')

        self.assertListEqual(parser('h'), [])

    def test_that_fmap_successfully_parses_parsable_stuff(self) -> None:
        parser = int * char('3')

        self.assertGreater(len(parser('3')), 0)

    def test_that_fmap_maps_parsed_stuff(self) -> None:
        parser = int * char('3')

        self.assertListEqual(parser('3'), [(3, '')])

    def test_with_a_different_function(self) -> None:
        parser = (lambda x: x + 90) * (int * char('3'))

        self.assertListEqual(parser('3'), [(93, '')])
