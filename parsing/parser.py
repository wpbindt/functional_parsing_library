from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar, Generic, Callable

T = TypeVar('T', covariant=True)
S = TypeVar('S')


@dataclass(frozen=True)
class ParseResults(Generic[T]):
    result: T
    remainder: str


@dataclass(frozen=True)
class CouldNotParse:
    pass


class Parser(Generic[T]):
    def __init__(self, parser_function: Callable[[str], ParseResults[T] | CouldNotParse]) -> None:
        self._parser_function = parser_function

    def __call__(self, to_parse: str) -> ParseResults[T] | CouldNotParse:
        return self._parser_function(to_parse)

    def __or__(self, other: Parser[S]) -> Parser[T | S]:
        from parsing.combinators.parse_or import or_2
        return or_2(parser_1=self, parser_2=other)

    def __and__(self, other: Parser[S]) -> Parser[tuple[T, S]]:
        from parsing.combinators.parse_and import and_2
        return and_2(parser_1=self, parser_2=other)

    def __rmul__(self, other: Callable[[T], S]) -> Parser[S]:
        from parsing.fmap import fmap
        return fmap(function=other, parser=self)

    def __gt__(self, other: Parser[S]) -> Parser[S]:
        from parsing.combinators.ignore_left import ignore_left
        return ignore_left(left=self, right=other)

    def __lt__(self, other: Parser[S]) -> Parser[T]:
        from parsing.combinators.ignore_right import ignore_right
        return ignore_right(left=self, right=other)
