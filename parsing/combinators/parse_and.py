from typing import Any, TypeVarTuple, Unpack, Callable, overload, TypeVar

from asserts import assert_parsing_fails, assert_parsing_succeeds
from parsing.fmap import fmap
from parsing.strings.char import char
from parsing.parser import Parser, S, T, ParseResults, CouldNotParse


def and_2(parser_1: Parser[T], parser_2: Parser[S]) -> Parser[tuple[T, S]]:
    def parser(to_parse: str) -> ParseResults[tuple[T, S]] | CouldNotParse:
        result_1 = parser_1(to_parse)
        if isinstance(result_1, CouldNotParse):
            return result_1
        result_2 = parser_2(result_1.remainder)
        if isinstance(result_2, CouldNotParse):
            return result_2
        return ParseResults((result_1.result, result_2.result), result_2.remainder)

    return Parser(parser)

Ts = TypeVarTuple('Ts')

def and_(
    *parsers: Parser[T],
) -> Parser[tuple[T, ...]]:
    if len(parsers) == 1:
        return (lambda x: (x,)) * parsers[0]
    return (lambda x: (x[0], *x[1])) * (parsers[0] & and_(*parsers[1:]))


def test_fail_upon_nonsense() -> None:
    parser = char('a') & char('b')

    assert_parsing_fails(parser, 'dingeling')


def test_fail_not_both_parsers_are_matched() -> None:
    parser = char('a') & char('b')

    assert_parsing_fails(parser, 'adingeling')


def test_succeed_upon_successful_match() -> None:
    parser = char('a') & char('b')

    assert_parsing_succeeds(parser, 'abingeling').with_result(('a', 'b')).with_remainder('ingeling')


def test_ampersand_is_ugly_beyond_two() -> None:
    parser = char('a') & char('b') & char('c')

    assert_parsing_succeeds(parser, 'abc').with_result((('a', 'b'), 'c'))


def test_and_many_works_better_than_that() -> None:
    parser = and_(char('a'), char('b'), char('c'))

    assert_parsing_succeeds(parser, 'abcdefg').with_result(('a', 'b', 'c')).with_remainder('defg')


U = TypeVar('U')


@overload
def new_and(left: Parser[Callable[[T, U, *Ts], S]], right: Parser[T]) -> Parser[Callable[[U, *Ts], S]]:
    pass


@overload
def new_and(left: Parser[Callable[[T], S]], right: Parser[T]) -> Parser[S]:
    pass


def new_and(left, right):
    if left.is_map:
        def parser_(to_parse: str) -> ParseResults[Callable[[U, *Ts], S]] | CouldNotParse:
            left_result = left(to_parse)
            if isinstance(left_result, CouldNotParse):
                return left_result

            parsed_function = left_result.result
            remainder = left_result.remainder
            right_result = right(remainder)
            if isinstance(right_result, CouldNotParse):
                return right_result

            return ParseResults(
                result=lambda *ts: parsed_function(right_result.result, *ts),
                remainder=right_result.remainder
            )

        return Parser(parser_)

    def parser(to_parse: str) -> ParseResults[S] | CouldNotParse:
        left_result = left(to_parse)
        if isinstance(left_result, CouldNotParse):
            return left_result

        parsed_function = left_result.result
        remainder = left_result.remainder
        right_result = right(remainder)
        if isinstance(right_result, CouldNotParse):
            return right_result

        return ParseResults(
            result=parsed_function(right_result.result),
            remainder=right_result.remainder
        )

    return Parser(parser)


def test_new_and_deals_with_callables() -> None:
    def plus(left: str, right: str) -> str:
        return f'{left} plus {right}'

    a = char('a')
    b = char('b')
    parser = new_and(fmap(plus, a), b)
    assert_parsing_succeeds(parser, 'abc').with_result('a plus b').with_remainder('c')


def test_new_and_deals_with_callables_with_more_arguments() -> None:
    def plus(left: str, middle: str, right: str) -> str:
        return f'{left} plus {middle} plus {right}'

    a = char('a')
    b = char('b')
    c = char('c')
    parser = new_and(new_and(fmap(plus, a), b), c)
    assert_parsing_succeeds(parser, 'abc').with_result('a plus b plus c')
