import unittest

from parser import Parser


def char(c: str) -> Parser[str]:
    def parser(to_parse: str) -> list[tuple[str, str]]:
        pass

    return Parser(parser)


class TestChar(unittest.TestCase):
    def test_that_parsing_a_different_character_fails(self) -> None:
        h_parser = char('h')
        parse_result = h_parser('n')
        self.assertListEqual(parse_result, [])

    def test_that_parsing_h_succeeds(self) -> None:
        h_parser = char('h')
        parse_result = h_parser('h')
        self.assertListEqual(parse_result, [('h', '')])

    def test_that_parsing_h_with_remainder_gives_remainder(self) -> None:
        h_parser = char('h')
        parse_result = h_parser('hoi')
        self.assertListEqual(parse_result, [('h', 'oi')])
