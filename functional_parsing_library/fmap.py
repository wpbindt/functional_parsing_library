from inspect import signature
from typing import Callable, TypeVarTuple, overload, TypeVar, TypeGuard

from functional_parsing_library.parser import Parser, T, S, ParseResults, CouldNotParse, MappedParser

Ts = TypeVarTuple('Ts')
U = TypeVar('U')


def to_int(string: str) -> int:
    return int(string)


def number_of_arguments(function: Callable) -> int:
    if function in (int, str, float, dict, set, list, tuple, bool):
        return 1
    return len(signature(function).parameters)


def accepts_single_argument(
    function: Callable[[T, U, *Ts], S] | Callable[[T], S],
) -> TypeGuard[Callable[[T], S]]:
    return number_of_arguments(function) == 1


def accept_many_arguments(
    function: Callable[[T, U, *Ts], S] | Callable[[T], S],
) -> TypeGuard[Callable[[T, U, *Ts], S]]:
    return not accepts_single_argument(function)


@overload
def fmap(function: Callable[[T], S], parser: Parser[T]) -> Parser[S]:
    pass


@overload
def fmap(function: Callable[[T, U, *Ts], S], parser: Parser[T]) -> MappedParser[S, U, *Ts]:
    pass


def fmap(
    function,
    parser,
):
    """
    Used to map over parsers. The `*` operator is overloaded to call this function. Given a parser `p` of type
    `Parser[T]` and a callable `f` of type `Callable[[T], S]`, the parser `f * p` will parse using `p`, and then
    apply `f` to the result, resulting in an object of type S. For example,
    >>> from functional_parsing_library.strings import char
    >>> parser = (lambda x: x + 'b') * char('a')
    >>> parser('a').result
    'ab'
    """
    if accepts_single_argument(function):
        def parser_(to_parse: str) -> ParseResults[S] | CouldNotParse:
            result = parser(to_parse)
            if isinstance(result, CouldNotParse):
                return result
            return ParseResults(
                result=function(result.result),
                remainder=result.remainder
            )
        return Parser(parser_)

    if accept_many_arguments(function):
        def parser_1(to_parse: str) -> ParseResults[Callable[[U, *Ts], S]] | CouldNotParse:
            result = parser(to_parse)
            if isinstance(result, CouldNotParse):
                return result
            return ParseResults(
                result=lambda u, *ts: function(result.result, u, *ts),
                remainder=result.remainder
            )

        if number_of_arguments(function) > 2:
            p = MappedParser(parser_1)
            p.is_multi_arg = True
            return p
        else:
            return MappedParser(parser_1)

    raise Exception('Function should accept either one or many arguments')
