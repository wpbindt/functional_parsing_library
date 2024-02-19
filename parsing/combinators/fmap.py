import unittest
from typing import Callable

from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.strings.char import char
from parsing.parser import Parser, T, S, ParseResults, CouldNotParse


def fmap(function: Callable[[T], S], parser: Parser[T]) -> Parser[S]:
    """
    fmap takes a function f from T to S, and a parser which results in Ts,
    and returns a parser which parses the exact same strings, but uses f to
    transform the result from a T to an S.
    Compare it with map, which takes a list of Ts and a function from T to S,
    and gives a list of Ss.
    The existence of fmap is (by definition) what makes Parser functorial. Other
    functors are List, Set, Optional, etc

    Parser.__rmul__ allows us to write f * p instead of fmap(f, p)
    """
    def parser_(to_parse: str) -> ParseResults[S] | CouldNotParse:
        pass

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
