import pytest

from functional_parsing_library.asserts import assert_parsing_succeeds
from functional_parsing_library.parser import InvalidParserSyntax
from functional_parsing_library.strings.modules.char import char
from functional_parsing_library.strings.modules.word import word


def test_that_ignore_left_parses_both_and_returns_right() -> None:
    left = char('&')
    right = word('the thing I want to parse')

    assert_parsing_succeeds(left > right, '&the thing I want to parse').with_result('the thing I want to parse')


def test_that_chaining_ignores_without_parens_is_illegal() -> None:
    a = char('a')
    b = char('b')
    c = char('c')

    with pytest.raises(InvalidParserSyntax):
        a < b < c
