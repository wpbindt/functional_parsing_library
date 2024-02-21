import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.parser import Parser, ParseResults, CouldNotParse


def word(word_to_parse_for: str) -> Parser[str]:
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        if not to_parse.startswith(word_to_parse_for):
            return CouldNotParse()
        return ParseResults(word_to_parse_for, to_parse[len(word_to_parse_for):])

    return Parser(parser)


class TestWord(unittest.TestCase):
    def test_that_parsing_a_different_character_fails(self) -> None:
        hoi_parser = word('hoi')
        assert_parsing_fails(self, hoi_parser, 'subaru')

    def test_that_parsing_h_succeeds(self) -> None:
        hoi_parser = word('hoi')
        assert_parsing_succeeds(self, hoi_parser, 'hoi').with_result('hoi').with_remainder('')

    def test_that_parsing_h_with_remainder_gives_remainder(self) -> None:
        hoi_parser = word('hoi')
        assert_parsing_succeeds(self, hoi_parser, 'hoi hoi').with_remainder(' hoi')
