import unittest

from asserts import assert_parsing_succeeds
from parsing.strings.char import char
from parsing.parser import Parser, S, T
from parsing.strings.word import word


def ignore_left(left: Parser[T], right: Parser[S]) -> Parser[S]:
    return (lambda t: t[1]) * (left & right)


class TestIgnoreLeft(unittest.TestCase):
    def test_that_ignore_left_parses_both_and_returns_right(self) -> None:
        left = char('&')
        right = word('the thing I want to parse')

        assert_parsing_succeeds(self, left > right, '&the thing I want to parse').with_result('the thing I want to parse')
