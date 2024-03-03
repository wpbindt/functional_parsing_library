from asserts import assert_parsing_succeeds
from parsing.parser import Parser, S, T
from parsing.strings.word import word


def ignore_right(left: Parser[T], right: Parser[S]) -> Parser[T]:
    return (lambda t, s: t) * left & right


def test_that_ignore_right_parses_both_and_returns_left() -> None:
    left = word('(This I want)')
    right = word('(This I ignore)')

    assert_parsing_succeeds(left < right, '(This I want)(This I ignore)').with_result('(This I want)').with_remainder('')
