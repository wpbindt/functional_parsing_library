from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library.combinators.sequence.until.many_till_exclusive import many_till_exclusive
from functional_parsing_library.strings import char
from functional_parsing_library.strings.modules.word import word


def test_that_many_till_exclusive_matches_many_and_keeps_remainder() -> None:
    assert_parsing_succeeds(many_till_exclusive(word('a'), word('b')), 'aab').with_result(['a', 'a']).with_remainder('b')


def test_that_many_till_exclusive_fails_on_nothing() -> None:
    assert_parsing_fails(many_till_exclusive(word('a'), word('b')), 'b')


def test_that_many_till_exclusive_fails_when_lookahead_fails() -> None:
    assert_parsing_fails(many_till_exclusive(word('a'), word('b')), 'a')


def test_that_many_till_exclusive_stops_when_delimiter_reached_even_when_overlap() -> None:
    assert_parsing_succeeds(many_till_exclusive(char('a'), word('ab')), 'aab').with_result(['a']).with_remainder('ab')
