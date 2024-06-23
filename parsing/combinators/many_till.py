from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.combinators.many import many
from parsing.parser import Parser, U, S
from parsing.strings.word import word


def many_till(parser: Parser[U], until: Parser[S]) -> Parser[list[U]]:
    return many(parser) < until


def test_that_many_till_matches_many_and_consumes_delimiter() -> None:
    assert_parsing_succeeds(many_till(word('a'), word('b')), 'aabc').with_result(['a', 'a']).with_remainder('c')


def test_that_many_till_fails_on_nothing() -> None:
    assert_parsing_fails(many_till(word('a'), word('b')), 'b')


def test_that_many_till_fails_when_lookahead_fails() -> None:
    assert_parsing_fails(many_till(word('a'), word('b')), 'a')
