import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from char import char
from parser import Parser, T, ParseResults, CouldNotParse


def some(parser: Parser[T]) -> Parser[list[T]]:
    def parser_(to_parse: str) -> ParseResults[list[T]]:
        remainder = to_parse
        result: list[T] = []
        while remainder:
            one_parse = parser(remainder)
            if isinstance(one_parse, CouldNotParse):
                break
            result.append(one_parse.result)
            remainder = one_parse.remainder

        return ParseResults(result=result, remainder=remainder)

    return Parser(parser_)


def many(parser: Parser[T]) -> Parser[list[T]]:
    return (lambda t: [t[0], *t[1]]) * (parser & some(parser))


class TestMany(unittest.TestCase):
    def test_some_parses_one(self) -> None:
        parser = some(char('a'))

        assert_parsing_succeeds(self, parser, 'a').with_result(['a'])

    def test_some_parses_more(self) -> None:
        parser = some(char('a'))

        assert_parsing_succeeds(self, parser, 'aa').with_result(['a', 'a'])

    def test_some_parses_none(self) -> None:
        parser = some(char('a'))

        assert_parsing_succeeds(self, parser, 'h').with_result([]).with_remainder('h')

    def test_many_fails_to_parse_unparsable(self) -> None:
        parser = many(char('a'))

        assert_parsing_fails(self, parser, 'b')

    def test_many_parses_one(self) -> None:
        parser = many(char('a'))

        assert_parsing_succeeds(self, parser, 'a').with_result(['a'])

    def test_many_parses_two(self) -> None:
        parser = many(char('a'))

        assert_parsing_succeeds(self, parser, 'aa').with_result(['a', 'a'])
