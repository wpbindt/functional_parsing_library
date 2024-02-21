from __future__ import annotations
from dataclasses import dataclass
from typing import Generic

from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.strings.char import char
from parsing.strings.digit import digit
from parsing.parser import Parser, T, ParseResults, CouldNotParse


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


open = char('(')
close = char(')')

bracketed: RecursiveParser[Bracketed] = RecursiveParser()

recursive_lang = digit | bracketed.parser
bracketed.parser = Bracketed * ((open > recursive_lang) < close)


def test_digit_is_parsed() -> None:
    assert_parsing_succeeds(recursive_lang, '3').with_result(3)


def test_we_can_do_parens() -> None:
    assert_parsing_succeeds(recursive_lang, '(3)').with_result(Bracketed(3))


def test_we_can_do_two_parens() -> None:
    assert_parsing_succeeds(recursive_lang, '((3))').with_result(Bracketed(Bracketed(3)))


def test_parens_must_close() -> None:
    assert_parsing_fails(recursive_lang, '((3)')


def test_we_can_do_many() -> None:
    assert_parsing_succeeds(recursive_lang, '((((3))))')
