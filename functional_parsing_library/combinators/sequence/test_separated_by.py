from functional_parsing_library.asserts import assert_parsing_fails, assert_parsing_succeeds
from functional_parsing_library.combinators.sequence.separated_by import separated_by, some_separated_by
from functional_parsing_library.strings.modules.char import char
from functional_parsing_library.strings.modules.word import word


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
