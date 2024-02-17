import unittest

from asserts import assert_parsing_succeeds
from char import char
from parser import Parser, S, T


def ignore_left(left: Parser[T], right: Parser[S]) -> Parser[S]:
    return (lambda t: t[1]) * (left & right)


class TestIgnoreLeft(unittest.TestCase):
    def test_that_ignore_left_parses_both_and_returns_right(self) -> None:
        left = char('a')
        right = char('b')

        assert_parsing_succeeds(self, left > right, 'ab').with_result('b')
