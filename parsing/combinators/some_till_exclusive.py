from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.combinators.lookahead import lookahead
from parsing.combinators.many import some
from parsing.parser import Parser, U, S
from parsing.strings.word import word


def some_till_exclusive(parser: Parser[U], until: Parser[S]) -> Parser[list[U]]:
    return lookahead(some(parser), look_for=until)


def test_that_some_till_exclusive_matches_some_and_keeps_remainder() -> None:
    assert_parsing_succeeds(some_till_exclusive(word('a'), word('b')), 'aab').with_result(['a', 'a']).with_remainder('b')


def test_that_some_till_exclusive_succeeds_on_nothing() -> None:
    assert_parsing_succeeds(some_till_exclusive(word('a'), word('b')), 'b').with_result([])


def test_that_some_till_exclusive_fails_when_lookahead_fails() -> None:
    assert_parsing_fails(some_till_exclusive(word('a'), word('b')), 'a')
