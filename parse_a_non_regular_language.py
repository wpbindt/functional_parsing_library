from typing import Any

from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.strings.char import char
from parsing.recursive_parser import RecursiveParser

a = char('a')
b = char('b')
wedged_term: RecursiveParser[Any] = RecursiveParser()
non_regular_parser = (a & b) | wedged_term.parser
wedged_term.parser = a & non_regular_parser & b


def test_basic_case() -> None:
    assert_parsing_succeeds(non_regular_parser, 'ab')


def test_another_case() -> None:
    assert_parsing_succeeds(non_regular_parser, 'aabb')


def test_parser_counts() -> None:
    assert_parsing_succeeds(non_regular_parser, 'aabb')


def test_parser_fails_on_stuff_too() -> None:
    assert_parsing_succeeds(non_regular_parser, 'aabbbb').with_remainder('bb')


def test_parser_fails_on_stuff_too_2() -> None:
    assert_parsing_fails(non_regular_parser, 'aa')


def test_many_cases() -> None:
    for n in range(1, 20):
        assert_parsing_succeeds(non_regular_parser, n * 'a' + n * 'b')
