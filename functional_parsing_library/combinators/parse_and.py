from typing import TypeVarTuple, Callable, overload, TypeVar

from functional_parsing_library.parser import Parser, S, T, ParseResults, CouldNotParse, MappedParser

Ts = TypeVarTuple('Ts')


U = TypeVar('U')


@overload
def parse_and(left: MappedParser[S, T], right: Parser[T]) -> Parser[S]:
    pass


@overload
def parse_and(left: MappedParser[S, T, U, *Ts], right: Parser[T]) -> MappedParser[S, U, *Ts]:
    pass


def parse_and(left, right):
    """
    Is used to combine parsers p and q to a parser which first parses using p and then the remainder using q. The `&`
    operator is overloaded to make use of this function.

    If p is of type Parser[T] and q is of type Parser[S], then it is not obvious what type p & q should have. For example,
    it could be of type Parser[tuple[T, S]], it could be of type Parser[list[T | S]], and so on. Therefore, `&` can only
    be used in combination with a callable f of type `Callable[[T, S], U]` which specifies how to combine the result of
    p with the result of q. Writing `p & q` without applying such a function will raise a TypeError.

    For example,
    >>> from functional_parsing_library.strings import char
    >>> a, b = char('a'), char('b')
    >>> plus = lambda x, y: x + ' and ' + y
    >>> parser = plus * a & b
    >>> parser('ab').result
    'a and b'

    This works with callables of more than two arguments as well:
    >>> c = char('c')
    >>> triple_plus = lambda x, y, z: x + y + z
    >>> parser = triple_plus * a & b & c
    >>> parser('abc').result
    'abc'
    """
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
