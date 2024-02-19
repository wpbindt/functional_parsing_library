import unittest

from asserts import assert_parsing_succeeds
from parsing.parser import Parser, S, T
from parsing.strings.word import word


def ignore_right(left: Parser[T], right: Parser[S]) -> Parser[T]:
    """
    It helps to implement fmap and and_2 first
    Parses left and right consecutively, and returns the results of the left parser
    The parser class implements the less than method with this function, so left < right
    is the same as ignore_right(left, right)
    """


class TestIgnoreRight(unittest.TestCase):
    def test_that_ignore_right_parses_both_and_returns_left(self) -> None:
        left = word('(This I want)')
        right = word('(This I ignore)')

        assert_parsing_succeeds(self, left < right, '(This I want)(This I ignore)').with_result('(This I want)').with_remainder('')
