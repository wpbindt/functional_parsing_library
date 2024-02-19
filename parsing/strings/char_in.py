import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.parser import Parser


def char_in(string: str) -> Parser[str]:
    """
    This parser matches anything starting with a character in string
    """
    pass


class TestCharIn(unittest.TestCase):
    def test_char_in_fails_on_no_characters_specified(self) -> None:
        assert_parsing_fails(self, parser=char_in(''), to_parse='whatever')
        # this is a helper function which asserts that the parser returns CouldNotParse()

    def test_char_in_succeeds_on_right_character(self) -> None:
        assert_parsing_succeeds(self, parser=char_in('w'), to_parse='w').with_result('w')
        # this is a helper function which asserts that the parser returns a ParseResults object
        # with result 'w'

    def test_char_in_keeps_remainder(self) -> None:
        assert_parsing_succeeds(self, char_in('w'), 'whatever').with_remainder('hatever')
        # this is a helper function which asserts that the parser returns a ParseResults object
        # with remainder 'hatever'

    def test_char_in_only_parses_one(self) -> None:
        assert_parsing_succeeds(self, char_in('i'), 'ii').with_result('i')
