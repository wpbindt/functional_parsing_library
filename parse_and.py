import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from char import char
from parser import Parser, S, T, ParseResults


def and_2(parser_1: Parser[T], parser_2: Parser[S]) -> Parser[tuple[T, S]]:
    def parser(to_parse: str) -> ParseResults[tuple[T, S]]:
        return [
            ((result_1, result_2), remainder_2)
            for result_1, remainder_1 in parser_1(to_parse)
            for result_2, remainder_2 in parser_2(remainder_1)
        ]

    return Parser(parser)


class TestParseAnd(unittest.TestCase):
    def test_fail_upon_nonsense(self) -> None:
        parser = char('a') & char('b')

        assert_parsing_fails(self, parser, 'dingeling')

    def test_fail_not_both_parsers_are_matched(self) -> None:
        parser = char('a') & char('b')

        assert_parsing_fails(self, parser, 'adingeling')

    def test_succeed_upon_successful_match(self) -> None:
        parser = char('a') & char('b')

        assert_parsing_succeeds(self, parser, 'abingeling').with_result(('a', 'b')).with_remainder('ingeling')
