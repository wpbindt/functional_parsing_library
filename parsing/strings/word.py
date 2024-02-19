import unittest

from parsing.parser import Parser, ParseResults, CouldNotParse


def word(word_to_parse_for: str) -> Parser[str]:
    """
    Matches strings starting with word_to_parse_for, and returns word_to_parse_for as the result
    For example, word('rinky') should parse 'rinky dinky' with result 'rinky', and remainder ' dinky'
    """
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        return CouldNotParse()

    return Parser(parser)


class TestWord(unittest.TestCase):
    def test_that_parsing_a_different_character_fails(self) -> None:
        hoi_parser = word('hoi')
        self.assertEqual(hoi_parser('subaru'), CouldNotParse())

    def test_that_parsing_hoi_succeeds(self) -> None:
        hoi_parser = word('hoi')
        self.assertEqual(hoi_parser('hoi'), ParseResults(result='hoi', remainder=''))

    def test_that_parsing_h_with_remainder_gives_remainder(self) -> None:
        hoi_parser = word('hoi')
        result = hoi_parser('hoi hoi')
        self.assertEqual(result, ParseResults(result='hoi', remainder=' hoi'))
