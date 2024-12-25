from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library import some, many, char


def test_some_parses_one() -> None:
    parser = some(char('a'))

    assert_parsing_succeeds(parser, 'a').with_result(['a'])


def test_some_parses_more() -> None:
    parser = some(char('a'))

    assert_parsing_succeeds(parser, 'aa').with_result(['a', 'a'])


def test_some_parses_none() -> None:
    parser = some(char('a'))

    assert_parsing_succeeds(parser, 'h').with_result([]).with_remainder('h')


def test_many_fails_to_parse_unparsable() -> None:
    parser = many(char('a'))

    assert_parsing_fails(parser, 'b')


def test_many_parses_one() -> None:
    parser = many(char('a'))

    assert_parsing_succeeds(parser, 'a').with_result(['a'])


def test_many_parses_two() -> None:
    parser = many(char('a'))

    assert_parsing_succeeds(parser, 'aa').with_result(['a', 'a'])
