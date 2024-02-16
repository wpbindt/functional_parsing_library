import unittest

from parser import Parser


def word(word_to_parse_for: str) -> Parser[str]:
    def parser(to_parse: str) -> list[tuple[str, str]]:
        pass

    return Parser(parser)


class TestWord(unittest.TestCase):
    def test_that_parsing_a_different_character_fails(self) -> None:
        hoi_parser = word('hoi')
        parse_result = hoi_parser('subaru')
        self.assertListEqual(parse_result, [])

    def test_that_parsing_h_succeeds(self) -> None:
        hoi_parser = word('hoi')
        parse_result = hoi_parser('hoi')
        self.assertListEqual(parse_result, [('hoi', '')])

    def test_that_parsing_h_with_remainder_gives_remainder(self) -> None:
        hoi_parser = word('h')
        parse_result = hoi_parser('hoi hoi')
        self.assertListEqual(parse_result, [('hoi', ' hoi')])
