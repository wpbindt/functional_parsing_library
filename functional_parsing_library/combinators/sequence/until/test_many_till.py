from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library import many_till, word, char


def test_that_many_till_matches_many_and_consumes_delimiter() -> None:
    assert_parsing_succeeds(many_till(word('a'), word('b')), 'aabc').with_result(['a', 'a']).with_remainder('c')


def test_that_many_till_fails_on_nothing() -> None:
    assert_parsing_fails(many_till(word('a'), word('b')), 'b')


def test_that_many_till_fails_when_lookahead_fails() -> None:
    assert_parsing_fails(many_till(word('a'), word('b')), 'a')


def test_that_many_till_stops_when_delimiter_reached_even_when_overlap() -> None:
    assert_parsing_succeeds(many_till(char('a'), word('ab')), 'aab').with_result(['a'])
