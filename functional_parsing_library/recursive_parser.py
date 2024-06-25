from __future__ import annotations
from dataclasses import dataclass
from typing import Generic

import pytest

from functional_parsing_library.asserts import assert_parsing_succeeds, assert_parsing_fails
from functional_parsing_library.strings.char import char
from functional_parsing_library.strings.digit import digit
from functional_parsing_library.parser import Parser, T, ParseResults, CouldNotParse


@dataclass(frozen=True)
class Bracketed:
    content: Bracketed | int


ParsedRecursiveLang = int | Bracketed


class RecursiveParser(Generic[T]):
    def __init__(self) -> None:
        self._parser: Parser[T] | None = None

    @property
    def parser(self) -> Parser[T]:
        return Parser(self._parse_function)

    @parser.setter
    def parser(self, parser: Parser[T]) -> None:
        self._parser = parser

    def _parse_function(self, to_parse: str) -> ParseResults[T] | CouldNotParse:
        if self._parser is None:
            raise NotImplementedError
        return self._parser(to_parse)


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
