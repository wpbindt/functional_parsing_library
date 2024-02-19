import unittest

from parsing.parser import Parser, ParseResults, CouldNotParse


def char(c: str) -> Parser[str]:
    """
    Matches the given character c, and returns it as the result
    For example, char('d') will match the string 'dingo', returning
    ParseResult(
        result='d',
        remainder='ingo',
    )
    Any string not starting with 'd' results in CouldNotParse()
    """
    def parser(to_parse: str) -> ParseResults[str] | CouldNotParse:
        return CouldNotParse()

    return Parser(parser)


class TestChar(unittest.TestCase):
    def test_that_strings_starting_with_a_different_character_do_not_parse(self) -> None:
        self.assertEqual(char('h')('dingo'), CouldNotParse())

    def test_empty_strings_do_not_parse(self) -> None:
        h_parser = char('h')
        self.assertEqual(h_parser(''), CouldNotParse())

    def test_that_parsing_h_succeeds(self) -> None:
        h_parser = char('h')
        result = h_parser('h')
        self.assertEqual(
            result,
            ParseResults(
                result='h',
                remainder='',
            )
        )

    def test_that_parsing_h_with_remainder_gives_remainder(self) -> None:
        h_parser = char('h')
        result = h_parser('hoi')
        self.assertEqual(
            result.remainder,
            'oi'
        )
