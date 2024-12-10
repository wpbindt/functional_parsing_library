from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library.combinators.sequence.n_times_parser import n_times
from functional_parsing_library.strings import char


def test_that_0_times_succeeds_with_empty_list() -> None:
    parser = n_times(0, char('a'))
    assert_parsing_succeeds(parser, 'bcd').with_result([]).with_remainder('bcd')


def test_that_1_times_succeeds_with_singleton() -> None:
    parser = n_times(1, char('a'))
    assert_parsing_succeeds(parser, 'abcd').with_result(['a']).with_remainder('bcd')


def test_that_1_times_fails_when_no_matches() -> None:
    parser = n_times(1, char('a'))
    assert_parsing_fails(parser, 'bcd')


def test_that_1_times_succeeds_with_singleton_even_if_more_matches() -> None:
    parser = n_times(1, char('a'))
    assert_parsing_succeeds(parser, 'aabcd').with_result(['a'])


def test_that_2_times_succeeds_with_singleton_even_if_more_matches() -> None:
    parser = n_times(2, char('a'))
    assert_parsing_succeeds(parser, 'aabcd').with_result(['a', 'a'])
