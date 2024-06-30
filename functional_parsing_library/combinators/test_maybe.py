from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.combinators.maybe import maybe
from functional_parsing_library.strings import char


def test_maybe_parses_like_parser() -> None:
    assert_parsing_succeeds(maybe(char('a')), 'a').with_result('a')


def test_maybe_parses_empty_string_as_none() -> None:
    assert_parsing_succeeds(maybe(char('a')), '').with_result(None)
