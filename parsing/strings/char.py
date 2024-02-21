import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.parser import Parser, ParseResults, CouldNotParse


def char(c: str) -> Parser[str]:
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        if len(to_parse) == 0 or to_parse[0] != c:
            return CouldNotParse()
        return ParseResults(c, to_parse[1:])

    return Parser(parser)


class TestChar(unittest.TestCase):
    def test_that_empty_strings_do_not_parse(self) -> None:
        assert_parsing_fails(self, char('h'), '')

    def test_that_parsing_a_different_character_fails(self) -> None:
        h_parser = char('h')
        assert_parsing_fails(self, h_parser, 'n')

    def test_that_parsing_h_succeeds(self) -> None:
        h_parser = char('h')
        assert_parsing_succeeds(self, h_parser, 'h').with_result('h')

    def test_that_parsing_h_with_remainder_gives_remainder(self) -> None:
        h_parser = char('h')
        assert_parsing_succeeds(self, h_parser, 'hoi').with_remainder('oi')
