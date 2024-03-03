from typing import TypeVarTuple, Callable, overload, TypeVar

from asserts import assert_parsing_succeeds
from parsing.parser import Parser, S, T, ParseResults, CouldNotParse, MappedParser
from parsing.strings.char import char

Ts = TypeVarTuple('Ts')


U = TypeVar('U')


@overload
def new_and(left: MappedParser[S, T], right: Parser[T]) -> Parser[S]:
    pass


@overload
def new_and(left: MappedParser[S, T, U, *Ts], right: Parser[T]) -> MappedParser[S, U, *Ts]:
    pass


def new_and(left, right):
    if left.is_multi_arg:
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

        return MappedParser(parser_)

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
    parser = plus * a & b
    assert_parsing_succeeds(parser, 'abc').with_result('a plus b').with_remainder('c')


def test_new_and_deals_with_callables_with_more_arguments() -> None:
    def plus(left: str, middle: str, right: str) -> str:
        return f'{left} plus {middle} plus {right}'

    a = char('a')
    b = char('b')
    c = char('c')
    parser = plus * a & b & c
    assert_parsing_succeeds(parser, 'abc').with_result('a plus b plus c')
