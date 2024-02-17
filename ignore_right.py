import unittest

from asserts import assert_parsing_succeeds
from char import char
from parser import Parser, S, T


def ignore_right(left: Parser[T], right: Parser[S]) -> Parser[T]:
    return (lambda t: t[0]) * (left & right)


class TestIgnoreRight(unittest.TestCase):
    def test_that_ignore_right_parses_both_and_returns_left(self) -> None:
        left = char('a')
        right = char('b')

        assert_parsing_succeeds(self, left < right, 'ab').with_result('a').with_remainder('')
