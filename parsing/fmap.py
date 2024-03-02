from inspect import signature
from typing import Callable, TypeVarTuple, overload, TypeVar, TypeGuard

from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.strings.char import char
from parsing.parser import Parser, T, S, ParseResults, CouldNotParse

Ts = TypeVarTuple('Ts')
U = TypeVar('U')


def accepts_single_argument(
    function: Callable[[T, U, *Ts], S] | Callable[[T], S],
) -> TypeGuard[Callable[[T], S]]:
    if function in (int, str, float, dict, set, list, tuple, bool):
        return True
    if len(signature(function).parameters) == 1:
        return True
    return False


def accept_many_arguments(
    function: Callable[[T, U, *Ts], S] | Callable[[T], S],
) -> TypeGuard[Callable[[T, U, *Ts], S]]:
    return not accepts_single_argument(function)


@overload
def fmap(function: Callable[[T], S], parser: Parser[T]) -> Parser[S]:
    pass


@overload
def fmap(function: Callable[[T, U, *Ts], S], parser: Parser[T]) -> Parser[Callable[[U, *Ts], S]]:
    pass


def fmap(
    function: Callable[[T, U, *Ts], S] | Callable[[T], S],
    parser: Parser[T],
) -> Parser[Callable[[U, *Ts], S]] | Parser[S]:
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

        return Parser(parser_1)

    raise Exception('Function should accept either one or many arguments')


def test_that_fmap_still_fails_to_parse_unparsable_stuff() -> None:
    parser = int * char('3')

    assert_parsing_fails(parser, 'h')


def test_that_fmap_successfully_parses_parsable_stuff() -> None:
    parser = int * char('3')

    assert_parsing_succeeds(parser, '3')


def test_that_fmap_maps_parsed_stuff() -> None:
    parser = int * char('3')

    assert_parsing_succeeds(parser, '3').with_result(3)


def test_with_a_different_function() -> None:
    parser = (lambda x: x + 90) * (int * char('3'))

    assert_parsing_succeeds(parser, '3').with_result(93)
