from inspect import signature
from typing import Callable, TypeVarTuple, overload, TypeVar, TypeGuard

from asserts import assert_parsing_succeeds, assert_parsing_fails
from parsing.parser import Parser, T, S, ParseResults, CouldNotParse, MappedParser
from parsing.strings.char import char

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


def test_that_fmap_still_fails_to_parse_unparsable_stuff() -> None:
    parser = to_int * char('3')

    assert_parsing_fails(parser, 'h')


def test_that_fmap_passes_on_failure_reason() -> None:
    parse_to_map_over = char('3')
    parser = to_int * parse_to_map_over
    to_parse = 'h'
    inner_result = parse_to_map_over(to_parse)
    assert isinstance(inner_result, CouldNotParse)
    inner_reason = inner_result.reason

    assert_parsing_fails(parser, to_parse).with_reason(inner_reason)


def test_that_fmap_successfully_parses_parsable_stuff() -> None:
    parser = to_int * char('3')

    assert_parsing_succeeds(parser, '3')


def test_that_fmap_maps_parsed_stuff() -> None:
    parser = to_int * char('3')

    assert_parsing_succeeds(parser, '3').with_result(3)


def test_with_a_different_function() -> None:
    parser = (lambda x: x + 90) * (to_int * char('3'))

    assert_parsing_succeeds(parser, '3').with_result(93)
