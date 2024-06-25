from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.strings.char import char
from functional_parsing_library.parser import Parser, S, T
from functional_parsing_library.strings.word import word


def ignore_left(left: Parser[T], right: Parser[S]) -> Parser[S]:
    return (lambda t, s: s) * left & right


def test_that_ignore_left_parses_both_and_returns_right() -> None:
    left = char('&')
    right = word('the thing I want to parse')

    assert_parsing_succeeds(left > right, '&the thing I want to parse').with_result('the thing I want to parse')
