import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.parser import Parser, ParseResults, CouldNotParse


def char_in(string: str) -> Parser[str]:
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        if to_parse[0] not in string:
            return CouldNotParse()
        return ParseResults(to_parse[0], to_parse[1:])

    return Parser(parser)


class TestCharIn(unittest.TestCase):
    def test_char_in_fails_on_no_characters_specified(self) -> None:
        assert_parsing_fails(self, char_in(''), 'whatever')

    def test_char_in_succeeds_on_right_character(self) -> None:
        assert_parsing_succeeds(self, char_in('w'), 'w').with_result('w')

    def test_char_in_keeps_remainder(self) -> None:
        assert_parsing_succeeds(self, char_in('w'), 'whatever').with_remainder('hatever')

    def test_char_in_only_parses_one(self) -> None:
        assert_parsing_succeeds(self, char_in('i'), 'ii').with_result('i')
