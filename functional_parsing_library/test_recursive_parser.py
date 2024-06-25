from __future__ import annotations

import pytest

from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library.parser import Parser
from functional_parsing_library.recursive_parser import Bracketed, RecursiveParser
from functional_parsing_library.strings.modules.char import char
from functional_parsing_library.strings.modules.digit import digit


@pytest.fixture
def parser() -> Parser[Bracketed | int]:
    open = char('(')
    close = char(')')

    bracketed: RecursiveParser[Bracketed] = RecursiveParser()

    recursive_lang = digit | bracketed.parser
    bracketed.parser = Bracketed * ((open > recursive_lang) < close)
    return recursive_lang


def test_digit_is_parsed(parser: Parser[Bracketed | int]) -> None:
    assert_parsing_succeeds(parser, '3').with_result(3)


def test_we_can_do_parens(parser: Parser[Bracketed | int]) -> None:
    assert_parsing_succeeds(parser, '(3)').with_result(Bracketed(3))


def test_we_can_do_two_parens(parser: Parser[Bracketed | int]) -> None:
    assert_parsing_succeeds(parser, '((3))').with_result(Bracketed(Bracketed(3)))


def test_parens_must_close(parser: Parser[Bracketed | int]) -> None:
    assert_parsing_fails(parser, '((3)')


def test_we_can_do_many(parser: Parser[Bracketed | int]) -> None:
    assert_parsing_succeeds(parser, '((((3))))')
