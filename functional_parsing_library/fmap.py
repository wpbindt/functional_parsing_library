from inspect import signature
from typing import Callable, TypeVarTuple, overload, TypeVar, TypeGuard, Any

from functional_parsing_library.parser import Parser, T, S, ParseResults, CouldNotParse, MappedParser, TokenStream

Ts = TypeVarTuple('Ts')
U = TypeVar('U')


def to_int(string: str) -> int:
    return int(string)


def _number_of_arguments(function: Callable[..., Any]) -> int:
    if function in (int, str, float, dict, set, list, tuple, bool):
        return 1
    return len(signature(function).parameters)


def _accepts_single_argument(
    function: Callable[[T, U, *Ts], S] | Callable[[T], S],
) -> TypeGuard[Callable[[T], S]]:
    return _number_of_arguments(function) == 1


def _accepts_many_arguments(
    function: Callable[[T, U, *Ts], S] | Callable[[T], S],
) -> TypeGuard[Callable[[T, U, *Ts], S]]:
    return not _accepts_single_argument(function)


@overload
def fmap(function: Callable[[T], S], parser: Parser[TokenStream, T]) -> Parser[TokenStream, S]:
    pass


@overload
def fmap(function: Callable[[T, U, *Ts], S], parser: Parser[TokenStream, T]) -> MappedParser[TokenStream, S, U, *Ts]:
    pass


def fmap(
    function: Callable[[T], S] | Callable[[T, U, *Ts], S],
    parser: Parser[TokenStream, T],
) -> Parser[TokenStream, S] | MappedParser[TokenStream, S, U, *Ts]:
    """
    Used to map over parsers. The `*` operator is overloaded to call this function. Given a parser `p` of type
    `Parser[TokenStream, T]` and a callable `f` of type `Callable[[T], S]`, the parser `f * p` will parse using `p`, and then
    apply `f` to the result, resulting in an object of type S. For example,
    >>> from functional_parsing_library.strings import char
    >>> parser = (lambda x: x + 'b') * char('a')
    >>> parser('a').result
    'ab'
    """
    if _accepts_single_argument(function):
        return _fmap_for_one_argument(function, parser)

    if _accepts_many_arguments(function):
        return _fmap_for_multiple_arguments(function, parser)

    raise Exception('Function should accept either one or many arguments')


def _fmap_for_one_argument(
    function: Callable[[T], S],
    parser: Parser[TokenStream, T],
) -> Parser[TokenStream, S]:
    def mapped_parser(to_parse: TokenStream) -> ParseResults[TokenStream, S] | CouldNotParse:
        result = parser(to_parse)
        if isinstance(result, CouldNotParse):
            return result
        return ParseResults(
            result=function(result.result),
            remainder=result.remainder
        )

    return Parser(mapped_parser)


def _fmap_for_multiple_arguments(
    function: Callable[[T, U, *Ts], S],
    parser: Parser[TokenStream, T],
) -> MappedParser[TokenStream, S, U, *Ts]:
    def mapped_parser(to_parse: TokenStream) -> ParseResults[TokenStream, Callable[[U, *Ts], S]] | CouldNotParse:
        result = parser(to_parse)
        if isinstance(result, CouldNotParse):
            return result
        return ParseResults(
            result=lambda u, *ts: function(result.result, u, *ts),
            remainder=result.remainder
        )

    p: MappedParser[TokenStream, S, U, *Ts] = MappedParser(mapped_parser)
    if _number_of_arguments(function) > 2:
        p.is_multi_arg = True

    return p
