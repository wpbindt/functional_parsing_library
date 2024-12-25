from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library import maybe, char


def test_maybe_parses_like_parser() -> None:
    assert_parsing_succeeds(maybe(char('a')), 'a').with_result('a').with_remainder('')


def test_maybe_parses_empty_string_as_none() -> None:
    assert_parsing_succeeds(maybe(char('a')), '').with_result(None)
