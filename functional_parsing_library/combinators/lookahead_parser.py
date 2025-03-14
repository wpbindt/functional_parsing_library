from typing import Any

from functional_parsing_library.combinators.try_parser_ import try_parser
from functional_parsing_library.parser import Parser, S, TokenStream


def lookahead(parser: Parser[TokenStream, S], look_for: Parser[TokenStream, Any]) -> Parser[TokenStream, S]:
    """
    Matches the same as the first parser, as long as it is followed by something matching the second parser. Does not
    consume whatever the second parser matches. For example,
    >>> from functional_parsing_library.strings import char
    >>> parser = lookahead(char('a'), char('b'))
    >>> parser('abbb').result
    'a'
    >>> parser('abbb').remainder
    'bbb'
    >>> from functional_parsing_library.parser import CouldNotParse
    >>> isinstance(parser('a'), CouldNotParse)
    True
    """
    return (lambda t, _: t) * parser & try_parser(look_for)
