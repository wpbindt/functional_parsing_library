import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.strings.char import char
from parsing.parser import Parser, S, T, ParseResults, CouldNotParse


def and_2(parser_1: Parser[T], parser_2: Parser[S]) -> Parser[tuple[T, S]]:
    def parser(to_parse: str) -> ParseResults[tuple[T, S]] | CouldNotParse:
        result_1 = parser_1(to_parse)
        if isinstance(result_1, CouldNotParse):
            return result_1
        result_2 = parser_2(result_1.remainder)
        if isinstance(result_2, CouldNotParse):
            return result_2
        return ParseResults((result_1.result, result_2.result), result_2.remainder)

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
