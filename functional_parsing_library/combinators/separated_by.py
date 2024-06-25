from typing import Any

from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library.combinators.many import some
from functional_parsing_library.parser import Parser, T
from functional_parsing_library.strings.char import char
from functional_parsing_library.strings.word import word


def separated_by(parser: Parser[T], separator: Parser[Any]) -> Parser[list[T]]:
    return (lambda t, ts: [t, *ts]) * parser & some(separator > parser)


nothing = word('')


def some_separated_by(parser: Parser[T], separator: Parser[Any]) -> Parser[list[T]]:
    return separated_by(parser, separator) | ((lambda x: []) * nothing)


def test_separated_by_fails_on_no_match() -> None:
    separator = char(',')
    parser = separated_by(word('hi'), separator)
    assert_parsing_fails(parser, '')


def test_separated_by_succeeds_on_one_match() -> None:
    separator = char(',')
    parser = separated_by(word('hi'), separator)
    assert_parsing_succeeds(parser, 'hi').with_result(['hi'])


def test_separated_by_succeeds_on_two_matches() -> None:
    separator = char(',')
    parser = separated_by(word('hi'), separator)
    assert_parsing_succeeds(parser, 'hi,hi').with_result(['hi', 'hi'])


def test_some_separated_by_succeeds_on_no_match() -> None:
    separator = char(',')
    parser = some_separated_by(word('hi'), separator)
    assert_parsing_succeeds(parser, '').with_result([])


def test_some_separated_by_succeeds_on_one_match() -> None:
    separator = char(',')
    parser = some_separated_by(word('hi'), separator)
    assert_parsing_succeeds(parser, 'hi').with_result(['hi'])


def test_some_separated_by_succeeds_on_two_matches() -> None:
    separator = char(',')
    parser = some_separated_by(word('hi'), separator)
    assert_parsing_succeeds(parser, 'hi,hi').with_result(['hi', 'hi'])
