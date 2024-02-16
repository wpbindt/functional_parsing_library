from typing import TypeVar, Protocol

T = TypeVar('T')
S = TypeVar('S')


class Parser(Protocol[T]):
    def __call__(self, to_parse: str) -> list[tuple[T, str]]:
        pass


class CouldNotParse(Exception):
    pass


def parse(parser: Parser[T], to_parse: str) -> T:
    for parsed, remainder in parser(to_parse):
        return parsed
    raise CouldNotParse
