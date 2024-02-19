from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar, Protocol, Generic, Callable

T = TypeVar('T', covariant=True)
S = TypeVar('S')


@dataclass(frozen=True)
class ParseResults(Generic[T]):
    result: T
    remainder: str


@dataclass(frozen=True)
class CouldNotParse:
    pass


class ParserFunction(Protocol[T]):
    def __call__(self, to_parse: str) -> ParseResults[T] | CouldNotParse:
        pass


class Parser(Generic[T]):
    """
    Class that parser functions should be wrapped in. Enables syntactic sugar
    for combinators. For example, you can write
        capitalize_name * ((first_name & last_name) | mononym) < period)
    instead of
        fmap(capitalize_name, ignore_right(or_2(and_2(name, surname), mononym), period))
    for a parser parsing "Frank Costanza." to "FRANK COSTANZA" and "Wilson." to "WILSON"
    """
    def __init__(self, parser_function: ParserFunction[T]) -> None:
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
        from parsing.combinators.fmap import fmap
        return fmap(function=other, parser=self)

    def __gt__(self, other: Parser[S]) -> Parser[S]:
        from parsing.combinators.ignore_left import ignore_left
        return ignore_left(left=self, right=other)

    def __lt__(self, other: Parser[S]) -> Parser[T]:
        from parsing.combinators.ignore_right import ignore_right
        return ignore_right(left=self, right=other)
