from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar, Generic, Callable, overload, TypeVarTuple

T = TypeVar('T', covariant=True)
Ts = TypeVarTuple('Ts')
S = TypeVar('S')
U = TypeVar('U')
TokenStream = TypeVar('TokenStream')


@dataclass(frozen=True)
class ParseResults(Generic[TokenStream, T]):
    result: T
    remainder: TokenStream


@dataclass(frozen=True)
class NoReasonSpecified:
    pass


FailureReason = NoReasonSpecified | str


@dataclass(frozen=True)
class CouldNotParse:
    reason: FailureReason = NoReasonSpecified()


class InvalidParserSyntax(Exception):
    pass


class Parser(Generic[TokenStream, T]):
    """
    This class is a wrapper for functions of signature `str -> ParseResults[TokenStream, T] | CouldNotParse` (i.e., parsers), and
    is used to overload the operators *, |, &, <, and > to make them call various parser combinators. If you wish to
    implement a parser which cannot be implemented by combining parsers found in this library, you implement a function
    `f` of signature `str -> ParseResults[TokenStream, T] | CouldNotParse`, and wrap it like so: `parser = Parser(f)`. Now your
    parser is ready for use and combination with other parsers.
    """
    def __init__(self, parser_function: Callable[[TokenStream], ParseResults[TokenStream, T] | CouldNotParse]) -> None:
        self._parser_function = parser_function

    def __call__(self, to_parse: TokenStream) -> ParseResults[TokenStream, T] | CouldNotParse:
        return self._parser_function(to_parse)

    def __or__(self, other: Parser[TokenStream, S]) -> Parser[TokenStream, T | S]:
        from functional_parsing_library.combinators.parse_or import or_2
        return or_2(parser_1=self, parser_2=other)

    @overload
    def __rmul__(self, other: Callable[[T, U, *Ts], S]) -> MappedParser[TokenStream, S, U, *Ts]:
        pass

    @overload
    def __rmul__(self, other: Callable[[T], S]) -> Parser[TokenStream, S]:
        pass

    def __rmul__(self, other: Callable[[T, U, *Ts], S] | Callable[[T], S]) -> MappedParser[TokenStream, S, U, *Ts] | Parser[TokenStream, S]:
        from functional_parsing_library.fmap import fmap
        return fmap(function=other, parser=self)

    def __gt__(self, other: Parser[TokenStream, S]) -> Parser[TokenStream, S]:
        from functional_parsing_library.combinators.ignore.ignore_left import ignore_left
        return ignore_left(left=self, right=other)

    def __lt__(self, other: Parser[TokenStream, S]) -> Parser[TokenStream, T]:
        from functional_parsing_library.combinators.ignore.ignore_right import ignore_right
        return ignore_right(left=self, right=other)

    @overload
    def __rand__(self, other: MappedParser[TokenStream, S, T]) -> Parser[TokenStream, S]:
        pass

    @overload
    def __rand__(self, other: MappedParser[TokenStream, S, T, U, *Ts]) -> MappedParser[TokenStream, S, U, *Ts]:
        pass

    def __rand__(self, other: MappedParser[TokenStream, S, T] | MappedParser[TokenStream, S, T, U, *Ts]) -> Parser[TokenStream, S] | MappedParser[TokenStream, S, U, *Ts]:
        from functional_parsing_library.combinators.parse_and import parse_and
        return parse_and(left=other, right=self)

    def __rshift__(self, other: Callable[[T], Parser[TokenStream, S]]) -> Parser[TokenStream, S]:
        from functional_parsing_library.bind_parser import bind
        return bind(self, other)

    def __bool__(self) -> bool:
        """
        Due to Python implementing comparison chaining so that "a < b < c" evaluates to "a < b and b < c", and because
        of "x and y" evaluating to y if x is truthy and to x if x is falsy, it's hard to support Parser.__bool__ without
        causing some weird behavior. Consider the parser
                char('a') > char('b') < char('c')
        The expected behavior here is that it parses 'abc' to 'b' (ignore a, keep b, ignore c). But if Parser.__bool__
        is True, then the above evaluates to
                char('a') > char('b') and char('b') < char('c'),
        which in turn evaluates to char('b') < char('c'), which parses 'bc', not 'abc'. As a means of preventing hard to
        debug situations like this, __bool__ raises an exception, so that statements like
                char('a') > char('b') < char('c')
        also raise exceptions, so that you're forced to write something like
                (char('a') > char('b')) < char('c')
        """
        raise InvalidParserSyntax


class MappedParser(Parser[TokenStream, Callable[[*Ts], S]], Generic[TokenStream, S, *Ts]):
    """
    This class exists only to make __rand__ work. In the expression
    a & b, only if a and b are of different types is __rand__ evaluated.
    If a and b are of the same type, __rand__ is implemented, and __and__ is
    not, an error is raised.
    """
    def __init__(
        self,
        parser_function: Callable[[TokenStream], ParseResults[TokenStream, Callable[[*Ts], S]] | CouldNotParse],
    ) -> None:
        super().__init__(parser_function)
        self.is_multi_arg = False
