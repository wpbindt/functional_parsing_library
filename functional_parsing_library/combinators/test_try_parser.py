from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library import char, try_parser, TrySucceeded


def test_that_try_succeeds_when_underlying_parser_does_and_consumes_nothing() -> None:
    parser = try_parser(char('a'))
    assert_parsing_succeeds(parser, 'a').with_result(TrySucceeded()).with_remainder('a')


def test_that_try_fails_when_underlying_parser_does() -> None:
    parser = try_parser(char('a'))
    assert_parsing_fails(parser, 'b')
