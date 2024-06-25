from typing import Any

from functional_parsing_library.combinators.sequence.many import some
from functional_parsing_library.parser import Parser, T
from functional_parsing_library.strings.word import word


def separated_by(parser: Parser[T], separator: Parser[Any]) -> Parser[list[T]]:
    return (lambda t, ts: [t, *ts]) * parser & some(separator > parser)


nothing = word('')


def some_separated_by(parser: Parser[T], separator: Parser[Any]) -> Parser[list[T]]:
    return separated_by(parser, separator) | ((lambda x: []) * nothing)
