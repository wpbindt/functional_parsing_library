from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library import some_till_exclusive, char, word


def test_that_some_till_exclusive_matches_some_and_keeps_remainder() -> None:
    assert_parsing_succeeds(some_till_exclusive(word('a'), word('b')), 'aab').with_result(['a', 'a']).with_remainder('b')


def test_that_some_till_exclusive_succeeds_on_nothing() -> None:
    assert_parsing_succeeds(some_till_exclusive(word('a'), word('b')), 'b').with_result([])


def test_that_some_till_exclusive_fails_when_lookahead_fails() -> None:
    assert_parsing_fails(some_till_exclusive(word('a'), word('b')), 'a')


def test_that_some_till_exclusive_stops_when_delimiter_reached_even_when_overlap() -> None:
    assert_parsing_succeeds(some_till_exclusive(char('a'), word('ab')), 'aab').with_result(['a']).with_remainder('ab')
