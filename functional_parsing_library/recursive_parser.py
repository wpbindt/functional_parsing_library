from __future__ import annotations
from dataclasses import dataclass
from typing import Generic

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
