import unittest

from asserts import assert_parsing_fails, assert_parsing_succeeds
from char import char
from parser import Parser, T, ParseResults


def many(parser: Parser[T]) -> Parser[list[T]]:
    def parser_(to_parse: str) -> ParseResults[list[T]]:
        result = parser(to_parse)
        if len(list(result)) == 0:
            return []
        parsed, remainder = next(iter(result))
        results = [parsed]
        while remainder:
            result = parser(remainder)
            if len(list(result)) == 0:
                break
            parsed, remainder = next(iter(result))
            results.append(parsed)
        return [(results, remainder)]
    return Parser(parser_)


class TestMany(unittest.TestCase):
    def test_many_fails_to_parse_unparsable(self) -> None:
        parser = many(char('a'))

        assert_parsing_fails(self, parser, 'b')

    def test_many_parses_one(self) -> None:
        parser = many(char('a'))

        assert_parsing_succeeds(self, parser, 'a').with_result(['a'])

    def test_many_parses_two(self) -> None:
        parser = many(char('a'))

        assert_parsing_succeeds(self, parser, 'aa').with_result(['a', 'a'])
