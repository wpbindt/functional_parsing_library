from __future__ import annotations

from typing import TypeVar, Protocol, Generic, Callable, Iterator

T = TypeVar('T', covariant=True)
S = TypeVar('S')


class ParseResults(Protocol[T]):
    def __iter__(self) -> Iterator[tuple[T, str]]:
        pass


class ParserFunction(Protocol[T]):
    def __call__(self, to_parse: str) -> ParseResults[T]:
        pass


class Parser(Generic[T]):
    def __init__(self, parser_function: ParserFunction[T]) -> None:
        self._parser_function = parser_function

    def __call__(self, to_parse: str) -> ParseResults[T]:
        return self._parser_function(to_parse)

    def __or__(self, other: Parser[S]) -> Parser[T | S]:
        from parse_or import or_2
        return or_2(parser_1=self, parser_2=other)

    def __and__(self, other: Parser[S]) -> Parser[tuple[T, S]]:
        from parse_and import and_2
        return and_2(parser_1=self, parser_2=other)

    def __rmul__(self, other: Callable[[T], S]) -> Parser[S]:
        from fmap import fmap
        return fmap(function=other, parser=self)


class CouldNotParse(Exception):
    pass


def parse(parser: Parser[T], to_parse: str) -> T:
    for parsed, remainder in parser(to_parse):
        return parsed
    raise CouldNotParse
