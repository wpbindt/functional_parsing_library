import unittest
from typing import Any

from asserts import assert_parsing_succeeds, assert_parsing_fails
from char import char
from recursive_parser import RecursiveParser

a = char('a')
b = char('b')
wedged_term: RecursiveParser[Any] = RecursiveParser()
non_regular_parser = (a & b) | wedged_term.parser
wedged_term.parser = a & non_regular_parser & b


class TestParseNonRegularLanguage(unittest.TestCase):
    def test_basic_case(self) -> None:
        assert_parsing_succeeds(self, non_regular_parser, 'ab')

    def test_another_case(self) -> None:
        assert_parsing_succeeds(self, non_regular_parser, 'aabb')

    def test_parser_counts(self) -> None:
        assert_parsing_succeeds(self, non_regular_parser, 'aabb')

    def test_parser_fails_on_stuff_too(self) -> None:
        assert_parsing_succeeds(self, non_regular_parser, 'aabbbb').with_remainder('bb')

    def test_parser_fails_on_stuff_too_2(self) -> None:
        assert_parsing_fails(self, non_regular_parser, 'aa')

    def test_many_cases(self) -> None:
        for n in range(1, 20):
            assert_parsing_succeeds(self, non_regular_parser, n * 'a' + n * 'b')
